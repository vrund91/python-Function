''' Write a Python function that accepts a string and counts the number of upper and lower case letters'''

def uper_lower(string1):
    upper_count=0
    lower_count=0

    for char in string1:
        if char.isupper():
            upper_count+=1
        elif char.islower():
            lower_count+=1
        else:
            print("valid value")

    return print("uppercase count:",(upper_count)),print("lowercase count:",(lower_count))

string1=input("Enter a string:")
uper_lower(string1)