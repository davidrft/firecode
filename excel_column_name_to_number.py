# We're sure you've used Microsoft Excel or Google Sheets at some point. Given a
# column name of the spreadsheet, return the corresponding column number.

# Note: Column name "A" corresponds to column number 1

# Examples:

# Input  : A
# Output : 1

# Input  : AA
# Output : 27

def excel_column_name_to_number(column_title: str) -> int:
    result = 0
    for c in column_title:
        result *= ord('Z') - ord('A') + 1
        result += ord(c) - ord('A') + 1
    return result

if __name__ == '__main__':
    assert(excel_column_name_to_number('A') == 1)
    assert(excel_column_name_to_number('AA') == 27)