import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("quick-sort.py")


def load_module():
    spec = importlib.util.spec_from_file_location("quick_sort_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class QuickSortTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_quicksort_sorts_unsorted_values(self) -> None:
        result = self.module.quicksort([7, 1, 5, 3])

        self.assertEqual(result, [1, 3, 5, 7])

    def test_quicksort2_sorts_values_with_duplicates(self) -> None:
        result = self.module.quicksort2([4, 2, 4, 1, 3])

        self.assertEqual(result, [1, 2, 3, 4, 4])


if __name__ == "__main__":
    unittest.main()
