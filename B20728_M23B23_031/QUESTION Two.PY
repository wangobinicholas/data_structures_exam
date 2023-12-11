class studentQueue:
    def__init__(self):
    self.queue = []
    def enqueue(self,student):
        self.queue.append(student)


        def dequeue(self):
            if not self.is_empty():
                return self.queue.pop(0)
            
        def is_empty(self):
            return len(self.queue)

        queue = studentQueue()
        queue.enqueue("male")
        queue.enqueue("wassajja")
        queue.enqueue("mivule")
        print(queue.size()) 
        served_student = queue.dequeue()
        print(served_student)

        print(queue.is_empty())
        print(queue.size())   














consider a scenario where students are waiting in a queue at the university's student dining hall.Implement a python code that simulates a queue data structure for managing the students queue.Design a class named StudentQueue with methods to enqueuw students joining the queue, dequeue students being served, check if the queue is empty, and determine the current size of the queue. Provide an example(without) usage of your implemented class, demonstrating how students join the queue,get served, and how to ascertain the size of the queue   this code should be able to run in pylance









