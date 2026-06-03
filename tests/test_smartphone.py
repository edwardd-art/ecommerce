import pytest
from smartphone import Smartphone


def test_smartphone_initialization():
    phone = Smartphone(
        "iPhone 15", "512GB", 120000.0, 10,
        98.5, "15", 512, "Black"
    )
    assert phone.name == "iPhone 15"
    assert phone.price == 120000.0
    assert phone.quantity == 10
    assert phone.efficiency == 98.5
    assert phone.model == "15"
    assert phone.memory == 512
    assert phone.color == "Black"


def test_smartphone_str():
    phone = Smartphone(
        "Samsung", "256GB", 80000.0, 5,
        95.0, "S23", 256, "Gray"
    )
    expected = "Samsung, 80000.0 руб. Остаток: 5 шт."
    assert str(phone) == expected


def test_smartphone_add_same_type():
    p1 = Smartphone("Phone1", "Desc", 1000.0, 2, 90.0, "M1", 128, "Red")
    p2 = Smartphone("Phone2", "Desc", 500.0, 3, 85.0, "M2", 256, "Blue")
    assert p1 + p2 == 1000 * 2 + 500 * 3  # 3500