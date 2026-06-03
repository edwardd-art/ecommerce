import pytest
from product import Product
from category import Category
from smartphone import Smartphone
from lawn_grass import LawnGrass


def test_category_add_product_valid():
    Category.category_count = 0
    Category.product_count = 0

    p = Product("P1", "D1", 100.0, 1)
    cat = Category("Cat", "Desc", [])
    cat.add_product(p)

    assert len(cat._Category__products) == 1
    assert Category.product_count == 1


def test_category_add_smartphone():
    Category.category_count = 0
    Category.product_count = 0

    phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.0, "M1", 128, "Red")
    cat = Category("Cat", "Desc", [])
    cat.add_product(phone)

    assert len(cat._Category__products) == 1
    assert Category.product_count == 1


def test_category_add_lawn_grass():
    Category.category_count = 0
    Category.product_count = 0

    grass = LawnGrass("Grass", "Desc", 500.0, 10, "RU", "7d", "Green")
    cat = Category("Cat", "Desc", [])
    cat.add_product(grass)

    assert len(cat._Category__products) == 1
    assert Category.product_count == 1


def test_category_add_invalid_type_raises_error():
    cat = Category("Cat", "Desc", [])
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
        cat.add_product("not a product")