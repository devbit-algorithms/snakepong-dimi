from dllist import DoubleLinkedList

class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()
    
    def isEmpty(self):
        return self.__list.isEmpty()
    
    def add(self, element):
        self.__list.addBack(element)
        return self

    def remove(self):
        return self.__list.removeFront()