from datetime import datetime
accepted_status=["completed","cancelled","refunded"]
class InvalidOrder(Exception):
    pass

def order_id_validation(content):
    if content["order_id"].strip() == "":
        raise InvalidOrder("Order id is missing")
    if not content["order_id"].startswith("ORD-"):
        raise InvalidOrder("Order_id patern is incomplete")
    if not content["order_id"][4:].isdigit():
        raise InvalidOrder("Order_id patern is incorect")
    if int(content["order_id"][4:]) <1001:
        raise InvalidOrder("Order_id number is too low")
    return content["order_id"][4:]

def customer_id_validation(content):
    if content["customer_id"].strip()=="":
        raise InvalidOrder("Customer id is missing")
    if not content["customer_id"].startswith("CUST-"):
        raise InvalidOrder("Customer_id patern is incomplete")
    if not content["customer_id"][5:].isdigit():
        raise InvalidOrder("Customer_id patern is incorect")


def status_order_validation(content):
    if content["status"].lower() not in accepted_status:
        raise InvalidOrder("Status is wrong")
    

def order_total_validation(content):
    if content["status"].lower() != "cancelled":    
        if content["order_total"]=="":
            raise InvalidOrder("Invalid order total")
    elif content["status"].lower() == "cancelled" and content["order_total"]=="":
        return
    
    number_total_order=content["order_total"].lower().replace("ron","").strip()
    try:
        amount=float(number_total_order)
    except:
        raise InvalidOrder("Order total not convertible")
    if(amount<1):
        raise InvalidOrder("Number is negative or 0")

def delivery_minutes_validation(content,suspicios_count):
    if content["delivery_minutes"]=="":
        raise InvalidOrder("Delivery time does not exist")
    if not content["delivery_minutes"].isnumeric():
        raise InvalidOrder("Delivery time should be a number")
    delivery_time=int(content["delivery_minutes"])
    if delivery_time<1:
        raise InvalidOrder("Delivery time should be greater than 0")
    if delivery_time>120 and delivery_time<240:
        suspicios_count=1
        return suspicios_count
    if delivery_time>240:
        raise InvalidOrder("Delivery time is invalid")
        
def rating_validation(content):
    if content["rating"]=="":
        raise InvalidOrder("Rating does not exist")
    if not content["rating"].isnumeric():
        raise InvalidOrder("Rating is not a number")
    if content["rating"]<'1' or content["rating"]>'5':
        raise InvalidOrder("Rating is not in the normal range")

def cupon_code_validator(content):
    if not (all(char.isalnum() or char in "-_" for char in content["coupon_code"])):
        raise InvalidOrder("Cupon code is invalid")
    return content["coupon_code"]

def order_date_validator(content):
    valid_formats=["%Y/%m/%d","%Y-%m-%d"]
    for fmt in valid_formats:
        try:
            datetime.strptime(content["order_date"],fmt)
            return
        except:
            pass
    
    raise InvalidOrder("Date does not match any valid format")

    


def validate_data(content,cupon_frequency_until_suspicious):
    validated_ids_dict={}
    suspicious_coupons_dict={}
    count_bad_order_ids=0
    count_bad_customer_ids=0
    count_bad_status_orders=0
    count_suspicious_delivery_time=0
    count_bad_rating=0
    count_suspicious_cupon=0
    count_bad_dates=0
    for row in content:
        try:
            row["flagged"]=False
            order_id=order_id_validation(row)
            if validated_ids_dict.get(order_id,0):
                raise InvalidOrder("Order_id is not unique")
            else:
                validated_ids_dict[order_id]=1
        except:
            count_bad_order_ids+=1
            row["flagged"]=True
        try:
            customer_id_validation(row)
        except:
            count_bad_customer_ids+=1
            row["flagged"]=True
        try:
            status_order_validation(row)
        except:
            row["flagged"]=True
        try:
            order_total_validation(row)
        except:
            row["flagged"]=True
        try:
           count_suspicious_delivery_time+=delivery_minutes_validation(row,count_suspicious_delivery_time)
        except:
            row["flagged"]=True
        try:
            rating_validation(row)
        except:
            count_bad_rating+=1
        try:
            coupon_code=cupon_code_validator(row)
            if coupon_code!="":
                if suspicious_coupons_dict.get(coupon_code,0):
                    suspicious_coupons_dict[coupon_code]+=1
                else:
                    suspicious_coupons_dict[coupon_code]=1
                if suspicious_coupons_dict.get(coupon_code)==cupon_frequency_until_suspicious:
                    raise InvalidOrder("Suspicious number of identic coupon codes")

        except:
            count_suspicious_cupon+=1
        try:
            order_date_validator(row)
        except:
            count_bad_dates+=1
            row["flagged"]=True
        yield row
            
        
        analysiz_dict = {
        "order_ids_bad": count_bad_order_ids,
        "customer_ids_bad": count_bad_customer_ids,
        "bad_status_orders": count_bad_status_orders,
        "suspicious_delivery": count_suspicious_delivery_time,
        "bad_ratings": count_bad_rating,
        "suspicious_coupon_codes": count_suspicious_cupon,
        "bad_dates": count_bad_dates
    }
    yield analysiz_dict
            
    

        
        
        
    



    

    