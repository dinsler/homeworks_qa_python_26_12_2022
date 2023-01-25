""" Task1.Form a string that contains information about a certain word.
"Word [here is a word] has [here is the length of the word] letters", for example "Word 'Python' has 6 letters".
Use a constant or the input() function to get the word to parse.
"""

# constant solution
NAME_WORD = "Odessa"

res = f"Word '{NAME_WORD}' has {len(NAME_WORD)} letters."
print(res)


# input() function solution
input_word = input("enter the word: ")
input_res = f"Word '{input_word}' has {len(input_word)} letters."
print(input_res)
