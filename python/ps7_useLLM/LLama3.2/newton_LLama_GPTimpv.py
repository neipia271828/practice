import math

def calculate_distance(initial_velocity, angle):
    # 2D運動方程式を使用
    initial_velocity_x = initial_velocity * math.cos(math.radians(angle))
    initial_velocity_y = initial_velocity * math.sin(math.radians(angle))
    acceleration = -9.81
    time_of_flight = -2 * initial_velocity_y / acceleration
    distance = initial_velocity_x * time_of_flight
    return distance, time_of_flight

# テスト
initial_velocity = 100  # m/s
angle = 45  # 度

distance, time_of_flight = calculate_distance(initial_velocity, angle)
print(f"初速度：{initial_velocity} m/s")
print(f"発射角度：{angle} 度")
print(f"飛距離：{distance:.2f} m")
print(f"飛時間：{time_of_flight:.2f} s")

import unittest

class TestCalculateDistance(unittest.TestCase):
    def test_calculate_distance(self):
        initial_velocity = 100  # m/s
        angle = 45  # 度

        distance, time_of_flight = calculate_distance(initial_velocity, angle)

        expected_distance = (initial_velocity ** 2 * math.sin(2 * math.radians(angle))) / 9.81
        self.assertAlmostEqual(distance, expected_distance, delta=0.01)

if __name__ == '__main__':
    unittest.main()