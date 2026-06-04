from reader import read_file
from validator import validate_data


file_path="Data/test_data.csv" # To be changed
citirea=read_file(file_path)
print(validate_data(citirea))
