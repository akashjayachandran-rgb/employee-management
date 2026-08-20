# Employee Management System

A Python project used to create, store, and display employee information.

## Project Features

- Add multiple employees
- Choose between a normal employee and a sales employee
- Calculate annual salary
- Store sales targets
- Display employee details
- Handle invalid employee-type selections

## Project Structure

```text
employee-management/
├── employee.py
├── main.py
├── .gitignore
└── README.md
```

## Files

### `employee.py`

Contains the `Employee` and `SalesEmployee` classes.

### `main.py`

Collects employee details from the user, creates employee objects, stores them in a list, and displays their information.

### `.gitignore`

Prevents Python cache files from being uploaded to GitHub.

```text
__pycache__/
```

## Employee Class

The `Employee` class stores:

- Employee name
- Employee ID
- Department
- Monthly salary

It also calculates the employee's annual salary.

```python
class Employee:

    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def calculate_annual_salary(self):
        return self.salary * 12

    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)
        print("Monthly Salary:", self.salary)
        print("Annual Salary:", self.calculate_annual_salary())
```

## SalesEmployee Class

The `SalesEmployee` class inherits from the `Employee` class.

It contains all employee properties and an additional `sales_target` property.

```python
class SalesEmployee(Employee):

    def __init__(
        self,
        name,
        employee_id,
        department,
        salary,
        sales_target
    ):
        super().__init__(
            name,
            employee_id,
            department,
            salary
        )

        self.sales_target = sales_target

    def display(self):
        super().display()
        print("Sales Target:", self.sales_target)
```

## Main Program

```python
from employee import Employee, SalesEmployee

employees = []

n = int(input("Enter the number of employees: "))

for i in range(n):

    print(f"\nEnter details of employee {i + 1}")

    print("1. Normal Employee")
    print("2. Sales Employee")

    employee_type = int(input("Select employee type: "))

    name = input("Enter name: ")
    employee_id = int(input("Enter employee ID: "))
    department = input("Enter department: ")
    salary = int(input("Enter monthly salary: "))

    if employee_type == 1:

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

    else:
        print("Invalid employee type")
        continue

    employees.append(employee)

print("\nEmployee Details:")

for employee in employees:
    print("--------------------")
    employee.display()
```

## How the Program Works

1. The user enters the number of employees.
2. A loop collects each employee's information.
3. The user selects normal employee or sales employee.
4. The appropriate employee object is created.
5. The object is added to the `employees` list.
6. Another loop displays all employee details.

## How to Run the Project

### Clone the repository

```bash
git clone https://github.com/akashjayachandran-rgb/employee-management.git
```

### Open the project directory

```bash
cd employee-management
```

### Run the program

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

## Python Concepts Used

- Classes and objects
- Constructors
- Methods
- Inheritance
- Method overriding
- `super()`
- Lists
- Loops
- Conditional statements
- User input

## Git Commands Used

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/akashjayachandran-rgb/employee-management.git
git push -u origin main
```

A separate branch was created using:

```bash
git switch -c employee-update
```

## Branches

- `main` – stable version of the project
- `employee-update` – employee-related updates

## Technologies Used

- Python
- Git
- GitHub
- Visual Studio Code

## Repository

[View the Employee Management repository](https://github.com/akashjayachandran-rgb/employee-management)

## Author

**Akash Jayachandran**