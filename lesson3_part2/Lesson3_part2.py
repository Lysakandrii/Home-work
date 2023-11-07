x = int(input("Please enter a four-digit integer number: "))

div, mod = divmod(x,1000)
print(div)
print(mod // 100)
y = (mod // 10)
print(y % 10)
print(x % 10)