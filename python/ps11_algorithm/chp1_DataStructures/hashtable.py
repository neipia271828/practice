from sympy import prime
import hashlib
import random

class HashTable:
    def __init__(self, table_size):
        #ハッシュテーブル作成
        self.table = []

        #長さ決定。素数長にして衝突を軽減
        self.table_size = prime(table_size)
        for i in range(self.table_size):
            self.table.append([])
    
    #組み込みのハッシュはシードが毎回変わるのでsha256を利用。
    def stable_hash(self, key):
        return int(hashlib.sha256(key.encode('utf-8')).hexdigest(),16)
    
    #アドレス検索
    def srch_adress(self, key):
        adress = self.cal_adress(key)
        for i in range(len(self.table[adress])):

            #アドレスのリストをイテラブルしたときkeyが一致するならば
            if self.table[adress][i][0] == key:
                #戻り値=アドレス
                return [adress, i]
            else:
                print("cant'searching adress. val is not found")
    
    #アドレス計算
    def cal_adress(self, key):
        hash_hex = self.stable_hash(key)
        adress = hash_hex % self.table_size
        return adress
    
    #要素追加
    def add_val(self, key, val):
        try:
            self.table[self.cal_adress(key)].append([key, val])
            print("process complete.")
        except:
            print("error")
    
    #要素削除
    def del_val(self, key):
        adress = self.srch_adress(key)
        print(adress)
        del self.table[adress[0]][adress[1]]

    #要素検索
    def rdg_val(self, key):
        adress = self.cal_adress(key)
        for i in self.table[adress]:
            if i[0] == key:
                return i
            else:
                print("not found")

if __name__ == "__main__":
    name_list = HashTable(3)
    name_list.add_val("Hinata","man")
    name_list.add_val("Motoki","man")
    name_list.add_val("Joe","man")
    name_list.add_val("Wakana","woman")
    name_list.add_val("Sachi","woman")

    print(name_list.rdg_val("Hinata"))
    print(name_list.table)

    name_list.del_val("Hinata")
    print(name_list.table)

class TestHashTable:
    def __init__(self, table_size, dataset,  Function=HashTable()):
        self.function = Function
        self.table_size  = table_size
        self.dataset = dataset
    
    def mk_table(self):
        for data in self.dataset:
            self.function.add_val(data[0],data[1])
        #今日はここまで、
        #print("")