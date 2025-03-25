import random

#リスト作成
def mk_list():
    size = random.randint(1,50)
    memo = []
    for i in range(size):
        memo.append(random.randint(-100,100))
    return memo

#ソーティング
target_list = sorted(mk_list())
print(f"sort:{target_list}")

#最大値表示
def find_max(target_list=target_list):
    return target_list[-1]
print(f"max:{find_max()}")

#最小値表示
def find_min(target_list=target_list):
    return target_list[0]
print(f"min:{find_min()}")

#平均値表示
def average(target_list=target_list):
    size = len(target_list)
    memo = 0
    for i in target_list:
        memo += i
    average = memo / size
    return average
print(f"ave:{average()}")

#二倍リスト
def double_lis(target_list=target_list):
    memo = []
    for i in target_list:
        memo.append(int(2 * i))
    return memo
print(f"double:{double_lis()}")