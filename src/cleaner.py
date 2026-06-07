def trim_spaces_from_columns(content):
    for row in content:
        if row["flagged"]==False:
            for key, value in row.items():
                if type(value) is str:
                    row[key] = value.strip()
        yield row

def normalize_columns(content):
    for row in content:
        row["status"]=row["status"].lower()
        row["coupon_code"]