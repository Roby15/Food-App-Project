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


def validate_data(content):
    validated_ids_dict={}
    for row in content:
        order_id=order_id_validation(row)
        if validated_ids_dict.get(order_id,0):
            raise InvalidOrder("Order_id is not unique")
        else:
            validated_ids_dict[order_id]=1
        
        
        
    



    

    