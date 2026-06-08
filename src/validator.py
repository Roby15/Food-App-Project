from datetime import datetime
from InvalidOrder import InvalidOrder

accepted_status = ["completed", "cancelled", "refunded"]


def order_id_validation(content):
    if content["order_id"].strip() == "":
        raise InvalidOrder.count_bad_order_id("Order ID is empty") 
    if not content["order_id"].startswith("ORD-"):
        raise InvalidOrder.count_bad_order_id("Order ID must start with ORD-")
    if not content["order_id"][4:].isdigit():
        raise InvalidOrder.count_bad_order_id("Order ID sequence must be numeric")
    if int(content["order_id"][4:]) < 1001:
        raise InvalidOrder.count_bad_order_id("Order ID sequence must be 1001 or greater")
    return content["order_id"][4:]


def customer_id_validation(content):
    if content["customer_id"].strip() == "":
        raise InvalidOrder.count_bad_customer_id("Customer id is missing")
    if not content["customer_id"].startswith("CUST-"):
        raise InvalidOrder.count_bad_customer_id("Customer_id patern is incomplete")
    if not content["customer_id"][5:].isdigit():
        raise InvalidOrder.count_bad_customer_id("Customer_id patern is incorect")


def status_order_validation(content):
    if content["status"].lower() not in accepted_status:
        raise InvalidOrder.count_bad_status_order("Status is wrong")


def order_total_validation(content):
    if content["status"].lower() != "cancelled":    
        if content["order_total"] == "":
            raise InvalidOrder("Invalid order total")
    elif content["status"].lower() == "cancelled" and content["order_total"] == "":
        return
    
    number_total_order = content["order_total"].lower().replace("ron", "").strip()
    try:
        amount = float(number_total_order)
    except:
        raise InvalidOrder("Order total not convertible")
    if amount < 1:
        raise InvalidOrder("Number is negative or 0")


def delivery_minutes_validation(content, suspicios_count):
    if content["delivery_minutes"] == "":
        raise InvalidOrder.count_bad_delivery_time()
    if not content["delivery_minutes"].isnumeric():
        raise InvalidOrder.count_bad_delivery_time()
    delivery_time = int(content["delivery_minutes"])
    if delivery_time < 1:
        raise InvalidOrder.count_suspicious_delivery_time("Delivery time should be greater than 0")
    if 120 < delivery_time < 240:
        suspicios_count = 1
        return suspicios_count
    if delivery_time > 240:
        raise InvalidOrder.count_suspicious_delivery_time("Delivery time is invalid")


def rating_validation(content):
    if content["rating"] == "":
        raise InvalidOrder.count_bad_rating("Rating does not exist")
    if not content["rating"].isnumeric():
        raise InvalidOrder.count_bad_rating("Rating is not a number")
    if content["rating"] < '1' or content["rating"] > '5':
        raise InvalidOrder.count_bad_rating("Rating is not in the normal range")


def cupon_code_validator(content):
    if not (all(char.isalnum() or char in "-_" for char in content["coupon_code"])):
        raise InvalidOrder.count_suspicious_cupon("Cupon code is invalid")
    return content["coupon_code"]


def order_date_validator(content):
    valid_formats = ["%Y/%m/%d", "%Y-%m-%d"]
    for fmt in valid_formats:
        try:
            datetime.strptime(content["order_date"], fmt)
            return
        except:
            pass
    
    raise InvalidOrder.count_bad_date("Date does not match any valid format")


def validate_data(content, cupon_frequency_until_suspicious):
    # Reset class-level counters
    InvalidOrder.count_bad_order_ids = 0
    InvalidOrder.count_duplicate_order_ids = 0
    InvalidOrder.count_bad_customer_ids = 0
    InvalidOrder.count_bad_status_orders = 0
    InvalidOrder.count_suspicious_delivery_times = 0
    InvalidOrder.count_bad_ratings = 0
    InvalidOrder.count_suspicious_cupons = 0
    InvalidOrder.count_bad_dates = 0

    validated_ids_dict = {}
    suspicious_coupons_dict = {}
    for row in content:
        try:
            row["flagged"] = False
            order_id = order_id_validation(row)
            if validated_ids_dict.get(order_id, 0):
                raise InvalidOrder.count_duplicate_order_id()
            else:
                validated_ids_dict[order_id] = 1
        except InvalidOrder:
            row["flagged"] = True
        try:
            customer_id_validation(row)
        except InvalidOrder:
            row["flagged"] = True
        try:
            status_order_validation(row)
        except InvalidOrder:
            row["flagged"] = True
        try:
            order_total_validation(row)
        except InvalidOrder:
            row["flagged"] = True
        try:
            res = delivery_minutes_validation(row, 0)
            if res:
                InvalidOrder.count_suspicious_delivery_time()
        except InvalidOrder:
            row["flagged"] = True
        try:
            rating_validation(row)
        except InvalidOrder:
            pass
        try:
            coupon_code = cupon_code_validator(row)
            if coupon_code != "":
                if suspicious_coupons_dict.get(coupon_code, 0):
                    suspicious_coupons_dict[coupon_code] += 1
                else:
                    suspicious_coupons_dict[coupon_code] = 1
                if suspicious_coupons_dict.get(coupon_code) == cupon_frequency_until_suspicious:
                    raise InvalidOrder.count_suspicious_cupon("Suspicious number of identic coupon codes")
        except InvalidOrder:
            pass
        try:
            order_date_validator(row)
        except InvalidOrder:
            row["flagged"] = True
        yield row