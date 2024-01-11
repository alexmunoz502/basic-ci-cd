import pytest
from litestar.testing import TestClient
from litestar.status_codes import HTTP_200_OK
from src.app import app


@pytest.fixture(scope="function")
def test_client() -> TestClient:
    return TestClient(app=app)


def test_index_message(test_client: TestClient) -> None:
    with test_client as client:
        response = client.get("/")
        assert response.status_code == HTTP_200_OK
        assert response.text == "Hello, World!"


def test_greeting_message__default(test_client: TestClient) -> None:
    with test_client as client:
        response = client.get("/greeting")
        assert response.status_code == HTTP_200_OK
        assert response.text == "Hello, World!"


def test_greeting_message(test_client: TestClient) -> None:
    with test_client as client:
        response = client.get("/greeting?name=alex")
        assert response.status_code == HTTP_200_OK
        assert response.text == "Hello, Alex!"
