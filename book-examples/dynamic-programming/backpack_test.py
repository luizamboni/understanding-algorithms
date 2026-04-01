import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("backpack.py")


def load_module():
    spec = importlib.util.spec_from_file_location("backpack_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class BackpackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_pick_the_best_returns_best_value_for_book_example(self) -> None:
        result = self.module.pick_the_best(
            [
                {"c": 3, "v": 10, "n": "agua"},
                {"c": 1, "v": 3, "n": "livros"},
                {"c": 2, "v": 9, "n": "comida"},
                {"c": 2, "v": 5, "n": "casaco"},
                {"c": 1, "v": 6, "n": "camera"},
            ],
            6,
        )

        self.assertEqual(result, 25)

    def test_pick_the_best_returns_best_value_for_small_capacity(self) -> None:
        result = self.module.pick_the_best(
            [
                {"c": 4, "v": 30, "n": "radio"},
                {"c": 3, "v": 20, "n": "notebook"},
                {"c": 1, "v": 15, "n": "violao"},
                {"c": 1, "v": 20, "n": "iphone"},
                {"c": 1, "v": 10, "n": "mp3 player"},
            ],
            4,
        )

        self.assertEqual(result, 45)


if __name__ == "__main__":
    unittest.main()
