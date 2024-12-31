# A code to generate a multiplication table from 1-12
# using while Loop

a = 3
b = 1
while b <= 12:
    print(a,"*", b, "=", a * b)
    b= b + 1
print("Enter new value to calculate")
c=int(input("Enter your value: \n"))
b = 1
while b <= 12:
    print(c,"*", b, "=", c * b)
    b= b + 1

#End code
