"""Dictionary related utility functions for exercise 8."""

__author__ = "730484878"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    # Returns a list of the rows. 
    result: list[dict[str, str]] = [] 

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Read that file.
    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close that file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = [] 
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Practice developing the head function as seen in data_wrangling."""
    result: dict[str, list[str]] = {}
    if n >= len(table):
        return table
    for column in table: 
        r_list: list[str] = [] 
        # r_list = return list
        i: int = 0 
        # establishes an empty list that returns only the (n) number of values that we want. 
        while i != n:
            r_list.append(table[column][i])
            # Using subscription notation appends the specific value at index i. 
            # Because Column it is table["str"][int].
            i += 1
        result[column] = r_list
    return result


def select(table: dict[str, list[str]], cnames: list[str]) -> dict[str, list[str]]:
    """Selects the specific columns based on their names that we want."""
    result: dict[str, list[str]] = {}
    for key in cnames:
        result[key] = table[key]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concats two dictionaries together."""
    result: dict[str, list[str]] = {} 
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else:
            result[column] = table_2[column]
    return result


def count(counters: list[str]) -> dict[str, int]:
    # I was getting a key error for running the count function as type dict[str, list[int]] furthermore the output of running it this way matches with the output that was given.
    """Counts the iterations of the different subjects."""        
    result: dict[str, int] = {}
    for item in counters:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


# Scrapes and organizes the data from the count dictionary. 
def want_synch(synch: dict[str, int]) -> dict[str, int]:
    """Writes down whether students are in favor of or against synchronous classes."""
    result_dict: dict[str, int] = {}
    for item in synch:
        counter: int = synch[item]
        if int(item) == 4:
            if "neutral" in result_dict:
                result_dict["neutral"] += counter
            else: 
                result_dict["neutral"] = counter
        elif int(item) > 4:
            if "synchronous" in result_dict:
                result_dict["synchronous"] += counter
            else:
                result_dict["synchronous"] = counter
        elif int(item) < 4:
            if "asynchronous" in result_dict:
                result_dict["asynchronous"] += counter
            else:
                result_dict["asynchronous"] = counter 
    return result_dict
