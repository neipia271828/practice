#基礎構造は全て同じ
class NeuralNetwork():
    def __init__(self, w1, w2, theta):
        self.w1 = w1
        self.w2 = w2
        self.theta = theta
    
    def NN(self, x1, x2):
        tmp = x1*self.w1 + x2*self.w2
        if tmp <= self.theta:
            return 0
        elif tmp > self.theta:
            return 1

#入力に対する重みと閾値を設定し関数を作る。
AND = NeuralNetwork(1,1,1.5)
OR = NeuralNetwork(1,1,0.5)
NAND = NeuralNetwork(-1,-1,-1.5)
NOR = NeuralNetwork(-1,-1,-0.5)

#テスト記述
def test(func, gate_name):
    print(f"testtarget is :{gate_name}")
    for i in range(2):
        for j in range(2):
            print(f"({i},{j}):{func.NN(i,j)}")

"""
#テスト実行
test(AND,"AND")
test(OR,"OR")
test(NAND,"NAND")
test(NOR,"NOR")

XOR = NeuralNetwork(1,1,1)

test(XOR,"XOR")

XOR_1 = NeuralNetwork(1,3,2)
XOR_2 = NeuralNetwork(1,1,-1)
XOR_3 = NeuralNetwork(-1,2,1)

target_func = [XOR_1,XOR_2,XOR_3]
for i in target_func:
    test(i,"")

"""

import random

for i in range(10000):
    func = NeuralNetwork(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10))
    if func.NN(1,0) == 1 and func.NN(0,1) == 1 and func.NN(1,1) != 1 and func.NN(0,0) != 1:
        print("hit")
        print(f"XORis({func.w1},{func.w2},{func.theta})")
        break

class XOR():
    def NN(self, x1, x2): 
        return AND.NN(NAND.NN(x1, x2), OR.NN(x1, x2))
xor = XOR()
test(xor, "XOR")