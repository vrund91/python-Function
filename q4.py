'''Write a program to create a recursive function to calculate the sum of numbers from
 0 to 10'''
def sum_func(n):
    if n==0:
        return 0
    else:
        return n + sum_func(n-1)
    
n = int(input("Enter a number:"))

print(sum_func(n))
