class PriorityQueueNode:
    def __init__(self, value, priority):
        self.ele = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        # Implement the isEmpty() function here

    def getSize(self):
        return len(self.pq)
        # Implement the getSize() function here

    def getMax(self):
        if self.getSize() == 0:
            return None
        else:
            return self.pq[0].ele
        # Implement the getMax() function here

    def __percolateup(self):
        childindex = self.getSize() - 1
        while childindex > 0:
            parenti = (childindex - 1) // 2
            if self.pq[parenti].priority < self.pq[childindex].priority:
                self.pq[parenti], self.pq[childindex] = self.pq[childindex], self.pq[parenti]
                childindex = parenti
            else:
                break

    def insert(self, ele, priority):


        pqNode = PriorityQueueNode(ele, priority)
        self.pq.append(pqNode)
        self.__percolateup()

        # Implement the insert() function here

    def __percolatedown(self, i):
        l = (2 * i) + 1
        r = (2 * i) + 2
        s = self.getSize()
        if (l < s and self.pq[i].priority < self.pq[l].priority):
            mx = l
        else:
            mx = i
        if (r < s and self.pq[mx].priority < self.pq[r].priority):
            mx = r
        if mx == i:
            return
        else:
            self.pq[mx], self.pq[i] = self.pq[i], self.pq[mx]
            self.__percolatedown(mx)

        pass

    def removeMax(self):
        if self.isEmpty():
            return None
        else:

            ans = self.pq[0].ele
            self.pq[0] = self.pq[self.getSize() - 1]
            self.pq.pop()
            self.__percolatedown(0)
            return ans
        # Implement the removeMax() function here


myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        myPq.insert(element, element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i += 1
