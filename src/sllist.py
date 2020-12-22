# defines a node in a singly linked list
class _Node:
    def __init__(self, element, nextNode):
        '''constructs a node with an element and a next node'''
        self.__element = element
        self.__next = nextNode

    def get(self):
        '''returns the element at the node'''
        return self.__element
    
    def next(self):
        '''returns the next node'''
        return self.__next

# defines a singly linked list
class SingleLinkedList:
    def __init__(self, first = None):
        '''constructs an empty singly linked list or if provided a _Node a singly linked list starting with the provided _Node'''
        self.__head = first

    def isEmpty(self):
        '''returns True if the singly linked list does not contain any elements'''
        return self.__head is None

    def head(self):
        '''returns the first element in the singly linked list or None if empty'''
        if self.isEmpty():
            return None
        else:
            return self.__head.get()
    
    def tail(self):
        '''returns a singly linked list containing all but the first element'''
        if self.isEmpty():
            return SingleLinkedList()
        else:
            return SingleLinkedList(self.__head.next())

    def prepend(self, element):
        '''adds an element at the front of the singly linked list'''
        self.__head = _Node(element, self.__head)
        return self
    
    def size(self):
        '''returns the number of elements in the list'''
        def count(n, node):
            if node is None:
                return n
            else:
                return count(n+1, node.next())

        return count(0, self.__head)
        #count = 0
        #cursor = self.__head
        #while not cursor is None:
        #    count = count + 1
        #    cursor = cursor.next()
        #return count   

    def contains(self, element):
        '''returns if the list contains the specified element'''
        def isElement(node):
            if node is None:
                return False
            elif element == node.get():
                return True
            else:
                return isElement(node.next())
        return isElement(self.__head)

    def append(self, element):
        '''adds an element at the end of the singly linked list'''
        if self.isEmpty():
            return self.prepend(element)
        else:
            newNode = _Node(element, None)
            def lastNode(node):
                '''get the last node of the singly linked list'''
                if node.next() is None:
                    return node
                else:
                    return lastNode(node.next())
            oldLastNode = lastNode(self.__head)
            oldLastNode._Node__next = newNode
            return self

    def removeLast(self):
        '''removes the last element of the singly linked list if exists'''
        if self.size() == 1:
            self.__head = None
        elif not self.isEmpty():
            def secondLastNode(node):
                '''get the second last node of the singly linked list'''
                if node.next().next() is None:
                    return node
                else:
                    return secondLastNode(node.next())
            oldLastNode = secondLastNode(self.__head)
            oldLastNode._Node__next = None
        return self

    def join(self, list):
        reversed = SingleLinkedList()
        node = list.__head
        while not node == None:
            reversed.prepend(node.get())
            node = node.next()
        node = reversed.__head
        while not node == None:
            self.prepend(node.get())
            node = node.next()
        return self

    def copy(self):
        list = SingleLinkedList()
        node = self.__head
        while not node == None:
            list.append(node.get())
            node = node.next()
        return list