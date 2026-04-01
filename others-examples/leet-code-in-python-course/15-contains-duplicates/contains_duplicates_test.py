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


class ContainsDuplicatesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.brute = load_module("brute-force.py", "contains_duplicates_bruteforce")
        cls.optimized = load_module("optmized.py", "contains_duplicates_optimized")

    def test_bruteforce_detects_duplicates(self) -> None:
        self.assertTrue(self.brute.check([2, 1, 3, 1]))

    def test_optimized_returns_false_for_unique_values(self) -> None:
        self.assertFalse(self.optimized.check([2, 1, 3, 4]))


if __name__ == "__main__":
    unittest.main()
