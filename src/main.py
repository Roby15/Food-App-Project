from cleaner import trim_spaces_from_columns
from reader import read_file
from validator import validate_data

cupon_frequency_until_suspicious=3
file_path="Data/test_data.csv" # To be changed
citirea=read_file(file_path)
Validated_date=validate_data(citirea,cupon_frequency_until_suspicious)
Cleaned_data=trim_spaces_from_columns(Validated_date)
for row in Cleaned_data:
    print(row)