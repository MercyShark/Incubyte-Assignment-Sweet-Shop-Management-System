class SweetShop:
    def __init__(self):
        self._inventory = []

    def add_sweet(self, sweet):
        self._inventory.append(sweet)

    def get_all_sweets(self):
        return self._inventory
