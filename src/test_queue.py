from queue import Queue

def test_empty_queue():
    queue = Queue()
    assert queue.isEmpty()

def test_filled_queue():
    queue = Queue()
    queue.add(1)
    assert queue.remove() == 1
    queue.add(1).add(2).add(3)
    assert queue.remove() == 1
    assert queue.remove() == 2