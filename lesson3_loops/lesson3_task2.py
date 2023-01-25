# Task2. Write code that creates a new list that contains only the string variables that are present in lst1.
# Note that lst1 is not static and can be dynamically generated from run to run.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for i in lst1:
    if type(i) != str:
        continue
    lst2.append(i)
print(lst2)
