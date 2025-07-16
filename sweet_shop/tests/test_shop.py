import unittest
from sweets.shop import SweetShop
from sweets.models import Sweet

class TestSweetShop_AddSweet(unittest.TestCase):

    def test_add_single_sweet(self):
        # Arrange: create shop and sweet
        shop = SweetShop()
        sweet = Sweet(
            id=1001,
            name="Kaju Katli",
            category="Nut-Based",
            price=50,
            quantity_in_stock=20
        )

        # Act: add sweet to the shop
        shop.add_sweet(sweet)

        # Assert: check sweet was added
        sweets = shop.get_all_sweets()
        self.assertEqual(len(sweets), 1)
        self.assertEqual(sweets[0].name, "Kaju Katli")

if __name__ == "__main__":
    unittest.main()
