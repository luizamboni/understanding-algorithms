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


class BinaryAddingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mine = load_module("my-solution.py", "binary_adding_mine")
        cls.official = load_module("official-solution.py", "binary_adding_official")

    def test_my_solution_sums_binary_strings(self) -> None:
        self.assertEqual(self.mine.sumBinaries("1111", "1101"), "11100")

    def test_official_solution_sums_binary_strings(self) -> None:
        self.assertEqual(self.official.sumBinaries("1011", "1101"), "11000")


if __name__ == "__main__":
    unittest.main()
