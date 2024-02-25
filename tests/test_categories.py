from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


@pytest.mark.parametrize("endpoint", [
    ("/"),
    ("category/1/")
])
def test_category_endpoints(endpoint):
    response = client.get(f"api/v1/categories/{endpoint[0]}")
    assert response.status_code == HTTPStatus.OK
