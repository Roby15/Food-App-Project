import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from cleaner import (
    trim_spaces_from_columns,
    normalize_columns,
    convert_columns,
    clean_item_names,
    parse_date_format,
    clean_data
)

class TestCleaner(unittest.TestCase):
    def test_trim_spaces_from_columns(self):
        row = {"order_id": " ORD-1001 ", "restaurant": " Burger Planet ", "flagged": False}
        res = list(trim_spaces_from_columns([row]))[0]
        self.assertEqual(res["order_id"], "ORD-1001")
        self.assertEqual(res["restaurant"], "Burger Planet")

    def test_normalize_columns(self):
        row = {
            "status": " Completed ",
            "coupon_code": " welcome10 ",
            "restaurant": " burger planet ",
            "flagged": False
        }
        # First trim spaces to simulate pipeline, then normalize
        trimmed = list(trim_spaces_from_columns([row]))[0]
        res = list(normalize_columns([trimmed]))[0]
        self.assertEqual(res["status"], "completed")
        self.assertEqual(res["coupon_code"], "WELCOME10")
        self.assertEqual(res["restaurant"], "Burger Planet")

    def test_convert_columns(self):
        row = {
            "order_total": " 58.50 ron ",
            "delivery_minutes": "32",
            "rating": "5",
            "flagged": False
        }
        # Trim first, then convert
        trimmed = list(trim_spaces_from_columns([row]))[0]
        res = list(convert_columns([trimmed]))[0]
        self.assertEqual(res["order_total"], 58.5)
        self.assertEqual(res["delivery_minutes"], 32)
        self.assertEqual(res["rating"], 5)

    def test_clean_item_names(self):
        row = {"items": " chicken burger |  fries ", "flagged": False}
        res = list(clean_item_names([row]))[0]
        self.assertEqual(res["items"], "Chicken Burger|Fries")

    def test_parse_date_format(self):
        row1 = {"order_date": "2026/04/12", "flagged": False}
        row2 = {"order_date": "2026-04-12", "flagged": False}
        
        res1 = list(parse_date_format([row1]))[0]
        res2 = list(parse_date_format([row2]))[0]
        
        self.assertEqual(res1["order_date"], "2026-04-12")
        self.assertEqual(res2["order_date"], "2026-04-12")

    def test_clean_data_integration(self):
        row = {
            "order_id": " ORD-1002 ",
            "customer_id": "CUST-502",
            "customer_name": " Mihai Ionescu ",
            "restaurant": "burger planet",
            "items": "Chicken Burger| fries ",
            "order_total": " 44.00 ron ",
            "delivery_minutes": " 41 ",
            "rating": "4",
            "coupon_code": "",
            "status": " Completed ",
            "order_date": "2026/04/12",
            "flagged": False
        }
        res = list(clean_data([row]))[0]
        self.assertEqual(res["order_id"], "ORD-1002")
        self.assertEqual(res["customer_name"], "Mihai Ionescu")
        self.assertEqual(res["restaurant"], "Burger Planet")
        self.assertEqual(res["items"], "Chicken Burger|Fries")
        self.assertEqual(res["order_total"], 44.0)
        self.assertEqual(res["delivery_minutes"], 41)
        self.assertEqual(res["rating"], 4)
        self.assertEqual(res["status"], "completed")
        self.assertEqual(res["order_date"], "2026-04-12")

if __name__ == "__main__":
    unittest.main()
