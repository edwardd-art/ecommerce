import pytest
from product import Product
from category import Category


def test_middle_price_with_products():
    p1 = Product("P1", "D1", 100.0, 2)
    p2 = Product("P2", "D2", 200.0, 3)
    p3 = Product("P3", "D3", 300.0, 1)
    cat = Category("Cat", "Desc", [p1, p2, p3])
    assert cat.middle_price() == 200.0


def test_middle_price_empty_category():
    cat = Category("Empty", "No products", [])
    assert cat.middle_price() == 0.0


def test_middle_price_single_product():
    p = Product("P1", "D1", 150.0, 5)
    cat = Category("Cat", "Desc", [p])
    assert cat.middle_price() == 150.0