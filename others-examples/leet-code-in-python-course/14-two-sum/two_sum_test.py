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


class TwoSumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.brute = load_module("brute-force.py", "two_sum_bruteforce")
        cls.mine = load_module("my-optimized.py", "two_sum_mine")
        cls.official = load_module("official-optimized.py", "two_sum_official")

    def test_bruteforce_returns_matching_pair(self) -> None:
        self.assertEqual(self.brute.find_two_sum(26), (1, 3))

    def test_my_solution_returns_matching_pair(self) -> None:
        self.assertEqual(self.mine.find_two_sum(26), (1, 3))

    def test_official_solution_returns_matching_pair(self) -> None:
        self.assertEqual(self.official.find_two_sum(26), (3, 1))


if __name__ == "__main__":
    unittest.main()
