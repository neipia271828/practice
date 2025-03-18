import unittest

class TestProjectileRange(unittest.TestCase):
    def test_max_range(self):
        # 最大到達距離は45度で発射された場合に得られると知られています。
        initial_velocity = 100.0  # m/s
        launch_angle = 45.0       # degrees
        expected_range = (initial_velocity ** 2) / g * math.sin(math.radians(90))
        
        calculated_range = calculate_range(initial_velocity, launch_angle)
        
        self.assertAlmostEqual(calculated_range, expected_range, places=2)

    def test_zero_angle(self):
        initial_velocity = 100.0
        launch_angle = 0.0
        
        # 発射角が0度の場合、飛距離はゼロになります。
        calculated_range = calculate_range(initial_velocity, launch_angle)
        
        self.assertAlmostEqual(calculated_range, 0.0, places=2)

    def test_vertical_launch(self):
        initial_velocity = 100.0
        launch_angle = 90.0
        
        # 発射角が90度の場合、水平方向への飛距離はゼロになります。
        calculated_range = calculate_range(initial_velocity, launch_angle)
        
        self.assertAlmostEqual(calculated_range, 0.0, places=2)

    def test_30_degree(self):
        initial_velocity = 100.0
        launch_angle = 30.0
        
        # 標準的な角度での計算確認
        calculated_range = calculate_range(initial_velocity, launch_angle)
        
        expected_range = (initial_velocity ** 2) * math.sin(math.radians(60)) / g
        self.assertAlmostEqual(calculated_range, expected_range, places=2)

if __name__ == '__main__':
    unittest.main()