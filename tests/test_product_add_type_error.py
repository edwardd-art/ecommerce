import pytest
from product import Product
from smartphone import Smartphone
from lawn_grass import LawnGrass


def test_product_add_different_types():
    p1 = Product("Prod", "Desc", 100.0, 2)
    p2 = Smartphone("Phone", "Desc", 200.0, 3, 90.0, "M1", 128, "Red")

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = p1 + p2


def test_smartphone_grass_add():
    phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.0, "M1", 128, "Red")
    grass = LawnGrass("Grass", "Desc", 500.0, 10, "RU", "7d", "Green")

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = phone + grass