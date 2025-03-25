NumPy を利用する Python コーディング課題

課題: 行列演算プログラムの作成

NumPy を使用して、以下の操作を行うプログラムを作成してください。

⸻

📌 条件
	1.	2つのランダムな整数行列 (A, B) を生成
	•	サイズは 4×4 の正方行列
	•	要素の値は 1 以上 10 以下の整数
	2.	以下の行列演算を実行
	•	行列の和: C = A + B
	•	行列の積: D = A \times B
	•	行列 A の転置行列: A^T
	•	行列 B の逆行列: B^{-1}（ただし、B が正則である場合のみ）
	3.	計算結果を出力
	•	各行列 (A, B, C, D, A^T, B^{-1}) を分かりやすく表示

⸻

⏳ ヒント
	•	np.random.randint() を使うと、指定範囲のランダムな整数行列を生成できます。
	•	行列の演算には、np.add() や np.matmul() などの NumPy 関数を活用できます。
	•	転置行列は .T、逆行列は np.linalg.inv() で求められます。
	•	逆行列を求める前に np.linalg.det() で行列式をチェックし、ゼロでないか確認してください。

⸻

🎯 追加課題 (発展編)
もし余裕があれば、次の拡張機能を追加してください！
✅ N×N の任意サイズの行列に対応できるようにする
✅ B が正則でない場合、擬似逆行列 (np.linalg.pinv()) を求める
✅ 各計算結果を matplotlib を使ってヒートマップで可視化する

⸻

この課題に挑戦してみてください！
できたらコードを見せてもらえれば、添削もできますよ！ 😊

よくできています！
ただ、いくつか修正すべき点があるので、添削しますね。

⸻




🔍 修正点

1. mk_array の書き方を NumPy の関数で簡潔に

あなたの mk_array 関数はループを使ってリストを作成していますが、NumPy の np.random.randint() を直接使えば、より簡潔に書けます。

修正前

def mk_array(array_size):
    ar = []
    for i in range(array_size):
        ar.append([])
        for j in range(array_size):
            ar[i].append(np.random.randint(-255,255))
    return ar

修正後

def mk_array(array_size):
    return np.random.randint(-255, 255, (array_size, array_size))

このようにすることで、ループを省略でき、コードが短くなります。

⸻

2. 逆行列の計算ミス

inv_array = np.linalg.det(array_2)

np.linalg.det() は行列式を求める関数であり、逆行列 (inv_array) を求めるのではありません。
正しくは np.linalg.inv(array_2) を使います。

修正前

if np.linalg.det(array_2) != 0:
    inv_array = np.linalg.det(array_2)  # ❌ 逆行列ではなく行列式を代入している

修正後

if np.linalg.det(array_2) != 0:
    inv_array = np.linalg.inv(array_2)  # ✅ 逆行列を求める

また、行列の大きさが 2×2 の場合は np.linalg.det() でゼロチェックをしても問題ないですが、
N×N 行列では数値誤差の影響で np.linalg.det() がゼロでなくても逆行列が求められないことがあります。
そのため、np.linalg.cond(array_2) を使い、条件数が大きすぎる場合は擬似逆行列に切り替えるのがベターです。

if np.linalg.cond(array_2) < 1 / np.finfo(array_2.dtype).eps:
    inv_array = np.linalg.inv(array_2)
else:
    inv_array = np.linalg.pinv(array_2)  # 条件数が大きすぎる場合は擬似逆行列

⸻

3. mk_heatmap の inv_array or pinv_array の修正

mk_heatmap(inv_array or pinv_array, "inv_array")

これは、inv_array が None の場合、pinv_array を使う意図ですが、
inv_array が None にならないように修正するので、mk_heatmap(inv_array, "inv_array") に統一してOKです。

⸻

📌 修正ポイント
	1.	mk_array() を NumPy の np.random.randint() に統一
	2.	np.linalg.det() の代わりに np.linalg.inv() を使用
	3.	行列の条件数 (np.linalg.cond()) を確認し、正則でない場合は np.linalg.pinv() を適用
	4.	mk_heatmap(inv_array, "inv_array") に統一

この修正により、コードの簡潔さ・精度・安全性が向上しました！
試してみてください！ 🎯✨

-ライブラリーへの理解が向上した。
-表現には改善の余地がある。
-行列はまだ勉強してないからいくつかのミスはしゃーない。