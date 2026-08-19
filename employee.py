class Employee:  # Creating the Employee class

    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    # New method added
    def calculate_annual_salary(self):
        return self.salary * 12

    def display(self):
        print("Name :", self.name)
        print("Employee ID :", self.employee_id)
        print("Department :", self.department)
        print("Salary :", self.salary)

        # Displaying annual salary
        print("Annual Salary :", self.calculate_annual_salary())


class SalesEmployee(Employee):  # Inheriting from Employee

    def __init__(self, name, employee_id, department, salary, sales_target):
        super().__init__(name, employee_id, department, salary)
        self.sales_target = sales_target

    def display(self):
        super().display()
        print("Sales Target :", self.sales_target)









        