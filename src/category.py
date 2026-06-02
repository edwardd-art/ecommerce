from typing import List
from product import Product


class Category:
    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    __products: List[Product]  # приватный атрибут

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
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result.strip()