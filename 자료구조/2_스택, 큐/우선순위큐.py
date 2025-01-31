class PriorityQueue:
    def __init__(self, size):
        # self.priority = priority
        # self.data = data
        self.que = []
        self.size = size

    def enqueue(self, priority, data):
        if self.is_full():
            print("큐가 가득 찼습니다.")
        else:
            pass

    def is_empty(self):
        '''큐가 비어있는지 판단'''
        return len(self.que) == 0

    def is_full(self):
        '''큐가 가득 찼는지 판단'''
        return len(self.que) >= self.size
