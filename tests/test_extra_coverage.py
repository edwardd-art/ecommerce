import pytest
from product import Product
from category import Category


def test_product_price_setter_zero():
    """Проверка сеттера с нулевой ценой"""
    p = Product("Test", "Desc", 100.0, 5)
    p.price = 0
    assert p.price == 100.0  # цена не изменилась


def test_product_price_setter_negative():
    """Проверка сеттера с отрицательной ценой"""
    p = Product("Test", "Desc", 100.0, 5)
    p.price = -50
    assert p.price == 100.0  # цена не изменилась


def test_category_products_property():
    """Проверка геттера products (строка)"""
    p1 = Product("P1", "D1", 100.0, 2)
    p2 = Product("P2", "D2", 200.0, 3)
    cat = Category("Cat", "Desc", [p1, p2])

    result = cat.products
    assert "P1, 100.0 руб. Остаток: 2 шт." in result
    assert "P2, 200.0 руб. Остаток: 3 шт." in result


def test_category_str():
    """Проверка строкового представления категории"""
    p1 = Product("P1", "D1", 100.0, 5)
    p2 = Product("P2", "D2", 200.0, 3)
    cat = Category("Electronics", "Devices", [p1, p2])

    expected = "Electronics, количество продуктов: 8 шт."
    assert str(cat) == expected