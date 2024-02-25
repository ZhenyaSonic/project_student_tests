import pytest
from http import HTTPStatus
from fastapi.testclient import TestClient
from app import app  # Подставьте имя вашего модуля FastAPI

client = TestClient(app)


@pytest.mark.parametrize("shop_id", [-1, 0, 1])
def test_feedbacks_endpoints(shop_id):

    endpoint = "/api/v1/feedbacks"
    # Тест для создания отзыва
    response = client.post(f"{endpoint}/")
    assert response.status_code == HTTPStatus.CREATED

    # Тест для получения отзывов о магазине
    response = client.get(f"{endpoint}/shop/{shop_id}/")
    assert response.status_code == HTTPStatus.OK

    # Тест для получения отзывов о продукте
    response = client.get(f"{endpoint}/prod/{shop_id}/")
    assert response.status_code == HTTPStatus.OK
