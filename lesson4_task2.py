# Write code that will find and display the names of stores whose prices are in the range between
# the minimum and maximum price.
my_dict = {
     "cito": 47.999,
     "BB_studio": 42.999,
     "momo": 49.999,
     "main-service": 37.245,
     "buy.now": 38.324,
     "x-store": 37.166,
     "the_partner": 38.988,
     "store": 37.720,
     "rozetka": 38.003
}
lower_limit = 35.9
upper_limit = 37.339
for key, value in my_dict.items():
    if upper_limit > value > lower_limit:
        print(f"Store '{key}' is in the range between the min and max price")
