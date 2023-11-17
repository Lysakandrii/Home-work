my_list = [1,2,3,7]

if len(my_list) == 0 or len(my_list) == 1:
    print(my_list)
else :
    x = [my_list.pop()]
    new_list = x + my_list
    print(new_list)