import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("solution.py")


def load_module():
    spec = importlib.util.spec_from_file_location("lru_cache_solution", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class LRUCacheTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_get_returns_value_for_recent_key(self) -> None:
        cache = self.module.LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)

        self.assertEqual(cache.get(1), 10)

    def test_put_evicts_least_recently_used_key(self) -> None:
        cache = self.module.LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.get(1)
        cache.put(3, 30)

        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 30)


if __name__ == "__main__":
    unittest.main()
