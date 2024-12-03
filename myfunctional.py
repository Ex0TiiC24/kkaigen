from typing import Callable,Any
from functools import reduce
# Problem 1:
# Write a function 'func01' that receives a list of integers and returns the sum of all even integers in the list. 
# If there are no even integers, return 0. This function does not validate its parameter. 
# Write this function in a functional style.
# Example usage:
# func01([1, 2, 3, 4, 5])  # Output: 6
# func01([1, 3, 5, 7])     # Output: 0
# func01([2, 4, 6, 8])     # Output: 20
def func01(ls: list[int]) -> int:
    return reduce(lambda x,y: x+y,filter(lambda x:x%2==0,ls),0)


# Problem 2:
# Write a function 'func02' that receives a list of strings and returns a new list containing only the strings that have more than 3 characters. 
# This function does not validate its parameter. Write this function in a functional style.
# Example usage:
# func02(['cat', 'dog', 'elephant', 'bat'])  # Output: ['elephant']
# func02(['one', 'two', 'three', 'four'])    # Output: ['three', 'four']
# func02(['a', 'bc', 'def'])                 # Output: ['def']
def func02(ls: list[str]) -> list[str]:
    return list(filter(lambda x : len(x)>3,ls))
print(func02(['cat', 'dog', 'elephant', 'bat']))

# Problem 3:
# Write a function 'func03' that receives a list of integers and returns a new list containing only the positive integers. 
# This function does not validate its parameter. Write this function in a functional style.
# Example usage:
# func03([1, -2, 3, -4, 5])  # Output: [1, 3, 5]
# func03([0, -1, -2])        # Output: [0]
# func03([-5, -6, -7])       # Output: []
def func03(ls: list[int]) -> list[int]:
    return list(filter(lambda x : x>=0,ls))


# Problem 4:
# Write a function 'func04' that receives a list of integers and returns a new list containing the squares of all the integers in the list. 
# This function does not validate its parameter. Write this function in a functional style.
# Example usage:
# func04([1, 2, 3, 4])  # Output: [1, 4, 9, 16]
# func04([0, -1, -2])   # Output: [0, 1, 4]
# func04([5])           # Output: [25]
def func04(ls: list[int]) -> list[int]:
    return list(map(lambda x : x**2,ls))

print(func04([1, 2, 3, 4]))

# Problem 5:
# Write a function 'func05' that receives a list of integers and returns the product of all the integers in the list. 
# If the list is empty, return `1`. This function does not validate its parameter. Write this function in a functional style.
# Example usage:
# func05([1, 2, 3, 4])  # Output: 24
# func05([2, 3, 5])     # Output: 30
# func05([])            # Output: 1
def func05(ls: list[int]) -> int:
    pass

# Problem 6:
# Write a function 'func06' that receives a list of strings and returns the list sorted by the length of the strings. 
# If the strings have the same length, maintain their original order in the list. 
# This function does not validate its parameter. Write this function in a functional style.
# Example usage:
# func06(['one', 'two', 'three', 'four', 'five'])  # Output: ['one', 'two', 'three', 'four', 'five']
# func06(['a', 'abc', 'ab', 'abcd'])                 # Output: ['a', 'ab', 'abc', 'abcd']
def func06(ls: list[str]) -> list[str]:
    pass

# Problem 7:
# Write a function 'func07' that receives a list of strings and a boolean function (that receives a string and returns a bool). 
# This function applies the boolean function to each string in the list, counts the number of `True` results, and returns the count. 
# This function does not validate its parameter. Write this function in a functional style.
# Example usage:
# func07(['apple', 'banana', 'cherry', 'date'], lambda s: len(s) > 5)  # Output: 2
# func07(['cat', 'dog', 'elephant'], lambda s: s.startswith('e'))      # Output: 1
# func07(['a', 'b', 'c'], lambda s: s == 'a')                         # Output: 1
def func07(ls: list[str], f: Callable[[str], bool]) -> int:
    pass