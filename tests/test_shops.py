from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from app import appI


client = TestClient(app)


@pytest.mark.parametrize("endpoint", [
    ("shop/1/"),
    ("category/1/"),
    ("placement/1/"),
    ("product/1/"),
    ("shop/1/favorite/"),
    ("shop/1/favorite/")
])
def test_endpoints(endpoint):
    response = client.get(f"api/v1/shops/{endpoint[0]}")
    assert response.status_code == HTTPStatus.OK
