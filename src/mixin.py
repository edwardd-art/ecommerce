class LogMixin:
    """
    Миксин для логирования создания объектов.
    При создании объекта выводит в консоль информацию о классе и параметрах.
    """

    def __init__(self, *args, **kwargs):
        # Формируем строку с параметрами для вывода
        params_repr = ", ".join(repr(arg) for arg in args)
        if kwargs:
            params_repr += ", " + ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())
        print(f"{self.__class__.__name__}({params_repr})")
        # НЕ вызываем super().__init__(), так как object не принимает аргументы
        # super().__init__(*args, **kwargs)  # ЭТУ СТРОКУ УДАЛИТЬ ИЛИ ЗАКОММЕНТИРОВАТЬ