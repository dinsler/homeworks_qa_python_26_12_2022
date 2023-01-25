# Task3.Write code that will determine the number of words in this text that end with "o"
# (both uppercase and lowercase are considered).


my_text = input("Enter your text: ")
count = 0
for i in my_text.split():
    if i.endswith('o') or i.endswith('O'):
        count += 1
print(f'Total count for words that ends with letters "o" or "O" is {count}')
