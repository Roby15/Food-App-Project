import csv

def read_file(filepath: str):
    file=open(filepath,"r")
    dictionar=csv.DictReader(file)
    for row in dictionar:
        yield row

