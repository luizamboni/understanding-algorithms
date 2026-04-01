import contextlib
import importlib.util
import io
import time
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("main.py")


def load_module():
    spec = importlib.util.spec_from_file_location("move_zeros_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    original_sleep = time.sleep
    time.sleep = lambda _seconds: None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(module)
    finally:
        time.sleep = original_sleep
    return module


class MoveZerosTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_my_solution_moves_zeroes_to_the_end(self) -> None:
        result = self.module.my_solution([0, 1, 0, 3, 12])

        self.assertEqual(result, [1, 3, 12, 0, 0])

    def test_course_solution_moves_zeroes_to_the_end(self) -> None:
        result = self.module.course_solution([0, 1, 0, 3, 12])

        self.assertEqual(result, [1, 3, 12, 0, 0])


if __name__ == "__main__":
    unittest.main()
