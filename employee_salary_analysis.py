
# ==========================================
# Project: Employee Salary Analysis
# Purpose: Analyze employee salaries and departments
# ==========================================

# Store employee details using dictionaries
employees = [
    {"name": "Anu", "salary": 75000, "department": "HR"},
    {"name": "John", "salary": 55000, "department": "IT"},
    {"name": "Rahul", "salary": 65000, "department": "IT"},
    {"name": "David", "salary": 85000, "department": "IT"},
    {"name": "Priya", "salary": 45000, "department": "Finance"}
]

# Extract all salaries into a list
salaries = [employee["salary"] for employee in employees]

# Calculate salary statistics
number_of_employees = len(employees)
total_salary = sum(salaries)
average_salary = total_salary / number_of_employees
minimum_salary = min(salaries)
maximum_salary = max(salaries)

# Display Employee Salary Report
print("=" * 33)
print("       EMPLOYEE SALARY REPORT")
print("=" * 33)

print("\nNumber of Employees:", number_of_employees)
print("Total Salary:", total_salary)
print("Average Salary:", int(average_salary))
print("Minimum Salary:", minimum_salary)
print("Maximum Salary:", maximum_salary)

# Find employees earning 70000 or more
print("\nEmployees earning 70000 or more:\n")

for employee in employees:
    if employee["salary"] >= 70000:
        print(employee["name"], "-", employee["salary"])

print("\n" + "=" * 33)

# ==========================================
# ASSIGNMENT 1: Employees in IT Department
# ==========================================

print("\nEmployees in IT:\n")

for employee in employees:
    if employee["department"] == "IT":
        print(employee["name"])

print("\n" + "=" * 21)

# ==========================================
# ASSIGNMENT 2: Employees earning above average
# ==========================================

above_average_employees = []

for employee in employees:
    if employee["salary"] > average_salary:
        above_average_employees.append(employee)

print("\nEmployees earning more than average salary:")
print("Average Salary:", int(average_salary))
print("Number of Employees:", len(above_average_employees))

for employee in above_average_employees:
    print(employee["name"], "-", employee["salary"])
