import string
combination = input("Please enter 2 letters (eg. d-H):")
first_index = string.ascii_letters.find(combination[0])
second_index = string.ascii_letters.find(combination[2])+1
print(string.ascii_letters[first_index:second_index])

