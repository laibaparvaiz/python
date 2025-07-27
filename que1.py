class QueueError(Exception):  
    pass

class Queue:
    def __init__(self):
        
        self.__queue = []
        

    def put(self, elem):
        
        self.__queue.insert(0,elem)
        

    def get(self):
        
        if len(self.__queue) == 0:
            raise QueueError("Queue is empty!")
        return self.__queue.pop()

class SuperQueue(Queue):
    def isempty(self):
        return len(self._Queue__queue) == 0

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
    