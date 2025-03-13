class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borowed = False
Books = {}
class Library():
    def add_book(self, title, author):
        tgbook = Book(title, author)
        tgbook.title = title
        tgbook.author = author
        Books[title] = tgbook
        self.library = Books


a = Library()

# 図書館を作成
library = Library()

# 本を追加
library.add_book("Python入門", "鈴木 太郎")
library.add_book("データ構造とアルゴリズム", "山田 花子")
print(library.library)
"""
# 図書館の本を表示
library.display_books()

# 本を貸し出す
library.borrow_book("Python入門")

# 本を再度表示（貸出状況が変わっているか確認）
library.display_books()

# 本を返却
library.return_book("Python入門")

# 最終的な本のリストを表示
library.display_books()
"""