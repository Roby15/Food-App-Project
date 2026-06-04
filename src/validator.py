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


    

    

def validate_data(content):
    validated_ids_dict={}
    count_bad_order_ids=0
    count_bad_customer_ids=0
    count_bad_status_orders=0
    for row in content:
        try:
            order_id=order_id_validation(row)
            if validated_ids_dict.get(order_id,0):
                raise InvalidOrder("Order_id is not unique")
            else:
                validated_ids_dict[order_id]=1
        except:
            count_bad_order_ids+=1
        try:
            customer_id_validation(row)
        except:
            count_bad_customer_ids+=1
        try:
            status_order_validation(row)
        except:
            ...
        try:
            order_total_validation(row)
        except:
            ...
        

    print("Order ids wrong:",count_bad_order_ids)
    print("Customer ids wrong:",count_bad_customer_ids)
    print("Bad status orders:",count_bad_status_orders)
            
    

        
        
        
    



    

    