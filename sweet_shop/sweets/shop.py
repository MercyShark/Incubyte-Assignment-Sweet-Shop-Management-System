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
