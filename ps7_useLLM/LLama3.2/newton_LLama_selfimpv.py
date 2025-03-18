import math
import unittest

def calculate_distance(initial_velocity, angle):
    # 2D運動方程式を使用
    try:
        initial_velocity = float(initial_velocity)  # 初速度が浮点数でなければならないようにチェックします。
        if initial_velocity <= 0:
            raise ValueError("初速度は負でなければなりません。")
        angle = math.radians(angle)
        
        acceleration = -9.81
        time_of_flight = 2 * initial_velocity / acceleration
        distance = (initial_velocity ** 2) * math.sin(2*angle)/acceleration

    except ValueError as ve:
        print(f"エラー：{ve}")
        return None, None

    except ZeroDivisionError as ze:
        print(f"エラー：{ze}")
        return None, None
    
    return distance, time_of_flight


class TestCalculateDistance(unittest.TestCase):
    def test_calculate_distance(self):
        initial_velocity = 100  # m/s
        angle = 45  # 度
        
        result = calculate_distance(initial_velocity, angle)
        
        if not result:
            self.fail("初速度や角度が不正なので、 flying距離と飛時間を計算できませんでした。")
        else:
            expected_distance = (initial_velocity ** 2) * math.sin(2*math.radians(angle)) / 9.81
            self.assertAlmostEqual(result[0], expected_distance, delta=0.01)
            self.assertAlmostEqual(result[1], 2*initial_velocity/9.81, delta=0.01)

    def test_zero_division(self):
        initial_velocity = 100  # m/s
        angle = 90  # 度
        
        result = calculate_distance(initial_velocity, angle)
        
        if not result:
            self.fail(" flying距離と飛時間を計算できませんでした。")
        else:
            self.assertAlmostEqual(result[0], None, delta=None)
            self.assertAlmostEqual(result[1], None, delta=None)

    def test_division_by_zero(self):
        initial_velocity = 100  # m/s
        angle = 180  # 度
        
        result = calculate_distance(initial_velocity, angle)
        
        if not result:
            self.fail(" flying距離と飛時間を計算できませんでした。")
        else:
            self.assertAlmostEqual(result[0], None, delta=None)
            self.assertAlmostEqual(result[1], None, delta=None)

if __name__ == '__main__':
    unittest.main()