def trim_spaces_from_columns(content):
    # Iterate over the incoming generator (row by row)
    for row in content:
        # Loop through every column in the current row
        for key, value in row.items():
            if isinstance(value, str):
                row[key] = value.strip()
        # Yield the cleaned row to the next step
        yield row