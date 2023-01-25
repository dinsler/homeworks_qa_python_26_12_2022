"""Task2. Write a movie theater cashier program that asks the user to enter their age
(you can use a constant or the input() function, only one message should be displayed on the screen,
also consider the options when the input is incorrect)."""

# constant solution
AGE = 17

if AGE < 7:
    print("Where are your parents?")
elif AGE < 16:
    print("This movie is for adults!")
elif AGE > 65:
    print("Show your pension certificate!")
elif "7" in str(AGE):
    print("You are lucky today!")
else:
    print("All tickets are sold!")

# input() function solution
input_age = input("set your age: ")
if input_age.isdigit():
    input_age = int(input_age)
    if input_age < 7:
        print("Where are your parents?")
    elif input_age < 16:
        print("This movie is for adults!")
    elif input_age > 65:
        print("Show your pension certificate!")
    elif "7" in str(input_age):
        print("You are lucky today!")
    else:
        print("All tickets are sold!")
else:
    print("enter number, please")
