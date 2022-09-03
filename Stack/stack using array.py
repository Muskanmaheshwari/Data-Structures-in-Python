class Stack:
    def __init__(self):
        self.__data=[]
    def push(self,item):
        self.__data.append(item)
    def pop(self):
        if self.isEmpty():
            print("hey stack is emppty")
            return

        return self.__data.pop()
    def isEmpty(self):
        return self.size() == 0
    def size(self):
        return len(self.__data)
    def top(self):
        if self.isEmpty():
            print("Hey stack is Empty")
            return
        return self.__data[len(self.__data)-1]

s=Stack()
s.push(12)
s.push(14)
print(s.pop())