''' Create an outer function that will accept two parameters a and b. Create an inner
 function inside an outer function that will calculate the addition of a and b. At last, an
 outer function will add 5 into addition and return it.'''
def outer(a,b):
    def inner(a,b):
        return a+b
    
    addition = inner(a,b)
    result = addition + 5
    return result

a = int(input("Enter a:"))
b = int(input("Enter b:"))

print("The result is:",outer(a,b))