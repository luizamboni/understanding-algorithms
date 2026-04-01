import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("solution.py")


def load_module():
    spec = importlib.util.spec_from_file_location("group_anagrams_solution", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class GroupAnagramsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_groups_words_by_sorted_signature(self) -> None:
        result = self.module.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        normalized = sorted(sorted(group) for group in result)

        self.assertEqual(normalized, [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])


if __name__ == "__main__":
    unittest.main()
