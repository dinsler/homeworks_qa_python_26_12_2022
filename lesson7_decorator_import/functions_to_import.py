import time
from typing import Union


def time_function_decorator(func):
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"Execution of {func.__name__} function took {runtime} secs")
        return res
    return _wrapper


@time_function_decorator
def cashier_job():
    while True:
        user_message = input("Введіть свій вік: ")

        user_age = check_input(user_message)
        if not user_age:
            continue

        ending = find_ending(user_age)
        message = get_message(user_age, ending)

        print(message)

        if_continue = input("Чи хочете ви знову ввести свій вік? Введіть 'так' якщо хочете продовжити : ")
        if if_continue != "так":
            print("Заходьте ще!")
            break



def check_input(user_message: str) -> Union[int, None]:
    """
     check if user_message has only digits
    :return: user_message as integer.
    """

    try:
        res = int(user_message)
        if res not in range(1, 100):
            print("Please enter valid age!")
            return None
        return res
    except ValueError:
        print("enter number, please")


def find_ending(user_age: int) -> str:
    """
    depending on age we will return appropriate ending
    :return: ending as string.
    """
    res = "років"

    if user_age % 10 == 1 and user_age != 11:
        res = "рік"
    elif 1 < user_age % 10 < 5 and user_age not in [12, 13, 14]:
        res = "роки"

    return res


def get_message(user_age: int, ending: str) -> str:
    """
    depending on user age provide appropriate cashier message
    :return: message as a string.
    """
    user_age_as_string = str(user_age)
    symbol = user_age_as_string[0]
    count = user_age_as_string.count(symbol)

    res = f"Незважаючи на те, що вам {user_age} {ending}, білетів всеодно нема!"

    if count > 1:
        res = f"О, вам {user_age} {ending}! Який цікавий вік!"
    elif user_age < 7:
        res = f"Тобі ж {user_age} {ending}! Де твої батьки?"
    elif user_age < 16:
        res = f"Тобі лише {user_age} {ending}, а це е фільм для дорослих!"
    elif user_age > 65:
        res = f"Вам {user_age} {ending}? Покажіть пенсійне посвідчення?"

    return res


# cashier_job()


# cashier_job = time_function_decorator(cashier_job())
