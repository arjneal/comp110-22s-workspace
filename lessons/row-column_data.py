"""Practice creating functions that iterate through row and column data."""

row_data: list[dict[str, str]] = [ 
    {"name": "UNC", "city": "Chapel Hill"},  
    {"name": "Duke", "city": "Durham"}
]

col_data: dict[str, list[str]] = { 
    "name": ['UNC', 'Duke'],
    "city": ['Chapel Hill', 'Durham']
}

# Practice Looking up "UNC"
to_print: bool = True

if to_print:
    print(row_data[0]["name"])
    print(col_data["name"][0])


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Practice developing the head function as seen in data_wrangling."""
    result: dict[str, list[str]] = {}
    for column in table: 
        r_list: list[str] = [] 
        i: int = 0 
        while i != n:
            r_list.append(table[column][i])
            i += 1
        result[column] = r_list
    return result

print(head(col_data, 1))