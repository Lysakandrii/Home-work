def say_hi(name, age):
    arguments = "Hi. My name is " + name + " and I'm " + str(age) + " years old"
    return arguments

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
print('ОК')


print(say_hi("Jony",99))