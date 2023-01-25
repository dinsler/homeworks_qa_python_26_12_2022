# Task3. Write a loop that will require the user to enter a word that contains the letter "o".
# The loop should not terminate if the user entered a word without the letter "o".
while True:
    my_word = input("Please enter the word!: ")
    if "O" in my_word or "o" in my_word:
        print(f"Thank u,{my_word} has correct letter!")
        break
    else:
        print("Please enter another word!")