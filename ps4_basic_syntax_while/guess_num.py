import random

#乱数を生成
def make_random_num():
    result = random.randint(1,100)
    result = round(result)
    return result
target_num = make_random_num()

#処理を定義
def guess_num():
    #変数の取り込み
    global target_num
    num = input("please type num:")

    #処理内容
    if num == str(target_num):
        print("Congratulation!")
        return False
    
    elif num == "exit":
        print("Game Over")
        return False
    
    else:
        if int(num) > target_num:
            print("smaller")

        elif int(num) < target_num:
            print("bigger")
        return True

#処理を実行
def process():
    while guess_num():
        pass

process()