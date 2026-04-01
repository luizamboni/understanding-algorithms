import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("backpack-2.py")


def load_module():
    spec = importlib.util.spec_from_file_location("backpack_2_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class Backpack2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_knapsack_returns_known_example_value(self) -> None:
        result = self.module.knapsack([60, 100, 120], [10, 20, 30], 50)

        self.assertEqual(result, 220)

    def test_knapsack_returns_zero_for_zero_capacity(self) -> None:
        result = self.module.knapsack([60, 100], [10, 20], 0)

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
