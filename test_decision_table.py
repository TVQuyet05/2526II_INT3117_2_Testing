import unittest
from main import calculate_cost

class TestDecisionTable(unittest.TestCase):

    # --- KIỂM THỬ TRƯỜNG HỢP NGOẠI LỆ (R1, R5) ---
    def test_invalid_distance(self):
        """Kiểm tra quãng đường âm"""
        with self.assertRaisesRegex(ValueError, "Invalid"):
            calculate_cost(-1, 1)  # R1
        with self.assertRaisesRegex(ValueError, "Invalid"):
            calculate_cost(-1, 2)  # R5

    # --- KIỂM THỬ LOẠI XE 1 (R2, R3, R4) ---
    def test_type_1_bike(self):
        # R2: 
        self.assertEqual(calculate_cost(1, 1), 13200)
        # R3: 
        self.assertEqual(calculate_cost(9, 1), 55800)
        # R4: 
        self.assertEqual(calculate_cost(20, 1), 102000)

    # --- KIỂM THỬ LOẠI XE 2 (R6, R7, R8) ---
    def test_type_2_taxi(self):
        # R6: 
        self.assertEqual(calculate_cost(1, 2), 30500)
        # R7: 
        self.assertEqual(calculate_cost(9, 2), 169500)
        # R8: 
        self.assertEqual(calculate_cost(20, 2), 326400)

if __name__ == '__main__':
    unittest.main()