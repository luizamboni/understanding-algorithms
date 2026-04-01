import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("words-comparison.py")


def load_module():
    spec = importlib.util.spec_from_file_location("words_comparison_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class WordsComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_find_similarity_returns_common_substring_length(self) -> None:
        result = self.module.find_similariry("hish", "fish")

        self.assertEqual(result, 3)

    def test_find_subsequence_returns_common_subsequence_length(self) -> None:
        result = self.module.find_subsequence("fosh", "fish")

        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
