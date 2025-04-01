from transistors import Transistors
class LogicGates():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    
    def NAND(self):
        pMOS1 = Transistors(1,self.v1)
        out1 = pMOS1.pFET()
        
        pMOS2 = Transistors(1,self.v2)
        out2 = pMOS2.pFET()

        total_out = 0
        if out1 + out2 > 0:
            total_out = 1
        else:
            total_out = 0
        return total_out
    
    def NOR(self):
        pMOS1 = Transistors(1,self.v1)
        out1 = pMOS1.pFET()

        pMOS2 = Transistors(out1,self.v2)
        out2 = pMOS2.pFET()

        return out2


for i in range(2):
    for j in range(2):
        test = LogicGates(i,j)
        print(test.NAND())

for i in range(2):
    for j in range(2):
        test = LogicGates(i,j)
        print(test.NOR())