import mysql.connector as mysql
import re

class database_class:
    #   init
    def __init__(self):
        self.dbhostname = "MainServer" 
        self.databaseusername = "root"
        self.dbpassword = "...ppptkinter"
        self.dbname = "littlewood"
        self.conn = mysql.connect(
                host = self.dbhostname,
                username = self.databaseusername,
                password = self.dbpassword,
                database = self.dbname
                )
        self.pointer = self.conn.cursor(buffered=True)

    #   DataBase Connection
    def database_connection_check(self):
        try:
            self.conn = mysql.connect(
                host = self.dbhostname,
                username = self.databaseusername,
                password = self.dbpassword,
                database = self.dbname
                )
            self.pointer = self.conn.cursor(buffered=True)
            return True
        except:
            return False
        
    #   USer Check
    def user_checking(self, user, password):
        a = database_class().database_connection_check()
        if a == True:
            u = user
            p = password
            query = "SELECT * FROM users WHERE user=%s AND password=%s AND activation=%s"
            self.pointer.execute(query, [u, p, True])
            details = self.pointer.fetchall()
            if details == []:
                return "NO MATCH"
            else:
                return details
        else:
            return False

    #   Stores
    def all_stores(self):
        a = database_class().database_connection_check()
        if a == True:
            query = "SELECT * FROM users WHERE type=%s AND activation=%s OR type=%s AND activation=%s ORDER BY id ASC;"
            self.pointer.execute(query, ["Main Store", True, "Sub-Store", True])
            details = self.pointer.fetchall()
            return details
        else:
            return False
    
    #   All Stores
    def all_stores_ad(self):
        a = database_class().database_connection_check()
        if a == True:
            query = "SELECT * FROM users WHERE type=%s OR type=%s ORDER BY id ASC;"
            self.pointer.execute(query, ["Main Store", "Sub-Store"])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    # User Detals
    def user_details_database(self, user):
        a = database_class().database_connection_check()
        if a == True:
            userid = ""
            for i in user:
                if i == "-":
                    break
                else:
                    userid = userid + i
            query = "SELECT * FROM users WHERE id=%s"
            self.pointer.execute(query, [userid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Save new User
    def save_new_user(self, username, pasword, storetype, storestatus):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = "SELECT user FROM users WHERE user=%s"
            self.pointer.execute(query, [username])
            details = self.pointer.fetchall()
            if details != []:
                return "Exists"
            else:
                statussetting = None
                if storestatus == "Activate":
                    statussetting = True
                elif storestatus == "Deactivate":
                    statussetting = False

                #   Query1
                query1 = "INSERT INTO users(user, password, activation, type) VALUES(%s,%s,%s,%s)"
                self.pointer.execute(query1, [username, pasword, statussetting, storetype])
                self.conn.commit()
                return "Save"
        else:
            return False

    #   Update user
    def update_user_database(self, username, pasword, storetype, storestatus, userid):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = "SELECT user FROM users WHERE user=%s AND id!=%s"
            self.pointer.execute(query, [username, userid])
            details = self.pointer.fetchall()
            if details != []:
                return "Exists"
            else:
                statussetting = None
                if storestatus == "Activate":
                    statussetting = True
                elif storestatus == "Deactivate":
                    statussetting = False

                #   Query1
                query1 = "UPDATE users SET user=%s, password=%s, activation=%s, type=%s WHERE id=%s"
                self.pointer.execute(query1, [username, pasword, statussetting, storetype, userid])
                self.conn.commit()
                return "Save"

#   Department
class department_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   Departments Data
    def new_department(self):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            newdepid = ""
            dep_key = "DEP-"
            query3 = "SELECT * FROM department"
            self.pointer.execute(query3)
            all_dep_ids = self.pointer.fetchall()
            if all_dep_ids == []:
                newdepid = dep_key+"1"
                return newdepid
            else:
                for i in all_dep_ids:
                    new = i[0] + 1
                    convert_string = str(new)
                    newdepid = dep_key+convert_string
                return newdepid
        else:
            return False
        
    #   Existing Deps
    def existing_departments(self):
        a = database_class().database_connection_check()
        if a == True:
            query = "SELECT dep_id, name FROM department"
            self.pointer.execute(query)
            dep_details = self.pointer.fetchall()
            return dep_details
        else:
            return False
        
    #   Save New Department
    def save_new_department(self, depname):
        a = database_class().database_connection_check()
        if a == True:
            if depname:
                newempid = department_database().new_department()
                depid = newempid

                query = "INSERT INTO department(dep_id, name) VALUES(%s, %s)"
                self.pointer.execute(query, [depid, depname])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False

    #   Save Editing
    def save_editing_department_database(self, depid, depname):
        a = database_class().database_connection_check()
        if a == True:
            if depid and depname:
                extractdepid = ""
                for i in depid:
                    if i == " ":
                        break
                    else:
                        extractdepid = extractdepid + i
                query = "UPDATE department SET name=%s WHERE dep_id=%s"
                self.pointer.execute(query, [depname, extractdepid])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False

    #   Department Details
    def department_default_details(self):
        a = database_class().database_connection_check()
        if a == True:    
            query = """SELECT department.*, 
                        COUNT(employee.dep_id) AS num_employees,
                        COUNT(CASE WHEN employee.type = 'Contractor' THEN 1 END) AS num_contractors,
                        COUNT(CASE WHEN employee.type = 'Salary' THEN 1 END) AS num_salary,
                        COUNT(CASE WHEN employee.type = 'Maker' THEN 1 END) AS num_makers
                    FROM department
                    LEFT JOIN employee ON department.dep_id = employee.dep_id
                    GROUP BY department.dep_id
                    ORDER BY department.id ASC;
                    ;
                    """
            self.pointer.execute(query)
            dep_details = self.pointer.fetchall()
            return dep_details
        else:
            return False

    #   Search Dep Details
    def search_dep_details_database(self, depid):
        a = database_class().database_connection_check()
        if a == True:
            extractdepid = ""
            for i in depid:
                if i == " ":
                    break
                else:
                    extractdepid = extractdepid + i
            query = """SELECT id, emp_id, name, father, cell, designation, type, salary
                    FROM employee
                    WHERE dep_id = %s
                    ORDER BY id ASC;
                    """
            self.pointer.execute(query, [extractdepid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   All Designations
    def all_designations(self):
        a = database_class().database_connection_check()
        if a == True:    
            query = """SELECT name FROM designation
                        ORDER by id ASC;"""
            self.pointer.execute(query)
            dep_details = self.pointer.fetchall()
            return dep_details
        else:
            return False

    #   Employee balance
    def employe_balnce_database(self, empid):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT
                        COALESCE(
                            SUM(CASE WHEN el.type = 'Short Term' AND el.category = 'Debit' THEN el.amount ELSE 0 END) -
                            SUM(CASE WHEN el.type = 'Short Term' AND el.category = 'Credit' THEN el.amount ELSE 0 END),
                            0
                        ) AS Short_Term_Balance,
                        COALESCE(
                            SUM(CASE WHEN el.type = 'Long Term' AND el.category = 'Debit' THEN el.amount ELSE 0 END) -
                            SUM(CASE WHEN el.type = 'Long Term' AND el.category = 'Credit' THEN el.amount ELSE 0 END),
                            0
                        ) AS Long_Term_Balance
                    FROM
                        employee_ledger AS el
                    WHERE
                        el.emp_id = %s;

                    """
            self.pointer.execute(query, [empid])
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
#   Employee
class employee_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   New Employee
    def new_employee(self):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            newdepid = ""
            dep_key = "EMP-"
            query3 = "SELECT * FROM employee"
            self.pointer.execute(query3)
            all_dep_ids = self.pointer.fetchall()
            if all_dep_ids == []:
                newdepid = dep_key+"1"
                return newdepid
            else:
                for i in all_dep_ids:
                    new = i[0] + 1
                    convert_string = str(new)
                    newdepid = dep_key+convert_string
                return newdepid
            
        else:
            return False

    #   Exisiting Employee List
    def existing_employee(self):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query3 = """SELECT employee.*, department.name AS dep_name
                        FROM employee
                        JOIN department ON employee.dep_id = department.dep_id;
                        """
            self.pointer.execute(query3)
            all_dep_ids = self.pointer.fetchall()
            return all_dep_ids
        else:
            return False
        
    #   Search by id
    def search_by_id(self, empid):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query3 = """SELECT employee.*, department.name AS dep_name
                        FROM employee
                        JOIN department ON employee.dep_id = department.dep_id
                        WHERE employee.id=%s OR employee.emp_id=%s OR employee.cnic=%s OR employee.cell=%s;
                        """
            self.pointer.execute(query3, [empid, empid, empid, empid])
            all_dep_ids = self.pointer.fetchall()
            if all_dep_ids == []:
                return "Empty"
            else:
                return all_dep_ids
        else:
            return False

    #   Save Employee
    def save_employee(self, empid, name, father, cell, cnic, address, salary, depid, designation, emptype, newdate, emppic):
        a = database_class().database_connection_check()
        if a == True:
            if empid and name and father and cell and cnic and address and salary and depid and designation and emptype:
                query = """SELECT * FROM employee WHERE cnic=%s OR cell=%s"""
                self.pointer.execute(query, [cnic, cell])
                existing = self.pointer.fetchall()
                if existing == []:
                    if emptype == "SALARY" and int(salary) == 0:
                        return "No Salary"
                    elif emptype == "CONTRACTOR" and int(salary) == 0 or emptype == "MAKER" and int(salary) == 0:
                        return "With Salary"
                    elif emptype == "SALARY" and int(salary) > 0  or emptype == "CONTRACTOR" and int(salary) != 0 or emptype == "MAKER" and int(salary) != 0:
                        extractdepid = ""
                        for i in depid:
                            if i == " ":
                                break
                            else:
                                extractdepid = extractdepid + i
                        query1 = """INSERT INTO employee(emp_id, name, father, cnic, cell, address, image, type, designation, salary, date, dep_id, status)
                                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                        self.pointer.execute(query1, [empid, name, father, cnic, cell, address, emppic, emptype, designation, salary, newdate, extractdepid, True])
                        self.conn.commit()
                        return "Save"
                else:
                    return "Exists"
            else:
                return "Empty"
        else:
           return False

    #   View Employee Details
    def view_emp_data(self, empid):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT *
                    FROM employee
                    JOIN department ON employee.dep_id = department.dep_id
                    WHERE employee.emp_id=%s
                    """
            self.pointer.execute(query, [empid])
            empdetails = self.pointer.fetchall()
            return empdetails
        else:
            return False

    #   View Bonus
    def emp_bonus_data(self, empid):
        a = database_class().database_connection_check()
        if a == True:
            query = "SELECT id, name, amount, user FROM bonus WHERE emp_id=%s"
            self.pointer.execute(query, [empid])
            bonusdetails = self.pointer.fetchall()
            if bonusdetails == []:
                return "Empty"
            else:
                return bonusdetails
        else:
            return False

    #   Edit Employee Data
    def edit_employee_data(self,empid, name, father, cell, cnic, address, salary, depid, designation, emptype):
        a = database_class().database_connection_check()
        if a == True:
            if empid and name and father and cell and cnic and address and salary and depid and designation and emptype:
                query = """SELECT * FROM employee WHERE cnic=%s AND emp_id!=%s"""
                self.pointer.execute(query, [cnic, empid])
                existing = self.pointer.fetchall()
                if existing == []:
                    if emptype == "Salary" and int(salary) == 0:
                        return "No Salary"
                    elif emptype == "Contractor" and int(salary) != 0 or emptype == "Maker" and int(salary) != 0:
                        return "With Salary"
                    elif emptype == "Salary" and int(salary) > 0  or emptype == "Contractor" and int(salary) == 0 or emptype == "Maker" and int(salary) == 0:
                        extractdepid = ""
                        for i in depid:
                            if i == " ":
                                break
                            else:
                                extractdepid = extractdepid + i
                        query1 = """UPDATE employee SET name=%s, father=%s, cnic=%s, cell=%s, address=%s, type=%s, designation=%s, salary=%s, dep_id=%s WHERE emp_id=%s"""
                        self.pointer.execute(query1, [name, father, cnic, cell, address, emptype, designation, salary, extractdepid, empid])
                        self.conn.commit()
                        return "Save"
                else:
                    return "Exists"
            else:
                return "Empty"

    #   Employee Bonus
    def employee_bonus_data(self, empid, details, salary, addeddate, user):
        a = database_class().database_connection_check()
        if a == True:
            if empid and details and salary:
                query = "INSERT INTO bonus(emp_id, name, amount, date, user) VALUES(%s,%s,%s,%s,%s)"
                self.pointer.execute(query, [empid, details, salary, addeddate, user])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False
            
    #   Bonus Editing
    def bonus_editing_database(self, empid, details, salary, addeddate, user, bonusid):
        a = database_class().database_connection_check()
        if a == True:
            if empid and details and salary and bonusid:
                query = "UPDATE bonus SET name=%s, amount=%s, date=%s, user=%s WHERE id=%s AND emp_id=%s"
                self.pointer.execute(query, [details, salary, addeddate, user, bonusid, empid])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False    

    #   Delete Bonus
    def delete_bonus_from_database(self, empid, bonusid):
        a = database_class().database_connection_check()
        if a == True:
            if empid and bonusid:
                query = "DELETE FROM bonus WHERE emp_id=%s AND id=%s"
                self.pointer.execute(query, [empid, bonusid])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False

    #   Designations
    def all_designation_from_database(self):
        a = database_class().database_connection_check()
        if a == True:
            query = "SELECT name FROM designation"
            self.pointer.execute(query)
            bonusdetails = self.pointer.fetchall()
            return bonusdetails
        else:
            return False

    #   Under Supervision
    def emp_under_super(self, empid):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT employee.id, employee.emp_id, employee.name, employee.father, employee.type, employee.designation
                    FROM employee
                    WHERE employee.under=%s
                    ORDER BY employee.id ASC;
                    """
            self.pointer.execute(query, [empid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Save UnderSupervision
    def save_under_supervision_database(self, empid, underid):
        a = database_class().database_connection_check()
        if a == True:
            if empid and underid:
                #   Query
                query = "UPDATE employee SET under=%s WHERE emp_id=%s"
                self.pointer.execute(query, [empid, underid])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False

    #   Remove Employee UnderSupervision
    def remove_undersupervision_database(self, empid):
        a = database_class().database_connection_check()
        if a == True:
            if empid:
                #   Query
                query = "UPDATE employee SET under=%s WHERE emp_id=%s"
                self.pointer.execute(query, [" ", empid])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False

    #   Employee Data With SUpervisor
    def employee_data_with_supervisor(self, empid):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = """SELECT employee.emp_id, employee.name, employee.father, employee.status, employee.under, employee.image 
                        FROM employee
                        WHERE employee.emp_id=%s OR employee.cnic=%s OR employee.id=%s OR employee.cell=%s"""
            self.pointer.execute(query, [empid, empid, empid, empid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

#   Customer Order
class customer_order_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   New Order
    def new_order(self):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query3 = "SELECT * FROM customer_order"
            self.pointer.execute(query3)
            all_dep_ids = self.pointer.fetchall()
            if all_dep_ids == []:
                newdepid = 1
                return newdepid
            else:
                newdepid = 0
                for i in all_dep_ids:
                    new = i[0] + 1
                    newdepid = new
                return newdepid
            
        else:
            return False

    #   Order Category
    def order_category(self):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT name FROM customer_order_category"
            self.pointer.execute(query)
            order_details = self.pointer.fetchall()
            return order_details
        else:
            return False

    #   Existing Pending Orders
    def pending_orders(self):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT customer_order.id, customer_order.factory_po, customer_order.customer_po, customer_order.name, customer_order.qty, customer_order.type, customer_order.status, customer_order.added_date, customer_order.added_time, 
                        customer_order.clear_date, customer_order.clear_time, customer_order.user, users.user 
                        FROM customer_order
                        LEFT JOIN users ON customer_order.user = users.id 
                        WHERE status=%s"""
            self.pointer.execute(query, [False])
            order_details = self.pointer.fetchall()
            return order_details
        else:
            return False
        
    #   All Orders
    def all_orders(self):
        a = database_class().database_connection_check()
        if a == True:
            query = "SELECT id, factory_po, customer_po, name, qty, type, status, added_date, added_time, clear_date, clear_time, user FROM customer_order"
            self.pointer.execute(query)
            order_details = self.pointer.fetchall()
            return order_details
        else:
            return False

    #   View Articals
    def view_articals(self, fpo):
        a = database_class().database_connection_check()
        if a == True:
            query = "SELECT id, art_id, factory_po, details, size, color, qty FROM customer_order_details WHERE factory_po=%s"
            self.pointer.execute(query, [fpo])
            articaldetails = self.pointer.fetchall()
            return articaldetails
        else:
            return False

    #   Save New Order
    def save_new_order(self, factory_po, custmer_po, name, ordertype, qty, addeddate, addedtime, user):
        a = database_class().database_connection_check()
        if a == True:
            if factory_po and custmer_po and name and ordertype and qty and addeddate and addedtime:
                query = """SELECT * FROM customer_order WHERE factory_po=%s"""
                self.pointer.execute(query, [factory_po])
                existing = self.pointer.fetchall()
                if existing == []:
                    extracted_user = ""
                    for i in user:
                        if i == "-":
                            break
                        else:
                           extracted_user = str(extracted_user)+str(i)

                    query1 = """INSERT INTO customer_order(factory_po, customer_po, name, qty, type, added_date, added_time, user)
                                VALUES(%s, %s, %s,%s, %s, %s,%s, %s)"""
                    self.pointer.execute(query1, [factory_po, custmer_po, name, qty, ordertype, addeddate, addedtime, extracted_user])
                    self.conn.commit()
                    return "Save"
                else:
                    return "Exists"
            else:
                return "Empty"
        else:
            return False

    #   Artical Id
    def artical_id(self, fpo):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT * FROM customer_order_details WHERE factory_po=%s"
            self.pointer.execute(query, [fpo])
            details = self.pointer.fetchall()
            if details == []:
                newid = str(fpo)+"-"+str(1)
                return newid
            elif details != []:
                newid = ""
                for i in details:
                    newid = i[7] + 1
                return newid
        else:
            return False

    #   Artical Number
    def artical_database_number(self, fpo):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT * FROM customer_order_details WHERE factory_po=%s"
            self.pointer.execute(query, [fpo])
            details = self.pointer.fetchall()
            if details == []:
                newid = 1
                return newid
            elif details != []:
                newid = ""
                for i in details:
                    newid = i[7] + 1
                return newid
        else:
            return False

    #   Save New Artical
    def save_new_artical(self, fpo, artid, artno, prono, size, color, qty):
        a = database_class().database_connection_check()
        if a == True:
            if fpo and artid and prono and size and color and artno and qty:
                query = "INSERT INTO customer_order_details(art_id, factory_po, details, size, color, qty, new_id) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                self.pointer.execute(query, [artid, fpo, prono, size, color, qty, artno])
                self.conn.commit()
                return "Save"
            else:
               return "Empty"
        else:
           return False

    #   Save Order Editing
    def save_order_editing(self, orderid, factory_po, custmer_po, name, ordertype, qty):
        a = database_class().database_connection_check()
        if a == True:
            if factory_po and custmer_po and name and ordertype and qty and orderid:
                query = """SELECT * FROM customer_order WHERE factory_po=%s AND id!=%s"""
                self.pointer.execute(query, [factory_po, orderid])
                existing = self.pointer.fetchall()
                if existing == []:
                    query1 = """UPDATE customer_order SET factory_po=%s, customer_po=%s, name=%s, qty=%s, type=%s WHERE id=%s"""
                    self.pointer.execute(query1, [factory_po, custmer_po, name, qty, ordertype, orderid])
                    self.conn.commit()
                    return "Save"
                else:
                    return "Exists"
            else:
                return "Empty"
        else:
            return False
        
    #   Search Order Data
    def search_all_order_data(self, fpo):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT customer_order.*, users.user 
                        FROM customer_order
                        LEFT JOIN users ON customer_order.user = users.id
                        WHERE customer_order.factory_po=%s OR customer_order.customer_po=%s OR customer_order.id=%s"""
            self.pointer.execute(query, [fpo, fpo, fpo])
            order_details = self.pointer.fetchall()
            if order_details == []:
                return "Empty"
            else:
                return order_details
        else:
            return False
        
#   Customer Order
class customer_order_process_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   Artical Id
    def process_id(self, fpo):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT * FROM customer_order_rate WHERE order_id=%s"
            self.pointer.execute(query, [fpo])
            details = self.pointer.fetchall()
            if details == []:
                newid = 1
                return newid
            elif details != []:
                newid = 0
                for i in details:
                    newid = i[6] + 1
                return newid
        else:
            return False

    #   View Pocess
    def view_saved_process(self, fpo):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = """SELECT customer_order_rate.*, users.user , department.name
                        FROM customer_order_rate
                        JOIN department ON customer_order_rate.dep_id = department.dep_id
                        JOIN users ON customer_order_rate.user = users.id
                        WHERE customer_order_rate.order_id = %s
                        ORDER BY customer_order_rate.new_id ASC;
                    """
            self.pointer.execute(query, [fpo])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Save New Process
    def save_new_process_database(self, rateid, depid, details, processid, orderid, user):
        a = database_class().database_connection_check()
        if a == True: 
            if rateid and depid and processid and orderid:
                extractdepid = ""
                for i in depid:
                    if i == " ":
                        break
                    else:
                        extractdepid = extractdepid + i
                extractuserid = ""
                for i in user:
                    if i == "-":
                        break
                    else:
                        extractuserid = extractuserid + i
                
                #   Query
                query = "INSERT INTO customer_order_rate(pro_no, order_id, dep_id, name, user, new_id) VALUES(%s, %s, %s, %s, %s, %s)"
                self.pointer.execute(query, [rateid, orderid, extractdepid, details, extractuserid, processid])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False

    #   New Sub Process id
    def new_sub_process_id(self, fpo):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT * FROM customer_order_process WHERE pro_id=%s"
            self.pointer.execute(query, [fpo])
            details = self.pointer.fetchall()
            if details == []:
                newid = 1
                return newid
            elif details != []:
                newid = ""
                for i in details:
                    newid = i[4] + 1
                return newid
        else:
            return False

    #   All Sub Process
    def all_sub_process(self, fpo):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = """SELECT *
                        FROM customer_order_process
                        WHERE customer_order_process.pro_id = %s
                        ORDER BY customer_order_process.id ASC;
                    """
            self.pointer.execute(query, [fpo])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Save New Sub Process
    def save_new_sub_process_database(self,proid, rateid, details, newrate, newid):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = "INSERT INTO customer_order_process(sub_pro_id, pro_id, name, rate, new_id) VALUES(%s, %s, %s, %s, %s)"
            self.pointer.execute(query, [proid, rateid, details, newrate, newid])
            self.conn.commit()
            return "Save"
        else:
            return False

    #   Total Added Amount
    def total_added_amount_database(self, fpo):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT SUM(rate) as total_rate 
                        FROM customer_order_process 
                        WHERE pro_id = %s;
                        """
            self.pointer.execute(query, [fpo])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Save Process Editing
    def save_process_editing_in_database(self, proid, depid, details, orderid):
        a = database_class().database_connection_check()
        if a == True:
            if proid and depid and details and orderid:
                extractdepid = ""
                for i in depid:
                    if i == " ":
                        break
                    else:
                        extractdepid = extractdepid + i
                #   Query
                query = "UPDATE customer_order_rate SET name=%s, dep_id=%s WHERE pro_no=%s AND order_id=%s"
                self.pointer.execute(query, [details, extractdepid, proid, orderid])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return "False"

    #   Process By Depwise
    def order_process_dep_wise_database(self, orderid, depid):
        a = database_class().database_connection_check()
        if a == True:
            extracteddepid = ""
            for i in depid:
                if i == " ":
                    break
                else:
                    extracteddepid = str(extracteddepid)+str(i)
            #   QUERY
            query = """SELECT customer_order_rate.*, department.name
                    FROM customer_order_rate
                    LEFT JOIN department ON customer_order_rate.dep_id = department.dep_id
                    WHERE customer_order_rate.order_id = %s AND customer_order_rate.dep_id = %s
                    ORDER BY customer_order_rate.id ASC;
                    """
            self.pointer.execute(query, [orderid, extracteddepid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Depwise Process Details
    def view_saved_process_dep_wise(self, orderid, extracted_depid):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = """SELECT customer_order_rate.*, users.user , department.name
                        FROM customer_order_rate
                        JOIN department ON customer_order_rate.dep_id = department.dep_id
                        JOIN users ON customer_order_rate.user = users.id
                        WHERE customer_order_rate.order_id = %s AND customer_order_rate.dep_id = %s
                        ORDER BY customer_order_rate.new_id ASC;
                    """
            self.pointer.execute(query, [orderid, extracted_depid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Save Editing Database
    def save_editing_database(self, rateid, details, newrate):
        a = database_class().database_connection_check()
        if a == True:
            if rateid and details and newrate:
                #   QUERY
                query = "UPDATE customer_order_process SET name=%s, rate=%s WHERE sub_pro_id=%s"
                self.pointer.execute(query, [details, newrate, rateid])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False

    #   Qty for Wages
    def wages_details_database(self, depid, proid):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT SUM(qty) as total_rate 
                        FROM customer_order_in_dep 
                        WHERE dep_id = %s AND pro_id=%s;"""
            self.pointer.execute(query, [depid, proid])
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
    #   Sub Process rate Details
    def subprocess_rate_details_database(self, proid):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT SUM(rate) as total_rate 
                        FROM customer_order_process
                        WHERE pro_id=%s;"""
            self.pointer.execute(query, [proid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   process And Sub process of an order
    def all_pro_and_subpro_details_database(self, fpo):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT customer_order_rate.*, users.user , department.name
                        FROM customer_order_rate
                        JOIN department ON customer_order_rate.dep_id = department.dep_id
                        JOIN users ON customer_order_rate.user = users.id
                        WHERE customer_order_rate.order_id = %s
                        ORDER BY customer_order_rate.new_id ASC;
                    """
            self.pointer.execute(query, [fpo])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Check In main Process pc
    def check_in_main_process_pc_database(self, proid, artid):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT SUM(qty) as total_rate 
                        FROM customer_order_in_dep
                        WHERE pro_id=%s AND art_id = %s;"""
            self.pointer.execute(query, [proid, artid])
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
    #   Sub-Pro Qty in process
    def subpro_qty_in_details_database(self, subproid):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT customer_order_in_dep_receipt.sub_req_id, SUM(customer_order_sub_receipt_details.qty), SUM(customer_order_sub_receipt_details.rate)
                        FROM
                            customer_order_in_dep_receipt
                        LEFT JOIN customer_order_sub_receipt_details ON customer_order_in_dep_receipt.sub_req_id = customer_order_sub_receipt_details.sub_req
                        WHERE customer_order_in_dep_receipt.sub_pro = %s
                        """
            self.pointer.execute(query, [subproid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

#   Requsition
class requsition_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   New Request id
    def new_requisition_id(self, username):
        a = database_class().database_connection_check()
        if a == True:
            userid = ""
            for i in username:
                if i == "-":
                    break
                else:
                    userid = str(userid)+str(i)
                    
            #   QUERY
            query = "SELECT * FROM factory_requisition WHERE add_by=%s"
            self.pointer.execute(query, [userid])
            details = self.pointer.fetchall()
            if details == []:
                newid = str(1)
                return newid
            elif details != []:
                newid = ""
                for i in details:
                    newid = i[1] + 1
                n = str(newid)
                return n
        else:
            return False

    #   Save New request
    def save_requisition_database(self, reqid, reqno, depid, details, username, adddate, addtime):
        a = database_class().database_connection_check()
        if a == True:
            if depid and details:
                extractdepid = ""
                extracteduserid = ""
                for i in depid:
                    if i == " ":
                        break
                    else:
                        extractdepid = str(extractdepid) + str(i)

                for i in username:
                    if i == "-":
                        break
                    else:
                        extracteduserid = str(extracteduserid) + str(i)
                #   Query
                query = "INSERT INTO factory_requisition(req_id, req_no, dep_id, details, add_by, add_date, add_time, clear_status) VALUES(%s,%s, %s, %s, %s, %s, %s, %s)"
                self.pointer.execute(query,[reqid, reqno, extractdepid, details, extracteduserid, adddate, addtime, False])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False 

    #   Seacrh General Requisition
    def general_requisition_database(self, searchrequisition):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT 
                        factory_requisition.*,
                        addUser.user AS add_user,
                        approveUser.user AS approve_user,
                        clearUser.user AS clear_user,
                        department.name
                    FROM 
                        factory_requisition
                    LEFT JOIN 
                        users AS addUser ON factory_requisition.add_by = addUser.id
                    LEFT JOIN 
                        users AS approveUser ON factory_requisition.approve_by = approveUser.id
                    LEFT JOIN 
                        users AS clearUser ON factory_requisition.clear_by = clearUser.id
                    LEFT JOIN 
                        department ON factory_requisition.dep_id = department.dep_id
                    WHERE 
                        req_no = %s;
                    """
            self.pointer.execute(query, [searchrequisition])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Penind Requisitions
    def pending_requisitions(self):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT 
                        factory_requisition.*,
                        addUser.user AS add_user,
                        department.name
                    FROM 
                        factory_requisition
                    LEFT JOIN 
                        users AS addUser ON factory_requisition.add_by = addUser.id
                    LEFT JOIN 
                        department ON factory_requisition.dep_id = department.dep_id
                    WHERE
                        approve_status= %s;
                    """
            self.pointer.execute(query, [False])
            details = self.pointer.fetchall()
            return details
        else:
            return False

#   Raw Material
class raw_material_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   Existing Category
    def existing_category(self):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT id, name FROM material_category ORDER BY id ASC;"
            self.pointer.execute(query)
            all_dep_ids = self.pointer.fetchall()
            return all_dep_ids
        else:
            return False

    #   New Material id
    def new_material_id_database(self, catid):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT * FROM material_name WHERE type_id=%s"
            self.pointer.execute(query, [catid])
            details = self.pointer.fetchall()
            if details == []:
                newid = 1
                return newid
            elif details != []:
                newid = ""
                for i in details:
                    newid = i[6] + 1
                return newid
        else:
            return False

    #   Save New Material
    def save_raw_material_database(self, newid, category, matid, matname, matunit, color):
        a = database_class().database_connection_check()
        if a == True:
            if newid and category and matid and matname and matunit:
                #   Query
                extract_catid = ""
                for i in category:
                    if i == " ":
                        break
                    else:
                        extract_catid = extract_catid + i

                #   Query
                query = "INSERT INTO material_name(mat_id, name, color, unit, type_id, new_id) VALUES( %s, %s, %s, %s, %s, %s)"
                self.pointer.execute(query, [matid, matname, color, matunit, extract_catid, newid])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False
        
    #   All Existing Material Names
    def all_saved_material_names(self):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = """SELECT material_name.*, material_category.name AS type_name
                        FROM material_name
                        LEFT JOIN material_category ON material_name.type_id = material_category.id
                        ORDER BY material_name.type_id ASC;
                        ;"""
            self.pointer.execute(query)
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   New Article id
    def new_material_article_id_database(self, matid):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT * FROM material_article WHERE mat_id=%s"
            self.pointer.execute(query, [matid])
            details = self.pointer.fetchall()
            if details == []:
                newid = 1
                return newid
            elif details != []:
                newid = ""
                for i in details:
                    newid = i[4] + 1
                return newid
        else:
            return False

    #   All Articles
    def all_article_of_material(self, matid):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = """SELECT * FROM material_article WHERE mat_id=%s 
                        ORDER BY id ASC;"""
            self.pointer.execute(query, [matid])
            all_dep_ids = self.pointer.fetchall()
            return all_dep_ids
        else:
            return False

    #   Save New Article
    def save_new_article_in_database(self, new_id, artid, matid, artdetails):
        a = database_class().database_connection_check()
        if a == True:
            if new_id and artid and matid and artdetails:
                query = "INSERT INTO material_article(art_id, mat_id, name, new_id) VALUES(%s,%s,%s,%s)"
                self.pointer.execute(query, [artid, matid, artdetails, new_id])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False

    #   Save Editing
    def save_raw_material_edit_database(self, matname, matunit, color, oldid):
        a = database_class().database_connection_check()
        if a == True:
            if oldid and matname and matunit:
                #   Query
                query = """UPDATE material_name SET name=%s, color=%s, unit=%s WHERE mat_id=%s"""
                self.pointer.execute(query, [matname, color, matunit, oldid])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False  

    #   Search in Category
    def search_in_category_search(self, searchvalue):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT material_name.*, material_category.name AS mat_cat
                    FROM material_name
                    JOIN material_category ON material_name.type_id = material_category.id
                    WHERE material_name.type_id = %s
                    ORDER BY material_name.new_id ASC;"""
            self.pointer.execute(query, [searchvalue])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Search Material id
    def search_as_material_id(self, searchvalue):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT material_name.*, material_category.name AS type_name
                    FROM material_name
                    LEFT JOIN material_category ON material_name.type_id = material_category.id
                    WHERE material_name.mat_id = %s
                    ORDER BY material_name.new_id ASC;"""
            self.pointer.execute(query, [searchvalue])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Search Article id
    def search_as_article_id(self, searchvalue):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT material_article.*, material_name.*, material_category.name
                        FROM material_article
                        LEFT JOIN material_name ON material_article.mat_id = material_name.mat_id
                        LEFT JOIN material_category ON material_name.type_id = material_category.id
                        WHERE material_article.art_id = %s;
                    """
            self.pointer.execute(query, [searchvalue])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Save editing Database
    def save_article_editing_database(self, matid, artid, artname):
        a = database_class().database_connection_check()
        if a == True:
            if matid == "":
                if artid and artname:
                    #   Query
                    query = "UPDATE material_article SET name=%s WHERE art_id=%s"
                    self.pointer.execute(query, [artname, artid])
                    self.conn.commit()
                    return "Save"   
                else:
                    return "Empty"
            else:
                return "material id"
        else:
            return False

    #   Article in stock details
    def article_stock_details_database(self, artid):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT material_store.*, users.*
                    FROM material_store
                    LEFT JOIN users ON material_store.store_id = users.id
                    WHERE material_store.art_id=%s
                    ORDER BY material_store.id ASC;
                    """
            self.pointer.execute(query, [artid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Aricle details from database
    def article_details_from_database(self, artid):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT material_article.*, material_name.*, material_category.name
                    FROM material_article
                    JOIN material_name ON material_article.mat_id = material_name.mat_id
                    JOIN material_category ON material_name.type_id = material_category.id
                    WHERE material_article.art_id=%s"""
            self.pointer.execute(query, [artid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Save in Store Stock
    def save_stock_in_store_database(self, storeid, matid, artid, details, qty):
        a = database_class().database_connection_check()
        if a == True:
            if storeid and artid and qty and matid:
                extractdepid = ""
                for i in storeid:
                    if i == "-":
                        break
                    else:
                        extractdepid = extractdepid + i
                query = "SELECT * FROM material_store WHERE store_id=%s AND art_id=%s AND mat_id=%s"
                self.pointer.execute(query, [extractdepid, artid, matid])
                checking = self.pointer.fetchall()
                if checking != []:
                    return "Exist"
                elif checking == []:
                    #   Query1
                    query1 = "INSERT INTO material_store(store_id, mat_id, art_id, qty, details) VALUES(%s,%s,%s,%s,%s)"
                    self.pointer.execute(query1, [extractdepid, matid, artid, qty, details])
                    self.conn.commit()
                    return "Save"
            else:
                return "Empty"
        else:
            return False

    #   Storewise Stock information
    def storewise_stock_database(self, user, matid):
        a = database_class().database_connection_check()
        if a == True:
            userid = ""
            for i in user:
                if i == "-":
                    break
                else:
                    userid = userid = i

            query = """SELECT material_store.*, material_article.name, material_article.id
                        FROM material_store
                        LEFT JOIN material_article ON material_store.art_id = material_article.art_id
                        WHERE material_store.store_id = %s AND material_store.mat_id = %s
                        ORDER BY material_article.id ASC;
                        """
            self.pointer.execute(query, [userid, matid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Choose Material From Stock
    def material_from_stock_database(self, user):
        a = database_class().database_connection_check()
        if a == True:
            userid = ""
            for i in user:
                if i == "-":
                    break
                else:
                    userid = userid = i

            query = """SELECT material_store.mat_id, material_name.*
                        FROM material_store
                        LEFT JOIN material_name ON material_store.mat_id = material_name.mat_id
                        WHERE store_id=%s
                        ORDER BY material_name.id ASC;
                        """
            
            self.pointer.execute(query, [userid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Choose Article From Stock
    def article_from_selected_store_stock_database(self, user, artid):
        a = database_class().database_connection_check()
        if a == True:
            userid = ""
            for i in user:
                if i == "-":
                    break
                else:
                    userid = userid = i
            
            query = """SELECT material_store.*, material_name.*, material_article.name
                        FROM material_store
                        LEFT JOIN material_name ON material_store.mat_id = material_name.mat_id
                        LEFT JOIN material_article ON material_store.art_id = material_article.art_id
                        WHERE material_store.store_id = %s AND material_store.art_id = %s
                        ORDER BY material_store.art_id ASC;
                        """
            self.pointer.execute(query, [userid, artid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Article Qty in Store
    def art_qty_in_store_database(self, artid, store):
        a = database_class().database_connection_check()
        if a == True:
            storeid = ""
            for i in store:
                if i == "-":
                    break
                else:
                    storeid = str(storeid)+i

            query = "SELECT qty FROM material_store WHERE store_id=%s AND art_id=%s"
            self.pointer.execute(query, [storeid, artid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Material history
    def material_history_database(self, artid, startdate, enddate, user):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT material_out.*, users.user, customer_order.factory_po, customer_order.customer_po
                        FROM material_out
                        LEFT JOIN users ON material_out.user = users.id
                        LEFT JOIN customer_order ON material_out.order_id = customer_order.id
                        WHERE material_out.art_id = %s AND material_out.date BETWEEN %s AND %s AND material_out.user = %s
                        ORDER BY material_out.date ASC;
                        """
            self.pointer.execute(query, [artid, startdate, enddate, user])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Article Purchase for Order
    def material_article_total_purchase_for_order(self, orderid, artid):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT SUM(qty) as total_rate 
                        FROM material_out 
                        WHERE art_id = %s AND order_id=%s; 
                    """
            self.pointer.execute(query, [artid, orderid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Material balance
    def material_balance_database(self, artid):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT
                        COALESCE(
                            SUM(CASE WHEN material_out.category = 'Debit' THEN material_out.qty ELSE 0 END) -
                            SUM(CASE WHEN  material_out.qty = 'Credit' THEN material_out.qty ELSE 0 END),
                            0
                        ) AS Short_Term_Balance,
                    FROM
                        material_out
                    WHERE
                        material_out.art_id = %s;
                    """
            self.pointer.execute(query, [artid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

#   Order Average
class order_average_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   Existing Category
    def existing_material_use(self):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT id, name FROM material_use ORDER BY id ASC;"
            self.pointer.execute(query)
            all_dep_ids = self.pointer.fetchall()
            return all_dep_ids
        else:
            return False

    #   Existing Estimated Average
    def existing_estimated_avg(self, fpo):
        a = database_class().database_connection_check()
        if a == True:
            """SELECT material_average.*, material_article.name, material_name.name, material_name.color, material_name.unit, material_use.name, users.user
                FROM material_average
                LEFT JOIN material_name ON material_average.mat_id = material_name.mat_id
                LEFT JOIN material_article ON material_average.art_id = material_article.art_id
                LEFT JOIN material_use ON material_average.use_in = material_use.id
                LEFT JOIN users ON material_average.user = users.id
                WHERE material_average.order_id = %s
                ORDER BY material_average.id ASC;
                """
            query = """SELECT
                        material_average.*,
                        material_article.name,
                        material_name.name,
                        material_name.color,
                        material_name.unit,
                        material_use.name,
                        users.user,
                        IFNULL(
                            (
                                SELECT
                                    amount
                                FROM
                                    material_out
                                WHERE
                                    art_id = material_average.art_id
                                    AND type = 'Purchase'
                                    AND category = 'Debit'
                                ORDER BY
                                    date DESC
                                LIMIT 1
                            ),
                            0  -- Return 0 if there's no last purchase amount
                        ) AS last_purchase_amount
                    FROM
                        material_average
                    LEFT JOIN material_name ON material_average.mat_id = material_name.mat_id
                    LEFT JOIN material_article ON material_average.art_id = material_article.art_id
                    LEFT JOIN material_use ON material_average.use_in = material_use.id
                    LEFT JOIN users ON material_average.user = users.id
                    WHERE
                        material_average.order_id = %s
                    ORDER BY
                        material_average.id ASC;

                    """
            self.pointer.execute(query, [fpo])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Save Estimated Average
    def save_estimated_avg_databae(self, orderid, matid, artid, stdavg, estavg, usein, details, user):
        a = database_class().database_connection_check()
        if a == True:
            if orderid and matid and artid and stdavg and estavg and usein and user:
                cropuse = ""
                cropuser = ""
                for i in user:
                    if i == "-":
                        break
                    else:
                        cropuser = i
                
                for i in usein:
                    if i == "-":
                        break
                    else:
                        cropuse = i
                
                query = "SELECT * FROM material_average WHERE order_id=%s AND mat_id=%s AND art_id=%s AND use_in=%s"
                self.pointer.execute(query, [orderid, matid, artid, cropuse])
                match = self.pointer.fetchall()
                if match == []:
                    query1 = """INSERT INTO material_average(order_id, mat_id, art_id, std_avg, est_avg, use_in, details, user)
                                VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
                    self.pointer.execute(query1, [orderid, matid, artid, stdavg, estavg, cropuse, details, cropuser])
                    self.conn.commit()
                    return "Save"
                else:
                    return "Exists"
            else:
                return "Empty"
        else:
            return False

    #   Total Article Qty Out On Order
    def total_article_out_for_order(self, orderid, articleid):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT SUM(qty) as total_rate 
                    FROM material_out 
                    WHERE order_id=%s AND art_id=%s;"""
            self.pointer.execute(query, [orderid, articleid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

#   Order receipts
class order_receipts(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   New Receipt id
    def new_receipt_id(self, artid):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT * FROM customer_order_in_dep WHERE art_id=%s"
            self.pointer.execute(query, [artid])
            details = self.pointer.fetchall()
            if details == []:
                newid = 1
                return newid
            elif details != []:
                newid = ""
                for i in details:
                    newid = i[6] + 1
                return newid
        else:
            return False

    #   Order Details & Rate Database
    def order_details_and_rate_database(self, searchbar):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = """SELECT * FROM customer_order 
                    LEFT JOIN customer_order_details ON customer_order.id = customer_order_details.factory_po
                    WHERE customer_order.id=%s
                    ORDER BY customer_order_details.id ASC;"""
            self.pointer.execute(query, [searchbar])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Order Rate Dep Wise
    def order_all_rate_database(self, orderid):
        a = database_class().database_connection_check()
        if a == True:
            extractoderid = ""
            for i in orderid:
                if i == " ":
                    break
                else:
                    extractoderid = extractoderid + i
            #   QUERY
            query = """SELECT customer_order_rate.*, department.name AS dep_name
                        FROM customer_order_rate
                        LEFT JOIN department ON customer_order_rate.dep_id = department.dep_id
                        WHERE customer_order_rate.order_id = %s
                        ORDER BY customer_order_rate.id ASC;
                    """
            self.pointer.execute(query, [extractoderid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Check Article Qty in department
    def check_article_in_department_database(self, artid, depid):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            if artid and depid:
                parts = depid.split("|")
                extracteddepid = parts[1]
                parts2 = extracteddepid.split(" ")
                newdepid = parts2[0]

                #   Query
                query = """SELECT SUM(qty) as total_rate 
                        FROM customer_order_in_dep 
                        WHERE art_id=%s AND dep_id=%s;"""
                self.pointer.execute(query, [artid, newdepid])
                details = self.pointer.fetchall()
                return details
            else:
                return "Empty"
        else:
            return False

    #   Save Art in Department
    def save_art_in_dep_database(self,depid, artid, user,newqty, receiptno, databsereceiptno, empid, makedate, maketime, comments):
        a = database_class().database_connection_check()
        if a == True:
            if depid and artid and user and newqty and receiptno and databsereceiptno and empid:
                parts = depid.split("|")
                newdep = parts[1]
                pp = newdep = newdep.split(" ")
                extracteddepid = pp[0]
                parts1 = depid.split("|")
                extractedprono = parts1[0]
                parts2 = user.split("-")
                extracteduser = parts2[0]

                #   QUERY
                query = """INSERT INTO customer_order_in_dep(rep_id, pro_id, dep_id, art_id, qty, new_id, user, emp_id, date, time, comments)
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                self.pointer.execute(query, [receiptno, extractedprono, extracteddepid, artid, newqty, databsereceiptno, extracteduser, empid, makedate, maketime, comments])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False

    #   Book Work on Receipt
    def seacrh_receipt_for_work_booking(self, receiptno):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = """SELECT
                        customer_order_in_dep.*,
                        customer_order_rate.name AS rate_name,
                        department.name AS department_name,
                        customer_order_details.factory_po,
                        customer_order_details.details,
                        customer_order_details.size,
                        customer_order_details.color,
                        users.user,
                        employee.name AS employee_name,
                        employee.father,
                        employee.image,
                        customer_order.id,
                        customer_order.factory_po,
                        customer_order.customer_po,
                        customer_order.name,
                        customer_order.type,
                        customer_order.qty
                    FROM
                        customer_order_in_dep
                    LEFT JOIN customer_order_rate ON customer_order_in_dep.pro_id = customer_order_rate.pro_no
                    LEFT JOIN department ON customer_order_in_dep.dep_id = department.dep_id
                    LEFT JOIN customer_order_details ON customer_order_in_dep.art_id = customer_order_details.art_id
                    LEFT JOIN users ON customer_order_in_dep.user = users.id
                    LEFT JOIN employee ON customer_order_in_dep.emp_id = employee.emp_id
                    LEFT JOIN customer_order ON customer_order_details.factory_po = customer_order.id
                    WHERE
                        rep_id = %s;
                    """
            self.pointer.execute(query, [receiptno])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Already Added Receipts of Selected Process
    def already_saved_selected_process(self, artid, depid):
        a = database_class().database_connection_check()
        if a == True:
            parts = depid.split("|")
            extracteddepid = parts[1]
            parts2 = extracteddepid.split(" ")
            newdepid = parts2[0]

            extractedprono = parts[0]

            #   Query
            query = """SELECT
                        customer_order_in_dep.*,
                        employee.name AS employee_name,
                        employee.father,
                        users1.user AS user,
                        users2.user AS clear_user
                    FROM
                        customer_order_in_dep
                    LEFT JOIN employee ON customer_order_in_dep.emp_id = employee.emp_id
                    LEFT JOIN users AS users1 ON customer_order_in_dep.user = users1.id
                    LEFT JOIN users AS users2 ON customer_order_in_dep.clear_user = users2.id
                    WHERE
                        customer_order_in_dep.art_id = %s AND customer_order_in_dep.dep_id = %s;
                    """
            self.pointer.execute(query, [artid, newdepid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Check Sub-Pro Receipt Qty
    def check_sub_pro_receipt_qty(self, reqid, subproid):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT 
                        customer_order_in_dep_receipt.sub_pro, 
                        customer_order_in_dep_receipt.qty, 
                        customer_order_process.name, 
                        customer_order_process.rate
                    FROM 
                        customer_order_in_dep_receipt
                    LEFT JOIN customer_order_process ON customer_order_in_dep_receipt.sub_pro = customer_order_process.sub_pro_id
                    WHERE 
                        customer_order_in_dep_receipt.req_id = %s AND customer_order_in_dep_receipt.sub_pro = %s;


                    """
            self.pointer.execute(query,(reqid, subproid))
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
    #   Check Sub-Receipts Qty
    def check_already_qty_subreceipt_dataabse(self, reqid, subproid):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT 
                        customer_order_in_dep_receipt.qty
                    FROM 
                        customer_order_in_dep_receipt
                    WHERE 
                        customer_order_in_dep_receipt.req_id = %s AND customer_order_in_dep_receipt.sub_pro = %s;
                    """
            self.pointer.execute(query,(reqid, subproid))
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   New Sub Receipt No
    def new_sub_receipt_no(self, processid):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT * FROM customer_order_in_dep_receipt WHERE req_id=%s"
            self.pointer.execute(query, [processid])
            details = self.pointer.fetchall()
            if details == []:
                newid = 1
                return newid
            elif details != []:
                newid = ""
                for i in details:
                    newid = i[5] + 1
                return newid
        else:
            return False

    #   Save New Sub Receipt
    def save_sub_receipt_in_database(self, receiptno, subproid, empid, qty, newid, subreceiptid, adddate, addtime, userid, comments):
        a = database_class().database_connection_check()
        if a == True:
            if receiptno and subproid and userid and qty and empid and subreceiptid and newid:
                #   Query
                query = """INSERT INTO customer_order_in_dep_receipt(req_id, sub_pro, emp_id, qty, new_id, sub_req_id, date, time, user, comments)
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                self.pointer.execute(query, [receiptno, subproid, empid, qty, newid, subreceiptid, adddate, addtime, userid, comments])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False

    #   Check Sub receipt
    def check_subreceipt_database(self, receiptno):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT customer_order_in_dep_receipt.*,
                        customer_order_process.name AS rate_name,
                        customer_order_process.rate AS rate,
                        users.user,
                        employee.name AS employee_name,
                        employee.father,
                        employee.image
                    FROM
                        customer_order_in_dep_receipt
                        LEFT JOIN customer_order_process ON customer_order_in_dep_receipt.sub_pro = customer_order_process.sub_pro_id
                        LEFT JOIN users ON customer_order_in_dep_receipt.user = users.id
                        LEFT JOIN employee ON customer_order_in_dep_receipt.emp_id = employee.emp_id
                    WHERE
                        customer_order_in_dep_receipt.sub_req_id = %s;
                        """
            self.pointer.execute(query, [receiptno])
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
    #   Sub Receipt Details
    def sub_receipt_details_database(self,subreceiptno):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT customer_order_sub_receipt_details.*, 
                        users.user
                    FROM customer_order_sub_receipt_details
                    LEFT JOIN users ON customer_order_sub_receipt_details.user = users.id
                    WHERE sub_req = %s;
                    """
            self.pointer.execute(query, [subreceiptno])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Save Sub req Qty
    def save_sub_req_qty_database(self, subreceiptid, adddate, addtime,  user, qty):
        a = database_class().database_connection_check()
        if a == True:
            if subreceiptid and qty and user:
                #   Query
                query = """INSERT INTO customer_order_sub_receipt_details(sub_req, qty, date, time, user)
                            VALUES(%s, %s, %s, %s, %s)
                        """
                self.pointer.execute(query, [subreceiptid, qty, adddate, addtime, user])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False

    #   Process Receipts
    def process_receipts_database(self, depid, proid, artid):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT
                        customer_order_in_dep.*,
                        employee.name AS employee_name,
                        employee.father,
                        users1.user AS user,
                        users2.user AS clear_user
                    FROM
                        customer_order_in_dep
                    LEFT JOIN employee ON customer_order_in_dep.emp_id = employee.emp_id
                    LEFT JOIN users AS users1 ON customer_order_in_dep.user = users1.id
                    LEFT JOIN users AS users2 ON customer_order_in_dep.clear_user = users2.id
                    WHERE
                        customer_order_in_dep.pro_id = %s AND customer_order_in_dep.art_id = %s AND customer_order_in_dep.dep_id = %s;
                    """
            self.pointer.execute(query, [proid, artid, depid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Process Sub Receipt On Receipt Information
    def sub_receipt_information_on_database(self, receiptno, subprocess):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT 
                        customer_order_in_dep_receipt.*,
                        users.user,
                        employee.name AS employee_name,
                        employee.father,
                        employee.image,
                        customer_order_sub_receipt_details.qty,
                        customer_order_sub_receipt_details.date,
                        customer_order_sub_receipt_details.time,
                        customer_order_sub_receipt_details.user,
                        customer_order_sub_receipt_details.status
                    FROM 
                        customer_order_in_dep_receipt
                    LEFT JOIN 
                        users ON customer_order_in_dep_receipt.user = users.id
                    LEFT JOIN 
                        employee ON customer_order_in_dep_receipt.emp_id = employee.emp_id
                    LEFT JOIN 
                        customer_order_sub_receipt_details ON customer_order_in_dep_receipt.sub_req_id = customer_order_sub_receipt_details.sub_req
                    WHERE 
                        customer_order_in_dep_receipt.req_id = %s 
                        AND customer_order_in_dep_receipt.sub_pro = %s
                    ORDER BY 
                        customer_order_in_dep_receipt.new_id ASC;
                        """
            self.pointer.execute(query, [receiptno, subprocess])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   sub_receipt_total_qty
    def sub_receipt_total_qty_database(self, receiptno, subprocess):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT 
                            COALESCE(SUM(customer_order_in_dep_receipt.qty), 0) as total_rate,
                            customer_order_in_dep_receipt.sub_req_id,
                            COALESCE(SUM(customer_order_sub_receipt_details.qty), 0) as receipt_qty
                        FROM
                            customer_order_in_dep_receipt
                        LEFT JOIN customer_order_sub_receipt_details ON customer_order_in_dep_receipt.sub_req_id = customer_order_sub_receipt_details.sub_req
                        WHERE customer_order_in_dep_receipt.req_id = %s AND customer_order_in_dep_receipt.sub_pro = %s;
                    """
            self.pointer.execute(query, [receiptno, subprocess])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Sub Receipt Qty
    def sub_receipt_information_database(self, subreceiptno):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT customer_order_sub_receipt_details.*, users.user
                    FROM 
                        customer_order_sub_receipt_details
                    LEFT JOIN users ON customer_order_sub_receipt_details.user = users.id
                    WHERE
                        customer_order_sub_receipt_details.sub_req = %s
                        ORDER BY customer_order_sub_receipt_details.date ASC;
                    """
            self.pointer.execute(query, [subreceiptno])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Check All receipts of related Sub Receipt
    def check_all_sub_receipts_numbers(self, proid, receiptno):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT
                        customer_order_in_dep_receipt.sub_req_id,
                        customer_order_in_dep_receipt.emp_id,
                        customer_order_in_dep_receipt.qty,
                        SUM(customer_order_sub_receipt_details.qty),
                        employee.name,
                        employee.father
                    FROM
                        customer_order_in_dep_receipt
                    LEFT JOIN customer_order_sub_receipt_details ON customer_order_in_dep_receipt.sub_req_id = customer_order_sub_receipt_details.sub_req
                    LEFT JOIN employee ON customer_order_in_dep_receipt.emp_id = employee.emp_id
                    WHERE
                        customer_order_in_dep_receipt.sub_pro = %s AND customer_order_in_dep_receipt.req_id = %s
                    GROUP BY
                        customer_order_in_dep_receipt.sub_req_id,
                        customer_order_in_dep_receipt.emp_id,
                        customer_order_in_dep_receipt.qty,
                        employee.name,
                        employee.father
                    ORDER BY
                        customer_order_in_dep_receipt.id ASC;

                        """
            self.pointer.execute(query, [proid, receiptno])
            details = self.pointer.fetchall()
            return details
        else:
            return False

#   Material Issue On receipt    
class material_issue_on_receipt_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   Check receipt
    def check_receipt_status(self, receiptid):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "SELECT * FROM customer_order_receipt WHERE receipt_id=%s"
            self.pointer.execute(query, [receiptid])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Receipt Details
    def receipt_information_database(self, search):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY  
            query = """SELECT customer_order_receipt.*, employee.name, employee.father, customer_order_rate.name, department.name, customer_order_process.name, 
                        customer_order_details.factory_po, customer_order.factory_po, customer_order.customer_po, customer_order.name, customer_order.type, employee.image, employee.under,
                        customer_order_details.details, customer_order_details.size, customer_order_details.color
                        FROM customer_order_receipt
                        LEFT JOIN employee ON customer_order_receipt.emp_id = employee.emp_id
                        LEFT JOIN customer_order_rate ON customer_order_receipt.pro_id = customer_order_rate.pro_no
                        LEFT JOIN department ON customer_order_receipt.dep_id = department.dep_id
                        LEFT JOIN customer_order_process ON customer_order_receipt.sub_pro_id = customer_order_process.sub_pro_id
                        LEFT JOIN customer_order_details ON customer_order_receipt.art_id = customer_order_details.art_id
                        LEFT JOIN customer_order ON customer_order_details.factory_po = customer_order.id
                        WHERE customer_order_receipt.receipt_id = %s"""
        
            self.pointer.execute(query, [search])
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
    #   Material On Receipt
    def material_details_on_wages_receipt(self, receiptid, artid, issuetype):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT SUM(qty) as total_rate 
                        FROM material_out 
                        WHERE req_id = %s AND art_id=%s AND type=%s;"""
                        
            self.pointer.execute(query, [receiptid, artid, issuetype])
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
    #   Total Material on Order
    def material_details_on_order(self, orderid, artid):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT SUM(qty) as total_rate 
                        FROM material_out 
                        WHERE order_id = %s AND art_id=%s;"""
                        
            self.pointer.execute(query, [orderid, artid])
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
    #   Save Out Material On receipt
    def save_out_material_receipt_database(self, orderid, receiptid, artid, qty, date, time, store, outtype, price, stockqty):
        a = database_class().database_connection_check()
        if a == True:
            storeid = ""
            for i in store:
                if i == "-":
                    break
                else:
                    storeid = str(storeid)+i

            query = """INSERT INTO material_out(art_id, amount, req_id, date, time, qty, type, category, user, order_id, balance) VALUES(%s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s)"""
            self.pointer.execute(query, [artid, price, receiptid, date, time, qty, outtype, "Credit", store, orderid, stockqty])
            self.conn.commit()
            return "Save"
        else:
            return False

    #   Stock Update
    def update_store_stock(self, remainstock, artid, store):
        a = database_class().database_connection_check()
        if a == True:
            storeid = ""
            for i in store:
                if i == "-":
                    break
                else:
                    storeid = str(storeid)+i
            
            query = "UPDATE material_store SET qty=%s WHERE art_id=%s AND store_id=%s"
            self.pointer.execute(query, [remainstock, artid, storeid])
            self.conn.commit()
            return "Save"
        else:
            return False

#   Employee Ledger
class employee_ledger_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   Save new credit/Debit
    def save_new_credit_debit_database(self, empid, amount, name, currentdate, currenttime, amountcategory, amounttermtype, userid):
        a = database_class().database_connection_check()
        if a == True:
            if empid and amount and name and amountcategory and amounttermtype:
                query = """INSERT INTO employee_ledger(emp_id, amount, name, date, time, type, category, user)
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
                self.pointer.execute(query, [empid, amount, name, currentdate, currenttime, amountcategory, amounttermtype, userid])
                self.conn.commit()
                return "Save"
            else:
                return "Empty"
        else:
            return False
        
    #   Employee balance Details
    def employee_balance_details_database(self, empid, startdate, enddate, category):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT employee_ledger.*, users.user 
                        FROM employee_ledger
                        LEFT JOIN users ON employee_ledger.user = users.id
                        WHERE employee_ledger.emp_id = %s AND employee_ledger.date BETWEEN %s AND %s AND employee_ledger.type = %s
                        ORDER BY employee_ledger.date ASC;
                        """
            self.pointer.execute(query, [empid, startdate, enddate, category])
            details = self.pointer.fetchall()
            return details
        else:
            return False

    #   Employee All Ledger
    def employee_all_ledger_details_database(self, empid, selection):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT employee_ledger.*
                        FROM employee_ledger
                        LEFT JOIN users ON employee_ledger.user = users.id
                        WHERE employee_ledger.emp_id = %s AND employee_ledger.type = %s
                        ORDER BY employee_ledger.date ASC;
                        """
            self.pointer.execute(query, [empid, selection])
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
    #   Given Date balance
    def given_date_opening_balance_database(self,empid, selection ,startdate):
        a = database_class().database_connection_check()
        if a == True:
            query = """
                    SELECT
                    COALESCE(
                        SUM(CASE WHEN type = %s AND category = 'Debit' AND date < %s THEN amount ELSE 0 END) -
                        SUM(CASE WHEN type = %s AND category = 'Credit' AND date < %s THEN amount ELSE 0 END)
                    ) AS opening_balance
                    FROM
                        employee_ledger
                    WHERE emp_id=%s
                    """
            self.pointer.execute(query, [selection, startdate, selection, startdate, empid])
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
    #   last transaction details of employee
    def last_transaction_details_database(self, empid):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT *
                        FROM employee_ledger
                        WHERE emp_id = %s AND type = %s
                        ORDER BY date ASC;
                    """
            self.pointer.execute(query, [empid, "Short Term"])
            details = self.pointer.fetchall()
            return details
        else:
            return False

#   Employee Record
class employee_receord_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   Contractor Record
    def contractor_clearwork_database(self, empid):
        a = database_class().database_connection_check()
        if a == True:
            #   Query
            query = """SELECT customer_order_in_dep_receipt.sub_pro, customer_order_in_dep_receipt.qty, customer_order_in_dep_receipt.sub_req_id, customer_order_process.rate,
                    customer_order_sub_receipt_details.qty, customer_order_sub_receipt_details.status
                    FROM
                        customer_order_in_dep_receipt
                    LEFT JOIN customer_order_process ON customer_order_in_dep_receipt.sub_pro = customer_order_process.sub_pro_id
                    LEFT JOIN customer_order_sub_receipt_details ON customer_order_in_dep_receipt.sub_req_id = customer_order_sub_receipt_details.sub_req
                    WHERE customer_order_in_dep_receipt.emp_id=%s AND customer_order_in_dep_receipt.status=%s AND customer_order_sub_receipt_details.status=%s"""
            self.pointer.execute(query, [empid, False, False])
            details = self.pointer.fetchall()
            return details
        else:
            return False


