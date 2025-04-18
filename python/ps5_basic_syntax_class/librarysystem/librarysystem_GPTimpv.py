class Book:
    """ 本の情報を管理するクラス """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # 最初は貸し出しされていない

    def __str__(self):
        status = "貸出中" if self.is_borrowed else "利用可能"
        return f"📖 {self.title} - {self.author} ({status})"


class Library:
    """ 図書館の本を管理するクラス """
    def __init__(self):
        self.books = []  # 本のリストを管理

    def add_book(self, title, author):
        """ 新しい本を図書館に追加する """
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"✅ {title} を図書館に追加しました！")

    def borrow_book(self, title):
        """ 指定された本を貸し出す """
        for book in self.books:
            if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"📕 {title} を貸し出しました！")
                    return
                else:
                    print(f"⚠️ {title} はすでに貸出中です！")
                    return
        print(f"❌ {title} は図書館にありません！")

    def return_book(self, title):
        """ 指定された本を返却する """
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"📗 {title} を返却しました！")
                    return
                else:
                    print(f"⚠️ {title} は貸し出されていません！")
                    return
        print(f"❌ {title} は図書館にありません！")

    def display_books(self):
        """ 図書館の本一覧を表示する """
        print("\n📚 図書館の本一覧:")
        if not self.books:
            print("（本がありません）")
        for book in self.books:
            print(book)
        print("-" * 30)


# === 使用例（実行コード） ===
library = Library()

# 本を追加
library.add_book("Python入門", "鈴木 太郎")
library.add_book("データ構造とアルゴリズム", "山田 花子")

# 本の一覧を表示
library.display_books()

# 本を貸し出し
library.borrow_book("Python入門")

# もう一度本の一覧を表示（貸出状況を確認）
library.display_books()

# 本を返却
library.return_book("Python入門")

# 最後にもう一度本の一覧を表示
library.display_books()