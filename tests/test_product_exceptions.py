import pytest
from product import Product


def test_product_zero_quantity_raises_value_error():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test", "Desc", 100.0, 0)


def test_product_positive_quantity_ok():
    product = Product("Test", "Desc", 100.0, 5)
    assert product.quantity == 5