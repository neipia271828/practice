import array
import time

arr = array.array('f')
for i in range(100000000):
    arr.append(i)

print("accectime")
start = time.time()
print(arr[9999999])
end = time.time()
print(f"処理時間：{end - start}秒")

print("appendtime")
start = time.time()
arr.insert(2, 0.5)
end = time.time()
print(f"処理時間：{end - start}秒")