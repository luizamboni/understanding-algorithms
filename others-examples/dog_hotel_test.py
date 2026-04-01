import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("dog-hotel.py")


def load_module():
    spec = importlib.util.spec_from_file_location("dog_hotel_example", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class DogHotelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_maximizar_ganhos_com_indices_returns_best_non_adjacent_pick(self) -> None:
        indices, ganho = self.module.maximizar_ganhos_com_indices([3, 7, 2, 1, 60, 3])

        self.assertEqual(indices, [1, 4])
        self.assertEqual(ganho, 67)

    def test_maximizar_ganhos_handles_empty_input(self) -> None:
        indices, ganho = self.module.maximizar_ganhos_com_indices([])

        self.assertEqual(indices, [])
        self.assertEqual(ganho, 0)


if __name__ == "__main__":
    unittest.main()
