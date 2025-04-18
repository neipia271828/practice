import csv
from mk_random_number import mk_sample_number
from function_config import data_size

# サンプルデータセットの作成
def create_data_set(size):
    data_set = [[mk_sample_number()] for _ in range(size)]  # 各要素をリストにする
    return data_set

data_set = create_data_set(data_size)

# CSVファイルの保存場所を指定
file_path = 'ps2_deviation_value/csv/sample_data.csv'

# CSVファイルの作成
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_set)

print(f"CSVファイルが作成されました: {file_path}")