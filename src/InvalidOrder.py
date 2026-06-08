class InvalidOrder(Exception):
    # Plural counter variables
    count_bad_order_ids = 0
    count_duplicate_order_ids = 0
    count_bad_customer_ids = 0
    count_bad_status_orders = 0
    count_suspicious_delivery_times = 0
    count_bad_ratings = 0
    count_suspicious_cupons = 0
    count_bad_dates = 0
    count_bad_delivery_times=0

    # Singular counter/factory classmethods
    @classmethod
    def count_bad_order_id(cls, message="Invalid order ID"):
        cls.count_bad_order_ids += 1
        return cls(message)
    
    @classmethod
    def count_duplicate_order_id(cls, message="Duplicate order ID"):
        cls.count_duplicate_order_ids += 1
        return cls(message)

    @classmethod
    def count_bad_customer_id(cls, message="Invalid customer ID"):
        cls.count_bad_customer_ids += 1
        return cls(message)

    @classmethod
    def count_bad_status_order(cls, message="Invalid status"):
        cls.count_bad_status_orders += 1
        return cls(message)

    @classmethod
    def count_suspicious_delivery_time(cls, message="Suspicious delivery time"):
        cls.count_suspicious_delivery_times += 1
        return cls(message)

    @classmethod
    def count_bad_rating(cls, message="Invalid rating"):
        cls.count_bad_ratings += 1
        return cls(message)

    @classmethod
    def count_suspicious_cupon(cls, message="Suspicious coupon code"):
        cls.count_suspicious_cupons += 1
        return cls(message)

    @classmethod
    def count_bad_date(cls, message="Invalid date"):
        cls.count_bad_dates += 1
        return cls(message)

    @classmethod
    def count_bad_delivery_time(cls, message="Bad Delivery time"):
        cls.count_bad_delivery_times +=1
        return cls(message)

