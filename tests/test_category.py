import pytest
from product import Product
from category import Category


class TestCategory:
    """Тесты для класса Category"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_initialization(self):
        """Тест корректной инициализации категории"""
        product1 = Product("Product 1", "Desc 1", 100.0, 5)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)
        category = Category("Electronics", "Electronic devices", [product1, product2])

        assert category.name == "Electronics"
        assert category.description == "Electronic devices"
        assert len(category.products) == 2
        assert category.products[0] == product1
        assert category.products[1] == product2

    def test_category_count_increments(self):
        """Тест автоматического увеличения счетчика категорий"""
        p1 = Product("P1", "D1", 100.0, 1)
        p2 = Product("P2", "D2", 200.0, 2)

        c1 = Category("Cat1", "Desc1", [p1])
        assert Category.category_count == 1
        assert Category.product_count == 1

        c2 = Category("Cat2", "Desc2", [p1, p2])
        assert Category.category_count == 2
        assert Category.product_count == 3

    def test_product_count_multiple_categories(self):
        """Тест подсчета продуктов в нескольких категориях"""
        p1 = Product("P1", "D1", 100.0, 1)
        p2 = Product("P2", "D2", 200.0, 2)
        p3 = Product("P3", "D3", 300.0, 3)

        Category("Cat1", "Desc1", [p1])
        Category("Cat2", "Desc2", [p1, p2, p3])

        assert Category.category_count == 2
        assert Category.product_count == 4

    def test_category_with_empty_products(self):
        """Тест категории с пустым списком продуктов"""
        category = Category("Empty Category", "No products", [])
        assert len(category.products) == 0
        assert Category.category_count > 0
        assert Category.product_count == 0

    def test_category_attributes_types(self):
        """Тест типов атрибутов категории"""
        product = Product("P1", "D1", 100.0, 1)
        category = Category("Name", "Desc", [product])

        assert isinstance(category.name, str)
        assert isinstance(category.description, str)
        assert isinstance(category.products, list)
        assert isinstance(Category.category_count, int)
        assert isinstance(Category.product_count, int)

    def test_multiple_categories_same_products(self):
        """Тест: один и тот же продукт в разных категориях"""
        p = Product("Universal", "Desc", 100.0, 10)

        Category("Cat1", "Desc1", [p])
        Category("Cat2", "Desc2", [p])

        assert Category.category_count == 2
        assert Category.product_count == 2  # Продукт считается дважды

    def test_products_are_objects(self):
        """Тест: в списке продуктов хранятся объекты Product"""
        p1 = Product("P1", "D1", 100.0, 1)
        p2 = Product("P2", "D2", 200.0, 2)
        category = Category("Cat", "Desc", [p1, p2])

        assert isinstance(category.products[0], Product)
        assert isinstance(category.products[1], Product)