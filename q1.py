''' Write a program to create function calculation () such that it can accept two variables
 and calculate addition and subtraction. Also, it must return both addition and
 subtraction in a single return call.'''

def cal():
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    
    Add=a+b
    sub=a-b

    return Add,sub

result=cal()
print("(Addition),(Subtraction) is: ",result)
