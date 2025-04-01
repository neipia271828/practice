class Transistors():
    def __init__(self, S, G):
        self.S = S
        self.G = G

    def nFET(self):
        if self.S == 1 and self.G == 1:
            return 1
        else:
            return 0

    def pFET(self):
        if self.S == 1 and self.G == 0:
            return 1
        else:
            return 0