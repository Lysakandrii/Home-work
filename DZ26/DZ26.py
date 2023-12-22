def is_even(number):
    number = str(number)
    last_digit = number[-1]
    result = None
    even_numbers = str(list(range(0, 9, 2)))
    if last_digit in even_numbers:
        return True
    else:
        return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("ok")