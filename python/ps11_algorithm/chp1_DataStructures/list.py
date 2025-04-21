import time 

li = []
for i in range(100000000):
    li.append(i)

print("accectime")
start = time.time()
print(li[0])
end = time.time()
print(f"処理時間：{end - start}秒")

start = time.time()
print(li[99999999])
end = time.time()
print(f"処理時間：{end - start}秒")

print("appendtime")
start = time.time()
li.insert(100,50)
end = time.time()
print(f"処理時間：{end - start}秒")