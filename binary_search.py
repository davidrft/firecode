# Write a function that searches a list of ints for a given integer using the
# Binary Search Algorithm. If the input integer is found in the list, return
# True. Otherwise, return False. You can assume that the given list of integers
# is already sorted in ascending order.

# Examples: binary_search([2, 5, 7, 8, 9],9) -> True

# binary_search([2, 8, 9, 12],6) -> False

# binary_search([2],4) -> False

# binary_search([],9) -> False

# [] -> [Empty] Array 

from typing import List

def binary_search(a_list: List[int], item: int) -> bool:
    l, r = 0, len(a_list) - 1

    while l <= r:
        m = r + (l - r)//2
        if a_list[m] == item:
            return True
        elif a_list[m] < item:
            l = m + 1
        else:
            r = m - 1
    
    return False

if __name__ == '__main__':
    assert(binary_search([2, 5, 7, 8, 9], 9))
    assert(binary_search([0, 2, 4, 5, 6], 5))
