import random
my_list = []

for x in range(random.randint(3, 10)):
    my_list.append(random.randint(1,10))
print("Initial list:", my_list)

new_list = [my_list[0], my_list[2], my_list[len(my_list)-2]]
print("Final list:", new_list)