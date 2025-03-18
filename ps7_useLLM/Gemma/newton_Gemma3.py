import math

def calculate_range(initial_velocity, launch_angle_degrees):
  """
  砲弾の飛距離を計算します。

  Args:
    initial_velocity: 砲弾の初速度 (m/s)
    launch_angle_degrees: 発射角度 (度)

  Returns:
    飛距離 (m)
  """

  # 角度をラジアンに変換
  launch_angle_radians = math.radians(launch_angle_degrees)

  # 飛距離の公式
  range_value = (initial_velocity**2 * math.sin(2 * launch_angle_radians)) / 9.81

  return range_value

def test_calculate_range():
  """
  calculate_range関数のテストを行います。
  """

  # テストケース
  test_cases = [
      (20, 45, 42.9),  # 初速度 20 m/s, 発射角度 45度
      (30, 60, 86.6),  # 初速度 30 m/s, 発射角度 60度
      (10, 30, 17.32), # 初速度 10 m/s, 発射角度 30度
      (50, 90, 122.5), # 初速度 50 m/s, 発射角度 90度
  ]

  # テスト実行
  for initial_velocity, launch_angle_degrees, expected_range in test_cases:
    actual_range = calculate_range(initial_velocity, launch_angle_degrees)
    # 誤差を許容範囲とする
    tolerance = 0.1
    assert abs(actual_range - expected_range) < tolerance, f"Error for initial velocity {initial_velocity} and launch angle {launch_angle_degrees}: Expected {expected_range}, Actual {actual_range}"
    print(f"Initial Velocity: {initial_velocity} m/s, Launch Angle: {launch_angle_degrees} degrees, Range: {actual_range:.2f} m")

# テスト実行
if __name__ == "__main__":
  test_calculate_range()