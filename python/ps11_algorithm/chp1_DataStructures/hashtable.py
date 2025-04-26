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
    
    #要素検索
    def rdg_val(self, key):
        adress = self.cal_adress(key)
        for i in self.table[adress]:
            if i[0] == key:
                return i
            else:
                print("not found")
    
#テストコード
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
    def __init__(self, dataset,  table_size=16, Function=HashTable):
        self.table_size  = table_size
        self.function = Function(self.table_size)
        self.dataset = dataset
        self.test_target = []
        for i in range(10):
            self.test_target.append(self.dataset[random.randint(0,49)])
        print(f"test target is\n{self.test_target}")
    
    def mk_table(self):
        for data in self.dataset:
            self.function.add_val(data[0],data[1])
        print("prosecc compleate")
        print(self.function.table)
    
    def srch_test(self):
        case = 0
        for i in self.test_target:
            case += 1
            result = self.function.rdg_val(i[0])
            if i == result:
                print(f"case {case} clear")
                print(f"target is {i}")
                print(f"result is {result}")
            else:
                print("error")
    
    def do(self):
        self.mk_table()
        self.srch_test()



dataset = [
    ["Taro", "man"],
    ["Jiro", "man"],
    ["Saburo", "man"],
    ["Shiro", "man"],
    ["Goro", "man"],
    ["Ichiro", "man"],
    ["Kenta", "man"],
    ["Hiroshi", "man"],
    ["Takashi", "man"],
    ["Yusuke", "man"],
    ["Daichi", "man"],
    ["Ren", "man"],
    ["Satoshi", "man"],
    ["Masato", "man"],
    ["Yuji", "man"],
    ["Koji", "man"],
    ["Ryo", "man"],
    ["Haruto", "man"],
    ["Sho", "man"],
    ["Renji", "man"],
    ["Riku", "man"],
    ["Shun", "man"],
    ["Keisuke", "man"],
    ["Makoto", "man"],
    ["Daiki", "man"],
    ["Yumi", "woman"],
    ["Sakura", "woman"],
    ["Miyu", "woman"],
    ["Aiko", "woman"],
    ["Naoko", "woman"],
    ["Keiko", "woman"],
    ["Emi", "woman"],
    ["Kana", "woman"],
    ["Reina", "woman"],
    ["Mika", "woman"],
    ["Haruka", "woman"],
    ["Yui", "woman"],
    ["Rina", "woman"],
    ["Ayaka", "woman"],
    ["Mio", "woman"],
    ["Saki", "woman"],
    ["Natsuki", "woman"],
    ["Riko", "woman"],
    ["Sumire", "woman"],
    ["Mei", "woman"],
    ["Nana", "woman"],
    ["Akari", "woman"],
    ["Hina", "woman"],
    ["Miu", "woman"],
    ["Asuka", "woman"]
]

if __name__ == "__main__":
    test = TestHashTable(dataset)
    test.do()