from product import Product


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str
    ):
        # Передаём ВСЕ аргументы в родительский класс
        super().__init__(name, description, price, quantity, efficiency, model, memory, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color