'''Write a program to create a function employee () using the following conditions.
 a. It should accept the employees name and salary and display both.
 b. If the salary is missing in the function call, then assign default value 10000 to
 salary'''

emp_name = input("Enter employee name:")
emp_salary = input("Enter employee salary:")

def employee(emp_name,emp_salary):
    print("Employee name:",emp_name)
    
    if emp_salary:
     print("Employee salary:",emp_salary)
    else:
        emp_salary = 10000
        print("Employee salary:",emp_salary)

    
employee(emp_name,emp_salary)

