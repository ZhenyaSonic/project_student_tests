from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from app import app  # Подставьте имя вашего модуля FastAPI

client = TestClient(app)


@pytest.mark.parametrize("product_id", [-1, 0, 1])
def test_product_endpoints(product_id):

    endpoint = "/api/v1/products"
    # Тест для получения информации о продукте
    response = client.get(f"{endpoint}/{product_id}/")
    assert response.status_code == HTTPStatus.OK

    # Тест для получения информации о магазине
    response = client.get(f"{endpoint}/shop/{product_id}/")
    assert response.status_code == HTTPStatus.OK

    # Тест для добавления продукта в корзину
    response = client.post(f"{endpoint}/{product_id}/shopping_cart/")
    assert response.status_code == HTTPStatus.CREATED

    # Тест для удаления продукта из корзины
    response = client.delete(f"{endpoint}/{product_id}/shopping_cart/")
    assert response.status_code == HTTPStatus.NO_CONTENT
