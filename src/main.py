from cleaner import clean_data
from reader import read_file
from validator import validate_data,InvalidOrder
from Analyzer import analyzer
from reporter import generate_report


cupon_frequency_until_suspicious=3
file_path="Data/generated_orders.csv" # To be changed
citirea=read_file(file_path)
Validated_date=validate_data(citirea,cupon_frequency_until_suspicious)
Cleaned_data=clean_data(Validated_date)
analized_data=analyzer(Cleaned_data)
generate_report(analized_data)




