def amount(chi):
    if chi == "Tire rotation":
        return 19
    if chi == "Car wax":
        return 12
    if chi == "Oil change":
        return 35
    if chi == "Car wash":
        return 7


# the list / menu
print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")
number_one = input("Select first service:\n")  # user provides 1st service from user
number_two = input("Select second service:\n")  # user provides 2nd service from user

print("\nDavy's auto shop invoice\n")
first = amount(number_one)
second = 0
print("Service 1: %s, $%d" % (number_one, first))  # the prices along with the service

if number_two == '-':  # if only one service administered, print the no Service
    print("Service 2: No service")
else:
    second = amount(number_two)
    print("Service 2: %s, $%d" % (number_two, second))

print("\nTotal: $%d" % (first + second))
