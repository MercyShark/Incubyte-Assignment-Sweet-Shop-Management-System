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




class TestSweetShop_DeleteSweet(unittest.TestCase):
    def test_delete_sweet_by_id(self):
        """
        Test that a sweet can be successfully deleted from the inventory using its unique ID.
        """

        # Arrange: Create the shop and add one sweet to it
        shop = SweetShop()
        sweet = Sweet(
            id=1001,
            name="Kaju Katli",
            category="Nut-Based",
            price=50,
            quantity_in_stock=20
        )
        shop.add_sweet(sweet)

        # Act: Delete the sweet by its ID
        shop.delete_sweet(1001)

        # Assert: Ensure the inventory is empty after deletion
        sweets = shop.get_all_sweets()
        self.assertEqual(len(sweets), 0)




class TestSweetShop_ViewSweets(unittest.TestCase):
    def test_view_all_sweets_returns_correct_list(self):
        """
        Test that the shop returns a correct list of all sweets in the inventory.
        """

        # Arrange
        shop = SweetShop()
        sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity_in_stock=20)
        sweet2 = Sweet(id=1002, name="Gajar Halwa", category="VegetableBased", price=30, quantity_in_stock=15)

        shop.add_sweet(sweet1)
        shop.add_sweet(sweet2)

        # Act
        sweets = shop.get_all_sweets()

        # Assert
        self.assertEqual(len(sweets), 2)
        self.assertEqual(sweets[0].name, "Kaju Katli")
        self.assertEqual(sweets[1].name, "Gajar Halwa")


class TestSweetShop_SearchSweets(unittest.TestCase):
    def setUp(self):
        """
        Setup shop with example sweets for search tests:
          - Kaju Katli (Nut-Based)
          - Gajar Halwa (VegetableBased)
          - Gulab Jamun (Milk-Based)
        """
        self.shop = SweetShop()
        self.shop.add_sweet(Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity_in_stock=20))
        self.shop.add_sweet(Sweet(id=1002, name="Gajar Halwa", category="VegetableBased", price=30, quantity_in_stock=15))
        self.shop.add_sweet(Sweet(id=1003, name="Gulab Jamun", category="Milk-Based", price=10, quantity_in_stock=50))

    def test_search_by_name(self):
        """Search sweets by partial name, case-insensitive."""
        results = self.shop.search_sweets(name="gajar")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Gajar Halwa")

    def test_search_by_category(self):
        """Search sweets by exact category."""
        results = self.shop.search_sweets(category="Milk-Based")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Gulab Jamun")

    def test_search_by_price_range(self):
        """Search sweets within given price range (inclusive)."""
        results = self.shop.search_sweets(min_price=10, max_price=30)
        self.assertEqual(len(results), 2)
        found_names = sorted([sweet.name for sweet in results])
        self.assertListEqual(found_names, ["Gajar Halwa", "Gulab Jamun"])

if __name__ == "__main__":
    unittest.main()
