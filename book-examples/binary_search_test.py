import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("binary-search.py")


def load_module():
    spec = importlib.util.spec_from_file_location("binary_search_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class BinarySearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_regular_search_returns_index_for_present_value(self) -> None:
        result = self.module.regular_search([1, 2, 3, 4, 5], 4)

        self.assertEqual(result, 3)

    def test_binary_search_returns_index_for_present_value(self) -> None:
        result = self.module.binary_search([1, 2, 3, 4, 5], 4)

        self.assertEqual(result, 3)

    def test_binary_search_returns_none_for_missing_value(self) -> None:
        result = self.module.binary_search([1, 2, 3, 4, 5], 8)

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
