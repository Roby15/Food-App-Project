from datetime import datetime
def trim_spaces_from_columns(content):
    for row in content:
        if row["flagged"]==False:
            for key, value in row.items():
                if type(value) is str:
                    row[key] = value.strip()
        yield row

def normalize_columns(content):
    for row in content:
        if row["flagged"]==False:
            row["status"]=row["status"].lower()
            row["coupon_code"]=row["coupon_code"].upper()
            row["restaurant"]=row["restaurant"].title()
        yield row

def convert_columns(content):
    for row in content:
        if row["flagged"]==False:
            number_total_order=row["order_total"].lower().replace("ron","").strip()
            if number_total_order.isnumeric():
                row["order_total"]=float(number_total_order)
            row["delivery_minutes"]=int(row["delivery_minutes"])
            if row["rating"].isnumeric():
                row["rating"]=int(row["rating"])

        yield row
def clean_item_names(content):
    for row in content:
        if row["flagged"]==False:
            items=row["items"].split(sep="|")
            items_normalized=[]
            for item in items:
                item=item.strip()
                item=item.title()
                items_normalized.append(item)
            row["items"]="|".join(items_normalized)
        yield row

def parse_date_format(content):
    valid_formats = ["%Y/%m/%d", "%Y-%m-%d"]
    for row in content:
        if row["flagged"]==False:
            for fmt in valid_formats:
                try:
                    dt=datetime.strptime(row["order_date"],fmt)
                    row["order_date"]=dt.strftime("%Y-%m-%d")
                    break
                except ValueError:
                    pass
        yield row

def clean_data(content):
    trimed_content=trim_spaces_from_columns(content)
    normalized_content=normalize_columns(trimed_content)
    converted_content=convert_columns(normalized_content)
    cleaned_items=clean_item_names(converted_content)
    parsed_date_formats=parse_date_format(cleaned_items)
    return parsed_date_formats