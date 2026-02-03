#WAP to calculate sum of odd/even number from 1 to 20.
a = int(input("Enter the first number: "))
b = int(input("Enter the last number: "))

e = 0
o = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        e = e + i
    else:
        o = o + i

print("Sum of even numbers:", e)
print("Sum of odd numbers:", o)


