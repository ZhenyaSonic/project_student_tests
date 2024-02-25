from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_endpoints():
    # Test POST to `api/v1/admin/users/auth/`
    response = client.post("/api/v1/admin/users/auth/", json={"EMAIL": "test@test.com", "PASSWORD": "testpassword"})
    assert response.status_code == HTTPStatus.OK or response.status_code == HTTPStatus.CREATED

    # Test POST to `api/v1/admin/users/reg/`
    response = client.post("/api/v1/admin/users/reg/", json={"EMAIL": "test@test.com", "PASSWORD": "testpassword", "NAME": "Test", "ISADMIN": True, "SHOP_ID": 1})
    assert response.status_code == HTTPStatus.OK or response.status_code == HTTPStatus.CREATED

    # Test POST to `api/v1/admin/shops/`
    response = client.post("/api/v1/admin/shops/", json={
        "NAME": "Test Shop",
        "PLACEMENT": "Test Place",
        "DESCRIPTION": "Test Description",
        "IMAGE": "test.jpg",
        "CONTACT_PHONE": "1234567890"})
    assert response.status_code == HTTPStatus.CREATED

    # Test DELETE to `api/v1/admin/shops/{shop_id}/`
    response = client.delete("/api/v1/admin/shops/1")
    assert response.status_code == HTTPStatus.NO_CONTENT

    # Test POST to `api/v1/admin/categories/`
    response = client.post("/api/v1/admin/categories/", json={"NAME": "Test Category"})
    assert response.status_code == HTTPStatus.CREATED

    # Test DELETE to `api/v1/admin/categories/{category_id}/`
    response = client.delete("/api/v1/admin/categories/1")
    assert response.status_code == HTTPStatus.NO_CONTENT

    # Test POST to `api/v1/admin/products/`
    response = client.post("/api/v1/admin/products/", json={"NAME": "Test Product", "SHOP_ID": 1, "IMAGE": "test.jpg", "DESCRIPTION": "Test Description", "ISDELIVERABLE": True})
    assert response.status_code == HTTPStatus.CREATED

    # Test DELETE to `api/v1/admin/products/{product_id}/`
    response = client.delete("/api/v1/admin/products/1")
    assert response.status_code == HTTPStatus.NO_CONTENT

    # Test DELETE to `api/v1/admin/feedbacks/{feedback_id}/`
    response = client.delete("/api/v1/admin/feedbacks/1")
    assert response.status_code == HTTPStatus.NO_CONTENT
