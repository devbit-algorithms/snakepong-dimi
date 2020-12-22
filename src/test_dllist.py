from dllist import DoubleLinkedList

def test_empty_list():
    list = DoubleLinkedList()
    assert list.isEmpty()

def test_add_element_to_front():
    list = DoubleLinkedList()
    list.addFront(3)
    assert not list.isEmpty()
    list.addFront(2).addFront(1)
    assert list.front() == 1

def test_add_element_to_back():
    list = DoubleLinkedList()
    list.addBack(1)
    assert not list.isEmpty()
    list.addBack(2).addBack(3)
    assert list.back() == 3

def test_get_front_node():
    list = DoubleLinkedList()
    assert list.front() is None
    list.addFront(1)
    assert list.front() == 1

def test_get_back_node():
    list = DoubleLinkedList()
    assert list.back() is None
    list.addFront(1)
    assert list.back() == 1

def test_multiple_elements():
    list = DoubleLinkedList()
    list.addFront(1).addBack(2)
    assert list.front() == 1
    assert list.back() == 2

def test_remove_front():
    list = DoubleLinkedList()
    list.addFront(1).addFront(2)
    assert list.removeFront() == 2
    assert list.front() == 1
    assert list.removeFront() == 1
    assert list.isEmpty()
    list.removeFront()
    assert list.isEmpty()

def test_copy():
    list = DoubleLinkedList()
    list.addFront(1).addFront(2).addFront(3)
    copy = list.copy()
    assert not copy == list
    assert list.front() == 3
    assert copy.front() == 3
    assert copy.removeBack() == 1
    assert copy.back() == 2
    assert list.back() == 1