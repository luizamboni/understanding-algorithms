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


class MaxSubstringLenghtTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.brute = load_module("brute-force.py", "max_substring_bruteforce")
        cls.optimized = load_module("optmized.py", "max_substring_optimized")

    def test_bruteforce_returns_longest_unique_window(self) -> None:
        result = self.brute.max_substring_lenght("abcabcbb")

        self.assertEqual(result, 3)

    def test_optimized_returns_longest_unique_window(self) -> None:
        result = self.optimized.max_substring_lenght("pwwkew")

        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
