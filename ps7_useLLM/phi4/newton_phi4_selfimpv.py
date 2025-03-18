import math
import unittest

# 重力の大きさ（m/s^2）
g = 9.81

def calculate_range(initial_velocity, launch_angle):
    """
    Calculate the range of a projectile launched at an initial velocity and angle.

    Parameters:
    - initial_velocity: float, initial speed of the projectile in meters per second (m/s)
    - launch_angle: float, launch angle in degrees

    Returns:
    - float, horizontal distance traveled by the projectile in meters
    """
    # Convert angle from degrees to radians
    launch_angle_rad = math.radians(launch_angle)

    # Calculate range using the formula for projectile motion without air resistance
    range_distance = (initial_velocity ** 2) * math.sin(2 * launch_angle_rad) / g

    return range_distance

class TestProjectileRange(unittest.TestCase):
    def test_max_range(self):
        initial_velocity = 100.0  # m/s
        launch_angle = 45.0       # degrees
        
        # 最大到達距離は、発射角が45度のときに得られることを知っている。
        expected_range = (initial_velocity ** 2) * math.sin(math.radians(90)) / g
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
        expected_range = (initial_velocity ** 2) * math.sin(math.radians(60)) / g
        calculated_range = calculate_range(initial_velocity, launch_angle)
        
        self.assertAlmostEqual(calculated_range, expected_range, places=2)

if __name__ == '__main__':
    unittest.main()