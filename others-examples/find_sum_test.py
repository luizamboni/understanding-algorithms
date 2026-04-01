import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("find-sum.py")


def load_module():
    spec = importlib.util.spec_from_file_location("find_sum_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class FindSumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_find_sum_brute_returns_matching_indexes(self) -> None:
        result = self.module.find_sum_brute([1, 2, 4, 7], 11)

        self.assertEqual(result, (2, 3))

    def test_find_sum_optimized_returns_matching_indexes(self) -> None:
        result = self.module.find_sum_optimized([1, 2, 4, 7], 11)

        self.assertEqual(result, (2, 3))


if __name__ == "__main__":
    unittest.main()
