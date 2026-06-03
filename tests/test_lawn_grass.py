import pytest
from lawn_grass import LawnGrass


def test_lawn_grass_initialization():
    grass = LawnGrass(
        "Green Grass", "Soft grass", 500.0, 20,
        "Russia", "7 days", "Green"
    )
    assert grass.name == "Green Grass"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Russia"
    assert grass.germination_period == "7 days"
    assert grass.color == "Green"


def test_lawn_grass_str():
    grass = LawnGrass(
        "Elite Grass", "Dark green", 450.0, 15,
        "USA", "5 days", "Dark Green"
    )
    expected = "Elite Grass, 450.0 руб. Остаток: 15 шт."
    assert str(grass) == expected


def test_lawn_grass_add_same_type():
    g1 = LawnGrass("G1", "D1", 100.0, 10, "RU", "7d", "Green")
    g2 = LawnGrass("G2", "D2", 200.0, 2, "US", "5d", "Dark")
    assert g1 + g2 == 100 * 10 + 200 * 2  # 1400