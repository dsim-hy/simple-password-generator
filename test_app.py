import pytest

from app import app as flask_app


@pytest.fixture()
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


# ---------------------------------------------------------------------------
# GET /
# ---------------------------------------------------------------------------
class TestIndex:
    def test_get_returns_200(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_get_contains_form(self, client):
        html = client.get("/").data.decode()
        assert "<form" in html
        assert 'name="letters"' in html
        assert 'name="numbers"' in html
        assert 'name="symbols"' in html
        assert 'name="length"' in html
        assert 'name="count"' in html

    def test_get_no_results_section(self, client):
        html = client.get("/").data.decode()
        assert "Generated" not in html


# ---------------------------------------------------------------------------
# POST /generate — valid inputs
# ---------------------------------------------------------------------------
class TestGenerateValid:
    def _post(self, client, **kwargs):
        data = {
            "letters": "1",
            "numbers": "1",
            "symbols": "1",
            "length": "16",
            "count": "1",
        }
        data.update(kwargs)
        return client.post("/generate", data=data)

    def test_returns_200(self, client):
        assert self._post(client).status_code == 200

    def test_single_password_shown(self, client):
        html = self._post(client, count="1").data.decode()
        assert "Generated 1 password" in html

    def test_multiple_passwords_shown(self, client):
        html = self._post(client, count="3").data.decode()
        assert "Generated 3 passwords" in html

    def test_strength_badge_present(self, client):
        html = self._post(client, length="16", count="1").data.decode()
        assert "Strong password" in html

    def test_letters_only(self, client):
        response = client.post("/generate", data={
            "letters": "1",
            "length": "10",
            "count": "1",
        })
        assert response.status_code == 200
        assert "Generated 1 password" in response.data.decode()

    def test_max_length(self, client):
        html = self._post(client, length="128").data.decode()
        assert "Generated 1 password" in html

    def test_min_length(self, client):
        html = self._post(client, length="1").data.decode()
        assert "Generated 1 password" in html

    def test_max_count(self, client):
        html = self._post(client, count="10").data.decode()
        assert "Generated 10 passwords" in html


# ---------------------------------------------------------------------------
# POST /generate — invalid inputs
# ---------------------------------------------------------------------------
class TestGenerateInvalid:
    def test_no_character_type_shows_error(self, client):
        response = client.post("/generate", data={
            "length": "12",
            "count": "1",
        })
        html = response.data.decode()
        assert "at least one character type" in html

    def test_length_too_low_shows_error(self, client):
        response = client.post("/generate", data={
            "letters": "1",
            "length": "0",
            "count": "1",
        })
        html = response.data.decode()
        assert "at least 1" in html

    def test_length_too_high_shows_error(self, client):
        response = client.post("/generate", data={
            "letters": "1",
            "length": "129",
            "count": "1",
        })
        html = response.data.decode()
        assert "at most 128" in html

    def test_non_numeric_length_shows_error(self, client):
        response = client.post("/generate", data={
            "letters": "1",
            "length": "abc",
            "count": "1",
        })
        html = response.data.decode()
        assert "valid password length" in html

    def test_count_out_of_range_shows_error(self, client):
        response = client.post("/generate", data={
            "letters": "1",
            "length": "10",
            "count": "11",
        })
        html = response.data.decode()
        assert "between 1 and 10" in html

    def test_non_numeric_count_shows_error(self, client):
        response = client.post("/generate", data={
            "letters": "1",
            "length": "10",
            "count": "xyz",
        })
        html = response.data.decode()
        assert "valid number of passwords" in html

    def test_errors_preserve_form_values(self, client):
        response = client.post("/generate", data={
            "length": "20",
            "count": "3",
        })
        html = response.data.decode()
        assert 'value="20"' in html
        assert 'value="3"' in html
