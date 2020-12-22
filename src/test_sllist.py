from sllist import SingleLinkedList

def test_prepend_list():
    list = SingleLinkedList()
    assert list.head() is None
    list.prepend(1).prepend(2).prepend(3)
    assert list.head() == 3

def test_tail_list():
    list = SingleLinkedList()
    list.prepend(1).prepend(2).prepend(3)
    assert list.tail().head() == 2
    assert list.tail().tail().head() == 1

def test_tail_empty_list():
    list = SingleLinkedList()
    assert list.tail().isEmpty()

def test_size():
    list = SingleLinkedList()
    assert list.size() == 0
    list.prepend(1).prepend(2).prepend(3)
    assert list.size() == 3

def test_contains():
    list = SingleLinkedList()
    assert list.contains(1) == False
    list.prepend(1).prepend(2).prepend(3)
    assert list.contains(2)

def test_append():
    list = SingleLinkedList()
    list.append(1)
    assert list.head() == 1
    list.append(2).append(3)
    assert list.head() == 1

def test_remove_last():
    list = SingleLinkedList()
    list.removeLast()
    assert list.isEmpty()
    list.append(1).removeLast()
    assert list.isEmpty()
    list.prepend(3).prepend(2).prepend(1)
    assert list.size() == 3
    list.removeLast()
    assert list.head() == 1
    assert list.size() == 2
    list.removeLast().removeLast().removeLast()
    assert list.size() == 0

def test_join():
    list = SingleLinkedList()
    list2 = SingleLinkedList()
    list.join(list2)
    assert list.isEmpty()
    list.prepend(1).prepend(2).prepend(3)
    list2.prepend(4).prepend(5).prepend(6)
    list.join(list2)
    assert list.head() == 6
    assert list.size() == 6

def test_copy():
    list = SingleLinkedList()
    list.append(1).append(2).append(3)
    copy = list.copy()
    assert not copy == list
    assert copy.size() == 3
    assert copy.size() == list.size()
    assert copy.head() == 1