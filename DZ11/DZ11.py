next_calculation = True
while next_calculation is True:
    x = int(input("Please enter first number:"))
    y = int(input("Please enter second number:"))
    action = (input("Please enter action(+, -, *, /) :"))
    if action == "+":
        print("Your result is", x + y)
    elif action == "-":
        print("Your result is", x - y)
    elif action == "*":
        print("Your result is", x * y)
    elif action == "/" and y > 0:
        print("Your result is", x / y)
    else:
        print("You can't divide by 0")

    repeat = input('Do you want to perform another calculation(Yes/No):')
    if "n" in repeat.lower():
        next_calculation = False
        print("Have a nice day!")