def common_elements():
    x = list(range(3,100,3))
    y = list(range(5,100,5))
    intersection = set(x).intersection(set(y))
    return intersection

print(common_elements())
print(list(range(3,100,3)))
print(list(range(5,100,5)))
