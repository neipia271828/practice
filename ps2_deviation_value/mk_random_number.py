import random
from function_config import lower_limit, upper_limit, mean, std_dev

# 乱数の作成
def mk_random_number(mean=mean, std_dev=std_dev):
    return random.gauss(mean, std_dev)  # 乱数を返す

# 指定範囲内に収まる乱数を生成
def adjust_random_number(lower_limit=lower_limit, upper_limit=upper_limit):
    random_number = mk_random_number()  # 初回の乱数生成
    while random_number < lower_limit or random_number > upper_limit:
        random_number = mk_random_number()  # 範囲外なら再生成
    random_number = round(random_number) #　値を丸め込み
    return random_number

#　意味関数
def mk_sample_number():
    return adjust_random_number()

#　テスト
"""
for i in range(10):
    print(mk_sample_number())
"""