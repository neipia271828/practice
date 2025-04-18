students = {}

def add_student(name, score):
    students[name] = score

def del_student(name):
    del students[name]

def show_students_score(name):
    try:
        print(f"{name}:{students[name]}")
    except:
        print("There are no such students.")

def show_all_students_score():
    print(students)

add_student("田中", 15)
add_student("明美", 78)
add_student("秀吉", 99)

del_student("田中")

show_students_score("田中")
show_students_score("明美")

show_all_students_score()
