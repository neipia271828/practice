import random

# リスト作成
def mk_list():
    size = random.randint(1, 50)
    return [random.randint(-100, 100) for _ in range(size)]

# リスト生成とソート
target_list = sorted(mk_list())
print(f"sort: {target_list}")

# 最大値表示
def find_max(target_list):
    return max(target_list)

print(f"max: {find_max(target_list)}")

# 最小値表示
def find_min(target_list):
    return min(target_list)

print(f"min: {find_min(target_list)}")

# 平均値表示
def average(target_list):
    return sum(target_list) / len(target_list)

print(f"ave: {average(target_list)}")

# 二倍リスト
def double_lis(target_list):
    return [2 * i for i in target_list]

print(f"double: {double_lis(target_list)}")