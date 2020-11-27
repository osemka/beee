class CustomQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if item == 'veteran':
            self.items.insert(0,item)
        else:
            self.items.insert(self.size(),item)
        print('push ' + item)

    def pop(self):
        print('pop ' + self.items[self.size() - 1])
        return self.items.pop()

    def size(self):
        print('size ' + str(len(self.items)))
        return len(self.items)


q = CustomQueue()

q.size()
q.push('veteran')
q.size()
q.push('veteran')
q.size()
q.push('veteran')
q.size()
q.push('citizen')
q.size()
q.push('veteran')
q.size()
q.push('citizen')
q.size()

q.pop()
q.size()
q.pop()
q.size()
q.pop()
q.size()
q.pop()
q.size()
q.pop()
q.size()
