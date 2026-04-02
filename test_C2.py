import unittest
from main import calculate_cost

class TestShippingCostC2(unittest.TestCase):

    def test_case_1(self):
        # X=-1, T=1 (Không hợp lệ: X âm)
        with self.assertRaisesRegex(ValueError, "Invalid"):
            calculate_cost(-1, 1)

    def test_case_2(self):
        # X=2, T=1 (Xe máy: 2km đầu)
        # 2 * 13200 = 26400
        self.assertEqual(calculate_cost(2, 1), 26400)

    def test_case_3(self):
        # X=10, T=1 (Xe máy: trên 2km)
        # 2 * 13200 + 8 * 4200 = 26400 + 33600 = 60000
        self.assertEqual(calculate_cost(10, 1), 60000)

    def test_case_4(self):
        # X=1, T=2 (Ô tô: 2km đầu)
        # 1 * 30500 = 30500
        self.assertEqual(calculate_cost(1, 2), 30500)

    def test_case_5(self):
        # X=10, T=2 (Ô tô: từ 3km đến 12km)
        # 2 * 30500 + 8 * 15500 = 61000 + 124000 = 185000
        self.assertEqual(calculate_cost(10, 2), 185000)

    def test_case_6(self):
        # X=15, T=2 (Ô tô: trên 12km)
        # 2 * 30500 + 10 * 15500 + 3 * 13800 = 61000 + 155000 + 41400 = 257400
        self.assertEqual(calculate_cost(15, 2), 257400)

    def test_case_7(self):
        # X=1, T=0 (Không hợp lệ: T khác 1, 2)
        with self.assertRaisesRegex(ValueError, "Invalid"):
            calculate_cost(1, 0)

if __name__ == '__main__':
    unittest.main()
