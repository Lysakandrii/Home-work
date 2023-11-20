my_list = [1,3,5]
result = 0

for x, y in enumerate(my_list):
    if x % 2 == 0:
        result = result + y * my_list[len(my_list)-1]

print(result)
