with open('data_set.txt') as f:
    s = f.read()
    print(s)

with open('data_set.txt') as f:
    #_は空変数
    for _ in range(5):
        s_line = f.readline()
        print(s_line)
    if s_line == '':
        print("終了です")

with open('data_set_2.txt', "w") as f:
    f.write("エーエーエー\nビービービー\nシーシーシー")

with open("data_set_2.txt", "r") as f:
    s_line = f.readlines()
    print(s_line)
    for w in s_line:
        print(w)