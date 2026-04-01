import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


def load_module(filename: str, module_name: str):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class FourSumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.brute = load_module("brute-force.py", "four_sum_bruteforce")
        cls.optimized = load_module("optimized.py", "four_sum_optimized")

    def test_bruteforce_counts_zero_sum_quadruples(self) -> None:
        result = self.brute.four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2])

        self.assertEqual(result, 2)

    def test_optimized_counts_zero_sum_quadruples(self) -> None:
        result = self.optimized.four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2])

        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
