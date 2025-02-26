import matplotlib.pyplot as plt
import pandas as pd
# ランダムな数字のリストを生成 (0~100の範囲で1000個)
df = pd.read_csv('/Users/suzukiakiramuki/practice/ps2_deviation_value/csv/sample_data.csv', header=None)
df = df.values.tolist()

def adjust_df(df=df):
    ls = []
    for i in df:
        ls.append(i[0])
    return ls
sample_data = adjust_df()

# 度数分布のヒストグラムを作成
plt.hist(sample_data, bins=range(101), edgecolor='black', align='left')

# グラフのタイトルと軸ラベル
plt.title('Frequency Distribution of Random Numbers (0-100)')
plt.xlabel('Score')
plt.ylabel('Frequency')

# グラフを表示
plt.show()