#calculating factorial
num = int(input("Enter the number whose factorial you want to find = "))
fact = 1
while (num!=0):
    fact = fact * num
    num-=1
print("Factorial of the given number is = ", fact)
