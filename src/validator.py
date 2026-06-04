from reader import read_file


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

file_path="Data/test_data.csv" # To be changed
citirea=read_file(file_path)
validated_ids_list=[]
for row in citirea:
    validated_ids_list.append(order_id_validation(row))

is_unique= len(set(validated_ids_list))==len(validated_ids_list)
if not is_unique:
    raise InvalidOrder("Elements from the list are not unique")





    

    