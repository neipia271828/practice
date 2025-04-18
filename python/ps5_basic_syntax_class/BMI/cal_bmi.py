class BodyCondition():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    def cal_bmi(self):
        m_height = self.height / 100
        bmi = self.weight / m_height ** 2
        print(bmi)

A = BodyCondition(55, 150)
A.cal_bmi()