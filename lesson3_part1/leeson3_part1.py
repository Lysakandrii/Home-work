x = int(input("Please enter a five-digit integer number: "))

div, mod = divmod(x,10000)
A = div
B = mod // 1000
C = mod // 100 % 10
D = mod // 10 % 10
E = x % 10
print(E,D,C,B,A)