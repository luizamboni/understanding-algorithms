import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("selection-sort.py")


def load_module():
    spec = importlib.util.spec_from_file_location("selection_sort_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class SelectionSortTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_select_smaller_returns_index_of_lowest_value(self) -> None:
        result = self.module.selectSmaller([5, 3, 9, 1, 4])

        self.assertEqual(result, 3)

    def test_sort_by_selection_returns_sorted_values(self) -> None:
        values = [5, 3, 9, 1, 4]

        result = self.module.sortBySelection(values)

        self.assertEqual(result, [1, 3, 4, 5, 9])
        self.assertEqual(values, [])


if __name__ == "__main__":
    unittest.main()
