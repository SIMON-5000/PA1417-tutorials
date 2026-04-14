class ShoppingCart:
    """A simple in-memory shopping cart.

    Items are identified by name. Adding an item whose name is already
    present overwrites its price.

    Methods:
        add_item(name, price)  — add or update an item
        remove_item(name)      — remove an item; raises ValueError if absent
        total()                — sum of all item prices
        item_count()           — number of distinct items in the cart
        is_empty()             — True when the cart contains no items
    """

    def __init__(self) -> None:
        """Initialise a new empty shopping cart.

        parameters:
            none

        returns:
            none
        """
        self._items: dict[str, float] = {}

    def add_item(self, name: str, price: float) -> None:
        """Add an item to the cart, or overwrite its price if it already exists.

        parameters:
            name  -- the item name used as a unique identifier
            price -- the price of the item in SEK

        returns:
            none
        """
        self._items[name] = price

    def remove_item(self, name: str) -> None:
        """Remove an item from the cart by name.

        parameters:
            name -- the item name to remove

        returns:
            none

        raises:
            ValueError -- if name is not in the cart
        """
        if name not in self._items:
            raise ValueError(f"'{name}' is not in the cart")
        del self._items[name]

    def total(self) -> float:
        """Return the sum of all item prices in the cart.

        parameters:
            none

        returns:
            the total price as a float
        """
        return sum(self._items.values())

    def item_count(self) -> int:
        """Return the number of distinct items currently in the cart.

        parameters:
            none

        returns:
            an integer count of distinct items
        """
        return len(self._items)

    def is_empty(self) -> bool:
        """Return True if the cart contains no items.

        parameters:
            none

        returns:
            True  -- if the cart has no items
            False -- if the cart has one or more items
        """
        return len(self._items) == 0
