import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("case-1.py")


def load_module():
    spec = importlib.util.spec_from_file_location("epam_case_1_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class Case1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_calc_moves_counts_adjustments_for_first_example(self) -> None:
        result = self.module.calc_moves([4, 2, 4, 1, 3, 5])

        self.assertEqual(result, 2)

    def test_calc_moves_returns_zero_for_increasing_values(self) -> None:
        result = self.module.calc_moves([1, 5, 6, 10])

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
