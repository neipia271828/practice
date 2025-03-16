import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

array_size = 2

# 行列の値を表すリストを生成する（NumPyを活用）
def mk_array(array_size):
    return np.random.randint(-255, 255, (array_size, array_size))

# 行列を生成
array_1 = mk_array(array_size)
array_2 = mk_array(array_size)
print(f"first array:\n{array_1}")
print(f"second array:\n{array_2}")

# 行列の和を計算
sum_array = np.add(array_1, array_2)
print(f"sum array:\n{sum_array}")

# 行列の積を計算
mul_array = np.matmul(array_1, array_2)
print(f"mul array:\n{mul_array}")

# 転置行列を計算
T_array = array_1.T
print(f"T array:\n{T_array}")

# 逆行列を計算（条件数でチェック）
if np.linalg.cond(array_2) < 1 / np.finfo(array_2.dtype).eps:
    inv_array = np.linalg.inv(array_2)  # 正則なら逆行列
    print(f"inv array:\n{inv_array}")
else:
    inv_array = np.linalg.pinv(array_2)  # 逆行列が求められない場合は擬似逆行列
    print("array2 is nearly singular, using pseudo-inverse.")
    print(f"pinv array:\n{inv_array}")

# ヒートマップを作成
def mk_heatmap(target_array, title):
    plt.figure(figsize=(8, 6))
    sns.heatmap(target_array, annot=True, fmt=".2f", cmap="viridis")
    plt.title(title)
    plt.show()

mk_heatmap(array_1, "array_1")
mk_heatmap(array_2, "array_2")
mk_heatmap(sum_array, "sum_array")
mk_heatmap(mul_array, "mul_array")
mk_heatmap(T_array, "T_array")
mk_heatmap(inv_array, "inv_array")


