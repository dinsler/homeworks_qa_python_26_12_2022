# Task1. Write a function that as a result will return a list in which all strings will be in upper case.
# Use the map() function for this.


def get_uppercase_names(input_list: list) -> list:
    return list(map(str.upper, input_list))


lowercase_names = ['alfred', 'ben', 'william']
print(get_uppercase_names(lowercase_names))


# Task2.Write a function that will accept a list of floats as input, and as a result return a list in which all numbers
#  will be raised to the power of 2 and rounded to three decimal places
# Use the map() function for this.


def exponent_round_float_nums(fin_list: list) -> list:
    return list(map(lambda x: round(x ** 2, 3), fin_list))


float_nums = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
print(exponent_round_float_nums(fin_list=float_nums))


# Task3.Write a function that will accept two lists as input, and as a result return a list in which
# elements are combined in pairs in tuples. Use the zip() function for this.


def combine_letters_nums_list(lst1, lst2: list) -> list:
    return list(zip(lst1, lst2))


letters_list = ['a', 'b', 'c', 'd', 'e']
nums_list = [1, 2, 3, 4, 5]
print(combine_letters_nums_list(lst1=letters_list, lst2=nums_list))


# Task4. Write a function that will accept a list of strings and a number as input, and as a result return a list
# containing those strings whose length will be less than the number 5. Use the filter() function for this


def names_with_less_than_5_letters(new_list: list, row_len: int) -> list:
    return list(filter(lambda x: len(x) < row_len, new_list))


names_list = ["Jeff", "Alex", "Jonathan", "Richelle", "Anna"]
print(names_with_less_than_5_letters(new_list=names_list, row_len=5))
