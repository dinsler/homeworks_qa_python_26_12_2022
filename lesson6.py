# Task2. Write a movie theater cashier program that asks the user to enter their age.
# Do it all with a function

def cashier_job():
    while True:
        user_message = input("Введіть свій вік: ")

        user_age = check_input(user_message)
        if not user_age:
            continue

        ending = find_ending(user_age)
        message = get_message(user_age, ending)

        print(message)

        if_continue = input("Чи хочете ви знову ввести свій вік?: ")
        if if_continue == "так":
            continue
        else:
            break


def check_input(user_message):
    """
     check if user_message has only digits
    :return: user_message as integer
    """

    try:
        res = int(user_message)
        return res
    except ValueError:
        print("enter number, please")


def find_ending(user_age):
    """
    depending on age we will return appropriate ending
    :return: ending as string
    """
    if (user_age % 10 == 1) and (user_age != 11) and (user_age != 111):
        return "рік"
    elif (user_age % 10 > 1) and (user_age % 10 < 5) and (user_age != 12) and (user_age != 13) and (user_age != 14):
        return "роки"
    else:
        return "років"


def get_message(user_age, ending):
    """
    depending on user age provide appropriate cashier message
    :return: message as a string
    """
    user_age_as_string = str(user_age)
    symbol = user_age_as_string[0]
    count = user_age_as_string.count(symbol)
    if count > 1:
        return f"О, вам {user_age} {ending}! Який цікавий вік!"

    if user_age < 7:
        return f"Тобі ж {user_age} {ending}! Де твої батьки?"
    elif user_age < 16:
        return f"Тобі лише {user_age} {ending}, а це е фільм для дорослих!"
    elif user_age > 65:
        return f"Вам {user_age} {ending}? Покажіть пенсійне посвідчення?"
    else:
        return f"Незважаючи на те, що вам {user_age} {ending}, білетів всеодно нема!"


print(cashier_job())