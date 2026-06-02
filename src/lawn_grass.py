from product import Product


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str
    ):
        # Передаём ВСЕ аргументы в родительский класс
        super().__init__(name, description, price, quantity, country, germination_period, color)
        self.country = country
        self.germination_period = germination_period
        self.color = color