# tests/test_product.py
import pytest
from product import Product


def test_product_initialization():
    product = Product("Test Phone", "Test Description", 999.99, 10)
    assert product.name == "Test Phone"
    assert product.description == "Test Description"
    assert product.price == 999.99
    assert product.quantity == 10


def test_product_with_zero_price():
    product = Product("Free Item", "Description", 0.0, 5)
    assert product.price == 0.0


def test_product_with_negative_price():
    product = Product("Negative Price", "Description", -50.0, 1)
    assert product.price == -50.0


def test_product_attributes_types():
    product = Product("Name", "Desc", 99.99, 5)
    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)


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
    assert product.price == 100.0


def test_product_str():
    product = Product("Phone", "Desc", 120000.0, 10)
    expected = "Phone, 120000.0 руб. Остаток: 10 шт."
    assert str(product) == expected


def test_product_add():
    p1 = Product("P1", "D1", 1000.0, 2)
    p2 = Product("P2", "D2", 500.0, 3)
    assert p1 + p2 == 3500.0