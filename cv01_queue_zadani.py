#!/usr/bin/env python3

from typing import Any


class Item:
    """Trida Item slouzi pro reprezentaci objektu ve fronte.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        left    reference na dalsi prvek ve fronte
    """

    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.left: Item | None = None


class Queue:
    """Trida Queue reprezentuje frontu.

    Atributy:
        atribut first je reference na prvni prvek
        atribut last je reference na posledni prvek
    """

    def __init__(self) -> None:
        self.first: Item | None = None
        self.last: Item | None = None


def enqueue(queue: Queue, value: Any) -> None:
    """Metoda enqueue vlozi do fronty (queue) novy prvek s hodnotou
    (value).
    """
    item: Item = Item(value)
    
    if queue.last is not None:
        queue.last.left = item
        queue.last = item
    else:
        queue.first = item
        queue.last = item


def dequeue(queue: Queue) -> Any | None:
    """Metoda dequeue odebere prvni prvek z fronty (queue).
    Vraci hodnotu (value) odebraneho prvku, pokud je fronta prazdna,
    vraci None
    """

    output = queue.first

    if output is not None:
        queue.first = queue.first.left
    if output == queue.last:
        queue.last = None
    
    if output is not None:
        return output.value


def is_empty(queue: Queue) -> bool:
    """is_empty() vraci True v pripade prazdne fronty, jinak False."""
    return queue.first is None and queue.last is None


# Testy implementace
def test_enqueue_empty() -> None:
    print("Test 1. Vkladani do prazdne fronty: ", end="")

    queue = Queue()
    enqueue(queue, 1)

    if queue.first is None or queue.last is None:
        print("FAIL")
        return

    if (queue.first.value == 1 and queue.first.left is None and
            queue.last.value == 1 and queue.last.left is None):
        print("OK")
    else:
        print("FAIL")


def test_enqueue_nonempty() -> None:
    print("Test 2. Vkladani do neprazdne fronty: ", end="")

    queue = Queue()
    item = Item(1)
    item.left = None
    queue.first = item
    queue.last = item

    enqueue(queue, 2)

    if queue.first is None or queue.last is None:
        print("FAIL")
        return
    if (queue.last.value == 2 and queue.first == item and
            queue.first.left is not None and queue.first.left.value == 2):
        print("OK")
    else:
        print("FAIL")


def test_dequeue_empty() -> None:
    print("Test 3. Odebirani z prazdne fronty: ", end="")

    queue = Queue()
    value = dequeue(queue)

    if value is not None or queue.first is not None or queue.last is not None:
        print("FAIL")
    else:
        print("OK")


def test_dequeue_nonempty() -> None:
    print("Test 4. Odebirani z neprazdne fronty: ", end="")

    queue = Queue()
    item = Item(1)
    item.left = None
    queue.first = item
    queue.last = item

    value = dequeue(queue)

    if value != 1 or queue.first is not None or queue.last is not None:
        print("FAIL")
    else:
        print("OK")


def test_is_empty_empty() -> None:
    print("Test 5. is_empty na prazdne fronte: ", end="")

    queue = Queue()

    if is_empty(queue):
        print("OK")
    else:
        print("FAIL")


def test_is_empty_nonempty() -> None:
    print("Test 6. is_empty na neprazdne fronte: ", end="")

    queue = Queue()
    item = Item(1)
    item.left = None
    queue.first = item
    queue.last = item

    if is_empty(queue):
        print("FAIL")
    else:
        print("OK")


if __name__ == '__main__':
    test_enqueue_empty()
    test_enqueue_nonempty()
    test_dequeue_empty()
    test_dequeue_nonempty()
    test_is_empty_empty()
    test_is_empty_nonempty()
