import random

#基礎構造は全て同じ
class Perceptron():
    def __init__(self, w1, w2, theta):
        self.w1 = w1
        self.w2 = w2
        self.theta = theta
    
    def P(self, x1, x2):
        tmp = x1*self.w1 + x2*self.w2
        if tmp <= self.theta:
            return 0
        elif tmp > self.theta:
            return 1

#入力に対する重みと閾値を設定し関数を作る。
AND = Perceptron(1,1,1.5)
OR = Perceptron(1,1,0.5)
NAND = Perceptron(-1,-1,-1.5)
NOR = Perceptron(-1,-1,-0.5)

#テスト記述
def test(func, gate_name):
    print(f"testtarget is :{gate_name}")

    #入力のパターン四通りを出力する。
    for i in range(2):
        for j in range(2):
            print(f"({i},{j}):{func.P(i,j)}")

#テストコード
if __name__ == "__main__":
    #テスト実行
    test(AND,"AND")
    test(OR,"OR")
    test(NAND,"NAND")
    test(NOR,"NOR")

    #単純パーセプトロンでXORを表現しようという足掻き
    XOR = Perceptron(1,1,1)
    test(XOR,"XOR")

    XOR_1 = Perceptron(1,3,2)
    XOR_2 = Perceptron(1,1,-1)
    XOR_3 = Perceptron(-1,2,1)

    target_func = [XOR_1,XOR_2,XOR_3]
    for i in target_func:
        test(i,"")
    
    #単層パーセプトロンでランダムな重み一万通りを試しXORの重みを探索している。(XORは単層パーセプトロンで表現できないことがわかる。)
    for i in range(10000):
        func = Perceptron(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10))
        if func.P(1,0) == 1 and func.P(0,1) == 1 and func.P(1,1) != 1 and func.P(0,0) != 1:
            print("hit")
            print(f"XORis({func.w1},{func.w2},{func.theta})")
            break
        if i == 9999:
            print("No hit parameters")
    #XORの正解。OR出力とNAND出力をAND入力へ
    class XOR():
        def P(self, x1, x2): 
            return AND.P(NAND.P(x1, x2), OR.P(x1, x2))
    
    xor = XOR()
    test(xor, "XOR")