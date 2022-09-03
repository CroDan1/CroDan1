number = int(input("Enter the name : "))

factorial = 1

if (number < 0):
    print("Cant computer factorial for negative numbers")
elif (number < 2):
    print("{}! = {}". format(number, factorial))
else:
    for num in range(number, 1, -1):
        factorial = factorial * num

    print("{}! = {}".format(number, factorial))