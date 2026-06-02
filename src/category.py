from typing import List
from product import Product


class Category:
    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    __products: List[Product]

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для вывода списка продуктов в строковом формате"""
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result.strip()

    def __str__(self) -> str:
        """
        Строковое представление категории.
        Количество продуктов = сумма quantity всех продуктов в категории
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."