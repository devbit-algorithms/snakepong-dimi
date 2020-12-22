from stack import Stack

def test_empty_stack():
    stack = Stack()
    assert stack.isEmpty()

def test_filled_stack():
    stack = Stack()
    stack.push(1)
    assert stack.top() == 1
    stack.push(2).push(3)
    assert stack.top() == 3
    assert stack.size() == 3