from db_connection import get_connection
from auth import verify_admin
# Add Emplyoeee
def add_employee():
    if not verify_admin():
        return
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter employee name: ")
    phone= input("Enter phone number: ")
    role = input("Enter Employee role: ")
    salary = input("Enter salary: ")
    joining_date = input("Enter joining date (YYYY-MM-DD): ")
    address = input("Enter address: ")

    cursor.execute("""
        INSERT INTO employees (name, phone, role, salary, joining_date, address) 
        VALUES (%s, %s, %s,%s, %s, %s)
    """, (name,phone, role, salary, joining_date, address))

    conn.commit()
    conn.close()
    print("Employee added successfully!")
# View Employees
def view_employees():
    if not verify_admin():
        return
    conn = get_connection()
    cursor = conn.cursor()
    query ="select * from employees"  
    cursor.execute(query) 
    data=cursor.fetchall()
    print("\n===== Employee Details =====")
    print(f"Total Employees: {len(data)}")  
    for row in data:
        print(f"""
Employee ID   : {row[0]}
Employee Name : {row[1]}
Phone Number  : {row[2]}
Role          : {row[3]}
Salary        : ₹{row[4]}
Joining Date  : {row[5]}
Address       : {row[6]}
----------------------------------------
""")
    conn.close()

# Search Employee
def search_employee():
    if not verify_admin():
        return
    emp_id = input("Enter Employee ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM employees WHERE employee_id = %s"

    cursor.execute(query, (emp_id,))

    row = cursor.fetchone()

    if row:
        print(f"""
Employee ID : {row[0]}
Name        : {row[1]}
Phone       : {row[2]}
Role        : {row[3]}
Salary      : ₹{row[4]}
Joining Date: {row[5]}
Address     : {row[6]}
""")
    else:
        print("Employee not found!")

    conn.close()  

# Delete Employee
def delete_employee():
    if not verify_admin():
        return
    conn = get_connection()
    cursor = conn.cursor()
    emp_id = input("Enter Employee ID to delete: ")
    query = "DELETE FROM employees WHERE employee_id=%s"
    cursor.execute(query, (emp_id,))
    conn.commit()
    if cursor.rowcount:
        print("Employee deleted successfully!")
    else:
        print("Employee not found!")
    conn.close()