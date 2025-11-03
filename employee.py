import json
import os

# Employee Management System
EMPLOYEE_FILE = "employees.json"

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print("\n--- Employee Details ---")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.1

    def to_dict(self):
        return {
            "type": "Employee",
            "name": self.name,
            "emp_id": self.emp_id,
            "salary": self.salary
        }

    @staticmethod
    def from_dict(data):
        return Employee(data["name"], data["emp_id"], data["salary"])


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

    def calculate_bonus(self):
        return self.salary * 0.2

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Manager"
        data["department"] = self.department
        return data

    @staticmethod
    def from_dict(data):
        return Manager(data["name"], data["emp_id"], data["salary"], data["department"])


class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary * 0.5

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Developer"
        data["programming_language"] = self.programming_language
        return data

    @staticmethod
    def from_dict(data):
        return Developer(data["name"], data["emp_id"], data["salary"], data["programming_language"])


# --- JSON Load/Save Helpers ---
def load_employees():
    if os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        loaded = []
        for d in data:
            if d["type"] == "Employee":
                loaded.append(Employee.from_dict(d))
            elif d["type"] == "Manager":
                loaded.append(Manager.from_dict(d))
            elif d["type"] == "Developer":
                loaded.append(Developer.from_dict(d))
        return loaded
    return []

def save_employees(employees):
    with open(EMPLOYEE_FILE, "w", encoding="utf-8") as f:
        json.dump([e.to_dict() for e in employees], f, indent=2)

# --- Main Data ---
employees = load_employees()

# --- Employee Actions ---
def add_employee():
    print("\n--- Choose Employee Type ---")
    print("1. Regular Employee")
    print("2. Manager")
    print("3. Developer")
    choice = int(input("Enter your choice: ").strip())
    name = input("Enter Employee Name: ").strip()
    emp_id = input("Enter Employee ID: ").strip()
    salary = float(input("Enter Employee Salary: ").strip())
    if choice == 1:
        employees.append(Employee(name, emp_id, salary))
    elif choice == 2:
        department = input("Enter Department: ").strip()
        employees.append(Manager(name, emp_id, salary, department))
    elif choice == 3:
        programming_language = input("Enter Programming Language: ").strip()
        employees.append(Developer(name, emp_id, salary, programming_language))
    else:
        print("Invalid choice")
        return
    save_employees(employees)
    print("Employee added and data saved!")

def display_all_employees():
    print("\n--- All Employees ---")
    for employee in employees:
        employee.display_info()
        print(f"Bonus: {employee.calculate_bonus()}")

def find_employee_by_id():
    emp_id = input("Enter Employee ID to find: ").strip()
    found = False
    for employee in employees:
        if employee.emp_id == emp_id:
            employee.display_info()
            print(f"Bonus: {employee.calculate_bonus()}")
            found = True
    if not found:
        print("No employee found with that ID.")

# --- Main Menu ---
while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Find Employee by ID")
    print("4. Exit")
    choice = int(input("Enter your choice(1-4): ").strip())
    if choice == 1:
        add_employee()
    elif choice == 2:
        display_all_employees()
    elif choice == 3:
        find_employee_by_id()
    elif choice == 4:
        save_employees(employees)
        print("Exiting the program and saving data.")
        break
    else:
        print("Invalid choice")