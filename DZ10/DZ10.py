import keyword
import string

initial_string = ('get!value')
first_symbol = initial_string[0]
my_punctuationlist = string.punctuation.replace("_"," ")

first_check = initial_string.isdigit() is False and first_symbol.isdigit() is False and initial_string.count("_") <= 1 and initial_string in initial_string.lower() and initial_string not in keyword.kwlist

second_check = 0
for l in my_punctuationlist:
    if l in initial_string:
       second_check = l

if first_check == True and second_check == 0:
    print("True")
else:
    print("False")

