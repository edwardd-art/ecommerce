class LogMixin:
    """
    Миксин для логирования создания объектов.
    """

    def __init__(self, *args, **kwargs):
        params_repr = ", ".join(repr(arg) for arg in args)
        if kwargs:
            params_repr += ", " + ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())
        print(f"{self.__class__.__name__}({params_repr})")
        # Не вызываем super().__init__, так как в конце цепочки object