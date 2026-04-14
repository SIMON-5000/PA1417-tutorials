class Stack:
    """A last-in, first-out collection.

    methods:
        push(item)  -- add an item to the top of the stack
        pop()       -- remove and return the top item; raises ValueError if empty
        peek()      -- return the top item without removing it; raises ValueError if empty
        size()      -- return the number of items in the stack
        is_empty()  -- return True if the stack contains no items
    """

    def __init__(self):
        """Initialise a new empty stack.

        parameters:
            none

        returns:
            none
        """
        self._items = []

    def push(self, item: str):
        """Push an item onto the top of the stack.

        parameters:
            item -- the value to push

        returns:
            none
        """
        self._items.append(item)

    def pop(self) -> str:
        """Remove and return the item at the top of the stack.

        parameters:
            none

        returns:
            the top item as a string

        raises:
            ValueError -- if the stack is empty
        """
        if not self._items:
            raise ValueError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> str:
        """Return the item at the top of the stack without removing it.

        parameters:
            none

        returns:
            the top item as a string

        raises:
            ValueError -- if the stack is empty
        """
        if not self._items:
            raise ValueError("peek at empty stack")
        return self._items[-1]

    def size(self) -> int:
        """Return the number of items currently in the stack.

        parameters:
            none

        returns:
            an integer count of items
        """
        return len(self._items)

    def is_empty(self) -> bool:
        """Return True if the stack contains no items.

        parameters:
            none

        returns:
            True  -- if the stack has no items
            False -- if the stack has one or more items
        """
        return len(self._items) == 0
