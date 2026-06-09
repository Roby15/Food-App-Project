import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from Analyzer import analyzer

class TestAnalyzer(unittest.TestCase):
    def test_analyzer_calculations(self):
        # Controlled dataset
        # Pizza Palace: 2 completed orders, total revenue = 50 + 60 = 110, total delivery time = 30 + 40 = 70.
        #               Rating sum = 5 + 4 = 9, Rating count = 2. Avg rating = 4.5
        # Burger Planet: 1 completed order, total revenue = 40, total delivery time = 50.
        #                Rating sum = 3, Rating count = 1. Avg rating = 3.0
        # Dessert Den: 1 cancelled order.
        dataset = [
            {
                "order_id": "ORD-1001",
                "restaurant": "Pizza Palace",
                "items": "Pizza|Soda",
                "status": "completed",
                "order_total": 50.0,
                "delivery_minutes": 30,
                "rating": 5,
                "flagged": False,
                "suspicious": False
            },
            {
                "order_id": "ORD-1002",
                "restaurant": "Pizza Palace",
                "items": "Pizza|Garlic Dip",
                "status": "completed",
                "order_total": 60.0,
                "delivery_minutes": 40,
                "rating": 4,
                "flagged": False,
                "suspicious": False
            },
            {
                "order_id": "ORD-1003",
                "restaurant": "Burger Planet",
                "items": "Burger|Fries",
                "status": "completed",
                "order_total": 40.0,
                "delivery_minutes": 50,
                "rating": 3,
                "flagged": False,
                "suspicious": False
            },
            {
                "order_id": "ORD-1004",
                "restaurant": "Dessert Den",
                "items": "Cake",
                "status": "cancelled",
                "order_total": "",
                "delivery_minutes": "",
                "rating": "",
                "flagged": False,
                "suspicious": False
            }
        ]
        
        # Suppress prints during test
        import io
        sys.stdout = io.StringIO()
        try:
            res = analyzer(dataset)
        finally:
            sys.stdout = sys.__stdout__

        # General counts
        self.assertEqual(res["all_readings"], 4)
        self.assertEqual(res["valid_records"], 4)
        self.assertEqual(res["invalid_records"], 0)
        self.assertEqual(res["suspicious_records"], 0)
        
        # Status counts
        self.assertEqual(res["completed_orders"], 3)
        self.assertEqual(res["cancelled_orders"], 1)
        self.assertEqual(res["refunded_orders"], 0)

        # Revenue
        self.assertEqual(res["completed_revenue"], 150.0) # 50 + 60 + 40
        self.assertEqual(res["average_order_value"], 50.0) # 150 / 3

        # Delivery Time
        self.assertEqual(res["average_delivery_minutes"], 40.0) # (30 + 40 + 50) / 3

        # Restaurant stats
        self.assertEqual(res["restaurant_most_orders"], ("Pizza Palace", 2))
        self.assertEqual(res["restaurant_highest_revenue"], ("Pizza Palace", 110.0))
        self.assertEqual(res["slowest_delivery_time"], ("Burger Planet", 50.0))

        # Average ratings (sorted descending by rating)
        self.assertEqual(res["average_ratings"][0], ("Pizza Palace", 4.5))
        self.assertEqual(res["average_ratings"][1], ("Burger Planet", 3.0))

        # Popular Items
        # Pizza: 2 orders
        # Soda: 1 order
        # Garlic Dip: 1 order
        # Burger: 1 order
        # Fries: 1 order
        # (Top 3 items)
        pop_items = [item for item, qty in res["most_popular_items"]]
        self.assertIn("Pizza", pop_items)
        self.assertEqual(len(res["most_popular_items"]), 3)

if __name__ == "__main__":
    unittest.main()
