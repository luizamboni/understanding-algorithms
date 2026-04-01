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


class CountPrimesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.brute = load_module("brute-force.py", "count_primes_bruteforce")
        cls.optimized = load_module("optimized.py", "count_primes_optimized")

    def test_bruteforce_counts_primes_up_to_input(self) -> None:
        result = self.brute.count_primes(13)

        self.assertEqual(result, 5)

    def test_optimized_counts_primes_below_input(self) -> None:
        result = self.optimized.count_primes(13)

        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
