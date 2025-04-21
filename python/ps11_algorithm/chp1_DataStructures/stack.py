class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
    
if __name__=="__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("スタックサイズ：", stack.size())
    print("いちばん上の要素：", stack.peek())

    print("取り出した要素：", stack.pop())
    print("取り出した要素：", stack.pop())

    print("スタックサイズ：", stack.size())