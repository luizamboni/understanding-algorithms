import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("dijkstra.py")


def load_module():
    spec = importlib.util.spec_from_file_location("dijkstra_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class DijkstraTests(unittest.TestCase):
    def test_module_computes_expected_final_costs(self) -> None:
        module = load_module()

        self.assertEqual(module.custos, {"a": 5, "b": 2, "fim": 6})
        self.assertEqual(module.processados, ["b", "a", "fim"])

    def test_ache_o_custo_mais_baixo_skips_processed_nodes(self) -> None:
        module = load_module()
        module.processados[:] = ["b"]

        result = module.ache_o_custo_mais_baixo({"a": 5, "b": 2, "fim": 6})

        self.assertEqual(result, "a")


if __name__ == "__main__":
    unittest.main()
