class Que:
    def __init__(self):
        self.items = []
    
    def enque(self, target):
        self.items.append(target)
    
    def deque(self):
        self.items.pop(0)


if __name__=="__main__":

    que = Que()

    que.enque(1)
    que.enque(2)
    print(que.items)

    que.deque()
    print(que.items)
    