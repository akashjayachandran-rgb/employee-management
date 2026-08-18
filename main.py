from employee import Employee, SalesEmployee   # from the parent class importing both p and subclass

employees = [] # creating an empty list to get input 

n = int(input("Enter the number of employees: "))  # input in integer form

for i in range(n): # for loop so it iterates until range n 

    print(f"Enter details of employee {i + 1}") # i=1 as it goes 1 2 3 until range n and dosent start with 0
# so if we give say any number 1,2,3,4,5 it itereates each time asking for employee details and type of employee until range n
    print("1. Normal Employee") 
    print("2. Sales Employee")

    employee_type = int(input("Select employee type: ")) # input statement here to get employee type

    name = input("Enter name: ")
    employee_id = int(input("Enter employee ID: "))
    department = input("Enter department: ")
    salary = int(input("Enter salary: "))

    if employee_type == 1: # standard if or else statements so that the additional function sales target is added.

        employee = Employee(
            name,
            employee_id,
            department,
            salary
        )

    elif employee_type == 2:

        sales_target = int(input("Enter sales target: "))

        employee = SalesEmployee(
            name,
            employee_id,
            department,
            salary,
            sales_target
        )

    else: # else statement so any other number other than 1 or 2 would not be accepted also added a print statement
        print("Invalid employee type")
        continue

    employees.append(employee) #appending to the empty list 


print("Employee Details:") #lastly displaying with for loop so one displays below the other 

for employee in employees:
   
    employee.display()

    
