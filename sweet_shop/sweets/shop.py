class SweetShop:
    def __init__(self):
        self._inventory = []

    def add_sweet(self, sweet):
        self._inventory.append(sweet)

    def get_all_sweets(self):
        return self._inventory

    def delete_sweet(self, sweet_id: int):
        self._inventory = [s for s in self._inventory if s.id != sweet_id]
    