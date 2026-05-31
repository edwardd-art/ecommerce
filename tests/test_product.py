import pytest
from product import Product


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        """Тест корректной инициализации продукта"""
        product = Product("Test Phone", "Test Description", 999.99, 10)

        assert product.name == "Test Phone"
        assert product.description == "Test Description"
        assert product.price == 999.99
        assert product.quantity == 10

    def test_product_with_zero_price(self):
        """Тест продукта с нулевой ценой"""
        product = Product("Free Item", "Description", 0.0, 5)
        assert product.price == 0.0

    def test_product_with_zero_quantity(self):
        """Тест продукта с нулевым количеством"""
        product = Product("Out of Stock", "Description", 100.0, 0)
        assert product.quantity == 0

    def test_product_with_negative_price(self):
        """Тест продукта с отрицательной ценой (допустимо, но не логично)"""
        product = Product("Negative Price", "Description", -50.0, 1)
        assert product.price == -50.0

    def test_product_attributes_types(self):
        """Тест типов атрибутов продукта"""
        product = Product("Name", "Desc", 99.99, 5)
        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)