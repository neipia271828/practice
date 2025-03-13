📝 課題：「銀行口座システムを作成しよう！」

あなたは銀行のシステム開発者です。Python の クラス を利用して、銀行口座（BankAccount） を管理するプログラムを作成してください。

⸻

🔹 仕様
	1.	BankAccount クラス を作成し、以下の属性を持たせる。
	    •	account_holder（口座名義）
	    •	balance（残高、初期値は 0）
	2.	以下のメソッドを実装する。
    	•	deposit(amount): 指定した金額を入金し、残高を更新する。
	    •	withdraw(amount): 指定した金額を引き出し、残高を更新する。
    	•	ただし、残高が不足している場合は引き出せないようにする。
	    •	display_balance(): 現在の残高を表示する。
	3.	以下の処理を行うプログラムを作成する。
    	•	口座を作成し、初期の残高を表示する。
    	•	任意の金額を入金し、更新後の残高を表示する。
	    •	任意の金額を引き出し、更新後の残高を表示する。
    	•	残高不足の時はエラーメッセージを表示する。

🎉 実装おめでとうございます！ 🎉
コードの構造はしっかりしており、基本的な銀行口座の操作ができるようになっていますね！
ただ、いくつか 改善点 があるので、添削していきます。

⸻

✏️ 改善点

1️⃣ account_holder の指定方法

🔹 account_holder の初期値を 空文字 ("") にしていますが、インスタンス生成時に指定するのが自然 です。
→ 解決策: __init__ の引数で 必ず指定 するようにしましょう！

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

→ こうすることで、account_A.account_holder = "A" という書き換えが不要になります。

⸻

2️⃣ deposit メソッドの print()

🔹 deposit() メソッド内に 空の print() がありますが、不要です。
→ 解決策: 削除しましょう。

⸻

3️⃣ エラーメッセージを詳細に

🔹 withdraw() のエラーメッセージが "Error" だけだと、何が問題なのかわかりにくい です。
→ 解決策: 具体的なメッセージ にしましょう！

def withdraw(self, amount):
    if self.balance >= amount:
        self.balance -= amount
    else:
        print(f"Error: 残高不足です。（現在の残高: {self.balance}）")

→ 「現在の残高」も表示 することで、ユーザーが状況を理解しやすくなります。

⸻

4️⃣ display_balance() の文言改善

🔹 print(f"balance:{self.balance}") だと、英語と日本語が混ざっていて少し不自然。
→ 解決策: もう少し 分かりやすい表記 に改善しましょう！

def display_balance(self):
    print(f"📝 現在の残高: {self.balance} 円")

→ 視認性が向上 し、ユーザーにとってわかりやすくなります。

⸻

📌 まとめ

✅ account_holder は インスタンス生成時に指定 できるようにする
✅ deposit() の 不要な print() を削除
✅ withdraw() の エラーメッセージを詳細に する
✅ display_balance() の メッセージを改善

このように修正すると、より分かりやすく、実用的なコード になります！ 💡
ぜひ試してみてください！ 🚀