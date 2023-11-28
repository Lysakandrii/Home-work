input_number = input("please enter your number:")
int_number = int(input_number)
first_digit = int(input_number[0])
while int_number > 9:
    for l in input_number[1:]:
        l = int(l)
        first_digit = first_digit * l
    input_number = str(first_digit)
    first_digit = int(input_number[0])
    int_number = int(input_number)
print(input_number)
