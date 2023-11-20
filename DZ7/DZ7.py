my_list = [0,3,6,2,0,4,9,0,0,0,5]
list1 = []
list2 = []

for L in my_list:
    if L == 0:
        list2 = list2 + [L]
    else:
        list1 = list1 + [L]
print(list1 + list2)

