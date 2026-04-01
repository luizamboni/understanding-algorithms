import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("encode-decode.py")


def load_module():
    spec = importlib.util.spec_from_file_location("encode_decode_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class EncodeDecodeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_encode_collapses_repeated_characters(self) -> None:
        result = self.module.encode("aaaabbbcc")

        self.assertEqual(result, "a4b3c2")

    def test_decode_expands_multi_digit_counts(self) -> None:
        result = self.module.decode("a20b3c10")

        self.assertEqual(result, ("a" * 20) + ("b" * 3) + ("c" * 10))


if __name__ == "__main__":
    unittest.main()
