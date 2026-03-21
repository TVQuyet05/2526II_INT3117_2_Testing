import unittest
from main import calculate_cost

class TestBoundary(unittest.TestCase):

    # --- KIỂM THỬ TRƯỜNG HỢP KHÔNG HỢP LỆ (TC1, TC8) ---
    def test_invalid_cases(self):
        with self.assertRaisesRegex(ValueError, "Invalid"):
            calculate_cost(0, 1)  # TC1
        with self.assertRaisesRegex(ValueError, "Invalid"):
            calculate_cost(0, 2)  # TC8

    # --- KIỂM THỬ LOẠI XE 1 (TC2 - TC7) ---
    def test_type_1_sm_bike(self):
        # TC2: 
        self.assertEqual(calculate_cost(1, 1), 13200)
        # TC3: 
        self.assertEqual(calculate_cost(2, 1), 26400)
        # TC4: 
        self.assertEqual(calculate_cost(3, 1), 30600)
        # TC5: 
        self.assertEqual(calculate_cost(12, 1), 68400)
        # TC6: 
        self.assertEqual(calculate_cost(13, 1), 72600)
        # TC7: 
        self.assertEqual(calculate_cost(14, 1), 76800)

    # --- KIỂM THỬ LOẠI XE 2 (TC9 - TC14) ---
    def test_type_2_sm_taxi(self):
        # TC9: 
        self.assertEqual(calculate_cost(1, 2), 30500)
        # TC10: 
        self.assertEqual(calculate_cost(2, 2), 61000)
        # TC11: 
        self.assertEqual(calculate_cost(3, 2), 76500)
        # TC12: 
        self.assertEqual(calculate_cost(12, 2), 216000)
        # TC13: 
        self.assertEqual(calculate_cost(13, 2), 229800)
        # TC14: 
        self.assertEqual(calculate_cost(14, 2), 243600)

if __name__ == '__main__':
    unittest.main()