import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

array_size = 2

#行列の値を表すリストを生成する。
def mk_array(array_size):
    ar = []
    for i in range(array_size):
        ar.append([])
        for j in range(array_size):
            ar[i].append(np.random.randint(-255,255))
    return ar

#行列を生成
array_1 = np.array(mk_array(array_size))
array_2 = np.array(mk_array(array_size))
print(f"first array:\n{array_1}")
print(f"second array:\n{array_2}")

#行列の和を計算
sum_array = np.add(array_1,array_2)
print(f"sum array:\n{sum_array}")

#行列の積を計算
mul_array = np.matmul(array_1,array_2)
print(f"mul array:\n{mul_array}")

#転置行列を計算
T_array = array_1.T
print(f"T array:\n{T_array}")

#逆行列を計算
if np.linalg.det(array_2) != 0:
    inv_array = np.linalg.det(array_2)
    print(f"inv array:\n{inv_array}")
else:
    pinv_array = np.linalg.pinv(array_2)
    print("array2 equal 0")
    print(f"but pinv array:\n{pinv_array}")

#ヒートマップを作成
def mk_heatmap(target_array,title):
    plt.figure(figsize=(8,6))
    sns.heatmap(target_array, annot=True, fmt=".2f", cmap="viridis")
    plt.title(title)
    plt.show()

mk_heatmap(array_1, "array_1")
mk_heatmap(array_2, "array_2")
mk_heatmap(sum_array, "sum_array")
mk_heatmap(mul_array, "mul_array")
mk_heatmap(T_array, "T_array")
mk_heatmap(inv_array or pinv_array, "inv_array")
