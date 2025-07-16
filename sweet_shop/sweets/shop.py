class SweetShop:
    """
    Represents the sweet shop inventory and operations like adding, viewing, and deleting sweets.
    """

    def __init__(self):
        # Internal list to hold all sweet items in the inventory
        self._inventory = []

    def add_sweet(self, sweet):
        """
        Adds a sweet to the inventory.
        """
        self._inventory.append(sweet)

    def get_all_sweets(self):
        """
        Returns a list of all sweets currently in the inventory.
        """
        return self._inventory

    def delete_sweet(self, sweet_id: int):
        """
        Deletes a sweet from the inventory by its unique ID.
        
        Args:
            sweet_id (int): The ID of the sweet to be deleted.
        """
        self._inventory = [s for s in self._inventory if s.id != sweet_id]



    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        """
        Search sweets by optional filters: name (partial, case-insensitive), category, and price range
        """
        results = self._inventory

        if name:
            lower_name = name.lower()
            results = [s for s in results if lower_name in s.name.lower()]

        if category:
            results = [s for s in results if s.category == category]

        if min_price is not None:
            results = [s for s in results if s.price >= min_price]

        if max_price is not None:
            results = [s for s in results if s.price <= max_price]

        return results
    

    def sort_sweets(self, sort_by: str, ascending: bool = True):
        """
        Sort sweets by given attribute: 'name', 'price', or 'quantity'
        """
        key_func_map = {
            'name': lambda s: s.name.lower(),           # case-insensitive sort by name
            'price': lambda s: s.price,
            'quantity': lambda s: s.quantity_in_stock,
        }

        key_func = key_func_map.get(sort_by)
        if key_func is None:
            # If invalid sort_by, return unsorted list (or raise error if you want stricter validation)
            return self._inventory

        return sorted(self._inventory, key=key_func, reverse=not ascending)
