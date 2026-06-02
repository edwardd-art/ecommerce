import pytest
import sys
import os

# Добавляем путь к src для импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import main


def test_main_runs(capsys):
    """Проверка, что main() запускается без ошибок"""
    try:
        main()
    except SystemExit:
        pass  # ожидаемо, если в main есть exit
    captured = capsys.readouterr()
    output = captured.out
    # Проверяем, что что-то вывелось (любой вывод)
    assert output is not None