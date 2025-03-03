import random

# 乱数を生成
def make_random_num():
    return random.randint(1, 100)  # round()は不要

# 数字を当てる処理
def guess_num(target_num):
    while True:
        num = input("please type a number (or 'exit' to quit): ")

        # ゲーム終了の処理
        if num.lower() == "exit":
            print("Game Over")
            break
        
        # 数値チェック
        if not num.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        num = int(num)

        # 判定処理
        if num == target_num:
            print("Congratulations! 🎉")
            break
        elif num > target_num:
            print("smaller")
        else:
            print("bigger")

# ゲームの実行
def process():
    target_num = make_random_num()
    guess_num(target_num)

process()