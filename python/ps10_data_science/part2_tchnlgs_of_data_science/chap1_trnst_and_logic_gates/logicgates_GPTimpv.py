from transistors import Transistors

class LogicGates:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    def NAND(self):
        # NMOSでNANDを実装 (実際の回路動作を模倣)
        nMOS1 = Transistors(self.v1, self.v2)
        out1 = nMOS1.nFET()  # NAND用のNMOSの動作を考慮

        return 1 if out1 == 0 else 0  # NANDの特性
    
    #GPTくん間違ってます。
    def NOR(self):
        # PMOSでNORを実装
        pMOS1 = Transistors(1, self.v1)
        out1 = pMOS1.pFET()

        pMOS2 = Transistors(1, self.v2)
        out2 = pMOS2.pFET()

        return 1 if out1 == 0 and out2 == 0 else 0  # NORの特性

# 動作確認
for i in range(2):
    for j in range(2):
        test = LogicGates(i, j)
        print(f"NAND({i}, {j}) = {test.NAND()}")

for i in range(2):
    for j in range(2):
        test = LogicGates(i, j)
        print(f"NOR({i}, {j}) = {test.NOR()}")