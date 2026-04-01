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


class MissingNumberTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.brute = load_module("brute-force.py", "missing_number_bruteforce")
        cls.optimized = load_module("optimized.py", "missing_number_optimized")

    def test_bruteforce_finds_missing_value(self) -> None:
        result = self.brute.find_missing_number([3, 0, 1])

        self.assertEqual(result, 2)

    def test_optimized_finds_missing_value(self) -> None:
        result = self.optimized.find_missing_number([0, 1])

        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
