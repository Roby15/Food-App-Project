from reader import read_file
from validator import order_id_validation


file_path="Data/test_data.csv" # To be changed
citirea=read_file(file_path)
for row in citirea:
    print(order_id_validation(row))
