import pytest
from base_product import BaseProduct
from product import Product


def test_base_product_is_abstract():
    """Проверяем, что BaseProduct - абстрактный класс"""
    with pytest.raises(TypeError):
        BaseProduct()  # cannot instantiate abstract class


def test_product_inherits_from_base():
    """Проверяем, что Product наследует от BaseProduct"""
    assert issubclass(Product, BaseProduct)