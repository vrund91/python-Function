''' Write a Python function to calculate the factorial of a number (a non-negative integer). The function
 accepts the number as an argument'''
def fac(num):
    if num < 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num * fac(num-1)
    
num=int(input("Enter a number:"))
print("The factorial number is:",fac(num))