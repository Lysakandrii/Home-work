my_list = [4,2,6,7,3,6,1]

if len(my_list) == 0:
    new_list = [my_list] * 2
    print(new_list)
if len(my_list)> 1 and len(my_list) % 2 == 0:
    x = int(len(my_list) / 2)
    new_list = [my_list[:x], my_list[x:]]
    print(new_list)
if len(my_list)> 1 and len(my_list) % 2 == 1:
    x = int(len(my_list) // 2)
    new_list = [my_list[:-x], my_list[-x:]]
    print(new_list)
if len(my_list) == 1:
    new_list = [my_list,[]]
    print(new_list)