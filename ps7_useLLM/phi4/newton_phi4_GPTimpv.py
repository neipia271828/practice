import math
import unittest

# 重力加速度の定義
g = 9.81  # m/s^2

# 飛距離を計算する関数の定義
def calculate_range(initial_velocity, launch_angle):
    launch_angle_rad = math.radians(launch_angle)
    range = (initial_velocity ** 2) * math.sin(2 * launch_angle_rad) / g
    return range

class TestProjectileRange(unittest.TestCase):
    def test_max_range(self):
        initial_velocity = 100.0  # m/s
        launch_angle = 45.0       # degrees
        expected_range = (initial_velocity ** 2) / g * math.sin(math.radians(90))
        
        calculated_range = calculate_range(initial_velocity, launch_angle)
        
        self.assertAlmostEqual(calculated_range, expected_range, places=2)

    def test_zero_angle(self):
        initial_velocity = 100.0
        launch_angle = 0.0
        
        calculated_range = calculate_range(initial_velocity, launch_angle)
        
        self.assertAlmostEqual(calculated_range, 0.0, places=2)

    def test_vertical_launch(self):
        initial_velocity = 100.0
        launch_angle = 90.0
        
        calculated_range = calculate_range(initial_velocity, launch_angle)
        
        self.assertAlmostEqual(calculated_range, 0.0, places=2)

    def test_30_degree(self):
        initial_velocity = 100.0
        launch_angle = 30.0
        
        calculated_range = calculate_range(initial_velocity, launch_angle)
        
        expected_range = (initial_velocity ** 2) * math.sin(math.radians(60)) / g
        self.assertAlmostEqual(calculated_range, expected_range, places=2)

if __name__ == '__main__':
    unittest.main()