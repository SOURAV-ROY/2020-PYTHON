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


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(7)
print(f"Last Value : {my_stack.peek()}")
print(f"Length : {len(my_stack)}")
my_stack.push(5)
print('Push (5)')
print(f"Length : {len(my_stack)}")
print(f"Pop : {my_stack.pop()}")
print(f"Length : {len(my_stack)}")
print(f"Last Value : {my_stack.peek()}")
