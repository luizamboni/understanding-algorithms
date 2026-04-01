import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("recursion.py")


def load_module():
    spec = importlib.util.spec_from_file_location("recursion_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class RecursionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_suma_returns_sum_of_values(self) -> None:
        result = self.module.suma([2, 4, 6])

        self.assertEqual(result, 12)

    def test_cardinality_returns_number_of_values(self) -> None:
        result = self.module.cardinality([2, 4, 6, 8])

        self.assertEqual(result, 4)

    def test_maximum_returns_largest_value(self) -> None:
        result = self.module.maximum([2, 9, 4, 6])

        self.assertEqual(result, 9)

    def test_binary_search_returns_matching_value(self) -> None:
        result = self.module.binary_search([1, 2, 4, 5, 6, 8, 9], 5)

        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
