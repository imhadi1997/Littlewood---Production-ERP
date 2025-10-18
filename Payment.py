#   Tkinter Import
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import ttkthemes
import datetime
from tkcalendar import *
from tkinter.ttk import Combobox, Treeview
from tkinter import filedialog
from database import *
from tkinter import simpledialog

class payment_systemn:
    #   init
    def __init__(self, root, u):
        self.root = root
        self.username = u

        self.black = "black"
        self.white = "white"
        self.gray = "#ededf0"
        self.bgcolor = "#E6E7E8"
        self.powderblue = "powder blue"
        self.lightgreen = "#cdfac5"
        self.lightred = "#fac5d5"
        self.green = "green"
        self.red = "red"

        self.backiconphoto = Image.open("img/back_button.png")
        self.saveiconphoto = Image.open("img/save_button.png")
        self.searchiconphoto = Image.open("img/search_button.png")
        self.addimageiconphoto = Image.open("img/addimage_button.png")
        self.editiconphoto = Image.open("img/edit_button.png")
        self.cleariconphoto = Image.open("img/clear_button.png")
        self.printiconphoto = Image.open("img/print_button.png")
        self.debiticonphoto = Image.open("img/debit.png")
        self.multiplicationiconphoto = Image.open("img/multiplication.png")

    #   New Window
    def new_window(self):
        a = database_class().database_connection_check()
        if a == True:
            self.root2 = Toplevel(self.root)
            self.root2.geometry("1500x885")
            self.appiconphoto = Image.open("img/icon.png")
            icon_photo = ImageTk.PhotoImage(self.appiconphoto)
            self.root2.iconphoto(False, icon_photo)
            self.root2.resizable(False, False)
            self.root2.title("Littlewood Corporation(pvt) - ERP -  User: "+str(self.username))

            self.style = ttkthemes.ThemedStyle(self.root2)
            self.style.theme_use('clam')
            self.style.configure('Treeview', foreground=self.black, background=self.white, fieldbackground=self.white)
            self.style.configure('Treeview.Heading', foreground=self.black, background=self.powderblue)
            self.style.map('Treeview', background=[('selected', self.powderblue)], foreground=[('selected', self.black)])
            self.style.map('Treeview.Heading', background=[('selected', self.white)], foreground=[('selected', self.black)])
            
            self.menubar = Menu(self.root2, tearoff=1)
            self.menubar.add_command(label="Log Out", command=self.logout)
            self.root2.config(menu=self.menubar)
            self.root2.protocol("WM_DELETE_WINDOW", self.logout)

            self.payment_system_frame()
        else:
            messagebox.showerror(parent=self.root,title="Server Respone", message="Database connection lost")

    #   Receipt System Frame
    def payment_system_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            self.root2backgroundphoto = Image.open("img/background.png")
            self.depiconphoto = Image.open("img/dep_icon.png")
            self.empiconphoto = Image.open("img/emp_icon.png")
            self.ledgericonphoto = Image.open("img/ledger.png")

            self.bg_photo = ImageTk.PhotoImage(self.root2backgroundphoto)
            self.bg_label = Label(self.root2, image=self.bg_photo, width=1500, height=116)
            self.bg_label.place(x=0, y=0)

            self.blankhomeframe = Frame(self.root2, width=1500, bd=3, bg=self.bgcolor, relief=FLAT)
            self.blankhomeframe.place(x=1, y=117, height=770)

            #   Department Button
            self.depicon = ImageTk.PhotoImage(self.depiconphoto)
            self.departmentbutton = Button(self.blankhomeframe, width=130,  text="Department",font=("Time new rooman", 9, "bold", "italic"), image=self.depicon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=departments_class(self.root2, self.username, self.root).add_department_frame)
            self.departmentbutton.place(x=10, y=0, height=65)

            #   Employee
            self.empicon = ImageTk.PhotoImage(self.empiconphoto)
            self.addemployeebutton = Button(self.blankhomeframe, width=130, text="Employee", font=("Time new rooman", 9, "bold", "italic"), image=self.empicon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=employee_class(self.root2, self.username, self.root).add_employee_frame)
            self.addemployeebutton.place(x=150, y=0, height=65)

            #   Employee Ledger
            self.ledgericon = ImageTk.PhotoImage(self.ledgericonphoto)
            self.ledgerempbutton = Button(self.blankhomeframe, width=130, text="Employee\nLedger", font=("Time new rooman", 9, "bold", "italic"), image=self.ledgericon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=employee_ledger_class(self.root2, self.username, self.root).employee_ledger_frame)
            self.ledgerempbutton.place(x=290, y=0, height=65)

        else:
            messagebox.showerror(parent=self.root,title="Server Respone", message="Database connection lost")

    #   Log Out
    def logout(self):
        self.root2.withdraw()
        self.root.deiconify()
    
        #   CURRENT DATE
    
    #   Current Date
    def current_date(self):
        now = datetime.datetime.now()
        m = now.strftime("%G-%m-%d")
        return m
    
    #   Current Time
    def current_time(self):
        now = datetime.datetime.now()
        m = now.strftime("%I:%M %p")
        return m

    #   Current Day
    def current_day(self):
        now = datetime.datetime.now()
        m = now.strftime("%d")
        return m
    
    #   Current Month
    def current_month(self):
        now = datetime.datetime.now()
        m = now.strftime("%m")
        return m

    #   Current Year
    def current_year(self):
        now = datetime.datetime.now()
        m = now.strftime("%G")
        return m

    #   Bind Clear
    def bind_clear(self, eve):
        pass

#   Department
class departments_class(payment_systemn):
    #   init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)
   
    #   Department Frame
    def add_department_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.editempinfoframe = Frame(self.newdepinfoframemain, width=710, bg=self.gray, bd=4, relief=FLAT)
            self.editempinfoframe.place(x=0, y=0, height=70)

            #   DEP LABELS
            self.addnewemployeelabel = Label(self.editempinfoframe, text=" Department Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=250, y=0)
            self.depidlabel = Label(self.editempinfoframe, text="Department:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=8, y=26)

            existingdeps = department_database().existing_departments()
            depdefaultdetails = department_database().department_default_details()
            
            #   Variables
            self.editdepid_var = StringVar()

            d = [""]
            for i in existingdeps:
                d.append(i)
            #   Entry
            self.depentry = Combobox(self.editempinfoframe, values=d, textvariable=self.editdepid_var,  state="readonly")
            self.depentry.place(x=130, y=30, height=24, width=170)
            self.depentry.focus_set()

            #   TREE
            self.v = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v.pack(side=RIGHT, fill=Y)
            self.v.place(x=1469, y=75, height=373)

            self.tree = Treeview(self.newdepinfoframemain, height=17, columns=("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"), show="headings", yscrollcommand=self.v.set)
            self.tree.place(x=1, y=75, width=1466)

            self.tree.column("#1", anchor="nw", width=80)
            self.tree.column("#2", anchor="nw", width=320)
            self.tree.column("#3", anchor=CENTER, width=80)
            self.tree.column("#4", anchor=CENTER, width=80)
            self.tree.column("#5", anchor=CENTER, width=90)
            self.tree.column("#6", anchor=CENTER, width=80)
            self.tree.column("#7", anchor=CENTER, width=90)
            self.tree.column("#8", anchor=CENTER, width=90)
            self.tree.column("#9", anchor=CENTER, width=70)

            self.tree.heading("#1", text="Dep id")
            self.tree.heading("#2", text="Department Name")
            self.tree.heading("#3", text="Contractor")
            self.tree.heading("#4", text="SalaryBase")
            self.tree.heading("#5", text="Makers")
            self.tree.heading("#6", text="Total")
            self.tree.heading("#7", text="")
            self.tree.heading("#8", text="")
            self.tree.heading("#9", text="")

            self.v.config(command=self.tree.yview)

            for i in depdefaultdetails:
                self.tree.insert("", END, iid=i[1], values=(i[1], i[2], i[4], i[5], i[6], i[3]))

            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            
            self.searchbutton = Button(self.editempinfoframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_department, bd=2)
            self.searchbutton.place(x=320, y=28, height=25)

            self.backbutton = Button(self.editempinfoframe, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.payment_system_frame, bd=2)
            self.backbutton.place(x=420, y=25, height=40)
            self.clearbutton = Button(self.editempinfoframe, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen, bd=2)
            self.clearbutton.place(x=520, y=25, height=40)

            #   Bind
            self.root2.bind("<Control-f>", self.search_process_bind_function)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.back_bind_function)

        else:
           messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost") 

    #   Clear Screen
    def clear_screen(self):
        self.editdepid_var.set("")
        self.tree.delete(*self.tree.get_children())
        depdefaultdetails = department_database().department_default_details()
        for i in depdefaultdetails:
            self.tree.insert("", END, iid=i[1], values=(i[1], i[2], i[4], i[5], i[6], i[3]))
        d = [""]
        existingdeps = department_database().existing_departments()
        self.depentry.configure(values=d)
        for i in existingdeps:
            d.append(i)
        self.depentry.configure(values=d)
        self.tree.heading("#1", text="Dep id")
        self.tree.heading("#2", text="Department Name")
        self.tree.heading("#3", text="Contractor")
        self.tree.heading("#4", text="SalaryBase")
        self.tree.heading("#5", text="Makers")
        self.tree.heading("#6", text="Total")
        self.tree.heading("#7", text="")
        self.tree.heading("#8", text="")
        self.tree.heading("#9", text="")

    #   Search Dep
    def search_department(self):
        search = self.editdepid_var.get()
        if search:
            matchingdep = department_database().search_dep_details_database(search)
            alldesignations = department_database().all_designations()
            if matchingdep == False or alldesignations == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                for i in self.tree.get_children():
                    self.tree.delete(i)
                self.tree.heading("#1", text="Emp id")
                self.tree.heading("#2", text="Employee Name")
                self.tree.heading("#3", text="Short Term")
                self.tree.heading("#4", text="Long Term")
                self.tree.heading("#5", text="Work Done/Salary")
                self.tree.heading("#6", text="Pending/Absent")
                self.tree.heading("#7", text="Total")
                self.tree.heading("#8", text="Payable")
                self.tree.heading("#9", text="Contact")

                desdatabase = ""
                cb = 0
                sb = 0
                mb = 0
                self.tree.insert("", END, iid=search, values=("", search, "", "", "", "", "", "", ""))
                self.tree.insert("", END, iid="Space", values=("", "", "", "", "", "", "", "", ""))
                self.tree.insert("", END, iid="Salary", values=("", "Salary", "", "", "", "", "", "", ""))
                for k in alldesignations:
                    m = 0
                    desdatabase = k[0]
                    self.tree.insert("", END, iid=str(desdatabase)+"salary", values=("", k[0], "", "", "", "", "", "", ""))
                    for i in matchingdep:
                        if i[5] == k[0] and i[6] == "Salary":
                            emp = str(i[2])+" S/O "+str(i[3])
                            empid = i[1]
                            shortterm = 0
                            longterm = 0
                            empbalance = department_database().employe_balnce_database(empid)
                            if empbalance == False:
                                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                                break
                            else:
                                for z in empbalance:
                                    shortterm = z[0]
                                    longterm = z[1]
                                self.tree.insert("", END, iid=i[1], values=(i[1], emp, shortterm, longterm, "", "", "", "", i[4]))
                                m = m + 1
                    if m == 0:
                        self.tree.delete(str(desdatabase)+"salary")
                    else:
                        sb = sb + m
                        self.tree.set(str(desdatabase)+"salary", 1, value=(str(desdatabase)+"\t\t"+str(m)))

                if sb == 0:
                    self.tree.delete("Salary")
                else:
                    self.tree.set("Salary", 1, value=("Salary:  "+str(sb)))


                self.tree.insert("", END, iid="Space0", values=("", "", "", "", "", "", "", "", ""))
                self.tree.insert("", END, iid="Contractor", values=("", "Contractor", "", "", "", "", "", "", ""))
                for k in alldesignations:
                    m = 0
                    desdatabase = k[0]
                    self.tree.insert("", END, iid=str(desdatabase)+"contractor", values=("", k[0], "", "", "", "", "", "", ""))
                    for i in matchingdep:
                        if i[5] == k[0] and i[6] == "Contractor":
                            emp = str(i[2])+" S/O "+str(i[3])
                            empid = i[1]
                            shortterm = 0
                            longterm = 0
                            empbalance = department_database().employe_balnce_database(empid)
                            if empbalance == False:
                                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                                break
                            else:
                                for z in empbalance:
                                    shortterm = z[0]
                                    longterm = z[1]
                                self.tree.insert("", END, iid=i[1], values=(i[1], emp, shortterm, longterm, "", "", "", "", i[4]))
                                m = m + 1

                    if m == 0:
                        self.tree.delete(str(desdatabase)+"contractor")
                    else:
                        cb = cb + m
                        self.tree.set(str(desdatabase)+"contractor", 1, value=(str(desdatabase)+"\t\t"+str(m)))

                if cb == 0:
                    self.tree.delete("Contractor")
                else:
                    self.tree.set("Contractor", 1, value=("Contractor:  "+str(cb)))

                self.tree.insert("", END, iid="Space1", values=("", "", "", "", "", "", "", "", ""))
                self.tree.insert("", END, iid="Maker", values=("", "Maker", "", "", "", "", "", "", ""))
                for k in alldesignations:
                    m = 0
                    desdatabase = k[0]
                    self.tree.insert("", END, iid=str(desdatabase)+"maker", values=("", k[0], "", "", "", "", "", "", ""))
                    for i in matchingdep:
                        if i[5] == k[0] and i[6] == "Maker":
                            emp = str(i[2])+" S/O "+str(i[3])
                            empid = i[1]
                            shortterm = 0
                            longterm = 0
                            empbalance = department_database().employe_balnce_database(empid)
                            if empbalance == False:
                                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                                break
                            else:
                                for z in empbalance:
                                    shortterm = z[0]
                                    longterm = z[1]
                                self.tree.insert("", END, iid=i[1], values=(i[1], emp, shortterm, longterm, "", "", "", "", i[4]))
                                m = m + 1
                    if m == 0:
                        self.tree.delete(str(desdatabase)+"maker")
                    else:
                        mb = mb + m
                        self.tree.set(str(desdatabase)+"maker", 1, value=(str(desdatabase)+"\t\t"+str(m)))

                if mb == 0:
                    self.tree.delete("Maker")
                else:
                    self.tree.set("Maker", 1, value=("Maker:  "+str(mb)))  
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Searchbar is empty")  

    #   Search Bind
    def search_process_bind_function(self, eve):
        self.search_department()

    #   Back Bind
    def back_bind_function(self, eve):
        self.payment_system_frame()

#   Employee
class employee_class(payment_systemn):
    #   Init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)
        
    #   Employee Frame
    def add_employee_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.newempinfoframe = Frame(self.newdepinfoframemain, width=890, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe.place(x=0, y=0, height=300)
            self.editempinfoframe = Frame(self.newdepinfoframemain, width=710, bg=self.gray, bd=4, relief=FLAT)
            self.editempinfoframe.place(x=885, y=0, height=330)
            self.searchframe = Frame(self.newdepinfoframemain, width=630, bg=self.gray, bd=4, relief=FLAT)
            self.searchframe.place(x=0, y=275, height=55)
            self.newempinfoframe2 = Frame(self.newdepinfoframemain, width=890, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe2.place(x=0, y=575, height=280)

            #   DEP LABELS
            self.addnewemployeelabel = Label(self.newempinfoframe, text=" Employee Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=300, y=0)
            self.depidlabel = Label(self.newempinfoframe, text="Department:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.newempinfoframe, text="Designation:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=314, y=26)
            self.empidlabel = Label(self.newempinfoframe, text="Employee id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=12, y=61)
            self.emptypelabel = Label(self.newempinfoframe, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=318, y=61)
            self.empidlabel = Label(self.newempinfoframe, text="Employee Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=7, y=96)
            self.empidlabel = Label(self.newempinfoframe, text="Father Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=315, y=96)
            self.empidlabel = Label(self.newempinfoframe, text="C.N.I.C:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=30, y=131)
            self.empidlabel = Label(self.newempinfoframe, text="Contact No:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=318, y=131)
            self.empidlabel = Label(self.newempinfoframe, text="Address:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=23, y=166)
            self.empidlabel = Label(self.newempinfoframe, text="Salary:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=324, y=166)

            self.addnewemployeelabel = Label(self.editempinfoframe, text="Employee Incentive/Bonus", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=200, y=0)

            self.empidlabel = Label(self.searchframe, text="Search:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=30, y=7)

            self.addnewemployeelabel = Label(self.newempinfoframe2, text="Add Employee Undersupervision", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=270, y=0)
            self.depidlabel = Label(self.newempinfoframe2, text="Department:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.newempinfoframe2, text="Designation:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=314, y=26)
            self.empidlabel = Label(self.newempinfoframe2, text="Employee id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=12, y=61)
            self.emptypelabel = Label(self.newempinfoframe2, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=318, y=61)
            self.empidlabel = Label(self.newempinfoframe2, text="Employee Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=7, y=96)

            #   VARIABLES
            self.depid_var = StringVar()
            self.designation_var = StringVar()
            self.empid_var = StringVar()
            self.empnaem_var = StringVar()
            self.fathername_var = StringVar()
            self.empcnic_var = StringVar()
            self.empcell_var = StringVar()
            self.empsalary_var = StringVar()
            self.emptype_var = StringVar()
            self.empsalary_var = StringVar()
            self.editempid_var = StringVar()

            self.searchbar_var = StringVar()
            self.searchbyid_var = IntVar()

            self.underdepid_var = StringVar()
            self.underdesignation_var = StringVar()
            self.underempid_var = StringVar()
            self.undertype_var = StringVar()
            self.underempname_var = StringVar()

            newempid = employee_database().new_employee()
            existingemployees = employee_database().existing_employee()
            existinfdesignations = employee_database().all_designation_from_database()
            self.empid_var.set(newempid)
            designations = [""]
            for j in existinfdesignations:
                designations.append(j[0])

            #   Employee Details Entries
            self.depentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.depid_var, state="readonly", readonlybackground=self.white)
            self.depentry.place(x=130, y=30, height=24, width=170)
            self.designationentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.designation_var, state="readonly", readonlybackground=self.white)
            self.designationentry.place(x=440, y=30, height=24, width=170)
            self.empidentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.empid_var, state="readonly", readonlybackground=self.bgcolor, font=("Time new rooman", 9, "bold"))
            self.empidentry.place(x=130, y=65, height=24, width=170)
            self.emptypeentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.emptype_var, state="readonly", readonlybackground=self.white)
            self.emptypeentry.place(x=440, y=65, height=24, width=170)
            self.empnameentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.empnaem_var, state="readonly", readonlybackground=self.white)
            self.empnameentry.place(x=130, y=100, height=24, width=170)
            self.empnameentry.focus_set()
            self.fathernameentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.fathername_var, state="readonly", readonlybackground=self.white)
            self.fathernameentry.place(x=440, y=100, height=24, width=170)
            self.empcnicentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.empcnic_var, state="readonly", readonlybackground=self.white)
            self.empcnicentry.place(x=130, y=135, height=24, width=170)
            self.empcellentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black,textvariable=self.empcell_var, state="readonly", readonlybackground=self.white)
            self.empcellentry.place(x=440, y=135, height=24, width=170)
            self.empaddressentry = Text(self.newempinfoframe ,bd=2, font=("Time new rooman", 8),  relief=SUNKEN, bg=self.white, fg=self.black, state=DISABLED)
            self.empaddressentry.place(x=130, y=170, height=65, width=170)
            self.empsalaryentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.empsalary_var, state="readonly", readonlybackground=self.white)
            self.empsalaryentry.place(x=440, y=170, height=24, width=170)
            self.emppicentry = Text(self.newempinfoframe, font=("Time new rooman", 10, "bold"),bd=2, relief=GROOVE, bg=self.bgcolor, fg=self.black, state=DISABLED)
            self.emppicentry.place(x=625, y=30, height=200, width=250)

            self.underdepidentry = Entry(self.newempinfoframe2,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.underdepid_var, state="readonly", readonlybackground=self.white)
            self.underdepidentry.place(x=130, y=30, height=24, width=170)
            self.underdesignationentry = Entry(self.newempinfoframe2,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.underdesignation_var, state="readonly", readonlybackground=self.white)
            self.underdesignationentry.place(x=440, y=30, height=24, width=170)
            self.underempnameentry = Entry(self.newempinfoframe2,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.underempid_var, state="readonly", readonlybackground=self.white)
            self.underempnameentry.place(x=130, y=65, height=24, width=170)
            self.underemptypeentry = Entry(self.newempinfoframe2,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.undertype_var, state="readonly", readonlybackground=self.white)
            self.underemptypeentry.place(x=440, y=65, height=24, width=170)
            self.underempnameentry1 = Entry(self.newempinfoframe2,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.underempname_var, state="readonly", readonlybackground=self.white)
            self.underempnameentry1.place(x=130, y=100, height=24, width=480)
            self.emppicentry1 = Text(self.newempinfoframe2, font=("Time new rooman", 10, "bold"),bd=2, relief=GROOVE, bg=self.bgcolor, fg=self.black, state=DISABLED)
            self.emppicentry1.place(x=625, y=30, height=200, width=250)

            #   Search
            self.searchentrybar = Entry(self.searchframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchbar_var)
            self.searchentrybar.place(x=130, y=11, height=24, width=130)

            #   Radio Buttons
            self.searchbyidcheckentry = Radiobutton(self.searchframe, text="Emp-id/CNIC/Contact", variable=self.searchbyid_var, value=1, bg=self.gray)
            self.searchbyidcheckentry.place(x=260, y=9, height=30, width=160)
            self.searchbynamecheckentry = Radiobutton(self.searchframe, text="Emp Name", variable=self.searchbyid_var, value=2, bg=self.gray)
            self.searchbynamecheckentry.place(x=412, y=9, height=30, width=98)

            #   TREE
            self.v = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v.pack(side=RIGHT, fill=Y)
            self.v.place(x=1469, y=340, height=224)

            self.tree = Treeview(self.newdepinfoframemain, height=10, columns=("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"), show="headings", yscrollcommand=self.v.set)
            self.tree.place(x=1, y=340, width=1466)

            self.tree.column("#1", anchor="nw", width=80)
            self.tree.column("#2", anchor="nw", width=210)
            self.tree.column("#3", anchor="nw", width=210)
            self.tree.column("#4", anchor="nw", width=90)
            self.tree.column("#5", anchor="nw", width=90)
            self.tree.column("#6", anchor="nw", width=80)
            self.tree.column("#7", anchor="nw", width=110)
            self.tree.column("#8", anchor=CENTER, width=80)
            self.tree.column("#9", anchor="nw", width=70)
            self.tree.column("#10", anchor="nw", width=140)

            self.tree.heading("#1", text="Emp id")
            self.tree.heading("#2", text="Name")
            self.tree.heading("#3", text="Father Name")
            self.tree.heading("#4", text="CNIC")
            self.tree.heading("#5", text="Contact")
            self.tree.heading("#6", text="Category")
            self.tree.heading("#7", text="Designation")
            self.tree.heading("#8", text="Salary")
            self.tree.heading("#9", text="D/O/J")
            self.tree.heading("#10", text="Department")

            self.v.config(command=self.tree.yview)

            for k in existingemployees:
                depname = str(k[12])+" "+str(k[15])
                self.tree.insert("", END, iid=k[1], values=(k[1], k[2], k[3], k[4], k[5], k[8], k[9], k[10], k[11], depname))

            self.tree2 = Treeview(self.editempinfoframe, height=10, columns=("C1", "C2", "C3", "C4"), show="headings")
            self.tree2.place(x=0, y=30, width=600)

            self.tree2.column("#1", anchor="nw", width=20)
            self.tree2.column("#2", anchor="nw", width=200)
            self.tree2.column("#3", anchor=CENTER, width=100)
            self.tree2.column("#4", anchor=CENTER, width=80)

            self.tree2.heading("#1", text="id")
            self.tree2.heading("#2", text="Details")
            self.tree2.heading("#3", text="Amount")
            self.tree2.heading("#4", text="Added By")

            self.tree3 = Treeview(self.newdepinfoframemain, height=12, columns=("C1", "C2", "C3", "C4"), show="headings")
            self.tree3.place(x=891, y=575, width=600)

            self.tree3.column("#1", anchor="nw", width=20)
            self.tree3.column("#2", anchor="nw", width=200)
            self.tree3.column("#3", anchor=CENTER, width=100)
            self.tree3.column("#4", anchor=CENTER, width=80)

            self.tree3.heading("#1", text="Emp-id")
            self.tree3.heading("#2", text="Name")
            self.tree3.heading("#3", text="Category")
            self.tree3.heading("#4", text="Designation")

            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            
            
            self.searchbutton = Button(self.searchframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.saerch_employee, bd=2)
            self.searchbutton.place(x=520, y=11, height=25)
            self.backbutton = Button(self.editempinfoframe, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.payment_system_frame, bd=2)
            self.backbutton.place(x=250, y=260, height=40)
            self.clearbutton = Button(self.editempinfoframe, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen, bd=2)
            self.clearbutton.place(x=350, y=260, height=40)

            #   Pop Up
            self.popup = Menu(self.tree, tearoff=0)
            self.popup.add_separator()
            self.popup.add_command(label="View", command=self.view_employee)
            self.popup.add_separator()
            self.tree.bind("<Button-3>", self.do_popup_tree)

            self.popup3 = Menu(self.tree3, tearoff=0)
            self.popup3.add_separator()
            self.popup3.add_command(label="image", command=self.view_under_pic)
            self.popup3.add_separator()
            self.tree3.bind("<Button-3>", self.do_popup_tree3)

            #   Bind Function
            self.root2.bind("<Control-f>", self.search_bind_function)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.back_bind_function)
            self.root2.bind("<Control-u>", self.undersupervision_bind_function)
        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Clear Screen
    def clear_screen(self):
        self.tree.delete(*self.tree.get_children())
        self.tree2.delete(*self.tree2.get_children())
        self.tree3.delete(*self.tree3.get_children())
        
        self.searchbyid_var.set(0)
        self.depid_var.set("")
        self.designation_var.set("")
        self.empnaem_var.set("")
        self.fathername_var.set("")
        self.empcnic_var.set("")
        self.empcell_var.set("")
        self.empsalary_var.set("")
        self.emptype_var.set("")
        self.empsalary_var.set("")
        self.editempid_var.set("")
        self.searchbar_var.set("")
        self.undertype_var.set("")
        self.underdepid_var.set("")
        self.underdesignation_var.set("")
        self.underempid_var.set("")
        self.underempname_var.set("")
        self.empaddressentry.delete("1.0", END)
        self.emppicentry.config(state=NORMAL)
        self.emppicentry.delete("1.0", END)
        self.emppicentry.config(state=DISABLED)
        self.emppicentry1.config(state=NORMAL)
        self.emppicentry1.delete("1.0", END)
        self.emppicentry1.config(state=DISABLED)
        self.empnameentry.focus_set()
        existingemployees = employee_database().existing_employee()
        existinfdesignations = employee_database().all_designation_from_database()
        for k in existingemployees:
            depname = str(k[12])+" "+str(k[15])
            self.tree.insert("", END, iid=k[1], values=(k[1], k[2], k[3], k[4], k[5], k[8], k[9], k[10], k[11], depname))
        
        designations = [""]
        for j in existinfdesignations:
            designations.append(j[0])

        self.designationentry.config(values=designations)

    #   Pop Up In Tree
    def do_popup_tree(self, eve):
        r_id = self.tree.focus()
        details = self.tree.item(r_id)
        row = details['values']
        x = self.tree.selection()
        if row != '' and x:
            self.popup.selection = self.tree.set(self.tree.identify_row(eve.y))
            self.popup.post(eve.x_root, eve.y_root)
        else:
            pass

    #   View Employee
    def view_employee(self):
        a = database_class().database_connection_check()
        if a == True:
            r_id = self.tree.focus()
            details = self.tree.item(r_id)
            row = details['values']
            x = self.tree.selection()
            if row != '' and x:
                empid = x[0]
                c = employee_database().view_emp_data(empid)
                bonusinfo = employee_database().emp_bonus_data(empid)
                undersupervision = employee_database().emp_under_super(empid)
                if c == False or bonusinfo == False or undersupervision == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                elif c:
                    self.underdepid_var.set("")
                    self.underdesignation_var.set("")
                    self.underempid_var.set("")
                    self.underempname_var.set("")
                    self.undertype_var.set("")
                    self.emppicentry1.config(state=NORMAL)
                    self.emppicentry1.delete("1.0", END)
                    self.emppicentry1.config(state=DISABLED)
                    for i in self.tree3.get_children():
                        self.tree3.delete(i)

                    for i in self.tree2.get_children():
                        self.tree2.delete(i)
                    address = ""
                    dep = ""
                    emppic = ""
                    for i in c:
                        self.editempid_var.set(i[1])
                        self.empnaem_var.set(i[2])
                        self.fathername_var.set(i[3])
                        self.empcnic_var.set(i[4])
                        self.empcell_var.set(i[5])
                        address = str(i[6])
                        emppic = str(i[7])
                        self.emptype_var.set(i[8])
                        self.empsalary_var.set(i[10])
                        dep = str(i[16])+" "+str(i[17])
                        self.depid_var.set(dep)
                        self.designation_var.set(i[9])
                    
                    self.empaddressentry.delete("1.0", END)
                    self.empaddressentry.insert("1.0", address)

                    self.emppicentry.config(state=NORMAL)
                    self.emppicentry.delete("1.0", END)
                    img = ImageTk.PhotoImage(Image.open(emppic))
                    self.emppicentry.imgtk = img
                    self.emppicentry.image_create(END, image=img)
                    self.emppicentry.config(state=DISABLED)
                    self.empnameentry.focus_set()

                    if bonusinfo == "Empty":
                        pass
                    else:
                        for k in bonusinfo:
                            self.tree2.insert("", END, iid=k[0], values=(k[0], k[1], k[2], k[3]))

                    if undersupervision == "Empty":
                        pass
                    else:
                        for i in undersupervision:
                            name = str(i[2])+" S/O "+str(i[3])
                            self.tree3.insert("", END, iid=i[1], values=(i[1], name, i[4], i[5]))
        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Search EMployee
    def saerch_employee(self):
        searchbar = str(self.searchbar_var.get()).capitalize()
        searchtype = self.searchbyid_var.get()
        if searchtype == 0 or searchbar == "":
            messagebox.showwarning(parent=self.root2, title="Empty", message="Searchbar/Search type is empty")
        elif searchbar and searchtype == 1:
            existingemployees = employee_database().search_by_id(searchbar)
            if existingemployees == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif existingemployees == "Empty":
                self.clear_screen()
                messagebox.showerror(parent=self.root2, title="No Match", message="No match found")
            elif existingemployees:
                for i in self.tree.get_children():
                    self.tree.delete(i)
                for k in existingemployees:
                    depname = str(k[12])+" "+str(k[15])
                    self.tree.insert("", END, iid=k[1], values=(k[1], k[2], k[3], k[4], k[5], k[8], k[9], k[10], k[11], depname))
        elif searchbar and searchtype == 2:
            existingemployees = employee_database().existing_employee()
            result = []
            for m in self.tree.get_children():
                self.tree.delete(m)
            for i in existingemployees:
                name = str(i[2]).lower()
                if searchbar.lower() in name:
                    result.append(i)
            if result != []:
                for k in result:
                    depname = str(k[12])+" "+str(k[15])
                    self.tree.insert("", END, iid=k[1], values=(k[1], k[2], k[3], k[4], k[5], k[8], k[9], k[10], k[11], depname))
            else:
                self.clear_screen()

    #   Search Bind
    def search_bind_function(self, eve):
        self.searchentrybar.focus_set()
        self.saerch_employee()

    #   Back Bind
    def back_bind_function(self, eve):
        self.payment_system_frame()

    #   Undersupervision bind
    def undersupervision_bind_function(self, eve):
        self.save_under_supervision()

    #   Pop Up In Tree2
    def do_popup_tree3(self, eve):
        r_id = self.tree3.focus()
        details = self.tree3.item(r_id)
        row = details['values']
        x = self.tree3.selection()
        if row != '' and x:
            self.popup3.selection = self.tree3.set(self.tree3.identify_row(eve.y))
            self.popup3.post(eve.x_root, eve.y_root)
        else:
            pass

    #   Under Supervision pic
    def view_under_pic(self):
        a = database_class().database_connection_check()
        if a == True:
            r_id = self.tree3.focus()
            details = self.tree3.item(r_id)
            row = details['values']
            x = self.tree3.selection()
            if row != '' and x:
                empid = str(row[0])
                self.underdepid_var.set("")
                self.underdesignation_var.set("")
                self.underempid_var.set("")
                self.underempname_var.set("")
                self.undertype_var.set("")
                self.emppicentry1.config(state=NORMAL)
                self.emppicentry1.delete("1.0", END)
                self.emppicentry1.config(state=DISABLED)
                empname = ""
                designation = ""
                dep = ""
                empic = ""
                emptypee = ""
                viewempdata = employee_database().view_emp_data(empid)
                for i in viewempdata:
                    empname = str(i[2])+" S/O "+str(i[3])
                    designation = i[9]
                    dep = str(i[12]+" "+str(i[17]))
                    emptypee = str(i[8])
                    empic = str(i[7])
                
                self.underdepid_var.set(dep)
                self.underdesignation_var.set(designation)
                self.underempid_var.set(empid)
                self.underempname_var.set(empname)
                self.undertype_var.set(emptypee)
                self.emppicentry1.config(state=NORMAL)
                self.emppicentry1.delete("1.0", END)
                img = ImageTk.PhotoImage(Image.open(empic))
                self.emppicentry1.imgtk = img
                self.emppicentry1.image_create(END, image=img)
                self.emppicentry1.config(state=DISABLED)
            else:
                pass
        else:
           messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

#   Employee Ledger
class employee_ledger_class(payment_systemn):
    #   Init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)

    #   Employee Ledger Frame
    def employee_ledger_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.newempinfoframe = Frame(self.newdepinfoframemain, width=890, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe.place(x=0, y=0, height=300)
            self.searchframe = Frame(self.newdepinfoframemain, width=890, bg=self.gray, bd=4, relief=FLAT)
            self.searchframe.place(x=0, y=250, height=55)
            self.editempinfoframe = Frame(self.newdepinfoframemain, width=710, bg=self.gray, bd=4, relief=FLAT)
            self.editempinfoframe.place(x=891, y=0, height=70)
            self.newempinfoframe1 = Frame(self.newdepinfoframemain, width=890, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe1.place(x=0, y=535, height=300)
            self.editempinfoframe1 = Frame(self.newdepinfoframemain, width=710, bg=self.gray, bd=4, relief=FLAT)
            self.editempinfoframe1.place(x=891, y=71, height=200)
            
            #   DEP LABELS
            self.addnewemployeelabel = Label(self.newempinfoframe, text=" Employee Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=300, y=0)
            self.depidlabel = Label(self.newempinfoframe, text="Department:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.newempinfoframe, text="Designation:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=314, y=26)
            self.empidlabel = Label(self.newempinfoframe, text="Employee id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=12, y=61)
            self.emptypelabel = Label(self.newempinfoframe, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=318, y=61)
            self.empidlabel = Label(self.newempinfoframe, text="Employee Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=7, y=96)
            self.empidlabel = Label(self.newempinfoframe, text="Father Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=315, y=96)
            self.empidlabel = Label(self.newempinfoframe, text="C.N.I.C:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=30, y=131)
            self.empidlabel = Label(self.newempinfoframe, text="Contact No:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=318, y=131)
            self.empidlabel = Label(self.newempinfoframe, text="Address:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=23, y=166)
            self.empidlabel = Label(self.newempinfoframe, text="Salary:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=324, y=166)

            self.addnewemployeelabel = Label(self.editempinfoframe, text=" Balance Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=200, y=0)
            self.depidlabel = Label(self.editempinfoframe, text="Short Term:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.editempinfoframe, text="Long Term:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=308, y=26)

            self.addnewemployeelabel = Label(self.editempinfoframe1, text="Last Transaction Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=170, y=0)
            self.depidlabel = Label(self.editempinfoframe1, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.editempinfoframe1, text="Transaction Type:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=298, y=26)
            self.depidlabel = Label(self.editempinfoframe1, text="Description:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=61)
            self.empidlabel = Label(self.editempinfoframe1, text="Amount:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=18, y=96)
            self.empidlabel = Label(self.editempinfoframe1, text="Date:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=320, y=96)

            self.addnewemployeelabel = Label(self.newempinfoframe1, text="New Transaction Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=305, y=0)
            self.depidlabel = Label(self.newempinfoframe1, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.newempinfoframe1, text="Transaction Type:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=308, y=26)
            self.depidlabel = Label(self.newempinfoframe1, text="Description:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=61)
            self.empidlabel = Label(self.newempinfoframe1, text="Amount:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=18, y=96)


            self.empidlabel = Label(self.searchframe, text="Search:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=30, y=7)
            self.empidlabel = Label(self.searchframe, text="From:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=380, y=7)
            self.empidlabel = Label(self.searchframe, text="To:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=535, y=7)

            #   Variable
            self.depid_var = StringVar()
            self.designation_var = StringVar()
            self.empid_var = StringVar()
            self.emptype_var = StringVar()
            self.empnaem_var = StringVar()
            self.fathername_var = StringVar()
            self.empcnic_var = StringVar()
            self.empcell_var = StringVar()
            self.empcell_var = StringVar()
            self.empsalary_var = StringVar()
            self.searchbar_var = StringVar()

            self.shortterm_var = StringVar()
            self.longterm_var = StringVar()

            self.term_var = StringVar()
            self.trasactiontype_var = StringVar()
            self.amountdescription_var = StringVar()
            self.amount_var = StringVar()

            self.lastterm_var = StringVar()
            self.lasttrasactiontype_var = StringVar()
            self.lastamountdescription_var = StringVar()
            self.lastamount_var = StringVar()
            self.lastdate_var = StringVar()

            self.selection_var = StringVar()

            term = ["", "Short Term", "Long Term"]
            typeofamount = ["", "Credit", "Debit"]

            #   Employee Details Entries
            self.depentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.depid_var, state="readonly", readonlybackground=self.white)
            self.depentry.place(x=130, y=30, height=24, width=170)
            self.designationentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.designation_var, state="readonly", readonlybackground=self.white)
            self.designationentry.place(x=440, y=30, height=24, width=170)
            self.empidentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.empid_var, state="readonly", readonlybackground=self.white, font=("Time new rooman", 9, "bold"))
            self.empidentry.place(x=130, y=65, height=24, width=170)
            self.emptypeentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.emptype_var, state="readonly", readonlybackground=self.white)
            self.emptypeentry.place(x=440, y=65, height=24, width=170)
            self.empnameentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.empnaem_var, state="readonly", readonlybackground=self.white)
            self.empnameentry.place(x=130, y=100, height=24, width=170)
            self.empnameentry.focus_set()
            self.fathernameentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.fathername_var, state="readonly", readonlybackground=self.white)
            self.fathernameentry.place(x=440, y=100, height=24, width=170)
            self.empcnicentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.empcnic_var, state="readonly", readonlybackground=self.white)
            self.empcnicentry.place(x=130, y=135, height=24, width=170)
            self.empcellentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black,textvariable=self.empcell_var, state="readonly", readonlybackground=self.white)
            self.empcellentry.place(x=440, y=135, height=24, width=170)
            self.empaddressentry = Text(self.newempinfoframe ,bd=2, font=("Time new rooman", 8),  relief=SUNKEN, bg=self.white, fg=self.black, state=DISABLED)
            self.empaddressentry.place(x=130, y=170, height=65, width=170)
            self.empsalaryentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.empsalary_var, state="readonly", readonlybackground=self.white)
            self.empsalaryentry.place(x=440, y=170, height=24, width=170)
            self.emppicentry = Text(self.newempinfoframe, font=("Time new rooman", 10, "bold"),bd=2, relief=GROOVE, bg=self.bgcolor, fg=self.black, state=DISABLED)
            self.emppicentry.place(x=625, y=30, height=200, width=250)
            self.shorttermentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.shortterm_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.white)
            self.shorttermentry.place(x=115, y=30, height=24, width=170)
            self.longtermentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.longterm_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.white)
            self.longtermentry.place(x=420, y=30, height=24, width=170)

            self.lastcategoryentry = Entry(self.editempinfoframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.lastterm_var, state="readonly", readonlybackground=self.white)
            self.lastcategoryentry.place(x=115, y=30, height=24, width=170)
            self.lasttransactionentry = Entry(self.editempinfoframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.lasttrasactiontype_var, state="readonly", readonlybackground=self.white)
            self.lasttransactionentry.place(x=420, y=30, height=24, width=170)
            self.lastdescriptionentry = Entry(self.editempinfoframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.lastamountdescription_var, state="readonly", readonlybackground=self.white)
            self.lastdescriptionentry.place(x=115, y=65, height=24, width=478)
            self.lastamountentry = Entry(self.editempinfoframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, font=("Time new rooman", 9, "bold"), textvariable=self.lastamount_var, state="readonly", readonlybackground=self.white)
            self.lastamountentry.place(x=115, y=100, height=24, width=170)
            self.lastamountdateentry = Entry(self.editempinfoframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, font=("Time new rooman", 9, "bold"), textvariable=self.lastdate_var, state="readonly", readonlybackground=self.white)
            self.lastamountdateentry.place(x=420, y=100, height=24, width=170)
            
            self.categoryentry = Combobox(self.newempinfoframe1, values=term, textvariable=self.term_var,  state="readonly")
            self.categoryentry.place(x=130, y=30, height=24, width=170)
            self.transactionentry = Combobox(self.newempinfoframe1, values=typeofamount, textvariable=self.trasactiontype_var,  state="readonly")
            self.transactionentry.place(x=440, y=30, height=24, width=170)
            self.descriptionentry = Entry(self.newempinfoframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.amountdescription_var)
            self.descriptionentry.place(x=130, y=65, height=24, width=480)
            self.amountentry = Entry(self.newempinfoframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, font=("Time new rooman", 9, "bold"), textvariable=self.amount_var)
            self.amountentry.place(x=130, y=100, height=24, width=170)

            #   Search
            self.searchentrybar = Entry(self.searchframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchbar_var)
            self.searchentrybar.place(x=130, y=11, height=24, width=130)
            self.searchentrybar.focus_set()

            #   Date Entry
            y = int(self.current_year())
            self.fromdateentry = DateEntry(self.searchframe, values="Text", year=y, date_pattern="yyyy-mm-dd", bd=2, state="readonly")
            self.fromdateentry.place(x=440, y=11, height=24, width=85)
            self.todateentry = DateEntry(self.searchframe, values="Text", year=y, date_pattern="yyyy-mm-dd", bd=2, state="readonly")
            self.todateentry.place(x=575, y=11, height=24, width=85)
            self.selectionentry = Combobox(self.searchframe, values=term, textvariable=self.selection_var,  state="readonly")
            self.selectionentry.place(x=668, y=11, height=24, width=115)

            #   TREE
            self.v = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v.pack(side=RIGHT, fill=Y)
            self.v.place(x=1469, y=300, height=224)

            self.tree = Treeview(self.newdepinfoframemain, height=10, columns=("C1", "C2", "C3", "C4", "C5", "C6", "C7"), show="headings", yscrollcommand=self.v.set)
            self.tree.place(x=1, y=300, width=1466)

            self.tree.column("#1", anchor="nw", width=90)
            self.tree.column("#2", anchor="nw", width=460)
            self.tree.column("#3", anchor=CENTER, width=60)
            self.tree.column("#4", anchor=CENTER, width=60)
            self.tree.column("#5", anchor=CENTER, width=60)
            self.tree.column("#6", anchor=CENTER, width=60)
            self.tree.column("#7", anchor=CENTER, width=80)

            self.tree.heading("#1", text="Date/Time")
            self.tree.heading("#2", text="Description")
            self.tree.heading("#3", text="Credit")
            self.tree.heading("#4", text="Debit")
            self.tree.heading("#5", text="Balance")
            self.tree.heading("#6", text="Category")
            self.tree.heading("#7", text="User")

            self.v.config(command=self.tree.yview)

            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            self.saveicon = ImageTk.PhotoImage(self.saveiconphoto)

            self.searchbutton = Button(self.searchframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.saerch_employee, bd=2)
            self.searchbutton.place(x=270, y=11, height=25)
            self.searchbutton1 = Button(self.searchframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_emp_balance_datewise, bd=2)
            self.searchbutton1.place(x=810, y=11, height=25)

            self.savebutton = Button(self.newempinfoframe1, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_new_credit_debit, bd=2)
            self.savebutton.place(x=330, y=100, height=40)
            self.backbutton = Button(self.editempinfoframe1, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.payment_system_frame, bd=2)
            self.backbutton.place(x=150, y=131, height=40)
            self.clearbutton = Button(self.editempinfoframe1, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen1, bd=2)
            self.clearbutton.place(x=250, y=131, height=40)

            #   Bind
            self.root2.bind("<Control-f>", self.search_bind_function)
            self.root2.bind("<Alt-f>", self.search_datewise_bind_function)
            self.root2.bind("<Control-s>", self.save_bind_function)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.back_bind_function)
        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
        
    #   Clear Screen 
    def clear_screen1(self):
        self.searchentrybar.focus_set()
        self.empid_var.set("")
        self.searchbar_var.set("")
        self.clear_screen()

    #   Clear Screen
    def clear_screen(self):
        self.depid_var.set("")
        self.designation_var.set("")
        self.empnaem_var.set("")
        self.fathername_var.set("")
        self.empcnic_var.set("")
        self.empcell_var.set("")
        self.empsalary_var.set("")
        self.emptype_var.set("")
        self.empsalary_var.set("")
        self.empaddressentry.config(state=NORMAL)
        self.empaddressentry.delete("1.0", END)
        self.empaddressentry.config(state=DISABLED)
        self.emppicentry.config(state=NORMAL)
        self.emppicentry.delete("1.0", END)
        self.emppicentry.config(state=DISABLED)
        self.shortterm_var.set("")
        self.longterm_var.set("")
        self.term_var.set("")
        self.trasactiontype_var.set("")
        self.amountdescription_var.set("")
        self.amount_var.set("")
        self.selection_var.set("")
        self.tree.delete(*self.tree.get_children())
        self.lastterm_var.set("")
        self.lasttrasactiontype_var.set("")
        self.lastamountdescription_var.set("")
        self.lastamount_var.set("")
        self.lastdate_var.set("")

    #   Search EMployee
    def saerch_employee(self):
        searchbar = self.searchbar_var.get()
        if searchbar:
            existingemployees = employee_database().search_by_id(searchbar)
            if existingemployees == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif existingemployees == "Empty":
                messagebox.showerror(parent=self.root2, title="No Match", message="No match found")
            elif existingemployees:
                self.clear_screen()
                empid = ""
                empname = ""
                fathername = ""
                cnic = ""
                cell = ""
                address = ""
                emppic = ""
                category = ""
                designation = ""
                salary = ""
                depname = ""
                shortterm = ""
                longterm = ""
                for i in existingemployees:
                    empid = i[1]
                    empname = i[2]
                    fathername = i[3]
                    cnic = i[4]
                    cell = i[5]
                    address = i[6]
                    emppic = i[7]
                    category = i[8]
                    designation = i[9]
                    salary = i[10]
                    depname = str(i[12])+" "+str(i[15])

                if empid:
                    self.empid_var.set(empid)
                    self.empnaem_var.set(empname)
                    self.fathername_var.set(fathername)
                    self.empcnic_var.set(cnic)
                    self.empcell_var.set(cell)
                    self.emptype_var.set(category)
                    self.designation_var.set(designation)
                    self.empsalary_var.set(salary)
                    self.depid_var.set(depname)
                    
                    self.empaddressentry.config(state=NORMAL)
                    self.empaddressentry.delete("1.0", END)
                    self.empaddressentry.insert("1.0", address)
                    self.empaddressentry.config(state=DISABLED)
                    
                    self.emppicentry.config(state=NORMAL)
                    self.emppicentry.delete("1.0", END)
                    img = ImageTk.PhotoImage(Image.open(emppic))
                    self.emppicentry.imgtk = img
                    self.emppicentry.image_create(END, image=img)
                    self.emppicentry.config(state=DISABLED)

                    empbalance = department_database().employe_balnce_database(empid)
                    lasttransaction = employee_ledger_database().last_transaction_details_database(empid)
                    if empbalance == False or lasttransaction == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    else:
                        for z in empbalance:
                            shortterm = z[0]
                            longterm = z[1]
                        self.shortterm_var.set(shortterm)
                        self.longterm_var.set(longterm)

                        for j in lasttransaction:
                            addeddate = str(j[4])+" / "+str(j[5])
                            amount = str(j[2])
                            name = str(j[3])
                            typetra = str(j[6])
                            tcategory = str(j[7])

                            self.lastdate_var.set(addeddate)
                            self.lastamount_var.set(amount)
                            self.lastamountdescription_var.set(name)
                            self.lastterm_var.set(typetra)
                            self.lasttrasactiontype_var.set(tcategory)
                else:
                    pass

    #   Save Credit/Debit
    def save_new_credit_debit(self):
        empid = self.empid_var.get()
        amount = self.amount_var.get()
        name = str(self.amountdescription_var.get()).capitalize()
        currentdate = self.current_date()
        currenttime = self.current_time()
        amountcategory = self.term_var.get()
        amounttermtype = self.trasactiontype_var.get()
        username = self.username
        if empid and amount and name:
            if amount.isdigit() == True:
                if int(amount) > 0:
                    n = username.split("-")
                    userid = n[0]
                    savenewamountbalance = employee_ledger_database().save_new_credit_debit_database(empid, amount, name, currentdate, currenttime, amountcategory, amounttermtype, userid)
                    if savenewamountbalance == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif savenewamountbalance == "Empty":
                        messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
                    elif savenewamountbalance == "Save":
                        self.searchbar_var.set(empid)
                        messagebox.showinfo(parent=self.root2, title="Saved", message=str(amountcategory)+" "+str(amounttermtype)+"   has been saved")
                        self.saerch_employee()
                else:
                    messagebox.showwarning(parent=self.root2, title="Credit/Debit", message="Credit/Debit amount must be greater than 0")
            else:
                messagebox.showwarning(parent=self.root2, title="Credit/Debit", message="Credit/Debit amount must be int")
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")

    #   Search Datewise Employee Balance
    def search_emp_balance_datewise(self):
        startdate = self.fromdateentry.get_date()
        enddate =  self.todateentry.get_date()
        empid = self.empid_var.get()
        selection = self.selection_var.get()
        if startdate > enddate:
            messagebox.showerror(parent=self.root2, title="invalid date", message="Start date can't be greater than end date")
        elif empid == "" and selection == "":
            messagebox.showwarning(parent=self.root2, title="Empty", message="Employee details are empty")
        elif empid and startdate <= enddate and selection:
            self.tree.delete(*self.tree.get_children())
            allbalancedetails = employee_ledger_database().given_date_opening_balance_database(empid, selection ,startdate)
            balancedetails = employee_ledger_database().employee_balance_details_database(empid, startdate, enddate, selection)
            print(balancedetails)
            print(allbalancedetails)
            if balancedetails == False or allbalancedetails == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif balancedetails == [] and allbalancedetails == []:
                pass
            elif balancedetails != [] and allbalancedetails != []:
                credit = 0
                debit = 0
                opening_balance = 0
                transactions_details = []
                for i in allbalancedetails:
                    opening_balance = i[0]

                for j in balancedetails:
                    if j[7] == "Credit":
                        credit = j[2]
                        debit = 0

                    elif j[7] == "Debit":
                        debit = j[2]
                        credit = 0
                    else:
                        pass

                    transactions_details.append({
                        "id" : j[0],
                        "datetime" : str(j[4])+" / "+str(j[5]),
                        "credit" : credit,
                        "debit" : debit,
                        "category" : j[7],
                        "username" : str(j[8])+"-"+str(j[9]),
                        "name" : j[3]
                        })
                    
                if transactions_details == []:
                    pass
                else:
                    self.tree.insert("", END, iid="datefrom", values=("", "From:  "+str(startdate)+"  To:  "+str(enddate), "", "", "", "", ""))
                    self.tree.insert("", END, iid="opening_balance", values=("", "Opening Balance", "", "", opening_balance, "", ""))

                    for i in transactions_details:
                        idno = i["id"]
                        datetime = i['datetime']
                        creditamounts = i['credit']
                        debitamounts = i['debit']
                        categorydetails = i['category']
                        username = i['username']
                        namedetails = i['name']
                        if creditamounts == 0:
                            opening_balance = opening_balance + debitamounts
                            self.tree.insert("", END, iid=idno, values=(datetime, namedetails, "", debitamounts, opening_balance, categorydetails, username))
                        elif debitamounts == 0:
                            opening_balance = opening_balance - creditamounts
                            self.tree.insert("", END, iid=idno, values=(datetime, namedetails, creditamounts, "", opening_balance, categorydetails, username))
                        else:
                            pass

    #   Search datawise bind
    def search_datewise_bind_function(self, eve):
        self.search_emp_balance_datewise()

    #   Search Bind
    def search_bind_function(self, eve):
        self.searchentrybar.focus_set()
        self.saerch_employee()

    #   Back Bind
    def back_bind_function(self, eve):
        self.payment_system_frame()

    #   Save bind
    def save_bind_function(self, eve):
        self.categoryentry.focus_set()
        self.save_new_credit_debit()












