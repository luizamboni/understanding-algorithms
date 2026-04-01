import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("solution.py")


def load_module():
    spec = importlib.util.spec_from_file_location("min_window_solution", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class MinWindowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_returns_known_minimum_window_for_classic_example(self) -> None:
        self.assertEqual(self.module.find_min_window("ADOBECODEBANCC", "ABC"), "BANC")

    def test_returns_known_window_for_shade_example(self) -> None:
        self.assertEqual(self.module.find_min_window("asdhnsshadeeweq", "shade"), "shade")


if __name__ == "__main__":
    unittest.main()
