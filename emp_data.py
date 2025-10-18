import mysql.connector as mysql
import pandas as pd

# Establish a database connection
dbhostname = "MainServer" 
databaseusername = "root"
dbpassword = "...ppptkinter"
dbname = "new_littlewood"
conn = mysql.connect(
    host=dbhostname,
    user=databaseusername,
    password=dbpassword,
    database=dbname
)
pointer = conn.cursor(buffered=True)

# Define your SQL query
query = """
    SELECT employee.emp_id, employee.name, employee.father, employee.cnic, employee.date, employee.dep_id, employee.designation, employee.salary, employee.type, department.name
    FROM employee
    LEFT JOIN department ON employee.dep_id = department.dep_id
    ORDER BY employee.id ASC;
"""

# Execute the query and fetch the data into a DataFrame
pointer.execute(query)
data = pointer.fetchall()
df = pd.DataFrame(data, columns=["emp_id", "name", "father", "cnic", "date", "dep_id", "designation", "salary", "type", "department_name"])

# Export the DataFrame to an Excel file
excel_file_path = "employee_data.xlsx"  # Replace with your desired file path
df.to_excel(excel_file_path, index=False)

# Close the database connection
conn.close()

print("Data exported to Excel:", excel_file_path)
