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
        


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
    