import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("fibonacci.py")


def load_module():
    spec = importlib.util.spec_from_file_location("fibonacci_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class FibonacciTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_fibonacci_returns_ninth_value(self) -> None:
        result = self.module.fibonacci(9)

        self.assertEqual(result, 34)

    def test_fibonacci_returns_first_value(self) -> None:
        result = self.module.fibonacci(1)

        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
