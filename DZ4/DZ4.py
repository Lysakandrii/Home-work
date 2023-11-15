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
