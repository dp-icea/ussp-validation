from os import environ


# Example TC
def test_api_url() -> None:
    api_url = environ.get("USSP_URL")
    assert api_url == "https://localhost:8000"
