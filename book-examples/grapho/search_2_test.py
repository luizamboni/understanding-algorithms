import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("search-2.py")


def load_module():
    spec = importlib.util.spec_from_file_location("search_2_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class Search2Tests(unittest.TestCase):
    def test_module_queue_search_reaches_goal_node(self) -> None:
        module = load_module()

        self.assertEqual(module.ja_visitado, ["jato", "tato", "gato", "gato", "chato", "grato"])
        self.assertEqual(module.fila, ["grato", "gado", "gado"])

    def test_e_o_fim_returns_true_only_for_goal(self) -> None:
        module = load_module()

        self.assertTrue(module.e_o_fim("gado"))
        self.assertFalse(module.e_o_fim("tato"))


if __name__ == "__main__":
    unittest.main()
