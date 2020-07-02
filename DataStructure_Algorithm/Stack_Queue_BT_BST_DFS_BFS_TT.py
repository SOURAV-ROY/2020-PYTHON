from DataStructure_Algorithm.LinkedList import DoubleLinkedList


class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def push(self, val):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val

    def is_empty(self):
        return self.__list.size == 0

    def peek(self):
        return self.__list.back()

    def __len__(self):
        return self.__list.size


# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# my_stack.push(7)
# print(f"Last Value : {my_stack.peek()}")
# print(f"Length : {len(my_stack)}")
# my_stack.push(5)
# print('Push (5)')
# print(f"Length : {len(my_stack)}")
# print(f"Pop : {my_stack.pop()}")
# print(f"Length : {len(my_stack)}")
# my_stack.push(10)
# print('Push (10)')
# print(f"Length : {len(my_stack)}")
# print(f"Last Value : {my_stack.peek()}")

class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enqueue(self, val):
        return self.__list.add(val)

    def dequeue(self):
        val = self.__list.front()
        self.__list.remove_first()
        return val

    def front(self):
        return self.__list.front()

    def is_empty(self):
        return self.__list.size == 0

    def __len__(self):
        return self.__list.size


# my_queue = Queue()
# my_queue.enqueue(2)
# my_queue.enqueue(1)
# my_queue.enqueue(3)
# print(f'Queue Len: {len(my_queue)}')
# print(f'Queue First Item: {my_queue.front()}')
# my_queue.enqueue(6)
# my_queue.enqueue(7)
# my_queue.enqueue(3100)
# print(f'Queue Len: {len(my_queue)}')
# print(f'Queue First Item: {my_queue.front()}')
# print(f'Dequeue: {my_queue.dequeue()}')
# print(f'Queue First Item: {my_queue.front()}')
# print(f'Dequeue: {my_queue.dequeue()}')
# print(f'Queue First Item: {my_queue.front()}')
