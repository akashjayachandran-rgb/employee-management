class Employee: #creating a class
    def __init__(self, name, employee_id, department, salary): # def__init__ intialising and self to work within this function
        self.name = name  # assigning it so acts like a variable to store data
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display(self): # assigining the display function
        print("Name :", self.name) #print statemtn after getting the details
        print("Employee ID :", self.employee_id)
        print("Department :", self.department)
        print("Salary :", self.salary)


class SalesEmployee(Employee):  # inheriting employee and creating a subclass
    def __init__(self, name, employee_id, department, salary, sales_target): # same process
        super().__init__(name, employee_id, department, salary) # super is used to like call or go to the parent class for the deets
        self.sales_target = sales_target # adding a new variable for just the sales employee

    def display(self):
        super().display() # again using the super command to copy the functions of def display self from the parent class
        print("Sales Target :", self.sales_target) 









        