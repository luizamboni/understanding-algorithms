import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("case-2.py")


def load_module():
    spec = importlib.util.spec_from_file_location("epam_case_2_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class Case2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_calculate_movies_matches_first_example(self) -> None:
        result = self.module.calculate_movies([7, 15, 10, 8])

        self.assertEqual(result, 7)

    def test_calculate_movies_returns_negative_one_when_balance_is_impossible(self) -> None:
        result = self.module.calculate_movies([7, 14, 10])

        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
