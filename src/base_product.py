from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта"""
        pass

    @abstractmethod
    def __add__(self, other: 'BaseProduct') -> float:
        """Сложение продуктов (общая стоимость)"""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер для цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой"""
        pass