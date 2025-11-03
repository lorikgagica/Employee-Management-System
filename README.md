# 👔 Employee Management System (Python)

A simple Python console app to manage employees, managers, and developers. All data is saved to a JSON file (`employees.json`) and you can quickly look up any employee by their ID.

---

## ✨ Features

- **Add employees, managers, or developers** with custom details
- **All data saved and loaded automatically** from `employees.json`
- **List all employees** in your organization with bonus calculations
- **Find employee by ID** — type in an ID and see their details instantly
- **Clear, menu-driven interface**

---

## 🚀 How to Run

1. Make sure Python is installed (3.7+ recommended).
2. Save the script as `employee.py` in your chosen folder.
3. Open a terminal/command prompt in that folder.
4. Run: `python employee.py`
5. Follow the menu prompts:
   - Add employees/managers/developers
   - Search by ID at any time
   - Exit to save

---

## 💡 Example Session

--- Employee Management System ---

Add Employee

Display All Employees

Find Employee by ID

Exit
Enter your choice(1-4): 1

--- Choose Employee Type ---

Regular Employee

Manager

Developer
Enter your choice: 2
Enter Employee Name: Alice
Enter Employee ID: 101
Enter Employee Salary: 1000
Enter Department: HR
Employee added and data saved!

--- Employee Management System ---
3
Enter Employee ID to find: 101

--- Employee Details ---
Name: Alice
Employee ID: 101
Salary: 1000.0
Department: HR
Bonus: 200.0

---

## 🗂 Data Storage

- All records are stored in a file called `employees.json` in the same folder.
- Each time you add, edit, or exit, your data is updated and preserved.

---

## 📄 License

MIT License — free to use, modify, and share.

---

Quickly manage your team and keep all your records safe!
