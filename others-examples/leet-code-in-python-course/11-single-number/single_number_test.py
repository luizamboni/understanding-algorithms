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


class SingleNumberTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.brute = load_module("brute-force.py", "single_number_bruteforce")
        cls.optimized = load_module("optimized-1.py", "single_number_optimized")
        cls.bit_better = load_module("bit-better.py", "single_number_bitbetter")

    def test_bruteforce_finds_unique_value(self) -> None:
        self.assertEqual(self.brute.single_number([4, 4, 2, 2, 3]), 3)

    def test_optimized_finds_unique_value(self) -> None:
        self.assertEqual(self.optimized.single_number([4, 4, 2, 2, 1]), 1)

    def test_bit_trick_finds_unique_value(self) -> None:
        self.assertEqual(self.bit_better.single_number([4, 4, 2, 2, 3]), 3)


if __name__ == "__main__":
    unittest.main()
