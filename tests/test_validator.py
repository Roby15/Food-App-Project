import unittest
import sys
import os

# Add src folder to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from validator import (
    order_id_validation,
    customer_id_validation,
    status_order_validation,
    order_total_validation,
    delivery_minutes_validation,
    rating_validation,
    cupon_code_validator,
    order_date_validator,
    validate_data
)
from InvalidOrder import InvalidOrder

class TestValidator(unittest.TestCase):
    def setUp(self):
        # Reset class-level counters before each test
        InvalidOrder.count_bad_order_ids = 0
        InvalidOrder.count_duplicate_order_ids = 0
        InvalidOrder.count_bad_customer_ids = 0
        InvalidOrder.count_bad_status_orders = 0
        InvalidOrder.count_suspicious_delivery_times = 0
        InvalidOrder.count_bad_ratings = 0
        InvalidOrder.count_suspicious_cupons = 0
        InvalidOrder.count_bad_dates = 0
        InvalidOrder.count_bad_delivery_times = 0
        InvalidOrder.count_suspicious_ratings = 0
        InvalidOrder.count_imposible_delivery_times = 0
        InvalidOrder.count_bad_order_totals = 0

    def test_order_id_validation_valid(self):
        row = {"order_id": "ORD-1001"}
        self.assertEqual(order_id_validation(row), "1001")

    def test_order_id_validation_empty(self):
        row = {"order_id": ""}
        with self.assertRaises(InvalidOrder):
            order_id_validation(row)

    def test_order_id_validation_bad_prefix(self):
        row = {"order_id": "ODR-1001"}
        with self.assertRaises(InvalidOrder):
            order_id_validation(row)

    def test_order_id_validation_bad_sequence(self):
        row = {"order_id": "ORD-100A"}
        with self.assertRaises(InvalidOrder):
            order_id_validation(row)
        row2 = {"order_id": "ORD-999"}
        with self.assertRaises(InvalidOrder):
            order_id_validation(row2)

    def test_customer_id_validation_valid(self):
        row = {"customer_id": "CUST-501"}
        customer_id_validation(row) # Should not raise

    def test_customer_id_validation_invalid(self):
        row = {"customer_id": "CUST-ABC"}
        with self.assertRaises(InvalidOrder):
            customer_id_validation(row)

    def test_status_order_validation_valid(self):
        for status in ["completed", "cancelled", "refunded", "COMPLETED"]:
            row = {"status": status}
            status_order_validation(row)

    def test_status_order_validation_invalid(self):
        row = {"status": "lost"}
        with self.assertRaises(InvalidOrder):
            status_order_validation(row)

    def test_order_total_validation_valid(self):
        row = {"status": "completed", "order_total": "58.50 RON"}
        order_total_validation(row)

    def test_order_total_validation_free_is_rejected(self):
        row = {"status": "completed", "order_total": "free"}
        with self.assertRaises(InvalidOrder):
            order_total_validation(row)

    def test_order_total_validation_negative_is_rejected(self):
        row = {"status": "completed", "order_total": "-10 RON"}
        with self.assertRaises(InvalidOrder):
            order_total_validation(row)

    def test_order_total_validation_cancelled_empty_is_allowed(self):
        row = {"status": "cancelled", "order_total": ""}
        order_total_validation(row) # Should not raise

    def test_delivery_minutes_validation_impossible_time(self):
        row = {"delivery_minutes": "-5"}
        with self.assertRaises(InvalidOrder):
            delivery_minutes_validation(row)

    def test_delivery_minutes_validation_suspicious_time(self):
        row = {"delivery_minutes": "130", "suspicious": False}
        with self.assertRaises(InvalidOrder):
            delivery_minutes_validation(row)

    def test_rating_validation_valid(self):
        for rating in ["1", "3", "5"]:
            row = {"rating": rating}
            rating_validation(row)

    def test_rating_validation_invalid(self):
        row = {"rating": "6"}
        with self.assertRaises(InvalidOrder):
            rating_validation(row)

    def test_cupon_code_validator_valid(self):
        row = {"coupon_code": "WELCOME-10"}
        self.assertEqual(cupon_code_validator(row), "WELCOME-10")

    def test_cupon_code_validator_invalid_characters(self):
        row = {"coupon_code": "WELCO$E10"}
        with self.assertRaises(InvalidOrder):
            cupon_code_validator(row)

    def test_order_date_validator_valid(self):
        row1 = {"order_date": "2026-04-12"}
        order_date_validator(row1)
        row2 = {"order_date": "2026/04/12"}
        order_date_validator(row2)

    def test_order_date_validator_invalid(self):
        row = {"order_date": "12-04-2026"}
        with self.assertRaises(InvalidOrder):
            order_date_validator(row)

    def test_validate_data_duplicate_detection(self):
        dataset = [
            {"order_id": "ORD-1001", "customer_id": "CUST-501", "restaurant": "Burger Planet", "items": "Cola", "status": "completed", "order_total": "10 RON", "delivery_minutes": "20", "rating": "5", "coupon_code": "", "order_date": "2026-04-12"},
            {"order_id": "ORD-1001", "customer_id": "CUST-502", "restaurant": "Burger Planet", "items": "Fries", "status": "completed", "order_total": "15 RON", "delivery_minutes": "25", "rating": "4", "coupon_code": "", "order_date": "2026-04-12"}
        ]
        validated = list(validate_data(dataset, 3))
        self.assertFalse(validated[0]["flagged"])
        self.assertTrue(validated[1]["flagged"])

    def test_validate_data_coupon_abuse_detection(self):
        dataset = [
            {"order_id": "ORD-1001", "customer_id": "CUST-501", "restaurant": "Burger Planet", "items": "Cola", "status": "completed", "order_total": "10 RON", "delivery_minutes": "20", "rating": "5", "coupon_code": "WELCOME10", "order_date": "2026-04-12"},
            {"order_id": "ORD-1002", "customer_id": "CUST-501", "restaurant": "Burger Planet", "items": "Cola", "status": "completed", "order_total": "10 RON", "delivery_minutes": "20", "rating": "5", "coupon_code": "WELCOME10", "order_date": "2026-04-12"},
            {"order_id": "ORD-1003", "customer_id": "CUST-501", "restaurant": "Burger Planet", "items": "Cola", "status": "completed", "order_total": "10 RON", "delivery_minutes": "20", "rating": "5", "coupon_code": "WELCOME10", "order_date": "2026-04-12"}
        ]
        validated = list(validate_data(dataset, 3))
        self.assertTrue(validated[2]["suspicious"])

if __name__ == "__main__":
    unittest.main()
