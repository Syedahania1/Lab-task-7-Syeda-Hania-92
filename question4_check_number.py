numbers = {10, 20, 30, 40, 50}
number = int(input("Enter a number: "))

if number in numbers:
    print(number, "exists in the set.")
else:
    print(number, "does not exist in the set.")
