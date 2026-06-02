import pytest
from product import Product
from category import Category


def test_category_initialization():
    """Тест корректной инициализации категории"""
    product1 = Product("Product 1", "Desc 1", 100.0, 5)
    product2 = Product("Product 2", "Desc 2", 200.0, 3)
    category = Category("Electronics", "Electronic devices", [product1, product2])

    assert category.name == "Electronics"
    assert category.description == "Electronic devices"
    assert "Product 1" in category.products
    assert "Product 2" in category.products
    assert len(category._Category__products) == 2


def test_category_attributes_types():
    """Тест типов атрибутов категории"""
    product = Product("P1", "D1", 100.0, 1)
    category = Category("Name", "Desc", [product])

    assert isinstance(category.name, str)
    assert isinstance(category.description, str)
    assert isinstance(category.products, str)


def test_products_are_objects():
    """Тест: в списке продуктов хранятся объекты Product"""
    p1 = Product("P1", "D1", 100.0, 1)
    p2 = Product("P2", "D2", 200.0, 2)
    category = Category("Cat", "Desc", [p1, p2])

    assert isinstance(category._Category__products[0], Product)
    assert isinstance(category._Category__products[1], Product)