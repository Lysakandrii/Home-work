def prime_generator(end):
    for possible_prime in range(2,end + 1):
        is_prime = True
        for num in range(2, possible_prime):
            if possible_prime % num == 0:
                is_prime = False
        if is_prime:
            yield possible_prime

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')