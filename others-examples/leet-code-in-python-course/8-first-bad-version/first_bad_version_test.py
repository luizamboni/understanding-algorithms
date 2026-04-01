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


class FirstBadVersionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.brute = load_module("brute-force.py", "first_bad_bruteforce")
        cls.optimized = load_module("optimized.py", "first_bad_optimized")
        cls.official = load_module("official-optimized.py", "first_bad_official")

    def test_bruteforce_returns_first_wrong_version(self) -> None:
        result = self.brute.findTheFirstWrongVersion()

        self.assertEqual(result, 3)

    def test_optimized_returns_first_wrong_version(self) -> None:
        result = self.optimized.findTheFirstWrongVersion()

        self.assertEqual(result, 7)

    def test_official_solution_returns_first_bad_version(self) -> None:
        result = self.official.Solution().firstBadVersion(10)

        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
