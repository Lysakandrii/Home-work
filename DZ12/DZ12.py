import string
initial_str = str(input('Enter your phrase to transform:'))
to_delete = string.punctuation+" "
initial_str = initial_str.title()
for l in initial_str:
    if l in to_delete:
        initial_str = initial_str.replace(l,"")

print("#" + initial_str[:139])