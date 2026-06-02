import pytest
from product import Product


def test_product_initialization():
    product = Product("Test", "Desc", 100.0, 5)
    assert product.name == "Test"
    assert product.price == 100.0
    assert product.quantity == 5


def test_product_price_getter():
    product = Product("Test", "Desc", 100.0, 5)
    assert product.price == 100.0


def test_product_price_setter_positive():
    product = Product("Test", "Desc", 100.0, 5)
    product.price = 150.0
    assert product.price == 150.0


def test_product_price_setter_negative(capsys):
    product = Product("Test", "Desc", 100.0, 5)
    product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0  # цена не изменилась


def test_product_price_setter_zero(capsys):
    product = Product("Test", "Desc", 100.0, 5)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0


def test_new_product_classmethod():
    data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
    product = Product.new_product(data)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    assert product.quantity == 5