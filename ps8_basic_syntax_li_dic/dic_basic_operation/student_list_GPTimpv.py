students = {}

def add_student(name, score):
    students[name] = score

def del_student(name):
    try:
        del students[name]
        print(f"{name} を削除しました。")
    except KeyError:
        print(f"{name} は登録されていません。")

def show_students_score(name):
    try:
        print(f"{name}: {students[name]}")
    except KeyError:
        print(f"{name} は登録されていません。")

def show_all_students_score():
    if not students:
        print("登録されている学生がいません。")
        return
    print("【全学生のスコア】")
    for name, score in students.items():
        print(f"{name}: {score}")

# データ追加
add_student("田中", 15)
add_student("明美", 78)
add_student("秀吉", 99)

# 田中を削除
del_student("田中")

# スコア表示
show_students_score("田中")  # 田中は削除されたためエラーメッセージが表示される
show_students_score("明美")  # 明美のスコアを表示

# 全学生のスコアを表示
show_all_students_score()