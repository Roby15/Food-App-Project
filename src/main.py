from cleaner import clean_data
from reader import read_file
from validator import validate_data,InvalidOrder


cupon_frequency_until_suspicious=3
file_path="Data/generated_orders.csv" # To be changed
citirea=read_file(file_path)
Validated_date=validate_data(citirea,cupon_frequency_until_suspicious)
Cleaned_data=clean_data(Validated_date)
for row in Cleaned_data:
    print(row)

counter=InvalidOrder.count_duplicate_order_ids
print(counter)


