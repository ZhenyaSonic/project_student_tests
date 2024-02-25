from http import HTTPStatus
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)


@pytest.mark.parametrize("endpoint, method, data", [
    (
        "api/v1/users/auth/", "post",
        {
            "email": "test@email.com",
            "password": "testpassword"
        }),

    (
        "api/v1/users/reg/", "post",
        {
            "email": "test@email.com",
            "password": "testpassword",
            "name": "testname"
        }),
    (
        "api/v1/users/user/1/", "get",
        {
            "id": "1",
            "email": "test@email.com",
        }),
])
def test_user_endpoints(endpoint, method, data):
    if method == "post":
        response = client.post(endpoint, json=data)
    elif method == "get":
        response = client.get(endpoint)
    assert response.status_code == HTTPStatus.OK
