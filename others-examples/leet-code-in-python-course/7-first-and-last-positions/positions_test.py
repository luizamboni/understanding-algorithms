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


class FirstAndLastPositionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.brute = load_module("brute-force.py", "first_last_bruteforce")
        cls.optimized = load_module("optimized.py", "first_last_optimized")

    def test_bruteforce_returns_first_and_last_indexes(self) -> None:
        result = self.brute.find_first_and_last([10, 11, 11, 11, 14, 15], 11)

        self.assertEqual(result, [1, 3])

    def test_optimized_returns_not_found_when_target_is_absent(self) -> None:
        result = self.optimized.find_first_and_last([10, 11, 11, 11, 14, 15], 12)

        self.assertEqual(result, [-1, -1])


if __name__ == "__main__":
    unittest.main()
