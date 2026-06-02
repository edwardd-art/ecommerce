from product import Product
from smartphone import Smartphone
from lawn_grass import LawnGrass
from mixin import LogMixin


def test_product_inherits_from_mixin():
    """Проверяем, что Product наследует от LogMixin"""
    assert issubclass(Product, LogMixin)


def test_product_logging_on_creation(capsys):
    """Проверяем, что при создании продукта выводится лог"""
    product = Product("Test", "Desc", 100.0, 5)
    captured = capsys.readouterr()
    assert "Product('Test', 'Desc', 100.0, 5)" in captured.out


def test_smartphone_logging_on_creation(capsys):
    """Проверяем, что при создании смартфона выводится лог"""
    phone = Smartphone("Phone", "Desc", 1000.0, 2, 95.0, "M1", 128, "Red")
    captured = capsys.readouterr()
    # Проверяем, что в логе есть название класса и основные параметры
    assert "Smartphone('Phone', 'Desc', 1000.0, 2" in captured.out


def test_lawn_grass_logging_on_creation(capsys):
    """Проверяем, что при создании травы выводится лог"""
    grass = LawnGrass("Grass", "Desc", 500.0, 10, "RU", "7d", "Green")
    captured = capsys.readouterr()
    # Проверяем, что в логе есть название класса и основные параметры
    assert "LawnGrass('Grass', 'Desc', 500.0, 10" in captured.out