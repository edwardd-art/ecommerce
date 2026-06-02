import pytest
from product import Product
from category import Category


def test_category_initialization():
    p1 = Product("P1", "D1", 100.0, 1)
    p2 = Product("P2", "D2", 200.0, 2)
    cat = Category("Cat", "Desc", [p1, p2])
    assert cat.name == "Cat"
    assert len(cat._Category__products) == 2


def test_add_product():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("P1", "D1", 100.0, 1)
    cat = Category("Cat", "Desc", [p1])
    assert Category.product_count == 1

    p2 = Product("P2", "D2", 200.0, 2)
    cat.add_product(p2)
    assert len(cat._Category__products) == 2
    assert Category.product_count == 2


def test_products_property():
    p1 = Product("Phone", "Smartphone", 50000.0, 10)
    p2 = Product("Tablet", "iPad", 30000.0, 5)
    cat = Category("Electronics", "Devices", [p1, p2])

    expected = (
        "Phone, 50000.0 руб. Остаток: 10 шт.\n"
        "Tablet, 30000.0 руб. Остаток: 5 шт."
    )
    assert cat.products == expected


def test_products_property_empty():
    cat = Category("Empty", "No products", [])
    assert cat.products == ""


def test_product_count_after_add():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("P1", "D1", 100.0, 1)
    cat = Category("Cat", "Desc", [p1])
    assert Category.product_count == 1

    p2 = Product("P2", "D2", 200.0, 2)
    cat.add_product(p2)
    assert Category.product_count == 2