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
    assert product.price == 100.0


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


def test_product_str():
    product = Product("iPhone 15", "512GB", 120000.0, 10)
    expected = "iPhone 15, 120000.0 руб. Остаток: 10 шт."
    assert str(product) == expected


def test_product_add():
    p1 = Product("Phone", "Desc", 1000.0, 2)
    p2 = Product("Tablet", "Desc", 500.0, 3)
    # 1000*2 + 500*3 = 2000 + 1500 = 3500
    assert p1 + p2 == 3500.0
    assert p2 + p1 == 3500.0  # коммутативность


def test_product_add_single():
    p1 = Product("Phone", "Desc", 1000.0, 2)
    p2 = Product("Phone2", "Desc", 0.0, 5)
    assert p1 + p2 == 2000.0  # второй продукт даёт 0