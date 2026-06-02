class LogMixin:
    """
    Миксин для логирования создания объектов.
    При создании объекта выводит информацию о классе и параметрах.
    """

    def __init__(self, *args, **kwargs):
        # Формируем строку с параметрами для вывода
        params_repr = ", ".join(repr(arg) for arg in args)
        if kwargs:
            params_repr += ", " + ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())
        print(f"{self.__class__.__name__}({params_repr})")
        super().__init__(*args, **kwargs)