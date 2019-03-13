# Write a function that takes in a string and returns the reversed version of
# the string.

# Examples:

# reverse_string("abcde") -> "edcba"

# reverse_string("1") -> "1"

# reverse_string("") -> ""

# reverse_string("madam") -> "madam"

def reverse_string(a_string: str) -> str:
    result = ""
    for c in a_string:
        result = c + result
    return result

if __name__ == '__main__':
    assert(reverse_string('abc') == 'cba')
    assert(reverse_string('a') == 'a')
