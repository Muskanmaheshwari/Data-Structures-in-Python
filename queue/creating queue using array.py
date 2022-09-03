class Queueclass:
    def __init__(self):
        self.__arr=[]
        self.__front =0
        self.__count = 0
    def enqueue(self, data):
        self.__arr.append(data)
        self.__count +=1
        pass
    def dequeue(self):
        if self.__count == 0:
            return -1
        ele = self.__arr[self.__front]
        self.__front = self.__front+1
        self.__count-=1
        return ele
        pass
    def front(self):
        if self.__count == 0:
            return -1
        return self.__arr[self.__front]
        pass

    def size(self):
        return self.__count
        pass
    def isEmpty(self):
        return self.size()==0


        pass

q = Queueclass()
q.enqueue(10)
q.enqueue(20)
q.enqueue(20)
print(q.size())
print(q.dequeue())
print(q.isEmpty())
print(q.front())


