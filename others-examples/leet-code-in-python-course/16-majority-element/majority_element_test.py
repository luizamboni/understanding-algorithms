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


class MajorityElementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.brute = load_module("brute-force.py", "majority_bruteforce")
        cls.optimized = load_module("optimized.py", "majority_optimized")
        cls.very_optimized = load_module("very-optimized.py", "majority_very_optimized")

    def test_bruteforce_returns_majority_element(self) -> None:
        self.assertEqual(self.brute.find_majority([2, 1, 3, 1, 1]), 1)

    def test_optimized_returns_majority_element(self) -> None:
        self.assertEqual(self.optimized.find_majority([2, 1, 3, 1, 1]), 1)

    def test_boyer_moore_returns_majority_element(self) -> None:
        self.assertEqual(self.very_optimized.find_majority([2, 1, 3, 1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
