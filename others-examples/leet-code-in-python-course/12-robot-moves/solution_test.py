import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("solution.py")


def load_module():
    spec = importlib.util.spec_from_file_location("robot_moves_solution", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class RobotMovesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_returns_true_when_robot_comes_back_to_origin(self) -> None:
        self.assertTrue(self.module.has_robot_returned("UDLR"))

    def test_returns_false_when_robot_does_not_come_back(self) -> None:
        self.assertFalse(self.module.has_robot_returned("UUDL"))


if __name__ == "__main__":
    unittest.main()
