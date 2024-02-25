from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from app import app  # Подставьте имя вашего модуля FastAPI

client = TestClient(app)


@pytest.mark.parametrize("user_id", [-1, 0, 1])
def test_orders_endpoints(user_id):

    endpoint = "/api/v1/orders"
    # Тест для создания заказа
    response = client.post("{endpoint}/")
    assert response.status_code == HTTPStatus.CREATED

    # Тест для получения информации о заказе
    response = client.get(f"{endpoint}/{user_id}/")
    assert response.status_code == HTTPStatus.OK
