import pandas as pd
import math
from function_config import data_size, self_score

# csv読み込み
df = pd.read_csv('/Users/suzukiakiramuki/practice/ps2_deviation_value/csv/sample_data.csv', header=None)
df = df.values.tolist()

#平均値計算
def cal_mean(data=df, self_score=self_score):
    sum = 0
    for i in range(len(data)):
        sum += data[i][0]
    sum += self_score
    mean = sum / (len(data) + 1)
    return mean
mean = cal_mean()

#分散を計算
def cal_variance(data=df, mean=mean, data_size=data_size):
    sum = 0
    for i in range(data_size):
        target_data = data[i][0]
        defference_memory = target_data - mean
        sum += defference_memory ** 2
    sum += (self_score - mean) ** 2
    variance = sum / (data_size + 1)
    return variance
variance = cal_variance()

#標準偏差を計算
def cal_standard_deviation(self_score=self_score, variance=variance, data_size=data_size, mean=mean): 
    root = math.sqrt(variance)
    return root
deviation = cal_standard_deviation()

#偏差値を計算
def cal_deviation_score(deviation=deviation, mean=mean, self_score=self_score):
    deviation_score = (((self_score - mean) / deviation) * 10) + 50
    return deviation_score
deviation_score = cal_deviation_score()

print(deviation_score)