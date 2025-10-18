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
import textwrap
from fpdf import FPDF
import platform

#   Director Class
class director_class:
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
            #self.root.attributes("-disabled", True)
            self.root2 = Toplevel(self.root)
            self.root2.geometry("1500x885")
            self.appiconphoto = Image.open("img/icon.png")
            icon_photo = ImageTk.PhotoImage(self.appiconphoto)
            self.root2.resizable(False, False)
            self.root2.iconphoto(False, icon_photo)
            
            self.root2.title("Littlewood Corporation(pvt) - ERP -  User: "+str(self.username))

            self.style = ttkthemes.ThemedStyle(self.root2)
            self.style.theme_use('vista')
            self.style.configure('Treeview', foreground=self.black, background=self.white, fieldbackground=self.white)
            self.style.configure('Treeview.Heading', foreground=self.black, background=self.powderblue)
            self.style.map('Treeview', background=[('selected', self.powderblue)], foreground=[('selected', self.black)])
            self.style.map('Treeview.Heading', background=[('selected', self.white)], foreground=[('selected', self.black)])
            
            self.menubar = Menu(self.root2, tearoff=1)
            self.menubar.add_command(label="Log Out", command=self.logout)
            self.root2.config(menu=self.menubar)
            self.root2.protocol("WM_DELETE_WINDOW", self.logout)

            self.director_frame()
        else:
            messagebox.showerror(parent=self.root,title="Server Respone", message="Database connection lost")

    #   director class
    def director_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            self.root2backgroundphoto = Image.open("img/background.png")
            self.depiconphoto = Image.open("img/dep_icon.png")
            self.empiconphoto = Image.open("img/emp_icon.png")
            self.ordericonphoto = Image.open("img/order_icon.png")
            self.orderrateiconphoto = Image.open("img/rate.png")
            self.requesticonphoto = Image.open("img/request_icon.png")
            self.storeiconphoto = Image.open("img/inventory_icon.png")
            self.avgiconphoto =  Image.open("img/avg_icon.png")
            self.productioniconphoto = Image.open("img/production_icon.png")
            self.storeiconphoto1 = Image.open("img/store_icon.png")
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

            #   Order Button
            self.ordericon = ImageTk.PhotoImage(self.ordericonphoto)
            self.addorderbutton = Button(self.blankhomeframe, width=130, text="Order\nDetails", font=("Time new rooman", 9, "bold", "italic"), image=self.ordericon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=order_class(self.root2, self.username, self.root).add_order_frame)
            self.addorderbutton.place(x=290, y=2, height=65)

            #   Order Rate Button
            self.orderrateicon = ImageTk.PhotoImage(self.orderrateiconphoto)
            self.orderratebutton = Button(self.blankhomeframe, width=130, text="Order\nRate/Process", font=("Time new rooman", 9, "bold", "italic"), image=self.orderrateicon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=order_rate_and_process(self.root2, self.username, self.root).order_rate_frame)
            self.orderratebutton.place(x=430, y=2, height=65)

            #   Requisition Button
            self.requesticon = ImageTk.PhotoImage(self.requesticonphoto)
            self.requestbutton = Button(self.blankhomeframe, width=130, text="Requisition", font=("Time new rooman", 9, "bold", "italic"), image=self.requesticon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=requsition_class(self.root2, self.username, self.root).requisition_frame)
            self.requestbutton.place(x=570, y=2, height=65)

            #   Inventory Data
            self.storeicon = ImageTk.PhotoImage(self.storeiconphoto)
            self.storebutton = Button(self.blankhomeframe, width=130,  text="Raw\nMaterial",font=("Time new rooman", 9, "bold", "italic"), image=self.storeicon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=raw_material_class(self.root2, self.username, self.root).raw_material_frame)
            self.storebutton.place(x=710, y=2, height=65)

            #   Average Button
            self.avgicon = ImageTk.PhotoImage(self.avgiconphoto)
            self.avgbutton = Button(self.blankhomeframe, width=130,  text="Material\nfor\nOrder",font=("Time new rooman", 9, "bold", "italic"), image=self.avgicon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=order_stimated_avg(self.root2, self.username, self.root).order_estimated_avg_frame)
            self.avgbutton.place(x=850, y=2, height=65)

            #   Production Details
            self.productionicon = ImageTk.PhotoImage(self.productioniconphoto)
            self.productiondetailsbutton = Button(self.blankhomeframe, width=130,  text="Production\nDetails",font=("Time new rooman", 9, "bold", "italic"), image=self.productionicon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=production_dep_details(self.root2, self.username, self.root).production_details_frame)
            self.productiondetailsbutton.place(x=990, y=2, height=65)

            #   Store Details
            self.storeicon1 = ImageTk.PhotoImage(self.storeiconphoto1)
            self.storebutton = Button(self.blankhomeframe, width=130,  text="Material\nStore",font=("Time new rooman", 9, "bold", "italic"), image=self.storeicon1, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=store_stock_details(self.root2, self.username, self.root).stock_details_frame)
            self.storebutton.place(x=1130, y=2, height=65)

            #   Employee Ledger
            self.ledgericon = ImageTk.PhotoImage(self.ledgericonphoto)
            self.ledgerempbutton = Button(self.blankhomeframe, width=130, text="Employee\nLedger", font=("Time new rooman", 9, "bold", "italic"), image=self.ledgericon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=employee_ledger_class(self.root2, self.username, self.root).employee_ledger_frame)
            self.ledgerempbutton.place(x=10, y=68, height=65)

            #   Save/Edit Order
            self.root2.bind("<Control-s>", self.bind_clear)
            self.root2.bind("<Alt-s>", self.bind_clear)
            self.root2.bind("<Control-e>", self.bind_clear)
            self.root2.bind("<Alt-a>", self.bind_clear)
            self.root2.bind("<Control-f>", self.bind_clear)
            self.root2.bind("<Control-b>", self.bind_clear)
            self.root2.bind("<Alt-b>", self.bind_clear)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.bind_clear)
            self.root2.bind("<Control-u>", self.bind_clear)
            self.root2.bind("<Control-p>", self.bind_clear)
        else:
           messagebox.showerror(parent=self.root,title="Server Respone", message="Database connection lost")

    #   Log Out
    def logout(self):
        self.root2.withdraw()
        self.root.deiconify()
    
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
class departments_class(director_class):
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
            self.newempinfoframe = Frame(self.newdepinfoframemain, width=835, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe.place(x=0, y=0, height=70)
            self.editempinfoframe = Frame(self.newdepinfoframemain, width=710, bg=self.gray, bd=4, relief=FLAT)
            self.editempinfoframe.place(x=836, y=0, height=70)

            #   DEP LABELS
            self.addnewemployeelabel = Label(self.newempinfoframe, text="New Department Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=300, y=0)
            self.depnamelabel = Label(self.newempinfoframe, text="Department Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=309, y=26)
            self.depidlabel = Label(self.newempinfoframe, text="Department:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=8, y=26)

            existingdeps = department_database().existing_departments()
            
            #   Variables
            self.depid_var = StringVar()
            self.depname_var = StringVar()
            self.editdepid_var = StringVar()

            d = [""]
            for i in existingdeps:
                d.append(i)

            #   Entry
            self.fathernameentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.depname_var)
            self.fathernameentry.place(x=440, y=30, height=24, width=170)
            self.fathernameentry.focus_set()
            self.depentry = Combobox(self.newempinfoframe, values=d, textvariable=self.editdepid_var,  state="readonly")
            self.depentry.place(x=130, y=30, height=24, width=170)

            #   TREE
            self.v = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v.pack(side=RIGHT, fill=Y)
            self.v.place(x=1469, y=75, height=373)

            self.tree = Treeview(self.newdepinfoframemain, height=19, columns=("C1","C2","C3","C4","C5","C6", "C7", "C8", "C9"), show="tree", yscrollcommand=self.v.set)
            self.tree.place(x=1, y=75, width=1466)
             
            self.tree.column("#0", width=200)

            self.tree.column("#1", width=50)
            self.tree.column("#2", width=310)
            self.tree.column("#3", width=75)
            self.tree.column("#4", width=80)
            self.tree.column("#5", width=80)
            self.tree.column("#6", width=80)
            self.tree.column("#7", width=80)
            self.tree.column("#8", width=80)
            self.tree.column("#9", width=80)
            
            self.v.config(command=self.tree.yview)
            
            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.saveicon = ImageTk.PhotoImage(self.saveiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.addimageicon = ImageTk.PhotoImage(self.addimageiconphoto)
            self.editicon = ImageTk.PhotoImage(self.editiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            self.printicon = ImageTk.PhotoImage(self.printiconphoto)

            self.savebutton = Button(self.newempinfoframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_department, bd=2)
            self.savebutton.place(x=630, y=22, height=40)
            self.editbutton = Button(self.newempinfoframe, width=74, text="Edit", font=("Time new rooman", 9, "bold", "italic"), image=self.editicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.editing_save, bd=2)
            self.editbutton.place(x=730, y=22, height=41)

            self.backbutton = Button(self.editempinfoframe, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.director_frame, bd=2)
            self.backbutton.place(x=320, y=25, height=40)
            self.clearbutton = Button(self.editempinfoframe, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen, bd=2)
            self.clearbutton.place(x=420, y=25, height=40)
            self.printbutton = Button(self.editempinfoframe, width=73, text="Print", font=("Time new rooman", 9, "bold", "italic"), image=self.printicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.print_out, bd=2)
            self.printbutton.place(x=520, y=25, height=40)


            #   Bind
            self.root2.bind("<Control-s>", self.save_process_bind_function)
            self.root2.bind("<Alt-s>", self.edit_process_bind_function)
            self.root2.bind("<Control-f>", self.search_process_bind_function)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.back_bind_function)

            self.search_department()

            #   Pop Up
            self.popup = Menu(self.tree, tearoff=0)
            self.popup.add_separator()
            self.popup.add_command(label="Print selected", command=self.selected_department_printout)
            self.popup.add_separator()
            self.tree.bind("<Button-3>", self.do_popup_tree)

        else:
           messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost") 

    #   Save Department
    def save_department(self):
        depname = (self.depname_var.get()).capitalize()
        if depname == "":
            messagebox.showwarning(parent=self.root2, title="Empty", message="Reuired fields are empty")
        elif depname:
            savedepartment = department_database().save_new_department(depname)
            if savedepartment == "Save":
                self.clear_screen()
                messagebox.showinfo(parent=self.root2, title="Saved", message="New department has been added")
            elif savedepartment == "Empty":
               messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
            elif savedepartment == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
    
    #   Edit Department
    def editing_save(self):
        depid = self.editdepid_var.get()
        depname = (self.depname_var.get()).capitalize()
        if depid == "" or depname == "":
            messagebox.showwarning(parent=self.root2, title="Empty", message="Reuired fields are empty")
        elif depid and depname:
            savedepartment = department_database().save_editing_department_database(depid, depname)
            if savedepartment == "Save":
                self.clear_screen()
                messagebox.showinfo(parent=self.root2, title="Edit", message="Department has been editted")
            elif savedepartment == "Empty":
               messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
            elif savedepartment == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Clear Screen
    def clear_screen(self):
        self.depname_var.set("")
        self.editdepid_var.set("")
        self.tree.delete(*self.tree.get_children())
        d = [""]
        existingdeps = department_database().existing_departments()
        self.depentry.configure(values=d)
        for i in existingdeps:
            d.append(i)
        self.depentry.configure(values=d)
        self.search_department()

    #   Search Dep
    def search_department(self):
        depdefaultdetails = department_database().department_default_details()
        alldesignations = department_database().all_designations()
        deps = []
        if depdefaultdetails == False or alldesignations == False:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
        elif depdefaultdetails == []:
            pass
        elif depdefaultdetails != []:
            for i in depdefaultdetails:                
                depid = i[1]
                deptreeid = "department-"+str(depid)
                heading = str(i[1])+" "+str(i[2])
                parent = self.tree.insert("", END, iid=deptreeid, text=(heading), values=("", "", "", "", "", ""))
                
                contractortreeidfortype = "Contractor"+str(depid)
                salarybasetreeidfortype = "Salarybase"+str(depid)
                makertreeidfortype = "Maker"+str(depid)
                
                parent2 = self.tree.insert(parent, END, iid=contractortreeidfortype, text=("Contractor"), values=("Emp-id", "Name", "Contact", "Salary", "Short term", "Long term", "Clear", "Work in-hand", "Payable"))
                parent3 = self.tree.insert(parent, END, iid=salarybasetreeidfortype, text=("Salary"), values=("Emp-id", "Name", "Contact", "Salary", "Short term", "Long term", "Clear", "", "Payable"))
                parent4 = self.tree.insert(parent, END, iid=makertreeidfortype, text=("Maker"), values=("Emp-id", "Name", "Contact", "Salary", "Short term", "Long term", "Clear", "Work in-hand", "Payable"))

                totalcontractor = 0
                totalsalary = 0
                totalmaker = 0 

                matchingdep = department_database().search_dep_details_database(depid)
                if matchingdep == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                elif matchingdep == []:
                    pass
                elif matchingdep != []:
                    for b in matchingdep:
                        empid = b[1]
                        empbalance = department_database().employe_balnce_database(empid)
                        for z in empbalance:
                            shortterm = z[0]
                            longterm = z[1]
                        if b[6] == "Contractor":
                            emptreeid = b[1]
                            empname = str(b[2])+" S/O "+str(b[3])
                            totalcontractor = totalcontractor + 1
                            clearworktotal = 0
                            unclearwoktotal = 0
                            contractorworkinhand = employee_receord_database().contractor_clearwork_database(empid)
                            if contractorworkinhand == False:
                                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                            elif contractorworkinhand == []:
                                self.tree.insert(parent2, END, iid=emptreeid, value=(b[1], empname, b[4], "", shortterm, longterm, clearworktotal, unclearwoktotal, 0, 0))
                            elif contractorworkinhand != []:
                                subpro = ""
                                totalofrate = 0
                                totalofqty = 0
                                totalofclear = 0
                                for work in contractorworkinhand:
                                    if work[0] == None:
                                        clearworktotal = clearworktotal + 0
                                    else:
                                        clearqty = work[4]
                                        prorate = work[3]
                                        clear = prorate * clearqty
                                        clearworktotal = clearworktotal + clear
                                        totalofqty = totalofqty + work[1]
                                        totalofclear = totalofclear + clearqty
                                        if subpro == "" or subpro != work[0]:
                                            totalofrate = totalofrate + prorate
                                            subpro = work[0]
                                        else:
                                            pass
                                remainqty = totalofqty - totalofclear
                                uncleart = totalofrate * remainqty
                                payable = int(clearworktotal) - int(shortterm)
                                
                                self.tree.insert(parent2, END, iid=emptreeid, value=(b[1], empname, b[4], "", shortterm, longterm, clearworktotal, uncleart, payable))

                        elif b[6] == "Salary":
                            emptreeid = b[1]
                            empname = str(b[2])+" S/O "+str(b[3])
                            self.tree.insert(parent3, END, iid=emptreeid, value=(b[1], empname, b[4], b[7], shortterm, longterm, "", "", ""))
                            totalsalary = totalsalary + 1
                        
                        elif b[6] == "Maker":
                            emptreeid = b[1]
                            empname = str(b[2])+" S/O "+str(b[3])
                            totalmaker = totalmaker + 1
                            clearworktotal = 0
                            unclearwoktotal = 0
                            makerworkinhand = employee_receord_database().contractor_clearwork_database(empid)
                            if makerworkinhand == False:
                                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                            elif makerworkinhand == []:
                                self.tree.insert(parent4, END, iid=emptreeid, value=(b[1], empname, b[4], "", shortterm, longterm, clearworktotal, unclearwoktotal, 0, 0))
                            elif makerworkinhand != []:
                                subpro = ""
                                totalofrate = 0
                                totalofqty = 0
                                totalofclear = 0
                                for work in makerworkinhand:
                                    if work[0] == None:
                                        clearworktotal = clearworktotal + 0
                                    else:
                                        clearqty = work[4]
                                        prorate = work[3]
                                        clear = prorate * clearqty
                                        clearworktotal = clearworktotal + clear
                                        totalofqty = totalofqty + work[1]
                                        totalofclear = totalofclear + clearqty
                                        if subpro == "" or subpro != work[0]:
                                            totalofrate = totalofrate + prorate
                                            subpro = work[0]
                                        else:
                                            pass
                                remainqty = totalofqty - totalofclear
                                uncleart = totalofrate * remainqty
                                payable = int(clearworktotal) - int(shortterm)

                                self.tree.insert(parent4, END, iid=emptreeid, value=(b[1], empname, b[4], "", shortterm, longterm, clearworktotal, uncleart, payable))
                    
                    self.tree.item(parent2, text="Contractor: "+str(totalcontractor))
                    self.tree.item(parent3, text="Salarybase: "+str(totalsalary))
                    self.tree.item(parent4, text="Maker: "+str(totalmaker))

                    totalempindep = totalcontractor + totalsalary + totalmaker
                    self.tree.insert(parent, END, iid="totalemps"+str(depid), text=("Total: "+str(totalempindep)))

    #   Save Bind Function
    def save_process_bind_function(self, eve):
        self.fathernameentry.focus_set()
        self.save_department()

    #   Edit Bind Function
    def edit_process_bind_function(self, eve):
        self.fathernameentry.focus_set()
        self.editing_save()

    #   Search Bind
    def search_process_bind_function(self, eve):
        self.search_department()

    #   Back Bind
    def back_bind_function(self, eve):
        self.director_frame()

    #   Print Out
    def print_out(self):
        logo = "img/icon.png"
        treedata = self.tree.get_children()
        desktop_path = platform.node()
        noofcontactor = 0 
        noofsalary = 0
        noofmaker = 0

        for parent_item in treedata:
            child_items = self.tree.get_children(parent_item)
            for child_item in child_items:
                details = self.tree.item(child_item)
                allvalues = details["text"]

                subchild = self.tree.get_children(child_item)
                for subchildren in subchild:
                    if "Contractor:" in allvalues:
                        noofcontactor = noofcontactor + 1
                    elif "Salarybase:" in allvalues:
                        noofsalary = noofsalary + 1
                    elif "Maker:" in allvalues:
                        noofmaker = noofmaker + 1

        nooftotalemp = noofcontactor + noofsalary + noofmaker


        pdf = FPDF(orientation='L', unit='mm', format='A4')
        pdf.set_fill_color(250, 250, 250)
        pdf.add_page()
        pdf.set_font("Arial", "B", size=10)
        pdf.cell(100, 8, txt="Littlewood Corporation", ln=0)
        pdf.image(logo, x=51, y=9, w=9, h=9)
        pdf.cell(55, 8, txt="Department Details", ln=0, align="C")
        pdf.ln(10)
        pdf.set_font("Arial", "B", size=8)
        pdf.cell(45, 6, txt="No of Department:   "+str(len(treedata)), ln=0, border=True)
        pdf.cell(45, 6, txt="No of Employee:   "+str(nooftotalemp), ln=0, border=True)
        pdf.cell(40, 6, txt="Contractor:   "+str(noofcontactor), ln=0, border=True) 
        pdf.cell(40, 6, txt="Salary:   "+str(noofsalary), ln=0, border=True) 
        pdf.cell(40, 6, txt="Maker:   "+str(noofmaker), ln=0, border=True)
        pdf.cell(65, 6, txt="Print by:   "+str(self.username)+"  "+str(desktop_path), ln=0, border=True)
        pdf.ln()

        for parent_item in treedata:
            pdf.ln(10)
            pdf.set_font("Arial", "B", size=8)
            details = self.tree.item(parent_item)
            description = details["text"]
            allvalues = details["values"]
            pdf.multi_cell(180, 6, txt=str(str(description)))
            child_items = self.tree.get_children(parent_item)
            for child_item in child_items:
                details1 = self.tree.item(child_item)
                childtext = details1["text"]
                childvalues = details1["values"]

                if "Contractor" in childtext or "Maker" in childtext:
                    empid = str(childvalues[0])
                    empname = str(childvalues[1]) 
                    contact = str(childvalues[2])
                    shortterm = str(childvalues[4])
                    longterm = str(childvalues[5])
                    workdone = str(childvalues[6])
                    workinhand = str(childvalues[7])
                    payable = childvalues[8]

                    pdf.set_font("Arial", "B", size=7)
                    pdf.cell(105, 6, txt=str(childtext), ln=0, border=True, align='L')
                    pdf.ln()
                    pdf.cell(20, 6, txt=str(empid), ln=0, border=True, align='L')
                    pdf.cell(85, 6, txt=str(empname), ln=0, border=True, align='C')
                    pdf.cell(27, 6, txt=str(contact), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(shortterm), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(longterm), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(workdone), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(workinhand), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(payable), ln=0, border=True, align='C')

                    pdf.ln()
                    subchild = self.tree.get_children(child_item)
                    for subchildren in subchild:
                        detaisl2 = self.tree.item(subchildren)
                        subchildtext = detaisl2['text']
                        subchildvalue = detaisl2['values']

                        employeeid = subchildvalue[0]
                        employeename = subchildvalue[1]
                        employeenumber = subchildvalue[2]
                        employeeshortterm = subchildvalue[4]
                        employeelongterm = subchildvalue[5]
                        employeeworkdone = subchildvalue[6]
                        employeeworkinhand = subchildvalue[7]
                        employeepayable = subchildvalue[8]

                        pdf.set_font("Arial", size=7)
                        pdf.cell(20, 6, txt=str(employeeid), ln=0, border=True, align='L')
                        pdf.cell(85, 6, txt=str(employeename), ln=0, border=True, align='L')
                        pdf.cell(27, 6, txt=str(employeenumber), ln=0, border=True, align='C')
                        pdf.cell(30, 6, txt=str(employeeshortterm), ln=0, border=True, align='C')
                        pdf.cell(30, 6, txt=str(employeelongterm), ln=0, border=True, align='C')
                        pdf.cell(30, 6, txt=str(employeeworkdone), ln=0, border=True, align='C')
                        pdf.cell(30, 6, txt=str(employeeworkinhand), ln=0, border=True, align='C')
                        pdf.cell(30, 6, txt=str(employeepayable), ln=0, border=True, align='C')

                        pdf.ln()

                elif "Salarybase" in childtext:
                    empid = str(childvalues[0])
                    empname = str(childvalues[1]) 
                    contact = str(childvalues[2])
                    shortterm = str(childvalues[4])
                    longterm = str(childvalues[5])
                    slary = str(childvalues[3])
                    workdone = str(childvalues[6])
                    payable = childvalues[8]

                    pdf.set_font("Arial", "B", size=7)
                    pdf.cell(105, 6, txt=str(childtext), ln=0, border=True, align='L')
                    pdf.ln()
                    pdf.cell(20, 6, txt=str(empid), ln=0, border=True, align='L')
                    pdf.cell(85, 6, txt=str(empname), ln=0, border=True, align='C')
                    pdf.cell(27, 6, txt=str(contact), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(shortterm), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(longterm), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(workdone), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(slary), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(payable), ln=0, border=True, align='C')
                    pdf.ln()
                    subchild = self.tree.get_children(child_item)
                    for subchildren in subchild:
                        detaisl2 = self.tree.item(subchildren)
                        subchildtext = detaisl2['text']
                        subchildvalue = detaisl2['values']

                        employeeid = subchildvalue[0]
                        employeename = subchildvalue[1]
                        employeenumber = subchildvalue[2]
                        employeeshortterm = subchildvalue[4]
                        employeelongterm = subchildvalue[5]
                        employeesalary = subchildvalue[3]
                        employeeworkdone = subchildvalue[6]
                        employeepayable = subchildvalue[8]

                        pdf.set_font("Arial", size=7)
                        pdf.cell(20, 6, txt=str(employeeid), ln=0, border=True, align='L')
                        pdf.cell(85, 6, txt=str(employeename), ln=0, border=True, align='L')
                        pdf.cell(27, 6, txt=str(employeenumber), ln=0, border=True, align='C')
                        pdf.cell(30, 6, txt=str(employeeshortterm), ln=0, border=True, align='C')
                        pdf.cell(30, 6, txt=str(employeelongterm), ln=0, border=True, align='C')
                        pdf.cell(30, 6, txt=str(employeeworkdone), ln=0, border=True, align='C')
                        pdf.cell(30, 6, txt=str(employeesalary), ln=0, border=True, align='C')
                        pdf.cell(30, 6, txt=str(employeepayable), ln=0, border=True, align='C')

                        pdf.ln()

        newpdfsave = filedialog.asksaveasfilename(
                        title=("Save Details"),
                        defaultextension=".pdf",
                        parent=self.root2)
        if newpdfsave:
            pdf.output(newpdfsave)
            messagebox.showinfo(parent=self.root2, title="Saved", message="File saved")
        else:
            pass

    #   Selected department print
    def selected_department_printout(self):
        logo = "img/icon.png"
        desktop_path = platform.node()
        noofcontactor = 0 
        noofsalary = 0
        noofmaker = 0

        r_id = self.tree.focus()
        details = self.tree.item(r_id)
        rowtext = details['text']
        rowvalue = details['values']
        x = self.tree.selection()[0]
        
        child_items = self.tree.get_children(x)

        for child_item in child_items:
            details = self.tree.item(child_item)
            allvalues = details["text"]

            subchild = self.tree.get_children(child_item)
            for subchildren in subchild:
                if "Contractor:" in allvalues:
                    noofcontactor = noofcontactor + 1
                elif "Salarybase:" in allvalues:
                    noofsalary = noofsalary + 1
                elif "Maker:" in allvalues:
                    noofmaker = noofmaker + 1

        nooftotalemp = noofcontactor + noofsalary + noofmaker

        pdf = FPDF(orientation='L', unit='mm', format='A4')
        pdf.set_fill_color(250, 250, 250)
        pdf.add_page()
        pdf.set_font("Arial", "B", size=10)
        pdf.cell(100, 8, txt="Littlewood Corporation", ln=0)
        pdf.image(logo, x=51, y=9, w=9, h=9)
        pdf.cell(55, 8, txt="Department Details", ln=0, align="C")
        pdf.ln(10)
        pdf.set_font("Arial", "B", size=8)
        pdf.cell(45, 6, txt=str(""), ln=0, border=True)
        pdf.cell(45, 6, txt="No of Employee:   "+str(nooftotalemp), ln=0, border=True)
        pdf.cell(40, 6, txt="Contractor:   "+str(noofcontactor), ln=0, border=True) 
        pdf.cell(40, 6, txt="Salary:   "+str(noofsalary), ln=0, border=True) 
        pdf.cell(40, 6, txt="Maker:   "+str(noofmaker), ln=0, border=True)
        pdf.cell(65, 6, txt="Print by:   "+str(self.username)+"  "+str(desktop_path), ln=0, border=True)
        pdf.ln()

        pdf.ln(10)
        pdf.set_font("Arial", "B", size=8)
        pdf.multi_cell(180, 6, txt=str(str(rowtext)))
        for child_item in child_items:
            details1 = self.tree.item(child_item)
            childtext = details1["text"]
            childvalues = details1["values"]

            if "Contractor" in childtext or "Maker" in childtext:
                empid = str(childvalues[0])
                empname = str(childvalues[1]) 
                contact = str(childvalues[2])
                shortterm = str(childvalues[4])
                longterm = str(childvalues[5])
                workdone = str(childvalues[6])
                workinhand = str(childvalues[7])
                payable = childvalues[8]

                pdf.set_font("Arial", "B", size=7)
                pdf.cell(105, 6, txt=str(childtext), ln=0, border=True, align='L')
                pdf.ln()
                pdf.cell(20, 6, txt=str(empid), ln=0, border=True, align='L')
                pdf.cell(85, 6, txt=str(empname), ln=0, border=True, align='C')
                pdf.cell(27, 6, txt=str(contact), ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=str(shortterm), ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=str(longterm), ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=str(workdone), ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=str(workinhand), ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=str(payable), ln=0, border=True, align='C')

                pdf.ln()
                subchild = self.tree.get_children(child_item)
                for subchildren in subchild:
                    detaisl2 = self.tree.item(subchildren)
                    subchildtext = detaisl2['text']
                    subchildvalue = detaisl2['values']

                    employeeid = subchildvalue[0]
                    employeename = subchildvalue[1]
                    employeenumber = subchildvalue[2]
                    employeeshortterm = subchildvalue[4]
                    employeelongterm = subchildvalue[5]
                    employeeworkdone = subchildvalue[6]
                    employeeworkinhand = subchildvalue[7]
                    employeepayable = subchildvalue[8]

                    pdf.set_font("Arial", size=7)
                    pdf.cell(20, 6, txt=str(employeeid), ln=0, border=True, align='L')
                    pdf.cell(85, 6, txt=str(employeename), ln=0, border=True, align='L')
                    pdf.cell(27, 6, txt=str(employeenumber), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(employeeshortterm), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(employeelongterm), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(employeeworkdone), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(employeeworkinhand), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(employeepayable), ln=0, border=True, align='C')

                    pdf.ln()

            elif "Salarybase" in childtext:
                empid = str(childvalues[0])
                empname = str(childvalues[1]) 
                contact = str(childvalues[2])
                shortterm = str(childvalues[4])
                longterm = str(childvalues[5])
                slary = str(childvalues[3])
                workdone = str(childvalues[6])
                payable = childvalues[8]

                pdf.set_font("Arial", "B", size=7)
                pdf.cell(105, 6, txt=str(childtext), ln=0, border=True, align='L')
                pdf.ln()
                pdf.cell(20, 6, txt=str(empid), ln=0, border=True, align='L')
                pdf.cell(85, 6, txt=str(empname), ln=0, border=True, align='C')
                pdf.cell(27, 6, txt=str(contact), ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=str(shortterm), ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=str(longterm), ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=str(workdone), ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=str(slary), ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=str(payable), ln=0, border=True, align='C')
                pdf.ln()
                subchild = self.tree.get_children(child_item)
                for subchildren in subchild:
                    detaisl2 = self.tree.item(subchildren)
                    subchildtext = detaisl2['text']
                    subchildvalue = detaisl2['values']

                    employeeid = subchildvalue[0]
                    employeename = subchildvalue[1]
                    employeenumber = subchildvalue[2]
                    employeeshortterm = subchildvalue[4]
                    employeelongterm = subchildvalue[5]
                    employeesalary = subchildvalue[3]
                    employeeworkdone = subchildvalue[6]
                    employeepayable = subchildvalue[8]

                    pdf.set_font("Arial", size=7)
                    pdf.cell(20, 6, txt=str(employeeid), ln=0, border=True, align='L')
                    pdf.cell(85, 6, txt=str(employeename), ln=0, border=True, align='L')
                    pdf.cell(27, 6, txt=str(employeenumber), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(employeeshortterm), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(employeelongterm), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(employeeworkdone), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(employeesalary), ln=0, border=True, align='C')
                    pdf.cell(30, 6, txt=str(employeepayable), ln=0, border=True, align='C')

                    pdf.ln()

        newpdfsave = filedialog.asksaveasfilename(
                        title=("Save Details"),
                        defaultextension=".pdf",
                        parent=self.root2)
        if newpdfsave:
            pdf.output(newpdfsave)
            messagebox.showinfo(parent=self.root2, title="Saved", message="File saved")
        else:
            pass

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

#   Employee
class employee_class(director_class):
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
            self.addnewemployeelabel = Label(self.newempinfoframe, text="New Employee Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
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
            self.empidlabel = Label(self.editempinfoframe, text="Employee id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=12, y=26)
            self.empidlabel = Label(self.editempinfoframe, text="Details:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=20, y=61)
            self.empidlabel = Label(self.editempinfoframe, text="Amount:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=20, y=131)

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
            self.bonusamount_var = StringVar()
            self.bonusid_var = StringVar()
            self.searchbar_var = StringVar()
            self.searchbyid_var = IntVar()

            self.underdepid_var = StringVar()
            self.underdesignation_var = StringVar()
            self.underempid_var = StringVar()
            self.undertype_var = StringVar()
            self.underempname_var = StringVar()

            newempid = employee_database().new_employee()
            existingdeps = department_database().existing_departments()
            existingemployees = employee_database().existing_employee()
            existinfdesignations = employee_database().all_designation_from_database()
            emp_types = ["" ,"Salary", "Contractor", "Maker"]
            self.empid_var.set(newempid)
            designations = [""]
            for j in existinfdesignations:
                designations.append(j[0])

            d = [""]
            for i in existingdeps:
                d.append(i)

            #   Employee Details Entries
            self.depentry = Combobox(self.newempinfoframe, values=d, textvariable=self.depid_var,  state="readonly")
            self.depentry.place(x=130, y=30, height=24, width=170)
            self.designationentry =  Combobox(self.newempinfoframe, values=designations, textvariable=self.designation_var,  state="readonly")
            self.designationentry.place(x=440, y=30, height=24, width=170)
            self.empidentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.empid_var, state="readonly", readonlybackground=self.bgcolor, font=("Time new rooman", 9, "bold"))
            self.empidentry.place(x=130, y=65, height=24, width=170)
            self.emptypeentry = Combobox(self.newempinfoframe, values=emp_types, textvariable=self.emptype_var, state="readonly")
            self.emptypeentry.place(x=440, y=65, height=24, width=170)
            self.empnameentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.empnaem_var)
            self.empnameentry.place(x=130, y=100, height=24, width=170)
            self.empnameentry.focus_set()
            self.fathernameentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.fathername_var)
            self.fathernameentry.place(x=440, y=100, height=24, width=170)
            self.empcnicentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.empcnic_var)
            self.empcnicentry.place(x=130, y=135, height=24, width=170)
            self.empcellentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black,textvariable=self.empcell_var)
            self.empcellentry.place(x=440, y=135, height=24, width=170)
            self.empaddressentry = Text(self.newempinfoframe ,bd=2, font=("Time new rooman", 8),  relief=SUNKEN, bg=self.white, fg=self.black)
            self.empaddressentry.place(x=130, y=170, height=65, width=170)
            self.empsalaryentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.empsalary_var, font=("Time new rooman", 10, "bold"))
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

            #   Bonus Entries
            self.editempidentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.editempid_var, state="readonly", readonlybackground=self.bgcolor, font=("Time new rooman", 9, "bold"))
            self.editempidentry.place(x=130, y=30, height=24, width=170)
            self.empincentivieentry = Text(self.editempinfoframe ,bd=2, font=("Time new rooman", 8),  relief=SUNKEN, bg=self.white, fg=self.black)
            self.empincentivieentry.place(x=130, y=65, height=65, width=170)
            self.empbonusentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.bonusamount_var, font=("Time new rooman", 10, "bold"))
            self.empbonusentry.place(x=130, y=135, height=24, width=170)

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

            self.tree2 = Treeview(self.editempinfoframe, height=6, columns=("C1", "C2", "C3", "C4"), show="headings")
            self.tree2.place(x=0, y=170, width=600)

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
            self.saveicon = ImageTk.PhotoImage(self.saveiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.addimageicon = ImageTk.PhotoImage(self.addimageiconphoto)
            self.editicon = ImageTk.PhotoImage(self.editiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            
            self.savebutton = Button(self.newempinfoframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_new_employee, bd=2)
            self.savebutton.place(x=350, y=202, height=40)
            self.editbutton = Button(self.newempinfoframe, width=76, text="Edit", font=("Time new rooman", 9, "bold", "italic"), image=self.editicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.edit_employee, bd=2)
            self.editbutton.place(x=450, y=200, height=43)
            self.addimagebutton = Button(self.newempinfoframe, width=70, text="Add\nImage", font=("Time new rooman", 9, "bold", "italic"), image=self.addimageicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.add_image, bd=2)
            self.addimagebutton.place(x=710, y=235, height=40)
            self.searchbutton = Button(self.searchframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.saerch_employee, bd=2)
            self.searchbutton.place(x=520, y=11, height=25)

            self.savebutton1 = Button(self.editempinfoframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.bonus, bd=2)
            self.savebutton1.place(x=350, y=30, height=40)
            self.editbutton1 = Button(self.editempinfoframe, width=73, text="Edit", font=("Time new rooman", 9, "bold", "italic"), image=self.editicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_bonus_editing, bd=2)
            self.editbutton1.place(x=350, y=76, height=40)

            self.backbutton = Button(self.editempinfoframe, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.director_frame, bd=2)
            self.backbutton.place(x=450, y=30, height=40)
            self.clearbutton = Button(self.editempinfoframe, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen, bd=2)
            self.clearbutton.place(x=450, y=76, height=40)

            self.savebutton2 = Button(self.newempinfoframe2, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_under_supervision, bd=2)
            self.savebutton2.place(x=350, y=130, height=40)

            #   Pop Up
            self.popup = Menu(self.tree, tearoff=0)
            self.popup.add_separator()
            self.popup.add_command(label="View", command=self.view_employee)
            self.popup.add_separator()
            self.popup.add_command(label="Select Undersupervision", command=self.select_under_employee)
            self.tree.bind("<Button-3>", self.do_popup_tree)

            self.popup2 = Menu(self.tree2, tearoff=0)
            self.popup2.add_separator()
            self.popup2.add_command(label="Edit", command=self.bonus_editing_selection)
            self.popup2.add_separator()
            self.popup2.add_command(label="Delete", command=self.delete_bonus)
            self.popup2.add_separator()
            self.tree2.bind("<Button-3>", self.do_popup_tree2)

            self.popup3 = Menu(self.tree3, tearoff=0)
            self.popup3.add_separator()
            self.popup3.add_command(label="image", command=self.view_under_pic)
            self.popup3.add_separator()
            self.popup3.add_command(label="Remove", command=self.delete_under_supervision)
            self.popup3.add_separator()
            self.tree3.bind("<Button-3>", self.do_popup_tree3)

            #   Bind Function
            #   Save/Edit Employee
            self.root2.bind("<Control-s>", self.save_employee_bind_function)
            self.root2.bind("<Alt-s>", self.save_edit_employee_bind_function)
            #   Save/Edit Bonus
            self.root2.bind("<Control-b>", self.save_bonus_bind_function)
            self.root2.bind("<Alt-b>", self.save_edit_bonus_bind_function)
            #   Search
            self.root2.bind("<Control-f>", self.search_bind_function)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.back_bind_function)
            self.root2.bind("<Control-u>", self.undersupervision_bind_function)
        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Clear Screen
    def clear_screen(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        for i in self.tree2.get_children():
            self.tree2.delete(i)

        for i in self.tree3.get_children():
            self.tree3.delete(i)
        
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
        self.bonusamount_var.set("")
        self.bonusid_var.set("")
        self.searchbar_var.set("")
        self.undertype_var.set("")
        self.underdepid_var.set("")
        self.underdesignation_var.set("")
        self.underempid_var.set("")
        self.underempname_var.set("")
        self.empaddressentry.delete("1.0", END)
        self.empincentivieentry.delete("1.0", END)
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

    #   ADD IMAGE
    def add_image(self):
        self.cpiclocation = filedialog.askopenfilename(parent=self.root2, title="Choose Employee's Image", defaultextension=".jpg")
        if self.cpiclocation == '':
            pass
        else:
            try:
                img = (Image.open(self.cpiclocation))
                self.resized_image= img.resize((250,255), Image.ANTIALIAS)
                self.new_image= ImageTk.PhotoImage(self.resized_image)
                self.emppicentry.config(state=NORMAL)
                self.emppicentry.delete("1.0", END)
                self.emppicentry.imgtk = self.new_image
                self.emppicentry.image_create(END, image=self.new_image)
                self.emppicentry.config(state=DISABLED)
                self.backbutton.config(command=self.add_employee_frame)
            except:
                messagebox.showerror(parent=self.root2, title="IMAGE", message="Choose only .jpg extension")

    #   Save New Employee
    def save_new_employee(self):
        empid = self.empid_var.get()
        empname = (self.empnaem_var.get()).capitalize()
        father = (self.fathername_var.get()).capitalize()
        cnic = self.empcnic_var.get()
        cell = self.empcell_var.get()
        address = (self.empaddressentry.get("1.0", END)).capitalize()
        salary = self.empsalary_var.get()
        depid = self.depid_var.get()
        designation = self.designation_var.get()
        emptype = self.emptype_var.get()
        adddate = str(self.current_date())
        emppic = 0
        try:
            p = self.emppicentry.image_configure("1.0")
            emppic = 1
        except:
            emppic = 0
        if salary.isdigit() == False:
            messagebox.showwarning(parent=self.root2, title="Salary", message="Salary must be int")
        elif emppic == 0:
            messagebox.showwarning(parent=self.root2, title="Image", message="Add employee image")
        elif salary.isdigit() == True:
            if len(cnic) == 15 and cnic[5] == "-" and cnic[13] == "-":
                c = 'EMP-PICS/'+str(empid)+".png"
                a = employee_database().save_employee(empid, empname, father, cell, cnic, address, salary, depid, designation, emptype, adddate, c)
                if a == "Save":
                    self.resized_image.save(c)
                    newempid = employee_database().new_employee()
                    self.empid_var.set(newempid)
                    self.clear_screen()
                    messagebox.showinfo(parent=self.root2, title="Saved", message="New employee has been added")
                elif a == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                elif a == "Exists":
                    messagebox.showerror(parent=self.root2,title="Contact/CNIC", message="Contact/CNIC already exists in database")
                elif a == "Empty":
                    messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
                elif a == "No Salary":
                    messagebox.showwarning(parent=self.root2, title="Salary", message="Salary must required for salary base employee")
                elif a == "With Salary":
                    messagebox.showwarning(parent=self.root2, title="Salary", message="Salary must be 0 for "+str(emptype))
            else:
                messagebox.showerror(parent=self.root2, title="CNIC", message="CNIC format is invalid, Please use *****-*******-*")

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

    #   Edit Employee
    def edit_employee(self):
        empid = self.editempid_var.get()
        empname = (self.empnaem_var.get()).capitalize()
        father = (self.fathername_var.get()).capitalize()
        cnic = self.empcnic_var.get()
        cell = self.empcell_var.get()
        address = (self.empaddressentry.get("1.0", END)).capitalize()
        salary = self.empsalary_var.get()
        depid = self.depid_var.get()
        designation = self.designation_var.get()
        emptype = self.emptype_var.get()
        if empid == "":
            messagebox.showwarning(parent=self.root2, title="Employee id", message="Select employee from List")
        elif salary.isdigit() == False:
            messagebox.showwarning(parent=self.root2, title="Salary", message="Salary must be int")
        elif salary.isdigit() == True:
            a = employee_database().edit_employee_data(empid, empname, father, cell, cnic, address, salary, depid, designation, emptype)
            if a == "Save":
                self.clear_screen()
                messagebox.showinfo(parent=self.root2, title="Edit", message="Employee has been editted")
            elif a == "Exists":
                messagebox.showerror(parent=self.root2,title="Contact/CNIC", message="Contact/CNIC already exists in database")
            elif a == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif a == "No Salary":
                messagebox.showwarning(parent=self.root2, title="Salary", message="Salary must required for salary base employee")
            elif a == "With Salary":
                messagebox.showwarning(parent=self.root2, title="Salary", message="Salary must be 0 for "+str(emptype))
            elif a == "Empty":
                messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")

    #   Employee Bonus
    def bonus(self):
        empid = self.editempid_var.get()
        details = (self.empincentivieentry.get("1.0", END)).capitalize()
        salary = self.bonusamount_var.get()
        addeddate = self.current_date()
        user = self.username
        if empid == "":
            messagebox.showwarning(parent=self.root2, title="Employee id", message="Select employee from List")
        elif salary.isdigit() == False:
            messagebox.showwarning(parent=self.root2, title="Amount", message="Amount must be int")
        elif salary.isdigit() == True:
            if int(salary) > 0:
                a = employee_database().employee_bonus_data(empid, details, salary, addeddate, user)
                if a == "Save":
                    for i in self.tree2.get_children():
                        self.tree2.delete(i)
                    self.empincentivieentry.delete("1.0", END)
                    self.bonusid_var.set("")
                    self.bonusamount_var.set("")
                    a = employee_database().view_emp_data(empid)
                    bonusinfo = employee_database().emp_bonus_data(empid)
                    self.empaddressentry.delete("1.0", END)
                    messagebox.showinfo(parent=self.root2, title="Add", message="Incentive has been saved")
                    for i in a:
                        self.editempid_var.set(i[1])
                        self.empnaem_var.set(i[2])
                        self.fathername_var.set(i[3])
                        self.empcnic_var.set(i[4])
                        self.empcell_var.set(i[5])
                        self.empaddressentry.insert("1.0", i[6])
                        self.emppicentry.config(state=NORMAL)
                        self.emppicentry.delete("1.0", END)
                        b = i[7]
                        img = ImageTk.PhotoImage(Image.open(b))
                        self.emppicentry.imgtk = img
                        self.emppicentry.image_create(END, image=img)
                        self.emppicentry.config(state=DISABLED)
                        self.emptype_var.set([8])
                        self.designation_var.set(i[9])
                        self.empsalary_var.set(i[10])
                        
                        e = str(i[0])+" "+str(i[1])
                        self.depid_var.set(e)
                    
                    if bonusinfo == "Empty":
                        pass
                    else:
                        for k in bonusinfo:
                            self.tree2.insert("", END, iid=k[0], values=(k[0], k[1], k[2], k[3]))
                elif a == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                elif a == "Empty":
                    messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields(Details, Amount)")
            else:
               messagebox.showwarning(parent=self.root2, title="Amount", message="Amount can't be 0 or less than 0") 

    #   Pop Up In Tree2
    def do_popup_tree2(self, eve):
        r_id = self.tree2.focus()
        details = self.tree2.item(r_id)
        row = details['values']
        x = self.tree2.selection()
        if row != '' and x:
            self.popup2.selection = self.tree2.set(self.tree2.identify_row(eve.y))
            self.popup2.post(eve.x_root, eve.y_root)
        else:
            pass

    #   Bonus Editting
    def bonus_editing_selection(self):
        a = database_class().database_connection_check()
        if a == True:
            r_id = self.tree2.focus()
            details = self.tree2.item(r_id)
            row = details['values']
            x = self.tree2.selection()
            if row != '' and x:
                self.bonusid_var.set(row[0])
                self.empincentivieentry.insert("1.0", row[1])
                self.bonusamount_var.set(row[2])
        else:
           messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost") 

    #   Save Bonus Editing
    def save_bonus_editing(self):
        bonusid = self.bonusid_var.get()
        empid = self.editempid_var.get()
        details = (self.empincentivieentry.get("1.0", END)).capitalize()
        salary = self.bonusamount_var.get()
        addeddate = self.current_date()
        user = self.username
        if empid == "":
            messagebox.showwarning(parent=self.root2, title="Employee id", message="Select employee from List")
        elif bonusid == "":
            messagebox.showwarning(parent=self.root2, title="Empty", message="Select incentive from List")
        elif salary.isdigit() == False:
            messagebox.showwarning(parent=self.root2, title="Amount", message="Amount must be int")
        elif salary.isdigit() == True:
            if int(salary) > 0:
                a = employee_database().bonus_editing_database(empid, details, salary, addeddate, user, bonusid)
                if a == "Save":
                    for i in self.tree2.get_children():
                        self.tree2.delete(i)
                    self.empincentivieentry.delete("1.0", END)
                    self.bonusid_var.set("")
                    self.bonusamount_var.set("")
                    c = employee_database().view_emp_data(empid)
                    bonusinfo = employee_database().emp_bonus_data(empid)
                    messagebox.showinfo(parent=self.root2, title="Edit", message="Incentive has been editted")
                    if bonusinfo == "Empty":
                        pass
                    else:
                        for k in bonusinfo:
                            self.tree2.insert("", END, iid=k[0], values=(k[0], k[1], k[2], k[3]))
                elif a == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                elif a == "Empty":
                    messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields(Details, Amount)")
            else:
               messagebox.showwarning(parent=self.root2, title="Amount", message="Amount can't be 0 or less than 0")

    #   Delete incentive
    def delete_bonus(self):
        a = database_class().database_connection_check()
        if a == True:
            r_id = self.tree2.focus()
            details = self.tree2.item(r_id)
            row = details['values']
            x = self.tree2.selection()
            if row != '' and x:
                bonusid = x[0]
                empid = self.editempid_var.get()
                question = messagebox.askquestion(parent=self.root2, title="Delete", message="Are you sure?")
                if question == "yes":
                    a = employee_database().delete_bonus_from_database(empid, bonusid)
                    if a == "Save":
                        for i in self.tree2.get_children():
                            self.tree2.delete(i)
                        self.empincentivieentry.delete("1.0", END)
                        self.bonusid_var.set("")
                        self.bonusamount_var.set("")
                        a = employee_database().view_emp_data(empid)
                        bonusinfo = employee_database().emp_bonus_data(empid)
                        messagebox.showinfo(parent=self.root2, title="Delete", message="Incentive has been deleted")
                        self.empaddressentry.delete("1.0", END)
                        for i in a:
                            self.editempid_var.set(i[1])
                            self.empnaem_var.set(i[2])
                            self.fathername_var.set(i[3])
                            self.empcnic_var.set(i[4])
                            self.empcell_var.set(i[5])
                            self.empaddressentry.insert("1.0", i[6])
                            self.emppicentry.config(state=NORMAL)
                            self.emppicentry.delete("1.0", END)
                            b = i[7]
                            img = ImageTk.PhotoImage(Image.open(b))
                            self.emppicentry.imgtk = img
                            self.emppicentry.image_create(END, image=img)
                            self.emppicentry.config(state=DISABLED)
                            self.emptype_var.set(i[8])
                            self.designation_var.set(i[9])
                            self.empsalary_var.set(i[10])
                            
                            e = str(i[0])+" "+str(i[1])
                            self.depid_var.set(e)
                        if bonusinfo == "Empty":
                            pass
                        else:
                            for k in bonusinfo:
                                self.tree2.insert("", END, iid=k[0], values=(k[0], k[1], k[2], k[3]))
                    elif a == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif a == "Empty":
                        messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields(Details, Amount)")
                else:
                    pass

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

    #   Save Employee Bind Function
    def save_employee_bind_function(self, eve):
        self.empnameentry.focus_set()
        self.save_new_employee()

    #   Save Edit Employee Bind Function
    def save_edit_employee_bind_function(self, eve):
        self.empnameentry.focus_set()
        self.edit_employee()

    #   Save Bonus Bind Function
    def save_bonus_bind_function(self, eve):
        self.bonus()

    #   Save Edit Bonus Bind Function
    def save_edit_bonus_bind_function(self, eve):
        self.save_bonus_editing()

    #   Search Bind
    def search_bind_function(self, eve):
        self.searchentrybar.focus_set()
        self.saerch_employee()

    #   Back Bind
    def back_bind_function(self, eve):
        self.director_frame()

    #   Undersupervision bind
    def undersupervision_bind_function(self, eve):
        self.save_under_supervision()

    #   Select Under Vision
    def select_under_employee(self):
        a = database_class().database_connection_check()
        if a == True:
            r_id = self.tree.focus()
            details = self.tree.item(r_id)
            row = details['values']
            x = self.tree.selection()
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

    #   Save UnderSupervision
    def save_under_supervision(self):
        empid = self.editempid_var.get()
        underempid = self.underempid_var.get()
        if empid != underempid:
            saveundersupervision = employee_database().save_under_supervision_database(empid, underempid)
            if saveundersupervision == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif saveundersupervision == "Empty":
                messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
            elif saveundersupervision == "Save":
                emsg = str(self.underempname_var.get())+" has been saved undersupervision of "+str(self.empnaem_var.get())
                for i in self.tree3.get_children():
                    self.tree3.delete(i)
                self.underdepid_var.set("")
                self.underdesignation_var.set("")
                self.underempid_var.set("")
                self.underempname_var.set("")
                self.undertype_var.set("")
                self.emppicentry1.config(state=NORMAL)
                self.emppicentry1.delete("1.0", END)
                self.emppicentry1.config(state=DISABLED)
                undersupervision = employee_database().emp_under_super(empid)
                for i in undersupervision:
                    name = str(i[2])+" S/O "+str(i[3])
                    self.tree3.insert("", END, iid=i[1], values=(i[1], name, i[4], i[5]))
                messagebox.showinfo(parent=self.root2,title="Saved", message=emsg)
        else:
            messagebox.showerror(parent=self.root2,title="Same Employee", message="Employee must be different")
          
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

    #   Remove UnderSupervision
    def delete_under_supervision(self):
        r_id = self.tree3.focus()
        details = self.tree3.item(r_id)
        row = details['values']
        x = self.tree3.selection()
        if row != '' and x:
            empid = row[0]
            removeemp = employee_database().remove_undersupervision_database(empid)
            if removeemp == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif removeemp == "Empty":
                messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
            elif removeemp == "Save":
                self.tree3.delete(empid)
                messagebox.showinfo(parent=self.root2,title="Removed", message="Employee has been removed")
        else:
            pass

#   Customer Orders
class order_class(director_class):
    #   init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)

    #   Employee Frame
    def add_order_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.newempinfoframe = Frame(self.newdepinfoframemain, width=740, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe.place(x=0, y=0, height=135)
            self.editempinfoframe = Frame(self.newdepinfoframemain, width=742, bg=self.gray, bd=4, relief=FLAT)
            self.editempinfoframe.place(x=741, y=0, height=185)
            self.searchframe = Frame(self.newdepinfoframemain, width=740, bg=self.gray, bd=4, relief=FLAT)
            self.searchframe.place(x=0, y=136, height=55)
            self.editorderinfoframe = Frame(self.newdepinfoframemain, width=680, bg=self.gray, bd=4, relief=FLAT)
            self.editorderinfoframe.place(x=790, y=504, height=185)

            #   Order LABELS
            self.addnewemployeelabel = Label(self.newempinfoframe, text="New Order Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=300, y=0)
            self.depidlabel = Label(self.newempinfoframe, text="Order id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.newempinfoframe, text="Factory-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=318, y=26)
            self.empidlabel = Label(self.newempinfoframe, text="Customer-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=3, y=61)
            self.emptypelabel = Label(self.newempinfoframe, text="Description:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=318, y=61)
            self.empidlabel = Label(self.newempinfoframe, text="Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=14, y=96)
            self.depnamelabel = Label(self.newempinfoframe, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=321, y=96)

            #   Artical LABELS
            self.addnewemployeelabel = Label(self.editempinfoframe, text="New Artical Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=300, y=0)
            self.depidlabel = Label(self.editempinfoframe, text="Order id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depidlabel = Label(self.editempinfoframe, text="Artical id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=317, y=26)
            self.depidlabel = Label(self.editempinfoframe, text="Product No:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=8, y=61)
            self.depnamelabel = Label(self.editempinfoframe, text="Size:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=328, y=61)
            self.depnamelabel = Label(self.editempinfoframe, text="Color:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=21, y=96)
            self.depnamelabel = Label(self.editempinfoframe, text="Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=320, y=96)
            self.depnamelabel = Label(self.editempinfoframe, text="Artical No:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=12, y=131)

            #   Editing Lable
            self.addnewemployeelabel = Label(self.editorderinfoframe, text="Edit Order Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=250, y=0)
            self.depidlabel = Label(self.editorderinfoframe, text="Order id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depidlabel = Label(self.editorderinfoframe, text="Artical id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=317, y=26)
            self.depnamelabel = Label(self.editorderinfoframe, text="Remain:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=16, y=61)

            #   Search Label
            self.empidlabel = Label(self.searchframe, text="Search:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=30, y=7)

            #   VAriables
            self.orderid_var = StringVar()
            self.factorypo_var = StringVar()
            self.customerpo_var = StringVar()
            self.description_var = StringVar()
            self.orderqty_var = StringVar()
            self.ordertype_var = StringVar()

            self.orderarticalid_var = StringVar()
            self.articaldatabaseno_var = StringVar()
            self.articalid_var = StringVar()
            self.productno_var = StringVar()
            self.size_var = StringVar()
            self.color_var = StringVar()
            self.articalqty_var = StringVar()

            self.editorderid_var = StringVar()
            self.editarticalid_var = StringVar()
            self.remainorderqty_var = IntVar()

            self.searchbar_var = StringVar()

            #   Getting ids
            neworderid = customer_order_database().new_order()
            existingorders = customer_order_database().pending_orders()
            ordercategory = customer_order_database().order_category()

            self.orderid_var.set(neworderid)
            emp_types = [""]
            for i in ordercategory:
                emp_types.append(i[0])

            #   Entry
            self.orderidentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.orderid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.orderidentry.place(x=130, y=30, height=24, width=170)
            self.factorypoentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.factorypo_var)
            self.factorypoentry.place(x=440, y=30, height=24, width=170)
            self.factorypoentry.focus_set()
            self.customerpoentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.customerpo_var)
            self.customerpoentry.place(x=130, y=65, height=24, width=170)
            self.orderdescriptionentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.description_var)
            self.orderdescriptionentry.place(x=440, y=65, height=24, width=170)
            self.orderqtyentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.orderqty_var, font=("Time new rooman", 10, "bold"))
            self.orderqtyentry.place(x=130, y=100, height=24, width=170)
            self.emptypeentry = Combobox(self.newempinfoframe, values=emp_types, textvariable=self.ordertype_var, state="readonly")
            self.emptypeentry.place(x=440, y=100, height=24, width=170)

            self.articalorderidentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.orderarticalid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articalorderidentry.place(x=130, y=30, height=24, width=170)
            self.articalidentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.articalid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articalidentry.place(x=440, y=30, height=24, width=170)
            self.productnoentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.productno_var)
            self.productnoentry.place(x=130, y=65, height=24, width=170)
            self.sizeentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.size_var)
            self.sizeentry.place(x=440, y=65, height=24, width=170)
            self.colorentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.color_var)
            self.colorentry.place(x=130, y=100, height=24, width=170)
            self.articalqtyentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.lightred, fg=self.black,textvariable=self.articalqty_var, font=("Time new rooman", 10, "bold"))
            self.articalqtyentry.place(x=440, y=100, height=24, width=170)
            self.articalnoentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.articaldatabaseno_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articalnoentry.place(x=130, y=135, height=24, width=170)

            self.editarticalorderidentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.editorderid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.editarticalorderidentry.place(x=130, y=30, height=24, width=170)
            self.editarticalidentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.editarticalid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.editarticalidentry.place(x=440, y=30, height=24, width=170)
            self.remainarticalqtyentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.remainorderqty_var, state="readonly", readonlybackground=self.lightgreen, font=("Time new rooman", 10, "bold"))
            self.remainarticalqtyentry.place(x=130, y=65, height=24, width=170)

            self.searchentrybar = Entry(self.searchframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchbar_var)
            self.searchentrybar.place(x=130, y=11, height=24, width=130)

            #   TREE
            self.v = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v.pack(side=RIGHT, fill=Y)
            self.v.place(x=1469, y=192, height=312)

            self.tree = Treeview(self.newdepinfoframemain, height=14, columns=("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"), show="headings", yscrollcommand=self.v.set)
            self.tree.place(x=1, y=192, width=1466)

            self.tree.column("#1", anchor="nw", width=80)
            self.tree.column("#2", anchor="nw", width=80)
            self.tree.column("#3", anchor="nw", width=80)
            self.tree.column("#4", anchor="nw", width=310)
            self.tree.column("#5", anchor=CENTER, width=90)
            self.tree.column("#6", anchor=CENTER, width=80)
            self.tree.column("#7", anchor=CENTER, width=90)
            self.tree.column("#8", anchor=CENTER, width=90)
            self.tree.column("#9", anchor="nw", width=70)

            self.tree.heading("#1", text="Order id")
            self.tree.heading("#2", text="Factory-PO")
            self.tree.heading("#3", text="Customer-PO")
            self.tree.heading("#4", text="Description")
            self.tree.heading("#5", text="Quantity")
            self.tree.heading("#6", text="Category")
            self.tree.heading("#7", text="Added Date")
            self.tree.heading("#8", text="Clearence")
            self.tree.heading("#9", text="Added By")

            self.v.config(command=self.tree.yview)
            for k in existingorders:
                added_date = str(k[7])+" / "+str(k[8])
                clear_date = str(k[9])+" / "+str(k[10])
                u = str(k[11])+"-"+str(k[12])
                self.tree.insert("", END, iid=k[0], values=(k[0], k[1], k[2], k[3], k[4], k[5], added_date, clear_date, u))

            self.tree2 = Treeview(self.newdepinfoframemain, height=16, columns=("C1", "C2", "C3", "C4", "C5"), show="headings")
            self.tree2.place(x=1, y=504, width=792)

            self.tree2.column("#1", anchor="nw", width=20)
            self.tree2.column("#2", anchor="nw", width=60)
            self.tree2.column("#3", anchor=CENTER, width=20)
            self.tree2.column("#4", anchor="nw", width=90)
            self.tree2.column("#5", anchor=CENTER, width=45)

            self.tree2.heading("#1", text="id")
            self.tree2.heading("#2", text="Product No")
            self.tree2.heading("#3", text="Size")
            self.tree2.heading("#4", text="Color")
            self.tree2.heading("#5", text="Quantity")

            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.saveicon = ImageTk.PhotoImage(self.saveiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            self.editicon = ImageTk.PhotoImage(self.editiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)

            self.savebutton = Button(self.newempinfoframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.new_order, bd=2)
            self.savebutton.place(x=630, y=30, height=40)
            self.editbutton = Button(self.newempinfoframe, width=73, text="Edit", font=("Time new rooman", 9, "bold", "italic"), image=self.editicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_order_editing, bd=2)
            self.editbutton.place(x=630, y=80, height=40)
            
            self.savebutton1 = Button(self.editempinfoframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_artical, bd=2)
            self.savebutton1.place(x=630, y=30, height=40)
            self.editbutton1 = Button(self.editempinfoframe, width=73, text="Edit", font=("Time new rooman", 9, "bold", "italic"), image=self.editicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE)#, command=self.save_editing, bd=2)
            self.editbutton1.place(x=630, y=80, height=40)

            self.searchbutton = Button(self.searchframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_order, bd=2)
            self.searchbutton.place(x=320, y=11, height=25)

            self.backbutton = Button(self.searchframe, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.director_frame, bd=2)
            self.backbutton.place(x=420, y=1, height=40)
            self.clearbutton = Button(self.searchframe, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen, bd=2)
            self.clearbutton.place(x=520, y=1, height=40)

            #   Pop Up
            self.popup = Menu(self.tree, tearoff=0)
            self.popup.add_command(label="Edit", command=self.edit_order_selection)
            self.popup.add_separator()
            self.popup.add_command(label="View Articals", command=self.view_articals)
            self.popup.add_separator()

            self.tree.bind("<Button-3>", self.do_popup_tree)

            #   Bind Function
            #   Save/Edit Order
            self.root2.bind("<Control-s>", self.save_order_bind_function)
            self.root2.bind("<Alt-s>", self.save_order_edit_bind_function)
            #   Save/Edit Artical
            self.root2.bind("<Control-e>", self.save_artical_bind_function)
            self.root2.bind("<Alt-e>", self.save_artical_bind_function)
            #   Search
            self.root2.bind("<Control-f>", self.search_bind_function)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.back_bind_function)
            
        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
       
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

    #   View Articals
    def view_articals(self):
        r_id = self.tree.focus()
        details = self.tree.item(r_id)
        row = details['values']
        x = self.tree.selection()
        if row != '' and x:
            fpo = row[0]
            articaldetails = customer_order_database().view_articals(fpo)
            articalid = customer_order_database().artical_id(fpo)
            articaldatabasenumber = customer_order_database().artical_database_number(fpo)
            if articaldetails == False or articalid == False or articaldatabasenumber == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif articaldetails != []:
                self.editorderid_var.set("")
                self.orderarticalid_var.set("")
                self.factorypo_var.set("")
                self.customerpo_var.set("")
                self.description_var.set("")
                self.ordertype_var.set("")
                self.orderqty_var.set("")
                self.remainorderqty_var.set(0)
                self.productnoentry.focus_set()
                for i in self.tree2.get_children():
                    self.tree2.delete(i)

                addedqty = 0
                for i in articaldetails:
                    addedqty = addedqty + i[6]
                    self.tree2.insert("", END, iid=i[1], values=(i[1], i[3], i[4], i[5], i[6]))
                
                r = 0
                if int(row[4]) > addedqty:
                    r = int(row[4]) - addedqty
                elif int(row[4]) == addedqty:
                    r = 0
                articalidnew = str(row[0])+"-"+str(articaldatabasenumber)
                self.articalid_var.set(articalidnew)
                self.articaldatabaseno_var.set(articaldatabasenumber)
                self.orderarticalid_var.set(row[0])
                self.remainorderqty_var.set(r)
            elif articaldetails == []:
                self.editorderid_var.set("")
                self.orderarticalid_var.set("")
                self.factorypo_var.set("")
                self.customerpo_var.set("")
                self.description_var.set("")
                self.ordertype_var.set("")
                self.orderqty_var.set("")
                self.remainorderqty_var.set(0)
                self.productnoentry.focus_set()
                for i in self.tree2.get_children():
                    self.tree2.delete(i)
                articalidnew = str(row[0])+"-"+str(articaldatabasenumber)
                self.articalid_var.set(articalidnew)
                self.articaldatabaseno_var.set(articaldatabasenumber)
                self.orderarticalid_var.set(row[0])
                self.remainorderqty_var.set(row[4])

    #   Clear SCreen
    def clear_screen(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for i in self.tree2.get_children():
            self.tree2.delete(i)

        self.factorypo_var.set("")
        self.customerpo_var.set("")
        self.description_var.set("")
        self.ordertype_var.set("")
        self.orderqty_var.set("")
        self.editorderid_var.set("")
        self.orderarticalid_var.set("")

        self.remainorderqty_var.set(0)

        self.productno_var.set("")
        self.size_var.set("")
        self.color_var.set("")
        self.articalqty_var.set("")
        self.articaldatabaseno_var.set("")

        self.searchbar_var.set("")

        existingorders = customer_order_database().pending_orders()
        for k in existingorders:
            added_date = str(k[7])+" / "+str(k[8])
            clear_date = str(k[9])+" / "+str(k[10])
            u = str(k[11])+"-"+str(k[12])
            self.tree.insert("", END, iid=k[0], values=(k[0], k[1], k[2], k[3], k[4], k[5], added_date, clear_date, u))

        self.factorypoentry.focus_set()

    #   Save new order
    def new_order(self):
        factory_po = (self.factorypo_var.get()).capitalize()
        custmer_po = (self.customerpo_var.get()).capitalize()
        name = (self.description_var.get()).capitalize()
        ordertype = self.ordertype_var.get()
        qty = self.orderqty_var.get()
        user = self.username
        if qty.isdigit() == False or qty == "0":
            messagebox.showwarning(parent=self.root2, title="Quantity", message="Quantity must be int and greater than 0")
        elif qty.isdigit() == True:
            addeddate = self.current_date()
            addedtime = self.current_time()
            saveorder = customer_order_database().save_new_order(factory_po, custmer_po, name, ordertype, qty, addeddate, addedtime, user)
            if saveorder == "Save":
                newempid = customer_order_database().new_order()
                self.orderid_var.set(newempid)
                self.clear_screen()
                messagebox.showinfo(parent=self.root2, title="Saved", message="New order has been added")
            elif saveorder == "Exists":
                messagebox.showerror(parent=self.root2,title="Factor-PO", message="Factor-PO already exists in database")
            elif saveorder == "Empty":
                messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
            elif saveorder == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Save Artical
    def save_artical(self):
        fpo = self.orderarticalid_var.get()
        artid = self.articalid_var.get()
        artno = self.articaldatabaseno_var.get()
        remain = self.remainorderqty_var.get()
        prono = (self.productno_var.get()).capitalize()
        size = (self.size_var.get()).capitalize()
        color = (self.color_var.get()).capitalize()
        qty = self.articalqty_var.get()
        remain = self.remainorderqty_var.get()
        if fpo == "" or artid == "" or artno == "":
            messagebox.showwarning(parent=self.root2, title="Order id/Artical id", message="Order id or Artical id is empty")
        elif qty.isdigit() == False or qty == "0":
            messagebox.showwarning(parent=self.root2, title="Quantity", message="Quantity must be int")
        elif fpo and artid and artno and qty.isdigit() == True:
            if int(qty) <= remain:
                saveartical = customer_order_database().save_new_artical(fpo, artid, artno, prono, size, color, qty)
                if saveartical == "Save":
                    self.productnoentry.focus_set()
                    self.productno_var.set("")
                    self.size_var.set("")
                    self.color_var.set("")
                    self.articalqty_var.set("")
                    self.articalid_var.set("")
                    self.articaldatabaseno_var.set("")
                    for i in self.tree2.get_children():
                        self.tree2.delete(i)

                    articaldetails = customer_order_database().view_articals(fpo)
                    articaldatabasenumber = customer_order_database().artical_database_number(fpo)
                    addedqty = remain - int(qty)
                    self.remainorderqty_var.set(addedqty)
                    for i in articaldetails:
                        self.tree2.insert("", END, iid=i[1], values=(i[1], i[3], i[4], i[5], i[6]))
                    articalidnew = str(fpo)+"-"+str(articaldatabasenumber)
                    self.articalid_var.set(articalidnew)
                    self.articaldatabaseno_var.set(articaldatabasenumber)
                    messagebox.showinfo(parent=self.root2, title="Saved", message="New Artical has been added")
                elif saveartical == "Empty":
                   messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
                elif saveartical == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                messagebox.showwarning(parent=self.root2, title="Quantity", message="Quantity can't be greater than remain articals quantity")

    #   Edit Order Selection
    def edit_order_selection(self):
        r_id = self.tree.focus()
        details = self.tree.item(r_id)
        row = details['values']
        x = self.tree.selection()
        if row != '' and x:
            fpo = row[0]
            articaldetails = customer_order_database().view_articals(fpo)
            if articaldetails == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                for i in self.tree2.get_children():
                    self.tree2.delete(i)

                self.factorypo_var.set("")
                self.customerpo_var.set("")
                self.description_var.set("")
                self.ordertype_var.set("")
                self.orderqty_var.set("")
                self.editorderid_var.set("")
                self.orderarticalid_var.set("")

                self.remainorderqty_var.set(0)

                self.productno_var.set("")
                self.size_var.set("")
                self.color_var.set("")
                self.articalqty_var.set("")
                self.articaldatabaseno_var.set("")
                self.articalid_var.set("")

                self.factorypoentry.focus_set()
                self.editorderid_var.set(row[0])
                self.factorypo_var.set(row[1])
                self.customerpo_var.set(row[2])
                self.description_var.set(row[3])
                self.orderqty_var.set(row[4])
                self.ordertype_var.set(row[5])

                addedqty = 0
                for i in articaldetails:
                    addedqty = addedqty + i[6]
                    self.tree2.insert("", END, iid=i[1], values=(i[1], i[3], i[4], i[5], i[6]))
                
                r = 0
                if int(row[4]) > addedqty:
                    r = int(row[4]) - addedqty
                elif int(row[4]) == addedqty:
                    r = 0

                self.remainorderqty_var.set(r)

    #   Save Order Editing
    def save_order_editing(self):
        orderid = self.editorderid_var.get()
        factory_po = (self.factorypo_var.get()).capitalize()
        custmer_po = (self.customerpo_var.get()).capitalize()
        name = (self.description_var.get()).capitalize()
        ordertype = self.ordertype_var.get()
        qty = self.orderqty_var.get()
        if orderid == "":
           messagebox.showwarning(parent=self.root2, title="Empty", message="Orderid is empty, Select order from list") 
        if qty.isdigit() == False or qty == "0":
            messagebox.showwarning(parent=self.root2, title="Quantity", message="Quantity must be int and greater than 0")
        elif qty.isdigit() == True:
            articaldetails = customer_order_database().view_articals(orderid)
            if articaldetails == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                addedqty = 0
                for i in articaldetails:
                    addedqty = addedqty + i[6]

                if int(qty) >= addedqty:
                    saveediting = customer_order_database().save_order_editing(orderid, factory_po, custmer_po, name, ordertype, qty)
                    if saveediting == "Save":
                        self.clear_screen()
                        messagebox.showinfo(parent=self.root2, title="Edit", message="Order has been editted")
                    elif saveediting == "Exists":
                        messagebox.showerror(parent=self.root2,title="Factor-PO", message="Factor-PO already exists in database")
                    elif saveediting == "Empty":
                        messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
                    elif saveediting == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                else:
                   messagebox.showwarning(parent=self.root2, title="Articals Quantity", message="More articals exsist in database.") 

    #   Search Order
    def search_order(self):
        searchbar = (self.searchbar_var.get()).capitalize()
        if searchbar:
            existingorders = customer_order_database().search_all_order_data(searchbar)
            if existingorders == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif existingorders == "Empty":
                messagebox.showerror(parent=self.root2,title="No Match", message="No match found")
            elif existingorders:
                for i in self.tree.get_children():
                    self.tree.delete(i)
                self.editorderid_var.set("")
                self.orderarticalid_var.set("")
                self.factorypo_var.set("")
                self.customerpo_var.set("")
                self.description_var.set("")
                self.ordertype_var.set("")
                self.orderqty_var.set("")
                self.remainorderqty_var.set(0)
                self.productnoentry.focus_set()
                for i in self.tree2.get_children():
                    self.tree2.delete(i)   

                for k in existingorders:
                    added_date = str(k[6])+" / "+str(k[7])
                    clear_date = str(k[9])+" / "+str(k[10])
                    u = str(k[11])+"-"+str(k[12])
                    self.tree.insert("", END, iid=k[0], values=(k[0], k[1], k[2], k[3], k[4], k[5], added_date, clear_date, u))
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Searchbar is empty")

    #   Bind Order Save
    def save_order_bind_function(self, eve):
        self.factorypoentry.focus_set()
        self.new_order()

    #   Bind Artical Save Function
    def save_artical_bind_function(self, eve):
        self.productnoentry.focus_set()
        self.save_artical()

    #   Bind Order Editing
    def save_order_edit_bind_function(self, eve):
        self.factorypoentry.focus_set()
        self.save_order_editing()

    #   Search Order Bind
    def search_bind_function(self, eve):
        self.searchentrybar.focus_set()
        self.search_order()

    #   Back Bind
    def back_bind_function(self, eve):
        self.director_frame()
        
#   Customer Order Rate and Process
class order_rate_and_process(director_class):
    #   init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)

    #   Order Rate Frame
    def order_rate_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            # FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.newempinfoframe = Frame(self.newdepinfoframemain, width=650, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe.place(x=0, y=0, height=135)
            self.editempinfoframe = Frame(self.newdepinfoframemain, width=830, bg=self.gray, bd=4, relief=FLAT)
            self.editempinfoframe.place(x=651, y=0, height=185)
            self.searchframe = Frame(self.newdepinfoframemain, width=1300, bg=self.gray, bd=4, relief=FLAT)
            self.searchframe.place(x=0, y=136, height=55)
            self.editorderinfoframe = Frame(self.newdepinfoframemain, width=655, bg=self.gray, bd=4, relief=FLAT)
            self.editorderinfoframe.place(x=0, y=500, height=220)

            #   Labels
            self.addnewemployeelabel = Label(self.newempinfoframe, text="Order Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=260, y=0)
            self.depidlabel = Label(self.newempinfoframe, text="Order id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.newempinfoframe, text="Factory-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=318, y=26)
            self.empidlabel = Label(self.newempinfoframe, text="Customer-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=3, y=61)
            self.emptypelabel = Label(self.newempinfoframe, text="Description:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=318, y=61)
            self.empidlabel = Label(self.newempinfoframe, text="Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=14, y=96)
            self.depnamelabel = Label(self.newempinfoframe, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=321, y=96)

            #   Rate LABELS
            self.addnewemployeelabel = Label(self.editempinfoframe, text="New Rate/Process", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=300, y=0)
            self.depidlabel = Label(self.editempinfoframe, text="Process id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=5, y=26)
            self.depidlabel = Label(self.editempinfoframe, text="Department:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=310, y=26)
            self.depidlabel = Label(self.editempinfoframe, text="Details/Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=311, y=61)
            self.depnamelabel = Label(self.editempinfoframe, text="Process No:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=5, y=61)
            self.depnamelabel = Label(self.editempinfoframe, text="Edit\nProcess id", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=0, y=96)

            #   Search Label
            self.empidlabel = Label(self.searchframe, text="Search(Order-id/Factory-PO):", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=8, y=7)

            self.addnewemployeelabel = Label(self.editorderinfoframe, text="Sub-Process Details", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=260, y=0)
            self.depidlabel = Label(self.editorderinfoframe, text="Process id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=10, y=26)
            self.depidlabel = Label(self.editorderinfoframe, text="Sub-Process id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=316, y=26)
            self.depidlabel = Label(self.editorderinfoframe, text="Details/Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=8, y=61)
            self.depnamelabel = Label(self.editorderinfoframe, text="Sub-Process Rate:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=310, y=61)
            self.depnamelabel = Label(self.editorderinfoframe, text="Sub-Process No:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=0, y=96)
            self.depnamelabel = Label(self.editorderinfoframe, text="Edit Sub-\nProcess id", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=8, y=131)

            #   VAriables
            self.orderid_var = StringVar()
            self.factorypo_var = StringVar()
            self.customerpo_var = StringVar()
            self.description_var = StringVar()
            self.orderqty_var = StringVar()
            self.ordertype_var = StringVar()

            self.rateid_var = StringVar()
            self.depid_var = StringVar()
            self.details_var = StringVar()
            self.processno_var = StringVar()
            self.editprocessid_var = StringVar()

            self.proidforsubpro_var = StringVar()
            self.subproid_var = StringVar()
            self.subprodetails_var = StringVar()
            self.subprorate_var = StringVar()
            self.subprocessno_var = StringVar()
            self.editsubprocessid_var = StringVar()

            self.searchbar_var = StringVar()

            existingdeps = department_database().existing_departments()
            d = [""]
            for i in existingdeps:
                d.append(i)
            #   Order Entry
            self.orderidentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.orderid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.orderidentry.place(x=130, y=30, height=24, width=170)
            self.factorypoentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.factorypo_var, state="readonly", readonlybackground=self.white)
            self.factorypoentry.place(x=440, y=30, height=24, width=170)
            self.customerpoentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.customerpo_var, state="readonly", readonlybackground=self.white)
            self.customerpoentry.place(x=130, y=65, height=24, width=170)
            self.orderdescriptionentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.description_var, state="readonly", readonlybackground=self.white)
            self.orderdescriptionentry.place(x=440, y=65, height=24, width=170)
            self.orderqtyentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.orderqty_var, font=("Time new rooman", 10, "bold"), state="readonly", readonlybackground=self.lightgreen)
            self.orderqtyentry.place(x=130, y=100, height=24, width=170)
            self.emptypeentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.ordertype_var, state="readonly", readonlybackground=self.white)
            self.emptypeentry.place(x=440, y=100, height=24, width=170)

            #   Rate Enrtry
            self.rateidentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.rateid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.rateidentry.place(x=130, y=30, height=24, width=170)
            self.depentry = Combobox(self.editempinfoframe, values=d, textvariable=self.depid_var,  state="readonly")
            self.depentry.place(x=440, y=30, height=24, width=170)
            self.detailsentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.details_var)
            self.detailsentry.place(x=440, y=65, height=24, width=170)
            self.processnoentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.processno_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.processnoentry.place(x=130, y=65, height=24, width=170)
            self.processnoidentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.editprocessid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.processnoidentry.place(x=130, y=100, height=24, width=170)
            
            self.searchentrybar = Entry(self.searchframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchbar_var)
            self.searchentrybar.place(x=190, y=11, height=24, width=130)
            self.searchentrybar.focus_set()

            #   Sub Process
            self.subprorateidentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.proidforsubpro_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.subprorateidentry.place(x=130, y=30, height=24, width=170)
            self.subproidentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.subproid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.subproidentry.place(x=440, y=30, height=24, width=170)
            self.subprodetailsentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.subprodetails_var)
            self.subprodetailsentry.place(x=130, y=65, height=24, width=170)
            self.subprorateentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen,font=("Time new rooman", 10, "bold"), fg=self.black, textvariable=self.subprorate_var)
            self.subprorateentry.place(x=440, y=65, height=24, width=170)
            self.subprocessnoentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.subprocessno_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.subprocessnoentry.place(x=130, y=100, height=24, width=170)
            self.editsubprocessnoidentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.editsubprocessid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.editsubprocessnoidentry.place(x=130, y=135, height=24, width=170)

            #   TREE
            self.v = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v.pack(side=RIGHT, fill=Y)
            self.v.place(x=823, y=192, height=310)

            self.tree = Treeview(self.newdepinfoframemain, height=14, columns=("C1", "C2", "C3", "C4", "C5"), show="headings", yscrollcommand=self.v.set)
            self.tree.place(x=1, y=192, width=820)

            self.tree.column("#1", anchor="nw", width=20)
            self.tree.column("#2", anchor="nw", width=110)
            self.tree.column("#3", anchor="nw", width=220)
            self.tree.column("#4", anchor=CENTER, width=45)
            self.tree.column("#5", anchor=CENTER, width=80)

            self.tree.heading("#1", text="id")
            self.tree.heading("#2", text="Department")
            self.tree.heading("#3", text="Details")
            self.tree.heading("#4", text="Added By")
            self.tree.heading("#5", text="Sequence")

            self.v.config(command=self.tree.yview)

            #   Tree2
            self.v2 = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v2.pack(side=RIGHT, fill=Y)
            self.v2.place(x=1467, y=192, height=310)

            self.tree2 = Treeview(self.newdepinfoframemain, height=14, columns=("C1", "C2", "C3", "C4"), show="headings", yscrollcommand=self.v2.set)
            self.tree2.place(x=845, y=192, width=620)

            self.tree2.column("#1", anchor="nw", width=20)
            self.tree2.column("#2", anchor="nw", width=115)
            self.tree2.column("#3", anchor=CENTER, width=20)
            self.tree2.column("#4", anchor=CENTER, width=40)

            self.tree2.heading("#1", text="id")
            self.tree2.heading("#2", text="Details/Name")
            self.tree2.heading("#3", text="Rate")
            self.tree2.heading("#4", text="Estimated Total")

            self.v2.config(command=self.tree2.yview)

            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.saveicon = ImageTk.PhotoImage(self.saveiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            self.editicon = ImageTk.PhotoImage(self.editiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.printicon = ImageTk.PhotoImage(self.printiconphoto)

            self.savebutton1 = Button(self.editempinfoframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_new_process, bd=2)
            self.savebutton1.place(x=630, y=30, height=40)
            self.editbutton1 = Button(self.editempinfoframe, width=73, text="Edit", font=("Time new rooman", 9, "bold", "italic"), image=self.editicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_process_editing, bd=2)
            self.editbutton1.place(x=630, y=80, height=40)

            self.backbutton = Button(self.searchframe, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.director_frame, bd=2)
            self.backbutton.place(x=550, y=5, height=40)
            self.clearbutton = Button(self.searchframe, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen, bd=2)
            self.clearbutton.place(x=650, y=5, height=40)
            self.printbutton = Button(self.searchframe, width=73, text="Print", font=("Time new rooman", 9, "bold", "italic"), image=self.printicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE)#, command=self.director_frame, bd=2)
            self.printbutton.place(x=750, y=5, height=40)
            self.searchbutton = Button(self.searchframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_order, bd=2)
            self.searchbutton.place(x=325, y=11, height=25)

            self.savebutton = Button(self.editorderinfoframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_new_sub_process, bd=2)
            self.savebutton.place(x=320, y=100, height=40)
            self.editbutton = Button(self.editorderinfoframe, width=73, text="Edit", font=("Time new rooman", 9, "bold", "italic"), image=self.editicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_sub_process_editing, bd=2)
            self.editbutton.place(x=420, y=100, height=40)

            #   Pop Up
            self.popup = Menu(self.tree, tearoff=0)
            self.popup.add_command(label="Add Sub-Process", command=self.selection_for_sub_process)
            self.popup.add_separator()
            self.popup.add_command(label="Edit", command=self.selection_for_editing)
            self.popup.add_separator()
            self.popup.add_command(label="Delete")
            self.popup.add_separator()

            self.tree.bind("<Button-3>", self.do_popup_tree)

            #   Pop Up 2
            self.popup2 = Menu(self.tree, tearoff=0)
            self.popup2.add_separator()
            self.popup2.add_command(label="Edit", command=self.selection_subpro_for_editing)
            self.popup2.add_separator()
            self.popup2.add_command(label="Delete")
            self.popup2.add_separator()

            self.tree2.bind("<Button-3>", self.do_popup_tree2)

            #   Bind
            self.root2.bind("<Control-s>", self.save_process_bind_function)
            self.root2.bind("<Control-f>", self.search_process_bind_function)
            self.root2.bind("<Control-b>", self.save_sub_process_bind_function)
            self.root2.bind("<Alt-b>", self.save_subprocess_editing_bind)
            self.root2.bind("<Alt-s>", self.save_edit_process_bind_function)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.back_bind_function)
        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Search Order
    def search_order(self):
        searchbar = (self.searchbar_var.get()).capitalize()
        if searchbar:
            for i in self.tree.get_children():
                self.tree.delete(i)
            self.orderid_var.set("")
            self.factorypo_var.set("")
            self.customerpo_var.set("")
            self.description_var.set("")
            self.orderqty_var.set("")
            self.ordertype_var.set("")
            self.rateid_var.set("")
            self.depid_var.set("")
            self.details_var.set("")
            self.processno_var.set("")
            self.editprocessid_var.set("")
            self.proidforsubpro_var.set("")
            self.subproid_var.set("")
            self.subprodetails_var.set("")
            self.subprorate_var.set("")
            self.subprocessno_var.set("")
            self.editsubprocessid_var.set("")
            for i in self.tree2.get_children():
                self.tree2.delete(i)
            existingorders = customer_order_database().search_all_order_data(searchbar)
            if existingorders == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif existingorders == "Empty":
                messagebox.showerror(parent=self.root2,title="No Match", message="No match found")
            elif existingorders:
                if len(existingorders) == 1:
                    self.detailsentry.focus_set()
                    for i in existingorders:
                        self.orderid_var.set(i[0])
                        self.factorypo_var.set(i[1])
                        self.customerpo_var.set(i[2])
                        self.description_var.set(i[3])
                        self.orderqty_var.set(i[4])
                        self.ordertype_var.set(i[5])
                    orderid = self.orderid_var.get()
                    proid = customer_order_process_database().process_id(orderid)
                    processdetails = customer_order_process_database().view_saved_process(orderid)
                    if proid == False or processdetails == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif proid:
                        
                        n = str(orderid)+"-"+str(proid)
                        self.processno_var.set(proid)
                        self.rateid_var.set(n)

                        for i in processdetails:
                            dep = str(i[3])+" "+str(i[8])
                            user = str(i[5])+"-"+str(i[7])
                            self.tree.insert("", END, iid=i[1], values=(i[1], dep, i[4], user))

                elif len(existingorders) > 1:
                    messagebox.showerror(parent=self.root2,title="Message", message="Search order id/Factory po")   
        else:
           messagebox.showerror(parent=self.root2,title="Empty", message="Searchbar is empty")

    #   Save Process
    def save_new_process(self):
        rateid = self.rateid_var.get()
        depid = self.depid_var.get()
        details = (self.details_var.get()).capitalize()
        processid = self.processno_var.get()
        orderid = self.orderid_var.get()
        user = self.username
        if rateid == "" or orderid == "" or processid == "" or depid == "":
            messagebox.showwarning(parent=self.root2, title="Empty", message="Reuired fields are empty")
        elif rateid and orderid and processid and depid:
            savenewrate = customer_order_process_database().save_new_process_database(rateid, depid, details, processid, orderid, user)
            if savenewrate == "Save":
                self.searchbar_var.set(orderid)
                self.search_order()
                messagebox.showinfo(parent=self.root2, title="Saved", message="New Process has been added")
            elif savenewrate == "Empty":
               messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
            elif savenewrate == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif savenewrate == "Exists":
                messagebox.showwarning(parent=self.root2,title="Exists", message="Process already exists for "+str(depid))

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
    
    #   Pop Up In Tree
    def do_popup_tree2(self, eve):
        r_id = self.tree2.focus()
        details = self.tree2.item(r_id)
        row = details['values']
        x = self.tree2.selection()
        if row != '' and x:
            if x[0] != "Total":
                self.popup2.selection = self.tree2.set(self.tree2.identify_row(eve.y))
                self.popup2.post(eve.x_root, eve.y_root)
            else:
                pass
        else:
            pass

    #   Selection for sub process
    def selection_for_sub_process(self):
        r_id = self.tree.focus()
        details = self.tree.item(r_id)
        row = details['values']
        x = self.tree.selection()
        if row != '' and x:
            self.proidforsubpro_var.set("")
            self.subproid_var.set("")
            self.subprodetails_var.set("")
            self.subprorate_var.set("")
            self.subprocessno_var.set("")
            self.editsubprocessid_var.set("")
            for i in self.tree2.get_children():
                self.tree2.delete(i)

            fpo = row[0]
            newsubprocessid = customer_order_process_database().new_sub_process_id(fpo)
            allsubprocess = customer_order_process_database().all_sub_process(fpo)
            if newsubprocessid == False or allsubprocess == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                totalestimated = 0
                totalonepc = 0
                self.subprodetailsentry.focus_set()
                newid = str(newsubprocessid)
                makeid = str(fpo)+"-"+str(newid)
                self.proidforsubpro_var.set(fpo)
                self.subproid_var.set(makeid)
                self.subprocessno_var.set(newid)
                orderqty = self.orderqty_var.get()
                for i in allsubprocess:
                    estimated = int(i[5]) * int(orderqty)
                    self.tree2.insert("", END, iid=i[1], values=(i[1], i[3], i[5], estimated))
                    totalestimated = totalestimated + estimated
                    totalonepc = totalonepc + int(i[5])
                self.tree2.insert("", END, iid="Total", values=("", "Total:", totalonepc, totalestimated))
        else:
            pass

    #   Save New Sub Process
    def save_new_sub_process(self):
        proid = self.subproid_var.get()
        rateid = self.proidforsubpro_var.get() 
        details = (self.subprodetails_var.get()).capitalize()
        newrate = self.subprorate_var.get()
        newid = self.subprocessno_var.get()
        if proid == "" or rateid == "" or details == "" or newrate == "" or newid == "":
            messagebox.showwarning(parent=self.root2, title="Empty", message="Reuired fields are empty")
        elif proid and rateid and details and newrate:
            if newrate.isdigit() == True:
                savesubprocess = customer_order_process_database().save_new_sub_process_database(proid, rateid, details, newrate, newid)
                if savesubprocess == "Save":
                    orderqty = self.orderqty_var.get()
                    newsubprocessid = customer_order_process_database().new_sub_process_id(rateid)
                    allsubprocess = customer_order_process_database().all_sub_process(rateid)
                    for i in self.tree2.get_children():
                        self.tree2.delete(i)
            
                    totalestimated = 0
                    totalonepc = 0
                    self.subprodetailsentry.focus_set()
                    for i in allsubprocess:
                        estimated = int(i[5]) * int(orderqty)
                        self.tree2.insert("", END, iid=i[1], values=(i[1], i[3], i[5], estimated))
                        totalestimated = totalestimated + estimated
                        totalonepc = totalonepc + int(i[5])
                    self.tree2.insert("", END, iid="Total", values=("", "Total:", totalonepc, totalestimated))

                    self.subprodetailsentry.focus_set()
                    self.subprodetails_var.set("")
                    self.subprorate_var.set("")
                    newid = str(newsubprocessid)
                    makeid = str(rateid)+"-"+str(newid)
                    self.subprocessno_var.set(newid)
                    self.subproid_var.set(makeid)
                    messagebox.showinfo(parent=self.root2, title="Saved", message="New Sub-Process of Process "+str(proid)+" has been added")
                elif savesubprocess == "Empty":
                    messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
                elif savesubprocess == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                messagebox.showerror(parent=self.root2,title="Integar", message="Rtae must be integar")    

    #   Selection For Process editing
    def selection_for_editing(self):
        r_id = self.tree.focus()
        details = self.tree.item(r_id)
        row = details['values']
        x = self.tree.selection()
        if row != '' and x:
            fpo = row[0]
            totaladdedamount = customer_order_process_database().total_added_amount_database(fpo)
            if totaladdedamount == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                self.rateid_var.set("")
                self.depid_var.set("")
                self.details_var.set("")
                self.processno_var.set("")
                self.editprocessid_var.set("")
                self.proidforsubpro_var.set("")
                self.subproid_var.set("")
                self.subprodetails_var.set("")
                self.subprorate_var.set("")
                self.subprocessno_var.set("")
                self.editsubprocessid_var.set("")
                for i in self.tree2.get_children():
                    self.tree2.delete(i)


                processid = row[0]
                depid = row[1]
                names = row[2]
                rate = row[3]
                self.editprocessid_var.set(processid)
                self.depid_var.set(depid)
                self.details_var.set(names)
                self.detailsentry .focus_set()

    #   Selection Sub-Process
    def selection_subpro_for_editing(self):
        r_id = self.tree2.focus()
        details = self.tree2.item(r_id)
        row = details['values']
        x = self.tree2.selection()
        if row != '' and x:
            self.subproid_var.set("")
            self.subprodetails_var.set("")
            self.subprorate_var.set("")
            self.subprocessno_var.set("")
            self.editsubprocessid_var.set("")
            self.subprodetails_var.set(row[1])
            self.subprorate_var.set(row[2])
            self.editsubprocessid_var.set(row[0])
            self.subprodetailsentry.focus_set()
        else:
            pass

    #   Save Process Editing
    def save_process_editing(self):
        proid = self.editprocessid_var.get()
        depid = self.depid_var.get()
        details = (self.details_var.get()).capitalize()
        orderid = self.orderid_var.get()
        if proid == "" or depid == "" or details == "" or orderid == "":
            messagebox.showwarning(parent=self.root2, title="Empty", message="Reuired fields are empty")
        elif proid and depid and details and orderid:
            editprocess = customer_order_process_database().save_process_editing_in_database(proid, depid, details, orderid)
            if editprocess == "Save":
                self.searchbar_var.set(orderid)
                self.search_order()
                messagebox.showinfo(parent=self.root2, title="Edit", message=str(proid)+" Process has been editted")
            elif editprocess == "Empty":
                messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
            elif editprocess == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Clear
    def clear_screen(self):
        self.searchentrybar.focus_set()
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.orderid_var.set("")
        self.factorypo_var.set("")
        self.customerpo_var.set("")
        self.description_var.set("")
        self.orderqty_var.set("")
        self.ordertype_var.set("")
        self.rateid_var.set("")
        self.depid_var.set("")
        self.details_var.set("")
        self.processno_var.set("")
        self.editprocessid_var.set("")
        self.proidforsubpro_var.set("")
        self.subproid_var.set("")
        self.subprodetails_var.set("")
        self.subprorate_var.set("")
        self.subprocessno_var.set("")
        self.editsubprocessid_var.set("")
        for i in self.tree2.get_children():
            self.tree2.delete(i)

    #   Save Bind
    def save_process_bind_function(self, eve):
        self.detailsentry.focus_set()
        self.save_new_process()

    #   Search Bind
    def search_process_bind_function(self, eve):
        self.searchentrybar.focus_set()
        self.search_order()

    #   Save Sub Process
    def save_sub_process_bind_function(self, eve):
        self.subprodetailsentry.focus_set()
        self.save_new_sub_process()

    #   Editing Save
    def save_edit_process_bind_function(self, eve):
        self.detailsentry.focus_set()
        self.save_process_editing()

    #   Back Bind
    def back_bind_function(self, eve):
        self.director_frame()

    #   Save Sub-Process Editing
    def save_subprocess_editing_bind(self, eve):
        self.subprodetailsentry.focus_set()
        self.save_sub_process_editing()

    #   Save Sub Process Editing
    def save_sub_process_editing(self):
        rateid = self.editsubprocessid_var.get()
        details = (self.subprodetails_var.get()).capitalize()
        newrate = self.subprorate_var.get()
        if rateid == "" or details == "" or newrate == "":
            messagebox.showwarning(parent=self.root2, title="Empty", message="Reuired fields are empty")
        elif rateid and details and newrate:
            if newrate.isdigit() == True:
                saveeditting = customer_order_process_database().save_editing_database(rateid, details, newrate)
                if saveeditting == "Save":
                    for i in self.tree2.get_children():
                        self.tree2.delete(i)
                    self.editsubprocessid_var.set("")
                    self.subprodetails_var.set("")
                    self.subprorate_var.set("")
                    proid = self.proidforsubpro_var.get()
                    orderqty = self.orderqty_var.get()
                    allsubprocess = customer_order_process_database().all_sub_process(proid)
                    totalestimated = 0
                    totalonepc = 0
                    self.subprodetailsentry.focus_set()
                    for i in allsubprocess:
                        estimated = int(i[5]) * int(orderqty)
                        self.tree2.insert("", END, iid=i[1], values=(i[1], i[3], i[5], estimated))
                        totalestimated = totalestimated + estimated
                        totalonepc = totalonepc + int(i[5])
                    self.tree2.insert("", END, iid="Total", values=("", "Total:", totalonepc, totalestimated))
                    messagebox.showinfo(parent=self.root2, title="Editted", message="Sub-Process has been editted")
                elif saveeditting == "Empty":
                    messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
                elif saveeditting == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                messagebox.showerror(parent=self.root2,title="Integar", message="Rtae must be integar")

#   Requsition
class requsition_class(director_class):
    #   init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)

    #   Requisition Frame
    def requisition_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.newempinfoframe = Frame(self.newdepinfoframemain, width=725, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe.place(x=0, y=0, height=450)
            self.newempinfoframe1 = Frame(self.newdepinfoframemain, width=725, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe1.place(x=725, y=0, height=450)

            #   Order LABELS
            self.addnewemployeelabel = Label(self.newempinfoframe, text="New Requisition Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=250, y=0)
            self.depidlabel = Label(self.newempinfoframe, text="id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=21, y=26)
            self.depidlabel = Label(self.newempinfoframe, text="Requisition#:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=320, y=26)
            self.depidlabel = Label(self.newempinfoframe, text="Department:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=8, y=61)
            self.empidlabel = Label(self.newempinfoframe, text="Details", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=470, y=61)

            self.addnewemployeelabel = Label(self.newempinfoframe1, text="Saved Requisition Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=250, y=0)
            self.emptypelabel = Label(self.newempinfoframe1, text="Added By:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=13, y=26)
            self.emptypelabel = Label(self.newempinfoframe1, text="Approved By:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=7, y=61)
            self.depidlabel = Label(self.newempinfoframe1, text="Clear By:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=96)
            self.depidlabel = Label(self.newempinfoframe1, text="Edit Requisition:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=2, y=131)
            self.depidlabel = Label(self.newempinfoframe1, text="Status:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=328, y=131)

            #   Search Label
            self.empidlabel = Label(self.newempinfoframe, text="Search Requisition:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=2, y=390)

            #   Database
            existingdeps = department_database().existing_departments()
            pendingrequsitions = requsition_database().pending_requisitions()
            requestid = requsition_database().new_requisition_id(self.username)


            #   Variable
            self.reno_var = StringVar()
            self.newrequestid_var = StringVar()
            self.depid_var = StringVar()
            self.editrequestid_var = StringVar()
            self.addeddate_var = StringVar()
            self.approvaldate_var = StringVar()
            self.cleardate_var = StringVar()
            self.reqstatus_var = StringVar()
            self.searchreq_var = StringVar()

            d = [""]
            for i in existingdeps:
                d.append(i)
            
            userid = ""
            for i in self.username:
                if i == "-":
                    break
                else:
                    userid = str(userid)+str(i)
            n = str(userid)+"-"+str(requestid)
            

            self.reno_var.set(requestid)
            self.newrequestid_var.set(n)

            #   Entry
            self.requestidentry1 = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.reno_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.requestidentry1.place(x=130, y=30, height=24, width=170)
            self.requestidentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.newrequestid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.requestidentry.place(x=440, y=30, height=24, width=170)
            self.depentry = Combobox(self.newempinfoframe, values=d, textvariable=self.depid_var,  state="readonly")
            self.depentry.place(x=130, y=65, height=24, width=170)
            self.emppicentry = Text(self.newempinfoframe, font=("Time new rooman", 10),bd=2, relief=GROOVE, bg=self.white, fg=self.black, state=NORMAL)
            self.emppicentry.place(x=1, y=100, height=200, width=700)
            self.emppicentry.focus_set()
            
            self.addeddateentry = Entry(self.newempinfoframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.addeddate_var, state="readonly", readonlybackground=self.white)
            self.addeddateentry.place(x=130, y=30, height=24, width=480)
            self.approvedateentry = Entry(self.newempinfoframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.approvaldate_var, state="readonly", readonlybackground=self.white)
            self.approvedateentry.place(x=130, y=65, height=24, width=480)
            self.cleardateentry = Entry(self.newempinfoframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.cleardate_var, state="readonly", readonlybackground=self.white)
            self.cleardateentry.place(x=130, y=100, height=24, width=480)
            self.cleardateentry = Entry(self.newempinfoframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.cleardate_var, state="readonly", readonlybackground=self.white)
            self.cleardateentry.place(x=130, y=100, height=24, width=480)
            self.editrequestidentry = Entry(self.newempinfoframe1,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.editrequestid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.editrequestidentry.place(x=130, y=135, height=24, width=170)
            self.reqstatusentry = Entry(self.newempinfoframe1,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.reqstatus_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.reqstatusentry.place(x=440, y=135, height=24, width=170)
            self.emppicentry1 = Text(self.newempinfoframe1, font=("Time new rooman", 10),bd=2, relief=GROOVE, bg=self.white, fg=self.black, state=DISABLED)
            self.emppicentry1.place(x=1, y=165, height=200, width=700)

            #   Search Entry
            self.searchentrybar = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchreq_var)
            self.searchentrybar.place(x=130, y=394, height=24, width=170)

            #   tree
            self.v3 = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v3.pack(side=RIGHT, fill=Y)
            self.v3.place(x=1069, y=455, height=368)

            self.tree = Treeview(self.newdepinfoframemain, height=17, columns=("C1", "C2", "C3", "C4", "C5"), show="headings", yscrollcommand=self.v3.set)
            self.tree.place(x=1, y=455, width=1066)

            self.tree.column("#1", anchor="nw", width=40)
            self.tree.column("#2", anchor="nw", width=480)
            self.tree.column("#3", anchor="nw", width=150)
            self.tree.column("#4", anchor="nw", width=100)
            self.tree.column("#5", anchor=CENTER, width=100)

            self.tree.heading("#1", text="id")
            self.tree.heading("#2", text="Details")
            self.tree.heading("#3", text="Department")
            self.tree.heading("#4", text="Added By")
            self.tree.heading("#5", text="Added Date")

            self.v3.config(command=self.tree.yview)

            for i in pendingrequsitions:
                reqdetails = str(i[4])
                dep = str(i[3])+" "+str(i[17])
                addby = str(i[5])+"-"+str(i[16])
                adddate = str(i[6])+" | "+str(i[7])
                wrapped_department = textwrap.fill(reqdetails, width=130)
                lines = wrapped_department.split('\n')
                for j, line in enumerate(lines):
                    if j == 0:
                        self.tree.insert("", END, iid=i[2], values=(i[2], line, dep, addby, adddate))
                    else:
                        self.tree.insert("", END, values=("", line, "", "", ""))


            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.saveicon = ImageTk.PhotoImage(self.saveiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            self.editicon = ImageTk.PhotoImage(self.editiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)

            self.editbutton = Button(self.newempinfoframe1, width=73, text="Edit", font=("Time new rooman", 9, "bold", "italic"), image=self.editicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE)#, command=self.save_editing, bd=2)
            self.editbutton.place(x=280, y=370, height=40)
            self.backbutton = Button(self.newempinfoframe, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.director_frame, bd=2)
            self.backbutton.place(x=180, y=305, height=40)
            self.clearbutton = Button(self.newempinfoframe, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen, bd=2)
            self.clearbutton.place(x=280, y=305, height=40)
            self.savebutton = Button(self.newempinfoframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_requisition, bd=2)
            self.savebutton.place(x=380, y=305, height=40)

            self.searchbutton = Button(self.newempinfoframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.serach_requistion, bd=2)
            self.searchbutton.place(x=310, y=394, height=25)

            #   Bind
            self.root2.bind("<Control-s>", self.bind_save_req)
            self.root2.bind("<Control-f>", self.bind_search_req)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.bind_back_screen)

        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Save Requisition
    def save_requisition(self):
        depid = self.depid_var.get()
        details = (self.emppicentry.get("1.0", END)).capitalize()
        reqno = self.newrequestid_var.get()
        reqid = self.reno_var.get()
        adddate = str(self.current_date())
        addtime = str(self.current_time())
        if depid and len(details) > 1 and reqno and reqid:
            saverequest = requsition_database().save_requisition_database(reqid, reqno, depid, details, self.username, adddate, addtime)
            if saverequest == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif saverequest == "Empty":
                messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
            elif saverequest == "Save":
                self.clear_screen()
                messagebox.showinfo(parent=self.root2, title="Saved", message="New requisition has been added")
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")

    #   Clear Screen
    def clear_screen(self):
        self.reno_var.set("")
        self.newrequestid_var.set("")
        self.depid_var.set("")
        self.editrequestid_var.set("")
        self.searchreq_var.set("")
        self.addeddate_var.set("")
        self.approvaldate_var.set("")
        self.cleardate_var.set("")
        self.reqstatus_var.set("")
        self.emppicentry.delete("1.0", END)
        self.emppicentry.focus_set()
        self.emppicentry1.config(state=NORMAL)
        self.emppicentry1.delete("1.0", END)
        self.emppicentry1.config(state=DISABLED)
        pendingrequsitions = requsition_database().pending_requisitions()
        requestid = requsition_database().new_requisition_id(self.username)
        userid = ""
        for i in self.username:
            if i == "-":
                break
            else:
                userid = str(userid)+str(i)
        n = str(userid)+"-"+str(requestid)
        self.reno_var.set(requestid)
        self.newrequestid_var.set(n)
        self.tree.delete(*self.tree.get_children())
        for i in pendingrequsitions:
            reqdetails = str(i[4])
            dep = str(i[3])+" "+str(i[17])
            addby = str(i[5])+"-"+str(i[16])
            adddate = str(i[6])+" | "+str(i[7])
            wrapped_department = textwrap.fill(reqdetails, width=130)
            lines = wrapped_department.split('\n')
            for j, line in enumerate(lines):
                if j == 0:
                    self.tree.insert("", END, iid=i[2], values=(i[2], line, dep, addby, adddate))
                else:
                    self.tree.insert("", END, values=("", line, "", "", ""))
    
    #   Clear Screen1
    def clear_screen1(self):
        self.editrequestid_var.set("")
        self.addeddate_var.set("")
        self.approvaldate_var.set("")
        self.cleardate_var.set("")
        self.reqstatus_var.set("")
        self.emppicentry1.config(state=NORMAL)
        self.emppicentry1.delete("1.0", END)
        self.emppicentry1.config(state=DISABLED)
        

    #   Search Requisition
    def serach_requistion(self):
        reqno = self.searchreq_var.get()
        if reqno:
            reqdetails = requsition_database().general_requisition_database(reqno)
            if reqdetails == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif reqdetails == []:
                messagebox.showerror(parent=self.root2,title="No Match", message="No match found")
            elif reqdetails != []:
                self.clear_screen1()
                req = ""
                dep = ""
                reqinfo = ""
                addby = ""
                adddate = ""
                approveby = ""
                approvedate = ""
                clearby = ""
                cleardate = ""
                reqstatus = ""
                for i in reqdetails:
                    req = i[2]
                    reqinfo = i[4]
                    dep = str(i[3])+" "+str(i[19])
                    addby = str(i[5])+"-"+str(i[16])
                    adddate = str(i[6])+" | "+str(i[7])
                    approveby = str(i[9])+"-"+str(i[17])
                    approvedate = str(i[10])+" | "+str(i[11])
                    clearby =  str(i[15])+"-"+str(i[18])
                    cleardate = str(i[13])+" | "+str(i[14])
                    if i[12] == False:
                        reqstatus = None
                    elif i[12] == True:
                        reqstatus = "Clear"
                
                addinfo = str(adddate)+"\t\tuser:"+str(addby)
                approveinfo = str(approvedate)+"\t\tuser:"+str(approveby)
                clearinfo = str(cleardate)+"\t\tuser:"+str(clearby)
                self.editrequestid_var.set(req)
                self.addeddate_var.set(addinfo)
                self.approvaldate_var.set(approveinfo)
                self.cleardate_var.set(clearinfo)
                self.reqstatus_var.set(reqstatus)

                self.emppicentry1.config(state=NORMAL)
                self.emppicentry1.insert("1.0", "\t\t"+str(dep)+"\n")
                self.emppicentry1.insert("2.0", reqinfo)
                self.emppicentry1.config(state=DISABLED)

        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Searchbar is empty")

    #   Bind Save
    def bind_save_req(self, eve):
        self.emppicentry.focus_set()
        self.save_requisition()

    #   back Bind
    def bind_back_screen(self, eve):
        self.director_frame()

    #   Bind Search
    def bind_search_req(self, eve):
        self.searchentrybar.focus_set()
        self.serach_requistion()

#   Raw Material
class raw_material_class(director_class):
    #   init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)

    #    Raw Material Frame
    def raw_material_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.newempinfoframe = Frame(self.newdepinfoframemain, width=630, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe.place(x=0, y=0, height=190)
            self.searchframe = Frame(self.newdepinfoframemain, width=820, bg=self.gray, bd=4, relief=FLAT)
            self.searchframe.place(x=0, y=190, height=55)
            self.newarticleframe = Frame(self.newdepinfoframemain, width=670, bg=self.gray, bd=4, relief=FLAT)
            self.newarticleframe.place(x=821, y=0, height=240)
            self.editorderinfoframe = Frame(self.newdepinfoframemain, width=630, bg=self.gray, bd=4, relief=FLAT)
            self.editorderinfoframe.place(x=0, y=553, height=190)

            existingcategory = raw_material_database().existing_category()
            existingstores = database_class().all_stores_ad()

            #   TREE
            self.tree = Treeview(self.newdepinfoframemain, height=10, columns=("C1", "C2"), show="headings")
            self.tree.place(x=630, y=0, width=190)

            self.tree.column("#1", anchor=CENTER, width=80)
            self.tree.column("#2", anchor="nw", width=100)

            self.tree.heading("#1", text="Category id")
            self.tree.heading("#2", text="Category Name")

            for i in existingcategory:
                self.tree.insert("", END, iid=i[0], values=(i[0], i[1]))

            #   Pop Up
            self.popup = Menu(self.tree, tearoff=0)
            self.popup.add_separator()
            self.popup.add_command(label="Add Material", command=self.select_category)
            self.popup.add_separator()
            self.tree.bind("<Button-3>", self.do_popup_tree)

            #   DEP LABELS
            self.addnewemployeelabel = Label(self.newempinfoframe, text="New Material Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=230, y=0)
            self.depidlabel = Label(self.newempinfoframe, text="id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=21, y=26)
            self.depnamelabel = Label(self.newempinfoframe, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=320, y=26)
            self.empidlabel = Label(self.newempinfoframe, text="Material id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=2, y=61)
            self.emptypelabel = Label(self.newempinfoframe, text="Material Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=314, y=61)
            self.emptypelabel = Label(self.newempinfoframe, text="Unit:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=18, y=96)
            self.emptypelabel = Label(self.newempinfoframe, text="Size/Color/Brand:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=310, y=96)

            #   New Article
            self.addnewemployeelabel = Label(self.newarticleframe, text="New Article Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=230, y=0)
            self.depidlabel = Label(self.newarticleframe, text="id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=24, y=26)
            self.depnamelabel = Label(self.newarticleframe, text="Article id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=324, y=26)
            self.empidlabel = Label(self.newarticleframe, text="Material id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=6, y=61)
            self.emptypelabel = Label(self.newarticleframe, text="Material Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=314, y=61)
            self.emptypelabel = Label(self.newarticleframe, text="Unit:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=22, y=96)
            self.emptypelabel = Label(self.newarticleframe, text="Size/Color/Brand:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=310, y=96)
            self.emptypelabel = Label(self.newarticleframe, text="Article Details:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=2, y=131)
            self.depnamelabel = Label(self.newarticleframe, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=320, y=131)

            #   New Store
            self.addnewemployeelabel = Label(self.editorderinfoframe, text="New Store Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=230, y=0)
            self.depidlabel = Label(self.editorderinfoframe, text="User name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=5, y=26)
            self.depnamelabel = Label(self.editorderinfoframe, text="Password:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=310, y=26)
            self.depidlabel = Label(self.editorderinfoframe, text="Store Status:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=0, y=61)
            self.depidlabel = Label(self.editorderinfoframe, text="Store Type:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=310, y=61)
            self.depidlabel = Label(self.editorderinfoframe, text="id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=21, y=96)

            #   Search Label
            self.empidlabel = Label(self.searchframe, text="Search:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=8, y=7)
            self.empidlabel = Label(self.searchframe, text="Search in:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=225, y=7)

            #   Variable
            self.newid_var = StringVar()
            self.categoryid_var = StringVar()
            self.matid_var = StringVar()
            self.matname_var = StringVar()
            self.matunit_var = StringVar()
            self.matcolor_var = StringVar()

            self.newarticalid_var = StringVar()
            self.articleid_var = StringVar()
            self.articlematerilid_var = StringVar()
            self.articlematerialname_var = StringVar()
            self.articlematerilunit_var = StringVar()
            self.articlematerialcolor_var = StringVar()
            self.articledetails_var = StringVar()
            self.articlecategory_var= StringVar()

            self.searchbar_var = StringVar()
            self.searchin_var = StringVar()

            self.newid_var2 = StringVar()
            self.categoryid_var2 = StringVar()
            self.matid_var2 = StringVar()
            self.matname_var2 = StringVar()
            self.matunit_var2 = StringVar()
            self.matcolor_var2 = StringVar()
            self.articleid_var2 = StringVar()
            self.articledetails_var2 = StringVar()
            self.user_var2 = StringVar()
            self.artqty_var2 = StringVar()
            self.artprice_var2 = StringVar()
            self.details_var2 = StringVar()

            self.newusername_var = StringVar()
            self.newpassword_var = StringVar()
            self.storetype_var = StringVar()
            self.storestatus_var = StringVar()
            self.storeuserid_var = StringVar()

            s = ["", "Category id", "Material id", "Material Name", "Article id"]
            s_status = ["", "Activate", "Deactivate"]
            s_types = ["", "Main Store", "Sub-Store"]

            #   Entry
            self.orderidentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.newid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.orderidentry.place(x=125, y=30, height=24, width=170)
            self.factorypoentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.categoryid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.factorypoentry.place(x=440, y=30, height=24, width=170)
            self.customerpoentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.matid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.customerpoentry.place(x=125, y=65, height=24, width=170)
            self.orderdescriptionentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.matname_var)
            self.orderdescriptionentry.place(x=440, y=65, height=24, width=170)
            self.orderdescriptionentry.focus_set()
            self.emptypeentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.matunit_var)
            self.emptypeentry.place(x=125, y=100, height=24, width=170)
            self.matcolorentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.matcolor_var)
            self.matcolorentry.place(x=440, y=100, height=24, width=170)

            #   Article Entry
            self.articlidentry = Entry(self.newarticleframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.newarticalid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articlidentry.place(x=125, y=30, height=24, width=170)
            self.articlenewidentry = Entry(self.newarticleframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articleid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articlenewidentry.place(x=440, y=30, height=24, width=170)
            self.articlematidentry = Entry(self.newarticleframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articlematerilid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articlematidentry.place(x=125, y=65, height=24, width=170)
            self.articlematnameentry = Entry(self.newarticleframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articlematerialname_var, state="readonly", readonlybackground=self.white)
            self.articlematnameentry.place(x=440, y=65, height=24, width=170)
            self.artcilematunitentry = Entry(self.newarticleframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articlematerilunit_var, state="readonly", readonlybackground=self.white)
            self.artcilematunitentry.place(x=125, y=100, height=24, width=170)
            self.articlematcolorentry = Entry(self.newarticleframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articlematerialcolor_var, state="readonly", readonlybackground=self.white)
            self.articlematcolorentry.place(x=440, y=100, height=24, width=170)
            self.articlecategoryentry = Entry(self.newarticleframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articlecategory_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articlecategoryentry.place(x=440, y=135, height=24, width=170)
            self.articledetailsentry = Entry(self.newarticleframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articledetails_var)
            self.articledetailsentry.place(x=125, y=135, height=24, width=170)

            #   New Store
            self.newstorenameentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.newusername_var, font=("Time new rooman", 9, "bold"))
            self.newstorenameentry.place(x=125, y=30, height=24, width=170)
            self.newstorepasswordentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.newpassword_var, font=("Time new rooman", 9, "bold"))
            self.newstorepasswordentry.place(x=440, y=30, height=24, width=170)
            self.storestatusentry = Combobox(self.editorderinfoframe, values=s_status, textvariable=self.storestatus_var,  state="readonly")
            self.storestatusentry.place(x=125, y=65, height=24, width=170)
            self.storetypeentry = Combobox(self.editorderinfoframe, values=s_types, textvariable=self.storetype_var,  state="readonly")
            self.storetypeentry.place(x=440, y=65, height=24, width=170)
            self.existstoreidentry = Entry(self.editorderinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.storeuserid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.existstoreidentry.place(x=125, y=100, height=24, width=170)

            #   Search Entry
            self.searchentrybar = Entry(self.searchframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchbar_var)
            self.searchentrybar.place(x=90, y=11, height=24, width=130)
            self.searchoptionentry = Combobox(self.searchframe, values=s, textvariable=self.searchin_var,  state="readonly")
            self.searchoptionentry.place(x=320, y=11, height=24, width=130)


            existingmaterials = raw_material_database().all_saved_material_names()

            #   Tree2
            self.v = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v.pack(side=RIGHT, fill=Y)
            self.v.place(x=823, y=240, height=312)

            self.tree2 = Treeview(self.newdepinfoframemain, height=14, columns=("C1", "C2", "C3", "C4", "C5"), show="headings", yscrollcommand=self.v.set)
            self.tree2.place(x=1, y=240, width=820)

            self.tree2.column("#1", anchor=CENTER, width=80)
            self.tree2.column("#2", anchor=CENTER, width=80)
            self.tree2.column("#3", anchor="nw", width=310)
            self.tree2.column("#4", anchor=CENTER, width=50)
            self.tree2.column("#5", anchor="nw", width=120)

            self.tree2.heading("#1", text="Material id")
            self.tree2.heading("#2", text="Category")
            self.tree2.heading("#3", text="Material")
            self.tree2.heading("#4", text="Unit")
            self.tree2.heading("#5", text="Size/Color/Brand")

            self.v.config(command=self.tree2.yview)
            for i in existingmaterials:
                unit = str(i[4])
                cate = str(i[5])+" "+str(i[7])
                self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))

            #   Pop Up
            self.popup2 = Menu(self.tree2, tearoff=0)
            self.popup2.add_separator()
            self.popup2.add_command(label="Add Article", command=self.select_material)
            self.popup2.add_separator()
            self.popup2.add_command(label="Edit Material", command=self.selection_material_for_editing)
            self.popup2.add_separator()
            self.tree2.bind("<Button-3>", self.do_popup_tree2)

            #   Tree3
            self.v2 = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v2.pack(side=RIGHT, fill=Y)
            self.v2.place(x=1469, y=240, height=312)

            self.tree3 = Treeview(self.newdepinfoframemain, height=14, columns=("C1", "C2"), show="headings", yscrollcommand=self.v2.set)
            self.tree3.place(x=845, y=240, width=620)

            self.tree3.column("#1", anchor=CENTER, width=80)
            self.tree3.column("#2", anchor="nw", width=310)

            self.tree3.heading("#1", text="Article id")
            self.tree3.heading("#2", text="Article Details")

            self.v2.config(command=self.tree3.yview)

            self.popup3 = Menu(self.tree2, tearoff=0)
            self.popup3.add_separator()
            self.popup3.add_command(label="Edit Article", command=self.select_article)
            self.popup3.add_separator()
            self.tree3.bind("<Button-3>", self.do_popup_tree3)

            self.tree5 = Treeview(self.newdepinfoframemain, height=13, columns=("C1", "C2", "C3", "C4", "C5"), show="headings", yscrollcommand=self.v2.set)
            self.tree5.place(x=632, y=553, width=720)

            self.tree5.column("#1", anchor=CENTER, width=80)
            self.tree5.column("#2", anchor=CENTER, width=100)
            self.tree5.column("#3", anchor=CENTER, width=100)
            self.tree5.column("#4", anchor=CENTER, width=50)
            self.tree5.column("#5", anchor=CENTER, width=80)

            self.tree5.heading("#1", text="id")
            self.tree5.heading("#2", text="Username")
            self.tree5.heading("#3", text="password")
            self.tree5.heading("#4", text="Store type")
            self.tree5.heading("#5", text="Status")

            for i in existingstores:
                storestatus = None
                if i[3] == False:
                    storestatus = "Deactivate"
                elif i[3] == True:
                    storestatus = "Activate"
                self.tree5.insert("", END, iid=i[0], values=(i[0],i[1],i[2], i[4], storestatus))

            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.saveicon = ImageTk.PhotoImage(self.saveiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.editicon = ImageTk.PhotoImage(self.editiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)

            self.backbutton = Button(self.newempinfoframe, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.director_frame, bd=2)
            self.backbutton.place(x=220, y=135, height=40)
            self.savebutton = Button(self.newempinfoframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_material, bd=2)
            self.savebutton.place(x=320, y=135, height=40)
            self.editbutton = Button(self.newempinfoframe, width=73, text="Edit", font=("Time new rooman", 9, "bold", "italic"), image=self.editicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_material_editing, bd=2)
            self.editbutton.place(x=420, y=135, height=40)

            self.clearbutton = Button(self.newarticleframe, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen, bd=2)
            self.clearbutton.place(x=230, y=170, height=40)
            self.savebutton1 = Button(self.newarticleframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_article, bd=2)
            self.savebutton1.place(x=330, y=170, height=40)
            self.editbutton1 = Button(self.newarticleframe, width=73, text="Edit", font=("Time new rooman", 9, "bold", "italic"), image=self.editicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_article_editing, bd=2)
            self.editbutton1.place(x=430, y=170, height=40)
            
            self.searchbutton = Button(self.searchframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_option, bd=2)
            self.searchbutton.place(x=480, y=11, height=25)

            self.savebutton2 = Button(self.editorderinfoframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_new_store, bd=2)
            self.savebutton2.place(x=320, y=100, height=40)
            self.editbutton1 = Button(self.editorderinfoframe, width=73, text="Edit", font=("Time new rooman", 9, "bold", "italic"), image=self.editicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_storeuser_editing, bd=2)
            self.editbutton1.place(x=420, y=100, height=40)

            #   Bind
            self.root2.bind("<Control-s>", self.save_material_bind)
            self.root2.bind("<Alt-s>", self.save_edit_material_bind)
            self.root2.bind("<Control-b>", self.save_new_article_bind)
            self.root2.bind("<Alt-b>", self.save_edit_article_bind)
            self.root2.bind("<Control-f>", self.search_material_bind)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.back_bind_function)
            self.tree5.bind("<Double-Button-1>", self.select_saved_store)
        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

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

    #   Pop Up In Tree
    def do_popup_tree2(self, eve):
        r_id = self.tree2.focus()
        details = self.tree2.item(r_id)
        row = details['values']
        x = self.tree2.selection()
        if row != '' and x:
            self.popup2.selection = self.tree2.set(self.tree2.identify_row(eve.y))
            self.popup2.post(eve.x_root, eve.y_root)
        else:
            pass

    #   Pop Up In Tree3
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

    #   Select Category
    def select_category(self):
        r_id = self.tree.focus()
        details = self.tree.item(r_id)
        row = details['values']
        x = self.tree.selection()
        if row != '' and x:
            catid = row[0]
            catname = row[1]
            newmaterialid = raw_material_database().new_material_id_database(catid)
            if newmaterialid == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                self.tree.selection_remove(x[0])
                self.clear_screen_4()
                cattype = str(catid)+" "+str(catname)
                matid = str(catid)+"-"+str(newmaterialid)
                self.newid_var.set(newmaterialid)
                self.categoryid_var.set(cattype)
                self.matid_var.set(matid)
                self.orderdescriptionentry.focus_set()

    #   Select Material
    def select_material(self):
        r_id = self.tree2.focus()
        details = self.tree2.item(r_id)
        row = details['values']
        x = self.tree2.selection()
        if row != '' and x:
            matid = row[0]
            cate = row[1]
            matname = row[2]
            matunit = row[3]
            matcolor = row[4]
            newarticleid = raw_material_database().new_material_article_id_database(matid)
            allarticlesofmaterial = raw_material_database().all_article_of_material(matid)
            if newarticleid == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                self.tree2.selection_remove(x[0])
                self.newid_var.set("")
                self.categoryid_var.set("")
                self.matid_var.set("")
                self.matname_var.set("")
                self.matunit_var.set("")
                self.matcolor_var.set("")
                for i in self.tree3.get_children():
                    self.tree3.delete(i)
                self.articledetailsentry.focus_set()
                new = str(matid)+"-"+str(newarticleid)
                self.newarticalid_var.set(newarticleid)
                self.articleid_var.set(new)
                self.articlematerilid_var.set(matid)
                self.articlematerialname_var.set(matname)
                self.articlematerilunit_var.set(matunit)
                self.articlematerialcolor_var.set(matcolor)
                self.articlecategory_var.set(cate)
                self.articledetails_var.set("")
                for i in allarticlesofmaterial:
                    self.tree3.insert("", END, iid=i[1], values=(i[1], i[3], i[4]))

    #   Save Material
    def save_material(self):
        newid = self.newid_var.get()
        category = self.categoryid_var.get()
        matid = self.matid_var.get()
        matname = (self.matname_var.get()).capitalize()
        matunit = (self.matunit_var.get()).capitalize()
        color = (self.matcolor_var.get()).capitalize()
        savenewmaterial = raw_material_database().save_raw_material_database(newid, category, matid, matname, matunit, color)
        if savenewmaterial == False:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
        elif savenewmaterial == "Empty":
            messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
        elif savenewmaterial == "Save":
            extract_catid = ""
            for i in category:
                if i == " ":
                    break
                else:
                    extract_catid = extract_catid + i
            newmaterialid = raw_material_database().new_material_id_database(extract_catid)
            existingmaterials = raw_material_database().all_saved_material_names()
            matid = str(extract_catid)+"-"+str(newmaterialid)
            self.matid_var.set(matid)
            self.newid_var.set(newmaterialid)
            self.matname_var.set("")
            self.matunit_var.set("")
            self.matcolor_var.set("")
            self.orderdescriptionentry.focus_set()
            for i in self.tree2.get_children():
                self.tree2.delete(i)
            for i in existingmaterials:
                unit = str(i[4])
                cate = str(i[5])+" "+str(i[7])
                self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))
            messagebox.showinfo(parent=self.root2, title="Save", message="Material has been added in Category "+str(category))

    #   Save Article
    def save_article(self):
        new_id = self.newarticalid_var.get()
        artid = self.articleid_var.get()
        matid = self.articlematerilid_var.get()
        artdetails = (self.articledetails_var.get()).capitalize()
        savenewarticle = raw_material_database().save_new_article_in_database(new_id, artid, matid, artdetails)
        if savenewarticle == False:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
        elif savenewarticle == "Empty":
            messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
        elif savenewarticle == "Save":
            self.articledetailsentry.focus_set()
            self.articledetails_var.set("")
            for i in self.tree3.get_children():
                self.tree3.delete(i)
            newarticleid = raw_material_database().new_material_article_id_database(matid)
            allarticlesofmaterial = raw_material_database().all_article_of_material(matid)
            new = str(matid)+"-"+str(newarticleid)
            self.newarticalid_var.set(newarticleid)
            self.articleid_var.set(new)
            for i in allarticlesofmaterial:
                self.tree3.insert("", END, iid=i[1], values=(i[1], i[3], i[4]))
            messagebox.showinfo(parent=self.root2, title="Save", message="Article has been added in Material "+str(matid))

    #   Save Material Bind
    def save_material_bind(self, eve):
        self.orderdescriptionentry.focus_set()
        self.save_material()

    #   Save New Article Bind
    def save_new_article_bind(self, eve):
        self.articledetailsentry.focus_set()
        self.save_article()

    #   Save Edit Bind
    def save_edit_material_bind(self, eve):
        self.orderdescriptionentry.focus_set()
        self.save_material_editing()

    #   Search Material Bind
    def search_material_bind(self, eve):
        self.searchentrybar.focus_set()
        self.search_option()
        
    #   Edit Material
    def selection_material_for_editing(self):
        r_id = self.tree2.focus()
        details = self.tree2.item(r_id)
        row = details['values']
        x = self.tree2.selection()
        if row != '' and x:
            self.tree2.selection_remove(x[0])
            self.orderdescriptionentry.focus_set()
            for i in self.tree3.get_children():
                self.tree3.delete(i)
            self.newid_var.set("")
            self.categoryid_var.set("")
            self.matid_var.set("")
            self.matname_var.set("")
            self.matunit_var.set("")
            self.matcolor_var.set("") 
            self.newarticalid_var.set("")
            self.articleid_var.set("")
            self.articlematerilid_var.set("")
            self.articlematerialname_var.set("")
            self.articlematerilunit_var.set("")
            self.articlematerialcolor_var.set("")
            self.articledetails_var.set("")
            self.articlecategory_var.set("")

            matid = row[0]
            cate = row[1]
            matname = row[2]
            matunit = row[3]
            matcolor = row[4]

            self.articlematerilid_var.set(matid)
            self.matname_var.set(matname)
            self.matunit_var.set(matunit)
            self.matcolor_var.set(matcolor)
            self.categoryid_var.set(cate)
            self.articlecategory_var.set(cate)

    #   Save Materil Editing
    def save_material_editing(self):
        matname = (self.matname_var.get()).capitalize()
        matunit = (self.matunit_var.get()).capitalize()
        color = (self.matcolor_var.get()).capitalize()
        oldid = self.articlematerilid_var.get()
        savenewmaterial = raw_material_database().save_raw_material_edit_database(matname, matunit, color, oldid)
        if savenewmaterial == False:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
        elif savenewmaterial == "Empty":
            messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
        elif savenewmaterial == "Save":
            self.clear_screen()
            messagebox.showinfo(parent=self.root2, title="Edit", message="Material has been editted")
        
    #   Clear Screen
    def clear_screen(self):
        self.orderdescriptionentry.focus_set()
        for i in self.tree3.get_children():
            self.tree3.delete(i)
        for i in self.tree2.get_children():
            self.tree2.delete(i)
        self.searchbar_var.set("")
        self.newid_var.set("")
        self.categoryid_var.set("")
        self.matid_var.set("")
        self.matname_var.set("")
        self.matunit_var.set("")
        self.matcolor_var.set("") 
        self.newarticalid_var.set("")
        self.articleid_var.set("")
        self.articlematerilid_var.set("")
        self.articlematerialname_var.set("")
        self.articlematerilunit_var.set("")
        self.articlematerialcolor_var.set("")
        self.articledetails_var.set("")
        self.articlecategory_var.set("")
        self.searchin_var.set("")
        self.newid_var2.set("")
        self.categoryid_var2.set("")
        self.matid_var2.set("")
        self.matname_var2.set("")
        self.matunit_var2.set("")
        self.matcolor_var2.set("")
        self.articleid_var2.set("")
        self.articledetails_var2.set("")
        self.user_var2.set("")
        self.artqty_var2.set("")
        self.artprice_var2.set("")
        self.details_var2.set("")
        self.newusername_var.set("")
        self.newpassword_var.set("")
        self.storetype_var.set("")
        self.storestatus_var.set("")
        self.storeuserid_var.set("")
        existingmaterials = raw_material_database().all_saved_material_names()
        for i in existingmaterials:
            unit = str(i[4])
            cate = str(i[5])+" "+str(i[7])
            self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))

    #   Clear Screen 2
    def clear_screen_2(self):
        self.searchentrybar.focus_set()
        for i in self.tree3.get_children():
            self.tree3.delete(i)
        for i in self.tree2.get_children():
            self.tree2.delete(i)
        self.newid_var.set("")
        self.categoryid_var.set("")
        self.matid_var.set("")
        self.matname_var.set("")
        self.matunit_var.set("")
        self.matcolor_var.set("") 
        self.newarticalid_var.set("")
        self.articleid_var.set("")
        self.articlematerilid_var.set("")
        self.articlematerialname_var.set("")
        self.articlematerilunit_var.set("")
        self.articlematerialcolor_var.set("")
        self.articledetails_var.set("")
        self.articlecategory_var.set("")
        self.newid_var2.set("")
        self.categoryid_var2.set("")
        self.matid_var2.set("")
        self.matname_var2.set("")
        self.matunit_var2.set("")
        self.matcolor_var2.set("")
        self.articleid_var2.set("")
        self.articledetails_var2.set("")
        self.user_var2.set("")
        self.artqty_var2.set("")
        self.artprice_var2.set("")
        self.details_var2.set("")

    #   Clear Screen #
    def clear_screen_4(self):
        self.newid_var.set("")
        self.categoryid_var.set("")
        self.matid_var.set("")
        self.matname_var.set("")
        self.matunit_var.set("")
        self.matcolor_var.set("") 
        self.newarticalid_var.set("")
        self.articleid_var.set("")
        self.articlematerilid_var.set("")
        self.articlematerialname_var.set("")
        self.articlematerilunit_var.set("")
        self.articlematerialcolor_var.set("")
        self.articledetails_var.set("")
        self.articlecategory_var.set("")
        self.newid_var2.set("")
        self.categoryid_var2.set("")
        self.matid_var2.set("")
        self.matname_var2.set("")
        self.matunit_var2.set("")
        self.matcolor_var2.set("")
        self.articleid_var2.set("")
        self.articledetails_var2.set("")
        self.user_var2.set("")
        self.artqty_var2.set("")
        self.artprice_var2.set("")
        self.details_var2.set("")

    #   Clear Screen 5
    def clear_screen5(self):
        self.newstorenameentry.focus_set()
        self.newusername_var.set("")
        self.newpassword_var.set("")
        self.storetype_var.set("")
        self.storestatus_var.set("")
        self.storeuserid_var.set("")
        existingstores = database_class().all_stores_ad()
        self.tree5.delete(*self.tree5.get_children())
        for i in existingstores:
            storestatus = None
            if i[3] == False:
                storestatus = "Deactivate"
            elif i[3] == True:
                storestatus = "Activate"
            self.tree5.insert("", END, iid=i[0], values=(i[0],i[1],i[2], i[4], storestatus))

    #   Search Option
    def search_option(self):
        searchvalue = (self.searchbar_var.get()).capitalize()
        searchoption = self.searchin_var.get()
        if searchvalue and searchoption:
            if searchoption == "Category id":
                categorywise = raw_material_database().search_in_category_search(searchvalue)
                if categorywise == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                elif categorywise == []:
                    self.clear_screen()
                    messagebox.showerror(parent=self.root2,title="No Match", message="Category not found")
                elif categorywise != []:
                    self.clear_screen_2()
                    for i in categorywise:
                        unit = str(i[4])
                        cate = str(i[5])+" "+str(i[7])
                        self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))
            elif searchoption == "Material id":
                materialwise = raw_material_database().search_as_material_id(searchvalue)
                if materialwise == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                elif materialwise == []:
                    self.clear_screen()
                    messagebox.showerror(parent=self.root2,title="No Match", message="Material not found")
                elif materialwise != []:
                    self.clear_screen_2()
                    for i in materialwise:
                        unit = str(i[4])
                        cate = str(i[5])+" "+str(i[7])
                        self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))
            elif searchoption == "Material Name":
                existingmaterials = raw_material_database().all_saved_material_names()
                if existingmaterials == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                else:
                    result = []
                    self.clear_screen_2()
                    for i in existingmaterials:
                        name = str(i[2]).lower()
                        if searchvalue.lower() in name:
                            result.append(i)
                    if result != []:
                        for i in result:
                            unit = str(i[4])
                            cate = str(i[5])+" "+str(i[7])
                            self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))
                    else:
                        self.clear_screen()
                        messagebox.showerror(parent=self.root2,title="No Match", message="Material Name not found")
            elif searchoption == "Article id":
                existingarticle = raw_material_database().search_as_article_id(searchvalue)
                if existingarticle == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                elif existingarticle == []:
                    self.clear_screen()
                    messagebox.showerror(parent=self.root2,title="No Match", message="Article not found")
                elif existingarticle != []:
                    self.clear_screen_2()
                    for i in existingarticle:
                        self.tree3.insert("", END, iid=i[1], values=(i[1], i[3]))
                        unit = str(i[9])
                        matcat = str(i[11])+" "+str(i[12])
                        self.tree2.insert("", END, iid=i[2], values=(i[6], matcat, i[7], unit, i[8]))
        else:
          messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")  

    #   Back Bind
    def back_bind_function(self, eve):
        self.director_frame()

    #   Save Article Edit Bind
    def save_edit_article_bind(self, eve):
        self.articledetailsentry.focus_set()
        self.save_article_editing()

    #   Select Article
    def select_article(self):
        r_id = self.tree3.focus()
        details = self.tree3.item(r_id)
        row = details['values']
        x = self.tree3.selection()
        if row != '' and x:
            self.newid_var.set("")
            self.categoryid_var.set("")
            self.matid_var.set("")
            self.matname_var.set("")
            self.matunit_var.set("")
            self.matcolor_var.set("") 
            self.newarticalid_var.set("")
            self.articleid_var.set("")
            self.articlematerialname_var.set("")
            self.articlematerilunit_var.set("")
            self.articlematerialcolor_var.set("")
            self.articledetails_var.set("")
            self.articlecategory_var.set("")

            artid = row[0]
            artname = row[1]
            
            self.articledetailsentry.focus_set()
            self.articleid_var.set(artid)
            self.articledetails_var.set(artname)
        else:
            pass

    #   Save Edititng
    def save_article_editing(self):
        selectedmat = self.articlematerilid_var.get()
        matid = self.newarticalid_var.get()
        articleid = self.articleid_var.get()
        articlename = (self.articledetails_var.get()).capitalize()
        savededitarticale = raw_material_database().save_article_editing_database(matid, articleid, articlename)
        if savededitarticale == False:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
        elif savededitarticale == "material id":
            messagebox.showerror(parent=self.root2,title="Disabled", message="Article editing is Disabled")
        elif savededitarticale == "Empty":
            messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
        elif savededitarticale == "Save":
            messagebox.showinfo(parent=self.root2, title="Edit", message="Article has been editted")
            newarticleid = raw_material_database().new_material_article_id_database(selectedmat)
            allarticlesofmaterial = raw_material_database().all_article_of_material(selectedmat)
            materialdetails = raw_material_database().search_as_material_id(selectedmat)
            for i in self.tree3.get_children():
                self.tree3.delete(i)
            self.articledetails_var.set("")
            self.articledetailsentry.focus_set()
            new = str(selectedmat)+"-"+str(newarticleid)
            self.newarticalid_var.set(newarticleid)
            self.articleid_var.set(new)
            self.articlematerilid_var.set(selectedmat)
            for i in materialdetails:
                matname = i[2]
                matunit = str(i[4])
                matcolor = i[3]
                cate = str(i[5])+" "+str(i[7])
                self.articlematerialname_var.set(matname)
                self.articlematerilunit_var.set(matunit)
                self.articlematerialcolor_var.set(matcolor)
                self.articlecategory_var.set(cate)

            for i in allarticlesofmaterial:
                self.tree3.insert("", END, iid=i[1], values=(i[1], i[3], i[4]))

    #   Save new Store
    def save_new_store(self):
        username = self.newusername_var.get()
        pasword = self.newpassword_var.get()
        storetype = self.storetype_var.get()
        storestatus = self.storestatus_var.get()
        if username and pasword and storetype and storestatus:
            savenewuser = database_class().save_new_user(username, pasword, storetype, storestatus)
            if savenewuser == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif savenewuser == "Exists":
                messagebox.showwarning(parent=self.root2,title="DataBase", message="Username already exists in database")
            elif savenewuser == "Save":
                self.clear_screen5()
                messagebox.showinfo(parent=self.root2,title="Save", message="New Store "+str(username)+" has been added in database as "+str(storetype))
        else:
           messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields") 

    #   Select Store
    def select_saved_store(self, eve):
        r_id = self.tree5.focus()
        details = self.tree5.item(r_id)
        row = details['values']
        x = self.tree5.selection()
        if row != '' and x:
            self.newstorenameentry.focus_set()
            self.newusername_var.set(row[1])
            self.newpassword_var.set(row[2])
            self.storetype_var.set(row[3])
            self.storestatus_var.set(row[4])
            self.storeuserid_var.set(row[0])
        else:
            pass

    #   Save Store User Editing
    def save_storeuser_editing(self):
        username = self.newusername_var.get()
        pasword = self.newpassword_var.get()
        storetype = self.storetype_var.get()
        storestatus = self.storestatus_var.get()
        userid = self.storeuserid_var.get()
        if username and pasword and storetype and storestatus and userid:
            savenewuser = database_class().update_user_database(username, pasword, storetype, storestatus, userid)
            if savenewuser == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif savenewuser == "Exists":
                messagebox.showwarning(parent=self.root2,title="DataBase", message="Username already exists in database")
            elif savenewuser == "Save":
                self.clear_screen5()
                messagebox.showinfo(parent=self.root2,title="Update", message="Store has been updated in database")
        else:
           messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields") 

#   Order Material Average
class order_stimated_avg(director_class):
    #   init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)
   
    #   Order Avg Frame
    def order_estimated_avg_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.newempinfoframe = Frame(self.newdepinfoframemain, width=650, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe.place(x=0, y=0, height=135)
            self.editempinfoframe = Frame(self.newdepinfoframemain, width=360, bg=self.gray, bd=4, relief=FLAT)
            self.editempinfoframe.place(x=618, y=0, height=135)
            self.searchframe = Frame(self.newdepinfoframemain, width=550, bg=self.gray, bd=4, relief=FLAT)
            self.searchframe.place(x=980, y=0, height=135)
            self.matinfoframe = Frame(self.newdepinfoframemain, width=760, bg=self.gray, bd=4, relief=FLAT)
            self.matinfoframe.place(x=0, y=435, height=210)
            self.avgmatinfoframe = Frame(self.newdepinfoframemain, width=760, bg=self.gray, bd=4, relief=FLAT)
            self.avgmatinfoframe.place(x=730, y=435, height=210)

            #   Order labels
            self.addnewemployeelabel = Label(self.newempinfoframe, text="Order Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=450, y=0)
            self.depidlabel = Label(self.newempinfoframe, text="Order id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.newempinfoframe, text="Factory-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=318, y=26)
            self.empidlabel = Label(self.newempinfoframe, text="Customer-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=3, y=61)
            self.emptypelabel = Label(self.newempinfoframe, text="Description:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=318, y=61)
            self.empidlabel = Label(self.newempinfoframe, text="Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=14, y=96)
            self.depnamelabel = Label(self.newempinfoframe, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=321, y=96)

            self.depidlabel = Label(self.editempinfoframe, text="Added Date:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=10, y=26)
            self.depidlabel = Label(self.editempinfoframe, text="Clearence:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=61)
            self.depidlabel = Label(self.editempinfoframe, text="Added By:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=13, y=96)

            #   New Article
            self.addnewemployeelabel = Label(self.matinfoframe, text="    Article Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=230, y=0)
            self.depnamelabel = Label(self.matinfoframe, text="Article id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=324, y=26)
            self.empidlabel = Label(self.matinfoframe, text="Material id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=6, y=26)
            self.emptypelabel = Label(self.matinfoframe, text="Material Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=5, y=61)
            self.emptypelabel = Label(self.matinfoframe, text="Unit:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=22, y=96)
            self.emptypelabel = Label(self.matinfoframe, text="Size/Color/Brand:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=310, y=96)
            self.emptypelabel = Label(self.matinfoframe, text="Article Details:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=2, y=131)
            self.depnamelabel = Label(self.matinfoframe, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=320, y=131)

            #   estimated Avg
            self.addnewemployeelabel = Label(self.avgmatinfoframe, text="Material Details for Order", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=230, y=0)
            self.depnamelabel = Label(self.avgmatinfoframe, text="Per Unit Usage:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=6, y=26)
            self.empidlabel = Label(self.avgmatinfoframe, text="Total Usage:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=334, y=26)
            self.emptypelabel = Label(self.avgmatinfoframe, text="Details:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=35, y=61)
            self.emptypelabel = Label(self.avgmatinfoframe, text="Use-in:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=35, y=96)

            #   Search Label
            self.empidlabel = Label(self.searchframe, text="Search Order:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=8, y=7)
            self.emptypelabel = Label(self.matinfoframe, text="Search:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=18, y=166)
            self.empidlabel = Label(self.matinfoframe, text="Search in:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=318, y=166)

            #   VAriables
            self.orderid_var = StringVar()
            self.factorypo_var = StringVar()
            self.customerpo_var = StringVar()
            self.description_var = StringVar()
            self.orderqty_var = StringVar()
            self.ordertype_var = StringVar()
            self.addeddate_var = StringVar()
            self.cleardate_var = StringVar()
            self.user_var = StringVar()
            self.searchbar_var = StringVar()
            self.searchmat_var = StringVar()
            self.searchin_var = StringVar()

            self.articleid_var = StringVar()
            self.articlematerilid_var = StringVar()
            self.articlematerialname_var = StringVar()
            self.articlematerilunit_var = StringVar()
            self.articlematerialcolor_var = StringVar()
            self.articledetails_var = StringVar()
            self.articlecategory_var= StringVar()

            self.stdavg_var = StringVar()
            self.estavg_var = StringVar()
            self.avgdetails_var = StringVar()
            self.usein_var = StringVar()

            existingmaterials = raw_material_database().all_saved_material_names()
            existingmatusein = order_average_database().existing_material_use()

            s = ["", "Category id", "Material id", "Material Name", "Article id"]
            useinlist = [""]

            for i in existingmatusein:
                n = str(i[0])+"-"+str(i[1])
                useinlist.append(n)
            #   Order Entry
            self.orderidentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.orderid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.orderidentry.place(x=130, y=30, height=24, width=170)
            self.factorypoentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.factorypo_var, state="readonly", readonlybackground=self.white)
            self.factorypoentry.place(x=440, y=30, height=24, width=170)
            self.customerpoentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.customerpo_var, state="readonly", readonlybackground=self.white)
            self.customerpoentry.place(x=130, y=65, height=24, width=170)
            self.orderdescriptionentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.description_var, state="readonly", readonlybackground=self.white)
            self.orderdescriptionentry.place(x=440, y=65, height=24, width=170)
            self.orderqtyentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.orderqty_var, font=("Time new rooman", 10, "bold"), state="readonly", readonlybackground=self.white)
            self.orderqtyentry.place(x=130, y=100, height=24, width=170)
            self.emptypeentry = Entry(self.newempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.ordertype_var, state="readonly", readonlybackground=self.white)
            self.emptypeentry.place(x=440, y=100, height=24, width=170)
            self.adddateentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.addeddate_var, state="readonly", readonlybackground=self.white)
            self.adddateentry.place(x=130, y=30, height=24, width=170)
            self.cleardateentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.cleardate_var, state="readonly", readonlybackground=self.white)
            self.cleardateentry.place(x=130, y=65, height=24, width=170)
            self.usernameentry = Entry(self.editempinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.user_var, state="readonly", readonlybackground=self.white)
            self.usernameentry.place(x=130, y=100, height=24, width=170)

            self.articlenewidentry = Entry(self.matinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articleid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articlenewidentry.place(x=440, y=30, height=24, width=170)
            self.articlematidentry = Entry(self.matinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articlematerilid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articlematidentry.place(x=125, y=30, height=24, width=170)
            self.articlematnameentry = Entry(self.matinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articlematerialname_var, state="readonly", readonlybackground=self.white)
            self.articlematnameentry.place(x=125, y=65, height=24, width=485)
            self.artcilematunitentry = Entry(self.matinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articlematerilunit_var, state="readonly", readonlybackground=self.white)
            self.artcilematunitentry.place(x=125, y=100, height=24, width=170)
            self.articlematcolorentry = Entry(self.matinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articlematerialcolor_var, state="readonly", readonlybackground=self.white)
            self.articlematcolorentry.place(x=440, y=100, height=24, width=170)
            self.articlecategoryentry = Entry(self.matinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articlecategory_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articlecategoryentry.place(x=440, y=135, height=24, width=170)
            self.articledetailsentry = Entry(self.matinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.articledetails_var, state="readonly", readonlybackground=self.white)
            self.articledetailsentry.place(x=125, y=135, height=24, width=170)

            self.stdavgentry = Entry(self.avgmatinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black, textvariable=self.stdavg_var)
            self.stdavgentry.place(x=130, y=30, height=24, width=170)
            self.estavgentry = Entry(self.avgmatinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black, textvariable=self.estavg_var)
            self.estavgentry.place(x=470, y=30, height=24, width=170)
            self.avgdetailsentry = Entry(self.avgmatinfoframe,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.avgdetails_var)
            self.avgdetailsentry.place(x=130, y=65, height=24, width=515)
            self.useinentry = Combobox(self.avgmatinfoframe, values=useinlist, textvariable=self.usein_var,  state="readonly")
            self.useinentry.place(x=130, y=100, height=24, width=170)

            #   Seacrh Entry
            self.searchentrybar = Entry(self.searchframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchbar_var)
            self.searchentrybar.place(x=130, y=11, height=24, width=240)
            self.searchentrybar.focus_set()
            self.searchentrybarmat = Entry(self.matinfoframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchmat_var)
            self.searchentrybarmat.place(x=125, y=170, height=24, width=170)
            self.searchoptionentry = Combobox(self.matinfoframe, values=s, textvariable=self.searchin_var,  state="readonly")
            self.searchoptionentry.place(x=440, y=170, height=24, width=170)

            # Create a dropdown tree
            self.dropdown_tree = Treeview(self.searchframe, height=3, columns=("C1"), show="headings")
            self.dropdown_tree.column("#1", anchor='nw', width=230)
            self.dropdown_tree.heading("#1", text='id/Factory Po/Customer Po')
            
            #   Tree
            self.v = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v.pack(side=RIGHT, fill=Y)
            self.v.place(x=1469, y=136, height=312)

            self.tree = Treeview(self.newdepinfoframemain, height=14, columns=("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"), show="tree", yscrollcommand=self.v.set)
            self.tree.place(x=1, y=136, width=1466)

            self.tree.column("#0", anchor=CENTER, width=60)

            self.tree.column("#1", anchor=CENTER, width=30)
            self.tree.column("#2", anchor="nw", width=400)
            self.tree.column("#3", anchor=CENTER, width=50)
            self.tree.column("#4", anchor=CENTER, width=50)
            self.tree.column("#5", anchor=CENTER, width=50)
            self.tree.column("#6", anchor=CENTER, width=50)
            self.tree.column("#7", anchor="nw", width=350)
            self.tree.column("#8", anchor=CENTER, width=50)
            
            self.v.config(command=self.tree.yview)

            #   Tree2
            self.v2 = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v2.pack(side=RIGHT, fill=Y)
            self.v2.place(x=823, y=643, height=209)

            self.tree2 = Treeview(self.newdepinfoframemain, height=9, columns=("C1", "C2", "C3", "C4", "C5"), show="headings", yscrollcommand=self.v2.set)
            self.tree2.place(x=1, y=643, width=820)

            self.tree2.column("#1", anchor=CENTER, width=80)
            self.tree2.column("#2", anchor=CENTER, width=80)
            self.tree2.column("#3", anchor="nw", width=310)
            self.tree2.column("#4", anchor=CENTER, width=50)
            self.tree2.column("#5", anchor="nw", width=120)

            self.tree2.heading("#1", text="Material id")
            self.tree2.heading("#2", text="Category")
            self.tree2.heading("#3", text="Material")
            self.tree2.heading("#4", text="Unit")
            self.tree2.heading("#5", text="Size/Color/Brand")

            self.v2.config(command=self.tree2.yview)
            for i in existingmaterials:
                unit = str(i[4])
                cate = str(i[5])+" "+str(i[7])
                self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))

            #   Pop Up
            self.popup2 = Menu(self.tree2, tearoff=0)
            self.popup2.add_separator()
            self.popup2.add_command(label="View Article", command=self.select_material)
            self.popup2.add_separator()
            self.tree2.bind("<Button-3>", self.do_popup_tree2)

            #   Tree3
            self.v2 = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v2.pack(side=RIGHT, fill=Y)
            self.v2.place(x=1469, y=643, height=209)

            self.tree3 = Treeview(self.newdepinfoframemain, height=9, columns=("C1", "C2"), show="headings", yscrollcommand=self.v2.set)
            self.tree3.place(x=845, y=643, width=620)

            self.tree3.column("#1", anchor=CENTER, width=80)
            self.tree3.column("#2", anchor="nw", width=310)

            self.tree3.heading("#1", text="Article id")
            self.tree3.heading("#2", text="Article Details")

            self.v2.config(command=self.tree3.yview)

            self.popup3 = Menu(self.tree2, tearoff=0)
            self.popup3.add_separator()
            self.popup3.add_command(label="Select Article", command=self.select_article)
            self.popup3.add_separator()
            self.tree3.bind("<Button-3>", self.do_popup_tree3)

            #   Bind
            self.searchentrybar.bind('<KeyRelease>', self.on_entry_change)
            self.dropdown_tree.bind("<Double-Button-1>", self.select_from_dropdown)

            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.saveicon = ImageTk.PhotoImage(self.saveiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.editicon = ImageTk.PhotoImage(self.editiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            self.printicon = ImageTk.PhotoImage(self.printiconphoto)

            self.searchbutton = Button(self.matinfoframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_option, bd=2)
            self.searchbutton.place(x=635, y=170, height=25)
            self.backbutton = Button(self.matinfoframe, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.director_frame, bd=2)
            self.backbutton.place(x=635, y=55, height=40)
            self.savebutton = Button(self.avgmatinfoframe, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_average, bd=2)
            self.savebutton.place(x=320, y=100, height=40)
            self.clearbutton = Button(self.searchframe, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen, bd=2)
            self.clearbutton.place(x=400, y=80, height=40)
            self.clearbutton1 = Button(self.matinfoframe, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_material3, bd=2)
            self.clearbutton1.place(x=635, y=110, height=40)
            self.printbutton = Button(self.searchframe, width=73, text="Print", font=("Time new rooman", 9, "bold", "italic"), image=self.printicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.print_out, bd=2)
            self.printbutton.place(x=400, y=35, height=40)

            #   Bind
            self.root2.bind("<Control-f>", self.search_material_bind)
            self.root2.bind("<Control-s>", self.save_avg_bind)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.back_bind_function)

        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Pop Up In Tree
    def do_popup_tree2(self, eve):
        r_id = self.tree2.focus()
        details = self.tree2.item(r_id)
        row = details['values']
        x = self.tree2.selection()
        if row != '' and x:
            self.popup2.selection = self.tree2.set(self.tree2.identify_row(eve.y))
            self.popup2.post(eve.x_root, eve.y_root)
        else:
            pass

     #   Pop Up In Tree3
    
    #   Pop Up in Tree3
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

    #   Entry Bind
    def on_entry_change(self, eve):
        search_text = (self.searchentrybar.get()).capitalize()
        if search_text:
            self.dropdown_tree.delete(*self.dropdown_tree.get_children())
            related_data = customer_order_database().search_all_order_data(search_text)
            if related_data == "Empty":
                self.dropdown_tree.place_forget()
            else:
                for i in related_data:
                    orderno = str(i[0])+" / "+str(i[1])+" / "+str(i[2])
                    self.dropdown_tree.insert('', END, iid=i[0], values=(orderno,))
                    self.dropdown_tree.place(x=self.searchentrybar.winfo_x(), y=self.searchentrybar.winfo_y() + self.searchentrybar.winfo_height())
        else:
            self.dropdown_tree.place_forget()

    #   Select Order
    def select_from_dropdown(self, eve):
        r_id = self.dropdown_tree.focus()
        details = self.dropdown_tree.item(r_id)
        row = details['values']
        x = self.dropdown_tree.selection()
        if row != '' and x:
            self.clear_screen()
            treeorderid = x[0]
            self.dropdown_tree.selection_remove(treeorderid)
            related_data = customer_order_database().search_all_order_data(treeorderid)
            if related_data == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                self.searchentrybarmat.focus_set()
                for i in related_data:
                    orderid = i[0]
                    factorypo = i[1]
                    customerpo = i[2]
                    description = i[3]
                    orderqty = i[4]
                    ordertype = i[5]
                    addeddate = str(i[6])+" / "+str(i[7])
                    cleardate = str(i[9])+" / "+str(i[10])
                    user = str(i[11])+"-"+str(i[12])
                    self.orderid_var.set(orderid)
                    self.factorypo_var.set(factorypo)
                    self.customerpo_var.set(customerpo)
                    self.description_var.set(description)
                    self.orderqty_var.set(orderqty)
                    self.ordertype_var.set(ordertype)
                    self.addeddate_var.set(addeddate)
                    self.cleardate_var.set(cleardate)
                    self.user_var.set(user)
                self.already_saved_standard_avg()
        else:
            pass

    #   clear Screen
    def clear_screen(self):
        self.orderid_var.set("")
        self.factorypo_var.set("")
        self.customerpo_var.set("")
        self.description_var.set("")
        self.orderqty_var.set("")
        self.ordertype_var.set("")
        self.addeddate_var.set("")
        self.cleardate_var.set("")
        self.user_var.set("")
        self.searchentrybar.focus_set()
        self.tree.delete(*self.tree.get_children())      
    
    #   Saved Standard Avg
    def already_saved_standard_avg(self):
        orderid = self.orderid_var.get()
        estimatedsavedavg = order_average_database().existing_estimated_avg(orderid)
        allusein = order_average_database().existing_material_use()
        if estimatedsavedavg == [] or allusein == []:
            pass
        else:
            self.tree.delete(*self.tree.get_children())
            for j in allusein:
                heading = str(j[0])+"-"+str(j[1])
                treeid = "use-"+str(j[0])
                parent = self.tree.insert("", END, iid=treeid, text=(heading), values=("id", "Name", "Unit", "Std Avg", "Est Avg", "Add by", "Details", "issued"))
                for i in estimatedsavedavg:
                    if str(j[0]) == str(i[6]):
                        avgid = i[0]
                        material = str(i[11])+"-"+str(i[10])
                        article = str(i[3])
                        stdavg = i[4]
                        estavg = i[5]
                        matunit = i[13]
                        details = i[7]
                        user = str(i[8])+"-"+str(i[15])
                        wrapped_text = textwrap.fill(details, width=300)
                        issuedqtyofart = 0 
                        self.tree.insert(parent, END, iid=avgid, values=(article, material, matunit, stdavg, estavg, user, wrapped_text, issuedqtyofart))
                        issuedqty = order_average_database().total_article_out_for_order(orderid, article)
                        if issuedqty == False:
                            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                            break
                        else:
                            for z in issuedqty:
                                if z[0] == None:
                                    issuedqtyofart = 0
                                else:
                                    issuedqtyofart = z[0]
                            
                            roundingissue = f"{float(issuedqtyofart):.2f}"
                            thkhonekbaad = float(roundingissue)
                            self.tree.set(avgid, column="C8", value=(thkhonekbaad))
                    else:
                        pass

    #   Select Material
    def select_material(self):
        r_id = self.tree2.focus()
        details = self.tree2.item(r_id)
        row = details['values']
        x = self.tree2.selection()
        if row != '' and x:
            matid = row[0]
            cate = row[1]
            matname = row[2]
            matunit = row[3]
            matcolor = row[4]
            newarticleid = raw_material_database().new_material_article_id_database(matid)
            allarticlesofmaterial = raw_material_database().all_article_of_material(matid)
            if newarticleid == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                self.tree2.selection_remove(x[0])
                self.articleid_var.set("")
                self.articlematerilid_var.set("")
                self.articlematerialname_var.set("")
                self.articlematerilunit_var.set("")
                self.articlematerialcolor_var.set("")
                self.articledetails_var.set("")
                self.articlecategory_var.set("")
                for i in self.tree3.get_children():
                    self.tree3.delete(i)
                self.articledetailsentry.focus_set()
                self.articlematerilid_var.set(matid)
                self.articlematerialname_var.set(matname)
                self.articlematerilunit_var.set(matunit)
                self.articlematerialcolor_var.set(matcolor)
                self.articlecategory_var.set(cate)
                
                for i in allarticlesofmaterial:
                    self.tree3.insert("", END, iid=i[1], values=(i[1], i[3], i[4]))

    #   Select Article
    def select_article(self):
        r_id = self.tree3.focus()
        details = self.tree3.item(r_id)
        row = details['values']
        x = self.tree3.selection()
        if row != '' and x:
            artid = row[0]
            articledetailsinstock = raw_material_database().article_stock_details_database(artid)
            articledetails = raw_material_database().article_details_from_database(artid)
            if articledetailsinstock == False or articledetails == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                self.stdavgentry.focus_set()
                self.articleid_var.set("")
                self.articlematerilid_var.set("")
                self.articlematerialname_var.set("")
                self.articlematerilunit_var.set("")
                self.articlematerialcolor_var.set("")
                self.articledetails_var.set("")
                self.articlecategory_var.set("")
                for i in articledetails:
                    cat = str(i[10])+" "+str(i[12])
                    unit = str(i[9])
                    self.articleid_var.set(i[1])
                    self.articledetails_var.set(i[3])
                    self.articlematerilid_var.set(i[6])
                    self.articlematerialname_var.set(i[7])
                    self.articlematerilunit_var.set(unit)
                    self.articlematerialcolor_var.set(i[8])
                    self.articlecategory_var.set(cat)
        else:
            pass

    #   Save Average
    def save_average(self):
        orderid = self.orderid_var.get()
        matid = self.articlematerilid_var.get()
        artid = self.articleid_var.get()
        valuestdavg = self.stdavg_var.get()
        valueestavg = self.estavg_var.get()
        usein = self.usein_var.get()
        details = (self.avgdetails_var.get()).capitalize()
        user = self.username
        if orderid and matid and artid and stdavg and estavg and usein:
            checking = self.check_float_values(stdavg, estavg)
            if checking == True:
                formatted_result = f"{float(valuestdavg):.2f}"
                stdavg = float(formatted_result)
                formatedest_result = f"{float(valueestavg):.2f}"
                estavg = float(formatedest_result)
                if float(stdavg) > 0 and float(estavg) > 0:
                    saveestimatedvalue = order_average_database().save_estimated_avg_databae(orderid, matid, artid, stdavg, estavg, usein, details, user)
                    if saveestimatedvalue == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif saveestimatedvalue == "Empty":
                        messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
                    elif saveestimatedvalue == "Exist":
                        messagebox.showerror(parent=self.root2,title="Exists", message="Article already exists for this order")
                    elif saveestimatedvalue == "Save":
                        self.stdavgentry.focus_set()
                        self.stdavg_var.set("")
                        self.estavg_var.set("")
                        self.usein_var.set("")
                        self.avgdetails_var.set("")
                        self.already_saved_standard_avg()
                        messagebox.showinfo(parent=self.root2,title="Saved", message="Material "+str(self.articlematerialname_var.get()+" Article "+str(self.articledetails_var.get()+" has been saved in order "+str(orderid))))
                else:
                    messagebox.showerror(parent=self.root2,title="Value", message="Std/Est can't be less then/equals to 0") 
            else:
                messagebox.showerror(parent=self.root2, title="Float Value", message="Std/Est must be float")
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")

    #   Check Float Values
    def check_float_values(self, stdavg, estavg):
        try:
            std = float(stdavg)
            est = float(estavg)
            return True
        except:
            return False

    #   Search material Bind
    def search_material_bind(self, eve):
        self.searchentrybarmat.focus_set()
        self.search_option()

    #   Back Bind
    def back_bind_function(self, eve):
        self.director_frame()

    #   Save Stand Avg bind
    def save_avg_bind(self, eve):
        self.stdavgentry.focus_set()
        self.save_average()

    #   Search Option
    def search_option(self):
        a = database_class().database_connection_check()
        if a == True: 
            searchvalue = (self.searchmat_var.get()).capitalize()
            searchoption = self.searchin_var.get()
            if searchvalue and searchoption:
                if searchoption == "Category id":
                    categorywise = raw_material_database().search_in_category_search(searchvalue)
                    if categorywise == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif categorywise == []:
                        self.clear_material3()
                        messagebox.showerror(parent=self.root2,title="No Match", message="Category not found")
                    elif categorywise != []:
                        self.tree2.delete(*self.tree2.get_children())
                        self.tree3.delete(*self.tree3.get_children())
                        for i in categorywise:
                            unit = str(i[4])
                            cate = str(i[5])+" "+str(i[7])
                            self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))
                elif searchoption == "Material id":
                    materialwise = raw_material_database().search_as_material_id(searchvalue)
                    if materialwise == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif materialwise == []:
                        self.clear_material3()
                        messagebox.showerror(parent=self.root2,title="No Match", message="Material not found")
                    elif materialwise != []:
                        self.tree2.delete(*self.tree2.get_children())
                        self.tree3.delete(*self.tree3.get_children())
                        for i in materialwise:
                            unit = str(i[4])
                            cate = str(i[5])+" "+str(i[7])
                            self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))
                elif searchoption == "Material Name":
                    existingmaterials = raw_material_database().all_saved_material_names()
                    if existingmaterials == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    else:
                        self.tree2.delete(*self.tree2.get_children())
                        self.tree3.delete(*self.tree3.get_children())
                        result = []
                        for i in existingmaterials:
                            name = str(i[2]).lower()
                            if searchvalue.lower() in name:
                                result.append(i)
                        if result != []:
                            for i in result:
                                unit = str(i[4])
                                cate = str(i[5])+" "+str(i[7])
                                self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))
                        else:
                            self.clear_material3()
                            messagebox.showerror(parent=self.root2,title="No Match", message="Material Name not found")
                elif searchoption == "Article id":
                    existingarticle = raw_material_database().search_as_article_id(searchvalue)
                    if existingarticle == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif existingarticle == []:
                        self.clear_material3()
                        messagebox.showerror(parent=self.root2,title="No Match", message="Article not found")
                    elif existingarticle != []:
                        self.tree2.delete(*self.tree2.get_children())
                        self.tree3.delete(*self.tree3.get_children())
                        for i in existingarticle:
                            self.tree3.insert("", END, iid=i[1], values=(i[1], i[3]))
                            unit = str(i[9])
                            matcat = str(i[11])+" "+str(i[12])
                            self.tree2.insert("", END, iid=i[2], values=(i[6], matcat, i[7], unit, i[8]))
            else:
                self.tree2.delete(*self.tree2.get_children())
                self.tree3.delete(*self.tree3.get_children())
                existingmaterials = raw_material_database().all_saved_material_names()
                for i in existingmaterials:
                    unit = str(i[4])
                    cate = str(i[5])+" "+str(i[7])
                    self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))
        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Clear Material
    def clear_material3(self):
        self.searchentrybarmat.focus_set()
        self.articleid_var.set("")
        self.articlematerilid_var.set("")
        self.articlematerialname_var.set("")
        self.articlematerilunit_var.set("")
        self.articlematerialcolor_var.set("")
        self.articledetails_var.set("")
        self.articlecategory_var.set("")
        self.tree2.delete(*self.tree2.get_children())
        self.tree3.delete(*self.tree3.get_children())
        existingmaterials = raw_material_database().all_saved_material_names()
        for i in existingmaterials:
            unit = str(i[4])
            cate = str(i[5])+" "+str(i[7])
            self.tree2.insert("", END, iid=i[1], values=(i[1], cate, i[2], unit, i[3]))

    #   Print Out
    def print_out(self):
        logo = "img/icon.png"
        treedata = self.tree.get_children()
        desktop_path = platform.node()

        orderid = self.orderid_var.get()
        factorypo = "Factory po:  "+str(self.factorypo_var.get())
        customerpo = self.customerpo_var.get()
        orderdescription = str(orderid)+"-"+str(self.description_var.get())
        orderqty = "Quantity:  "+str(self.orderqty_var.get())
        ordertype = "Category:  "+str(self.ordertype_var.get())
        orderadddate = "Add Date:  "+str(self.addeddate_var.get())
        ordercleardate = "Clear:  "+str(self.cleardate_var.get())
        orderaddby = "Add by:  "+str(self.user_var.get())

        pdf = FPDF(orientation='L', unit='mm', format='A4')
        pdf.set_fill_color(250, 250, 250)
        pdf.add_page()
        pdf.set_font("Arial", "B", size=10)
        pdf.cell(100, 8, txt="Littlewood Corporation", ln=0)
        pdf.image(logo, x=51, y=9, w=9, h=9)
        pdf.cell(55, 8, txt="Material Average Details", ln=0, align="C")
        pdf.ln(10)
        pdf.set_font("Arial", "B", size=8)
        pdf.cell(65, 6, txt="Customer Po:   "+str(customerpo), ln=0, border=True)
        pdf.cell(65, 6, txt="", ln=0, border=True)
        pdf.cell(65, 6, txt="", ln=0, border=True) 
        pdf.cell(80, 6, txt="Print by:   "+str(self.username)+"  "+str(desktop_path), ln=0, border=True)
        pdf.ln()
        pdf.cell(180, 6, txt=str(str(orderdescription)))
        pdf.ln()
        pdf.set_font("Arial", size=7)
        pdf.cell(65, 6, txt=str(factorypo), ln=0, border=True)
        pdf.cell(30, 6, txt=str(orderqty), ln=0, border=True)
        pdf.cell(50, 6, txt=str(orderadddate), ln=0, border=True)
        pdf.cell(50, 6, txt=str(orderaddby), ln=0, border=True)
        pdf.cell(50, 6, txt=str(ordercleardate), ln=0, border=True)
        pdf.cell(30, 6, txt=str(ordertype), ln=0, border=True)
        pdf.ln()

        for parent_item in treedata:
            pdf.ln(10)
            pdf.set_font("Arial", "B", size=8)
            details = self.tree.item(parent_item)
            description = details["text"]
            allvalues = details["values"]
            pdf.cell(180, 6, txt=str(str(description)))
            artid = allvalues[0]
            name = allvalues[1]
            unit = allvalues[2]
            stdavg = allvalues[3]
            estavg = allvalues[4]
            addby = allvalues[5]
            details = allvalues[6]
            issued = allvalues[7]
            pdf.ln()
            pdf.set_font("Arial", "B", size=7)
            pdf.cell(15, 6, txt=str(artid), ln=0, border=True, align='L')
            pdf.cell(85, 6, txt=str(name), ln=0, border=True, align='C')
            pdf.cell(15, 6, txt=str(unit), ln=0, border=True, align='C')
            pdf.cell(20, 6, txt=str(stdavg), ln=0, border=True, align='C')
            pdf.cell(25, 6, txt=str(estavg), ln=0, border=True, align='C')
            pdf.cell(20, 6, txt=str(addby), ln=0, border=True, align='C')
            pdf.cell(70, 6, txt=str(details), ln=0, border=True, align='C')
            pdf.cell(25, 6, txt=str(issued), ln=0, border=True, align='C')
            pdf.ln()
            child_items = self.tree.get_children(parent_item)
            for child_item in child_items:
                details1 = self.tree.item(child_item)
                childvalues = details1["values"]

                artdetails = childvalues[0]
                artvaluedetails =  childvalues[1]
                artunit =  childvalues[2]
                artstdavg =  childvalues[3]
                artestavg =  childvalues[4]
                artaddby =  childvalues[5]
                artdeatils =  childvalues[6]
                artissued =  childvalues[7]

                pdf.set_font("Arial", size=7)
                pdf.cell(15, 6, txt=str(artdetails), ln=0, border=True, align='L')
                pdf.cell(85, 6, txt=str(artvaluedetails), ln=0, border=True, align='L')
                pdf.cell(15, 6, txt=str(artunit), ln=0, border=True, align='C')
                pdf.cell(20, 6, txt=str(artstdavg), ln=0, border=True, align='C')
                pdf.cell(25, 6, txt=str(artestavg), ln=0, border=True, align='C')
                pdf.cell(20, 6, txt=str(artaddby), ln=0, border=True, align='L')
                pdf.cell(70, 6, txt=str(artdeatils), ln=0, border=True, align='L')
                pdf.cell(25, 6, txt=str(artissued), ln=0, border=True, align='C')
                pdf.ln()


        newpdfsave = filedialog.asksaveasfilename(
                        title=("Save Details"),
                        defaultextension=".pdf",
                        parent=self.root2)
        if newpdfsave:
            pdf.output(newpdfsave)
            messagebox.showinfo(parent=self.root2, title="Saved", message="File saved")
        else:
            pass

#   Production Details
class production_dep_details(director_class):
    #   init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)

    #   Employee Frame
    def production_details_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.searchframe = Frame(self.newdepinfoframemain, width=530, bg=self.gray, bd=4, relief=FLAT)
            self.searchframe.place(x=0, y=0, height=55)

            #   Search Label
            self.addnewemployeelabel = Label(self.newdepinfoframemain, text="Production Details/Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=630, y=0)
            self.empidlabel = Label(self.searchframe, text="Search Order:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=8, y=7)

            #   Variables
            self.searchbar_var = StringVar()
            self.searchtype_var = StringVar()
            self.typeprint = ""

            d = ["", "Process Details", "Wages", "Article"]
            #   Seacrh Entry
            self.searchentrybar = Entry(self.searchframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchbar_var)
            self.searchentrybar.place(x=110, y=11, height=24, width=150)
            self.searchentrybar.focus_set()
            self.orderdepentry = Combobox(self.searchframe, values=d, textvariable=self.searchtype_var,  state="readonly")
            self.orderdepentry.place(x=265, y=11, height=24, width=130)

            #   Tree
            self.v = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v.pack(side=RIGHT, fill=Y)
            self.v.place(x=1469, y=57, height=387)

            self.tree = Treeview(self.newdepinfoframemain, height=19, columns=("C1","C2","C3","C4","C5","C6", "C7", "C8"), show="tree", yscrollcommand=self.v.set)
            self.tree.place(x=1, y=57, width=1466)
             
            self.tree.column("#0", width=500)

            self.tree.column("#1", width=80)
            self.tree.column("#2", width=140)
            self.tree.column("#3", width=80)
            self.tree.column("#4", width=140)
            self.tree.column("#5", width=110)
            self.tree.column("#6", width=80)
            self.tree.column("#7", width=140)
            self.tree.column("#8", width=100)
            
            self.v.config(command=self.tree.yview)
            

            #   Button
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            self.printicon = ImageTk.PhotoImage(self.printiconphoto)
            

            self.searchbutton2 = Button(self.searchframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_order, bd=2)
            self.searchbutton2.place(x=420, y=11, height=25)
            
            self.backbutton = Button(self.newdepinfoframemain, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.director_frame, bd=2)
            self.backbutton.place(x=1200, y=450, height=40)
            self.clearbutton = Button(self.newdepinfoframemain, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen1, bd=2)
            self.clearbutton.place(x=1300, y=450, height=40)
            self.printbutton = Button(self.newdepinfoframemain, width=73, text="Print", font=("Time new rooman", 9, "bold", "italic"), image=self.printicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.print_out, bd=2)
            self.printbutton.place(x=1400, y=450, height=40)

            #   Bind
            self.root2.bind("<Control-f>", self.search_bind_fucn)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.back_bind_function)

        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Search Order
    def search_order(self):
        searchvalue = self.searchbar_var.get()
        searchtype = self.searchtype_var.get()
        if searchvalue and searchtype:
            orderinformation = customer_order_database().search_all_order_data(searchvalue)
            if orderinformation == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif orderinformation == "Empty":
                messagebox.showerror(parent=self.root2,title="No Match", message="no match found")
            elif orderinformation != []:
                self.clear_screen()
                if searchtype == "Process Details":
                    self.typeprint = "Process Details"
                    self.process_details(orderinformation)
                elif searchtype == "Wages":
                    self.typeprint = "Wages"
                    self.wages_details(orderinformation)
                elif searchtype == "Article":
                    self.typeprint = "Article"
                    self.article_details(orderinformation)
                
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Seacrh bar is empty")
                
    #   process Details
    def process_details(self, orderinformation):
        for a in orderinformation:
            orderid = a[0]
            factorypo = a[1]
            customerpo = a[2]
            orderdescription = a[3]
            orderqty = a[4]
            ordertype = a[5]
            orderadddate = str(a[6])+" / "+str(a[7])
            orderstatus = a[8]
            ordercleardate = str(a[9])+" / "+str(a[10])
            orderaddby = str(a[11])+"-"+str(a[12])

            doneprocess = []
            heading = str(orderid) + " - " +str(orderdescription)
            parent = self.tree.insert("", END, iid="order_no"+str(orderid), text=(heading), values=("Factory-Po", "Customer-Po", "Quantity", "Date/Time", "Add by", "", "Clear date/time", "Category"))
            
            self.tree.insert(parent, END, iid="orderdetails"+str(orderid), values=(factorypo, customerpo, orderqty, orderadddate, orderaddby, "", ordercleardate, ordertype))

            #   Article Details
            articaldetailsdatabase = customer_order_database().view_articals(orderid)
            orderdepartments = customer_order_process_database().all_pro_and_subpro_details_database(orderid)
            if articaldetailsdatabase == False or orderdepartments == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif orderdepartments == [] and articaldetailsdatabase != []:
                for b in articaldetailsdatabase:
                    artid = b[1]
                    prono = b[3]
                    size = b[4]
                    color = b[5]
                    totalqty = b[6]
                    

                    articletreeid = 'article of order'+str(artid)+'-'+str(orderid)
                    heading1 = str(artid) + " | " +str(prono) + " | " +str(size) + " | " +str(color)
                    parent1 = self.tree.insert(parent, END, iid=articletreeid, text=(heading1), values=("Quantity:", totalqty, "", "", "", ""))
            
            elif orderdepartments != [] and articaldetailsdatabase == []:
                for c in orderdepartments:
                    proid = str(c[1])
                    depid = c[3]
                    dep = str(c[3])+" "+str(c[8])
                    prodetails = str(c[4])
                    prousername = str(c[5])+"-"+str(c[7])

                    processtreeid = str(depid)+'-'+str(proid)
                    heading2 = str(proid) + " | " +str(prodetails)
                    parent2 = self.tree.insert(parent, END, iid=processtreeid, text=(heading2), values=("Department:", dep, "", "", "Add By:", prousername))

            elif orderdepartments != [] and articaldetailsdatabase != []:
                for c in orderdepartments:
                    proid = str(c[1])
                    depid = c[3]
                    dep = str(c[3])+" "+str(c[8])
                    prodetails = str(c[4])
                    prousername = str(c[5])+"-"+str(c[7])
                    qtyforprocess = 0

                    doneprocess.append(proid)
                    processtreeid = "processdetails"+str(depid)+'-'+str(proid)
                    
                    heading2 = str(proid) + " | " +str(dep)+ " | " +str(prodetails)
                    parent2 = self.tree.insert(parent, END, iid=processtreeid, text=(heading2), values=("For Process:", "", "", "", prousername, ""))

                    for b in articaldetailsdatabase:
                        artid = b[1]
                        prono = b[3]
                        size = b[4]
                        color = b[5]
                        totalqty = b[6]
                        fordepprocess = 0
                        completepc = 0
                        articletreeid = 'article of order process'+str(artid)+'-'+str(orderid)+"-"+str(proid)
                        heading1 = str(artid) + " | " +str(prono) + " | " +str(size) + " | " +str(color)
                        parent1 = self.tree.insert(parent2, END, iid=articletreeid, text=(heading1), values=("For Process:", "", totalqty, "Complete:", "", "", ""))

                        qtyinprocessofpro = customer_order_process_database().check_in_main_process_pc_database(proid, artid)
                        receiptofdatabase = order_receipts().process_receipts_database(depid, proid, artid)
                        subprocessdetails = customer_order_process_database().all_sub_process(proid)
                        if qtyinprocessofpro == False or receiptofdatabase == False or subprocessdetails == False:
                            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                            break
                        else:
                            qtyinprosum = 0
                            for proqty in qtyinprocessofpro:
                                if proqty[0] == None:
                                    qtyinprosum = 0
                                else:
                                    qtyinprosum = proqty[0]
                            
                            self.tree.set(articletreeid, column="C2", value=(qtyinprosum))
                            if receiptofdatabase == []:
                                self.tree.set(articletreeid, column="C7", value=("Remain : "+str(totalqty)))
                                self.tree.set(articletreeid, column="C2", value=(str(fordepprocess)))
                                self.tree.set(processtreeid, column="C2", value=(str(qtyforprocess)))
                            else:
                                qtyofreceipts = 0
                                for d in receiptofdatabase:
                                    receiptno = d[1]
                                    mainreceiptqty = d[5]
                                    receiptempid = d[8]
                                    receiptadddatetime = str(d[9])+ " / "+ str(d[10])
                                    receiptcomments = d[11]
                                    receiptstatus = d[12]
                                    receiptmakeruser = str(d[7])+"-"+str(d[19])
                                    receiptempname = str(d[17])+ " S/O "+ str(d[18])
                                    receiptclearuser = str(d[15])+"-"+str(d[20])
                                    cleardatetime = str(d[13])+ " / "+ str(d[14])
                                    qtyforprocess = qtyforprocess + mainreceiptqty
                                    qtyofreceipts = qtyofreceipts + mainreceiptqty
                                    subprowiseqtylist = 0

                                    mainreceipttreeid  = "mainreceipt"+str(receiptno)
                                    heading3 = str(receiptno) + " | " + str(receiptempid) + " | " + str(receiptempname)
                                    parent3 = self.tree.insert(parent1, END, iid=mainreceipttreeid, text=(heading3), values=("Complete:", "", mainreceiptqty, receiptadddatetime, receiptmakeruser))
                            
                                    if subprocessdetails == []:
                                        self.tree.set(mainreceipttreeid, column="C2", value=(str(subprowiseqtylist)))
                                    else:
                                        totalsubpro = len(subprocessdetails)
                                        totalofsubreceiptclearqty = 0
                                        for e in subprocessdetails:
                                            subproid = e[1]
                                            subprodetails = e[3]
                                            subprorate = e[5]
                                            startsubprocess = e[6]
                                            endsubprocess = e[7]
                                            subproofproid = e[3]

                                            subprotreeid = "subprocess-"+str(subproid)+"-"+str(mainreceipttreeid)

                                            heading4 = str(subproid) + " | " + str(subprodetails)
                                            parent4 = self.tree.insert(parent3, END, iid=subprotreeid, text=(heading4), values=("Complete:", "","", startsubprocess, "", endsubprocess))

                                            
                                            subprocesscomplete = 0

                                            subprocessqtydatabase = order_receipts().sub_receipt_information_on_database(receiptno, subproid)
                                            if subprocessqtydatabase == False:
                                                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                                                break
                                            elif subprocessqtydatabase == []:
                                                pass
                                            elif subprocessqtydatabase != []:
                                                checking = ""
                                                
                                                for f in subprocessqtydatabase:
                                                    if checking != str("subreceipt-"+str(f[6])):
                                                        subreceiptno = f[6]
                                                        subreceiptqty = f[4]
                                                        subreceiptadddateandtime = str(f[7])+ " / "+ str(f[8])
                                                        subreceiptaddby = str(f[9])+"-"+str(f[12])
                                                        subreceipttreeid = "subreceipt-"+str(f[6])

                                                        heading5 = str(subreceiptno)+ " | " + str(f[3])+ " | "+ str(f[13])+ " S/O "+ str(f[14])
                                                        parent5 = self.tree.insert(parent4, END, iid=subreceipttreeid, text=(heading5), values=("", "", subreceiptqty, subreceiptadddateandtime, subreceiptaddby," ", ""))
                                                        
                                                        checking = str("subreceipt-"+str(f[6]))
                                                        subqtyclear = order_receipts().sub_receipt_information_database(subreceiptno)
                                                        if subqtyclear == False:
                                                            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                                                            break
                                                        elif subqtyclear == []:
                                                            self.tree.set(subreceipttreeid, column="C7", value=("Remain : "+str(subreceiptqty)))
                                                            self.tree.set(subprotreeid, column="C2", value=(str(subprocesscomplete)))
                                                        elif subqtyclear != []:
                                                            subqtyforprocess = 0
                                                            for g in subqtyclear:
                                                                subreceiptclearqty = g[2]
                                                                subreceiptcleardatetimesub = str(g[3])+ " / "+ str(g[4])
                                                                subreceiptclearuser = str(g[5])+"-"+str(g[9])
                                                                subqtyforprocess = subqtyforprocess + subreceiptclearqty
                                                                subreceiptdetailstreeid = str(subreceipttreeid)+"-details-"+str(g[0])
                                                                self.tree.insert(parent5, END, iid=subreceiptdetailstreeid, values=("", "",subreceiptclearqty, "",  subreceiptclearuser, "", subreceiptcleardatetimesub))
                                                                subprocesscomplete = subprocesscomplete + subreceiptclearqty
                                                                totalofsubreceiptclearqty = totalofsubreceiptclearqty + subreceiptclearqty
                                                            self.tree.set(subprotreeid, column="C2", value=(str(subprocesscomplete)))
                                                    else:
                                                        pass
                                        
                                        checkreceiptpcs = totalsubpro * mainreceiptqty
                                        if checkreceiptpcs == totalofsubreceiptclearqty:
                                            completepc = completepc + mainreceiptqty
                                            self.tree.set(mainreceipttreeid, column="C2", value=(str(mainreceiptqty)))
                                        else:
                                            pass
                                r = totalqty - qtyofreceipts
                                self.tree.set(articletreeid, column="C7", value=("Remain : "+str(r)))
                        self.tree.set(articletreeid, column="C4", value=("Complete: "+str(completepc)))
                    self.tree.set(processtreeid, column="C2", value=(str(qtyforprocess)))
                         
    #   Wages Details
    def wages_details(self, orderinformation):
        for a in orderinformation:
            orderid = a[0]
            factorypo = a[1]
            customerpo = a[2]
            orderdescription = a[3]
            orderqty = a[4]
            ordertype = a[5]
            orderadddate = str(a[6])+" / "+str(a[7])
            orderstatus = a[8]
            ordercleardate = str(a[9])+" / "+str(a[10])
            orderaddby = str(a[11])+"-"+str(a[12])
            totalorderpaid = 0 

            doneprocess = []
            heading = str(orderid) + " - " +str(orderdescription)
            parent = self.tree.insert("", END, iid="order_no"+str(orderid), text=(heading), values=("Factory-Po", "Customer-Po", "Quantity", "Date/Time", "Add by", "", "Clear date/time", "Category"))
            
            self.tree.insert(parent, END, iid="orderdetails"+str(orderid), values=(factorypo, customerpo, orderqty, orderadddate, orderaddby, "", ordercleardate, ordertype))
            self.tree.insert(parent, END, iid="order_no_LABEL"+str(orderid), values=("Total Rate", "Estimated", "Quantity", "Amount", "Paid", "", "", ""))

            orderdepartments = customer_order_process_database().all_pro_and_subpro_details_database(orderid)
            if orderdepartments == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif orderdepartments == []:
                pass
            elif orderdepartments != []:

                for c in orderdepartments:
                    proid = str(c[1])
                    depid = c[3]
                    dep = str(c[3])+" "+str(c[8])
                    prodetails = str(c[4])

                    doneprocess.append(proid)
                    processtreeid = "wages-pro"+str(depid)+'-'+str(proid)
                    
                    heading2 = str(proid) + " | " +str(dep)+ " | " +str(prodetails)
                    parent2 = self.tree.insert(parent, END, iid=processtreeid, text=(heading2), values=("", "", "", "", "", ""))

                    totalpaidofpro = 0
                    receiptofdatabase = customer_order_process_database().wages_details_database(depid, proid)
                    subprocessdetails = customer_order_process_database().all_sub_process(proid)
                    if receiptofdatabase == False or subprocessdetails == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    else:
                        totalrateforprocess = 0
                        totalestimate = 0
                        
                        if subprocessdetails == []:
                            pass
                        else:
                            for e in subprocessdetails:
                                subproid = e[1]
                                subprodetails = e[3]
                                subprorate = e[5]
                                totalrateforprocess = totalrateforprocess + subprorate

                                estimatedamount = int(subprorate) * int(orderqty)
                                totalestimate = totalestimate + estimatedamount
                                subprotreeid = "wages-subpro"+str(subproid)

                                heading4 = str(subproid) + " | " + str(subprodetails)
                                parent4 = self.tree.insert(parent2, END, iid=subprotreeid, text=(heading4), values=("Rate: "+str(subprorate), "","", "", "", ""))

                                self.tree.set(subprotreeid, column="C2", value=(estimatedamount))

                                checksubproqtydetails = customer_order_process_database().subpro_qty_in_details_database(subproid)
                                if checksubproqtydetails == False:
                                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                                else:
                                    for f in checksubproqtydetails:
                                        if f[0] == None:
                                            qq = 0
                                            paid = 0
                                            totalpaidofpro = totalpaidofpro + paid
                                            totalorderpaid = totalorderpaid + totalpaidofpro
                                            estimatedsub = subprorate * qq
                                            self.tree.set(subprotreeid, column="C3", value=(str(qq)))
                                            self.tree.set(subprotreeid, column="C4", value=(str(estimatedsub)))
                                            self.tree.set(subprotreeid, column="C5", value=(str(paid)))
                                        else:
                                            qq = f[1]
                                            paid = f[2]
                                            totalpaidofpro = totalpaidofpro + paid
                                            totalorderpaid = totalorderpaid + totalpaidofpro
                                            estimatedsub = subprorate * qq
                                            self.tree.set(subprotreeid, column="C3", value=(str(qq)))
                                            self.tree.set(subprotreeid, column="C4", value=(str(estimatedsub)))
                                            self.tree.set(subprotreeid, column="C5", value=(str(paid)))
                                
                                

                            self.tree.set(processtreeid, column="C1", value=(totalrateforprocess))
                            self.tree.set(processtreeid, column="C2", value=(totalestimate))
                            self.tree.set(processtreeid, column="C5", value=(totalpaidofpro))
            self.tree.insert(parent, END, iid="totalamountoforder"+str(orderid), text=("Total:  "), values=(" ", "","", "", totalorderpaid, ""))

    #   Article Detasil
    def article_details(self, orderinformation):
        for a in orderinformation:
            orderid = a[0]
            factorypo = a[1]
            customerpo = a[2]
            orderdescription = a[3]
            orderqty = a[4]
            ordertype = a[5]
            orderadddate = str(a[6])+" / "+str(a[7])
            orderstatus = a[8]
            ordercleardate = str(a[9])+" / "+str(a[10])
            orderaddby = str(a[11])+"-"+str(a[12])

            doneprocess = []
            heading = str(orderid) + " - " +str(orderdescription)
            parent = self.tree.insert("", END, iid="order_no"+str(orderid), text=(heading), values=("Factory-Po", "Customer-Po", "Quantity", "Date/Time", "Add by", "", "Clear date/time", "Category"))
            
            self.tree.insert(parent, END, iid="orderdetails"+str(orderid), values=(factorypo, customerpo, orderqty, orderadddate, orderaddby, "", ordercleardate, ordertype))
            self.tree.insert(parent, END, iid="orderlabel"+str(orderid), values=("Art-id", "Color", "Size", "Quantity", "", "", "", ""))

            articaldetailsdatabase = customer_order_database().view_articals(orderid)
            if articaldetailsdatabase == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif articaldetailsdatabase == []:
                pass
            elif articaldetailsdatabase != []:
                for b in articaldetailsdatabase:
                    artid = b[1]
                    prono = b[3]
                    size = b[4]
                    color = b[5]
                    totalqty = b[6]
                    self.tree.insert(parent, END, iid="articles"+artid, values=(artid, color, size, totalqty, "", "", ""))

        #   clear Screen
    
    #   Clear Screen 1
    def clear_screen1(self):
        self.searchbar_var.set("")
        self.searchtype_var.set("")
        self.searchentrybar.focus_set()
        self.tree.delete(*self.tree.get_children())   
            
    #   clear Screen
    def clear_screen(self):
        self.searchentrybar.focus_set()
        self.tree.delete(*self.tree.get_children())   

    #   All Process Receipts
    def all_order_receipts(self):
        pass

    #   Print hardForm
    def print_out(self):
        logo = "img/icon.png"
        treedata = self.tree.get_children()
        customerpo = ""
        total = 0
        totalpaidoforders = 0
        desktop_path = platform.node()

        for parent_item in treedata:
            child_items = self.tree.get_children(parent_item)
            for child_item in child_items:
                if "orderdetails" in child_item:
                    details = self.tree.item(child_item)
                    allvalues = details["values"]
                    customerpo = allvalues[1]
                    total = total + allvalues[2]
                else:
                    pass

        pdf = FPDF(orientation='L', unit='mm', format='A4')
        pdf.set_fill_color(250, 250, 250)
        pdf.add_page()
        pdf.set_font("Arial", "B", size=10)
        pdf.cell(100, 8, txt="Littlewood Corporation", ln=0)
        pdf.image(logo, x=51, y=9, w=9, h=9)
        pdf.cell(55, 8, txt="Order Details", ln=0, align="C")
        pdf.ln(10)
        pdf.set_font("Arial", "B", size=8)
        pdf.cell(65, 6, txt="Customer Po:   "+str(customerpo), ln=0, border=True)
        pdf.cell(65, 6, txt="No of Order:   "+str(len(treedata)), ln=0, border=True)
        pdf.cell(65, 6, txt="Total Qty:   "+str(total), ln=0, border=True) 
        pdf.cell(80, 6, txt="Print by:   "+str(self.username)+"  "+str(desktop_path), ln=0, border=True)

        for parent_item in treedata:
            pdf.ln(10)
            pdf.set_font("Arial", "B", size=8)
            details = self.tree.item(parent_item)
            description = details["text"]
            allvalues = details["values"]
            pdf.multi_cell(180, 6, txt=str(str(description)))
            child_items = self.tree.get_children(parent_item)
            for child_item in child_items:
                details1 = self.tree.item(child_item)
                childvalues = details1["values"]
                if "orderdetails" in child_item:
                    fpo = str(allvalues[0]) + ":  "+str(childvalues[0])
                    totalqty = str(allvalues[2]) + ":  "+str(childvalues[2]) 
                    adddatetime = str(allvalues[3]) + ":  "+str(childvalues[3])
                    addby = str(allvalues[4]) + ":  "+str(childvalues[4])
                    clearby = str(allvalues[6]) + ":  "+str(childvalues[6])
                    categoryy = str(allvalues[7]) + ":  "+str(childvalues[7])

                    pdf.set_font("Arial", size=7)
                    pdf.cell(65, 6, txt=str(fpo), ln=0, border=True)
                    pdf.cell(30, 6, txt=str(totalqty), ln=0, border=True)
                    pdf.cell(50, 6, txt=str(adddatetime), ln=0, border=True)
                    pdf.cell(50, 6, txt=str(addby), ln=0, border=True)
                    pdf.cell(50, 6, txt=str(clearby), ln=0, border=True)
                    pdf.cell(30, 6, txt=str(categoryy), ln=0, border=True)

                    pdf.ln()
                
                elif "orderlabel" in child_item:
                    art = childvalues[0]
                    color = childvalues[1]
                    size = childvalues[2]
                    qtyofart = childvalues[3]
                    pdf.set_font("Arial", "B", size=7)
                    pdf.cell(40, 6, txt=str(art), ln=0, border=True)
                    pdf.cell(60, 6, txt=str(color), ln=0, border=True)
                    pdf.cell(25, 6, txt=str(size), ln=0, border=True)
                    pdf.cell(30, 6, txt=str(qtyofart), ln=0, border=True)
                    pdf.ln()
                elif "articles" in child_item:
                    art = childvalues[0]
                    color = childvalues[1]
                    size = childvalues[2]
                    qtyofart = childvalues[3]
                    pdf.set_font("Arial", size=7)
                    pdf.cell(40, 6, txt=str(art), ln=0, border=True)
                    pdf.cell(60, 6, txt=str(color), ln=0, border=True)
                    pdf.cell(25, 6, txt=str(size), ln=0, border=True)
                    pdf.cell(30, 6, txt=str(qtyofart), ln=0, border=True)
                    pdf.ln()
                elif "processdetails" in child_item:
                    prodetails = self.tree.item(child_item)
                    protext = prodetails['text']
                    provalue = prodetails['values']

                    forporcess = str(provalue[0])+"  "+str(provalue[1])
                    proaddby = str(protext)+"   \t\t\tAdd by: "+str(provalue[4])

                    pdf.set_font("Arial", "B", size=7)
                    pdf.ln()
                    pdf.cell(195, 6, txt=str(str(proaddby)), border=True)
                    pdf.cell(80, 6, txt=str(str(forporcess)), border=True)
                    pdf.ln()

                    childidofpro = self.tree.get_children(child_item)
                    for subchild in childidofpro:
                        if 'article of order process' in subchild:
                            childeatisl = self.tree.item(subchild)
                            childtext = childeatisl['text']
                            childvalue = childeatisl['values']

                            forpro = str(childvalue[0]) + " " + str(childvalue[1]) 
                            actualqty = "Total: "+str(childvalue[2])
                            completedetail = childvalue[3]
                            remaindetail = childvalue[6]

                            pdf.set_font("Arial", size=8)
                            pdf.cell(95, 6, txt=str(childtext), ln=0, border=True)
                            pdf.cell(30, 6, txt=str(actualqty), ln=0, border=True)
                            pdf.cell(35, 6, txt=str(forpro), ln=0, border=True)
                            pdf.cell(45, 6, txt=str(completedetail), ln=0, border=True)
                            pdf.cell(45, 6, txt=str(remaindetail), ln=0, border=True)
                            pdf.cell(25, 6, txt="", ln=0, border=True)
                            pdf.ln()


                            receiptsofpro = self.tree.get_children(subchild)
                            for receiptsno in receiptsofpro:
                                if 'mainreceipt' in receiptsno:
                                    receiptdetails1 = self.tree.item(receiptsno)
                                    receipttext = receiptdetails1["text"]
                                    receiptsvalue = receiptdetails1["values"]

                                    completereceipt = str(receiptsvalue[0])+" "+str(receiptsvalue[1])
                                    receiptqty = receiptsvalue[2]
                                    receiptdatetime = receiptsvalue[3]
                                    receiptaddby = "Add by: "+str(receiptsvalue[4])

                                    pdf.set_font("Arial", size=7)
                                    pdf.cell(100, 6, txt=str(receipttext), ln=0, border=True)
                                    pdf.cell(30, 6, txt=str(receiptqty), ln=0, border=True)
                                    pdf.cell(45, 6, txt=str(completereceipt), ln=0, border=True)
                                    pdf.cell(50, 6, txt=str(receiptdatetime), ln=0, border=True)
                                    pdf.cell(50, 6, txt=str(receiptaddby), ln=0, border=True)
                                    pdf.ln()

                elif "wages-pro" in child_item:
                    prodetails = self.tree.item(child_item)
                    protext = prodetails['text']
                    provalue = prodetails['values']

                    totalrate = "Total: "+str(provalue[0])
                    estimated = "Estimated: "+str(provalue[1])
                    totalpaid = "Paid: "+str(provalue[4])

                    pdf.set_font("Arial", "B", size=7)
                    pdf.ln()
                    pdf.cell(155, 6, txt=str(str(protext)))
                    pdf.cell(40, 6, txt=str(str(totalrate)), border=True)
                    pdf.cell(40, 6, txt=str(str(estimated)), border=True)
                    pdf.cell(40, 6, txt=str(str(totalpaid)), border=True)
                    pdf.ln()

                    childidofpro = self.tree.get_children(child_item)
                    for subchild in childidofpro:
                        childeatisl = self.tree.item(subchild)
                        childtext = childeatisl['text']
                        childvalue = childeatisl['values']

                        subrate = childvalue[0]
                        subestimated = "Estimated: "+str(childvalue[1])
                        subtotalpaid = "Paid: "+str(childvalue[4])
                        subqty = "Qty: "+str(childvalue[2])
                        subamount = "Amount: "+str(childvalue[3])

                        pdf.set_font("Arial", size=7)
                        pdf.cell(75, 6, txt=str(str(childtext)), border=True)
                        pdf.cell(40, 6, txt=str(str(subrate)), border=True)
                        pdf.cell(40, 6, txt=str(str(subestimated)), border=True)
                        pdf.cell(40, 6, txt=str(str(subtotalpaid)), border=True)
                        pdf.cell(40, 6, txt=str(str(subqty)), border=True)
                        pdf.cell(40, 6, txt=str(str(subamount)), border=True)
                        pdf.ln()
                elif "totalamountoforder" in child_item:
                    prodetails = self.tree.item(child_item)
                    protext = prodetails['text']
                    provalue = prodetails['values']

                    totalpaidoforders = totalpaidoforders + int(provalue[4])

                    tinfo = str(protext)+" "+str(int(provalue[4]))
                    pdf.set_font("Arial", "B", size=9)
                    pdf.cell(275, 6, txt=str(str(tinfo)), align="R")
                    pdf.ln()


        if totalpaidoforders != 0:
            abc = "Total: "+str(totalpaidoforders)
            pdf.set_font("Arial", "B", size=10)
            pdf.cell(275, 6, txt=abc, align="L")
            pdf.ln()
        else:
            pass

        newpdfsave = filedialog.asksaveasfilename(
                        title=("Save Details"),
                        defaultextension=".pdf",
                        parent=self.root2)
        if newpdfsave:
            pdf.output(newpdfsave)
            messagebox.showinfo(parent=self.root2, title="Saved", message="File saved")
        else:
            pass
     
    #   Search bin
    def search_bind_fucn(self, eve):
        self.searchentrybar.focus_set()
        self.search_order()

    #   back bind
    def back_bind_function(self, eve):
        self.director_frame()

#   Stock Details
class store_stock_details(director_class):
    #   init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)

    #   Stock Details
    def stock_details_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.stockframe = Frame(self.newdepinfoframemain, width=660, bg=self.gray, bd=4, relief=FLAT)
            self.stockframe.place(x=0, y=30, height=80)
            self.stockframe1 = Frame(self.newdepinfoframemain, width=720, bg=self.gray, bd=4, relief=FLAT)
            self.stockframe1.place(x=655, y=30, height=80)
            """self.matinfoframe = Frame(self.newdepinfoframemain, width=1450, bg=self.gray, bd=4, relief=FLAT)
            self.matinfoframe.place(x=0, y=0, height=210)
            self.editempinfoframe = Frame(self.newdepinfoframemain, width=650, bg=self.gray, bd=4, relief=FLAT)
            self.editempinfoframe.place(x=618, y=0, height=135)
            self.stockframe = Frame(self.newdepinfoframemain, width=1400, bg=self.gray, bd=4, relief=FLAT)
            self.stockframe.place(x=0, y=420, height=80)"""

            #   New Article
            self.addnewemployeelabel = Label(self.newdepinfoframemain, text="Material Store Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=620, y=0)

            self.emptypelabel = Label(self.stockframe, text="Search:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=18, y=4)
            self.empidlabel = Label(self.stockframe, text="Search in:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=318, y=4)
            self.depidlabel = Label(self.stockframe1, text="Store Details:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=1, y=4)
            self.depidlabel = Label(self.stockframe1, text="Select Store:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=319, y=4)

            #   Variable
            self.searchmat_var = StringVar()
            self.searchin_var = StringVar()
            self.storeusername_var1 = StringVar()
            self.savestore_var = StringVar()

            allstores = database_class().all_stores()
            all_store = [""]
            for i in allstores:
                storename = str(i[0])+"-"+str(i[1])
                all_store.append(storename)

            s = ["", "Material id", "Article id"]
            #   Entry
            self.searchoptionentry1 = Combobox(self.stockframe1, values=all_store, textvariable=self.savestore_var, state="readonly")
            self.searchoptionentry1.place(x=125, y=8, height=24, width=170)
            self.storedetailsentry1 = Entry(self.stockframe1,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, font=("Time new rooman", 9, "bold"), textvariable=self.storeusername_var1, state="readonly", readonlybackground=self.white)
            self.storedetailsentry1.place(x=440, y=8, height=24, width=170)


            #   Search
            self.searchentrybarmat = Entry(self.stockframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchmat_var)
            self.searchentrybarmat.place(x=125, y=8, height=24, width=170)
            self.searchentrybarmat.focus_set()
            self.searchoptionentry = Combobox(self.stockframe, values=s, textvariable=self.searchin_var,  state="readonly")
            self.searchoptionentry.place(x=440, y=8, height=24, width=170)

            #   Tree
            self.v3 = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v3.pack(side=RIGHT, fill=Y)
            self.v3.place(x=1469, y=80, height=348)

            self.tree4 = Treeview(self.newdepinfoframemain, height=16, columns=("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"), show="headings", yscrollcommand=self.v3.set)
            self.tree4.place(x=1, y=80, width=1466)

            self.tree4.column("#1", anchor=CENTER, width=80)
            self.tree4.column("#2", anchor="nw", width=310)
            self.tree4.column("#3", anchor=CENTER, width=50)
            self.tree4.column("#4", anchor="nw", width=120)
            self.tree4.column("#5", anchor=CENTER, width=80)
            self.tree4.column("#6", anchor="nw", width=220)
            self.tree4.column("#7", anchor=CENTER, width=80)
            self.tree4.column("#8", anchor=CENTER, width=80)
            self.tree4.column("#9", anchor="nw", width=135)

            self.tree4.heading("#1", text="Material id")
            self.tree4.heading("#2", text="Material")
            self.tree4.heading("#3", text="Unit")
            self.tree4.heading("#4", text="Size/Color/Brand")
            self.tree4.heading("#5", text="Article id")
            self.tree4.heading("#6", text="Article Details")
            self.tree4.heading("#7", text="Quantity")
            self.tree4.heading("#8", text="Price")
            self.tree4.heading("#9", text="Details")

            self.v3.config(command=self.tree4.yview)

            #   Button
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)

            self.searchbutton1 = Button(self.stockframe1, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_in_store_stock, bd=2)
            self.searchbutton1.place(x=625, y=8, height=25)

            #   Bind
            self.root2.bind("<Control-f>", self.search_material_bind)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.back_bind_function)
        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Clear Screen
    def clear_screen(self):
        self.searchmat_var.set("")
        self.searchin_var.set("")
        self.savestore_var.set("")
        self.storeusername_var1.set("")
        self.tree4.delete(*self.tree4.get_children())
        self.searchentrybarmat.focus_set()

    #   Clear Screen
    def clear_screen1(self):
        self.storeusername_var1.set("")
        self.tree4.delete(*self.tree4.get_children())

    #   Search Store
    def search_in_store_stock(self):
        a = database_class().database_connection_check()
        if a == True:
            searchvalue = (self.searchmat_var.get()).capitalize()
            searchoption = self.searchin_var.get()
            storeselection = self.savestore_var.get()
            if searchvalue and storeselection and searchoption:
                if searchoption == "Material id":
                    articleinstockdetails = raw_material_database().storewise_stock_database(storeselection, searchvalue)
                    userdetailsdatabase = database_class().user_details_database(storeselection)
                    materialnames = raw_material_database().search_as_material_id(searchvalue)
                    if userdetailsdatabase == False or articleinstockdetails == False or materialnames == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    else:
                        if articleinstockdetails == []:
                            self.clear_screen1()
                            messagebox.showwarning(parent=self.root2,title="Empty", message="Material not found in "+str(storeselection))
                        else:
                            self.clear_screen1()
                            userdetails = str(storeselection)+" "
                            for i in userdetailsdatabase:
                                userdetails = userdetails+" | "+str(i[4])
                            self.storeusername_var1.set(userdetails)
                            for i in materialnames:
                                unit = str(i[4])
                                self.tree4.insert("", END, iid=i[1], values=(i[1], i[2], unit, i[3])) 

                            for j in articleinstockdetails:
                                self.tree4.insert("", END, iid=j[3], values=("", "", "", "", j[3], j[6], j[4], "", j[5]))
                elif searchoption == "Article id":
                    articleinstockdetails = raw_material_database().article_from_selected_store_stock_database(storeselection, searchvalue)
                    userdetailsdatabase = database_class().user_details_database(storeselection)
                    if userdetailsdatabase == False or articleinstockdetails == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    else:
                        if articleinstockdetails == []:
                            self.clear_screen1()
                            messagebox.showwarning(parent=self.root2,title="Empty", message="Article not found in "+str(storeselection))
                        else:
                            self.clear_screen1()
                            userdetails = str(storeselection)+" "
                            for i in userdetailsdatabase:
                                userdetails = userdetails+" | "+str(i[4])
                            self.storeusername_var1.set(userdetails)
                            for i in articleinstockdetails:
                                self.tree4.insert("", END, iid=i[2], values=(i[2], i[8], i[10], i[9], "", "", "", "", ""))
                                self.tree4.insert("", END, iid=i[3], values=("", "", "", "", i[3], i[13], i[4], "", i[5]))
            elif searchvalue == "" and searchoption == "" and storeselection or searchvalue == "" or searchoption == "" and storeselection:
                stockinformation = raw_material_database().material_from_stock_database(storeselection)
                userdetailsdatabase = database_class().user_details_database(storeselection)
                if stockinformation == False or userdetailsdatabase == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                else:
                    self.clear_screen1()
                    userdetails = str(storeselection)+" "
                    for i in userdetailsdatabase:
                        userdetails = userdetails+" | "+str(i[4])
                    self.storeusername_var1.set(storeselection) 
                    matids = []
                    if stockinformation == []:
                        pass
                    else:
                        for i in stockinformation:
                            if i in matids:
                                pass
                            else:
                                matids.append(i)
                    if matids == []:
                        pass
                    else:
                        for i in matids:
                            self.tree4.insert("", END, iid=i[0], values=(i[0], i[3], i[5], i[4], "", "", "", "", ""))
                            articleinstockdetails = raw_material_database().storewise_stock_database(storeselection, i[0])
                            if articleinstockdetails == []:
                                pass
                            else:
                                for j in articleinstockdetails:
                                    self.tree4.insert("", END, iid=j[3], values=("", "", "", "", j[3], j[6], j[4], "", j[5]))
            elif searchvalue == "" and searchoption == "" and storeselection == "":
                self.clear_screen1()

    #   Back Bind
    def back_bind_function(self, eve):
        self.director_frame()

    #   Search material Bind
    def search_material_bind(self, eve):
        self.searchentrybarmat.focus_set()
        self.search_in_store_stock()

#   Employee Ledger
class employee_ledger_class(director_class):
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
            self.printicon = ImageTk.PhotoImage(self.printiconphoto)

            self.searchbutton = Button(self.searchframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.saerch_employee, bd=2)
            self.searchbutton.place(x=270, y=11, height=25)
            self.searchbutton1 = Button(self.searchframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_emp_balance_datewise, bd=2)
            self.searchbutton1.place(x=810, y=11, height=25)

            self.savebutton = Button(self.newempinfoframe1, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_new_credit_debit, bd=2)
            self.savebutton.place(x=330, y=100, height=40)
            self.backbutton = Button(self.editempinfoframe1, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.director_frame, bd=2)
            self.backbutton.place(x=150, y=131, height=40)
            self.clearbutton = Button(self.editempinfoframe1, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen1, bd=2)
            self.clearbutton.place(x=250, y=131, height=40)
            self.printbutton = Button(self.editempinfoframe1, width=73, text="Print", font=("Time new rooman", 9, "bold", "italic"), image=self.printicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.print_out, bd=2)
            self.printbutton.place(x=350, y=131, height=40)

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
                    self.tree.insert("", END, iid="datefrom", values=("", str(selection)+" |  From:  "+str(startdate)+"  To:  "+str(enddate), "", "", "", "", ""))
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
        self.director_frame()

    #   Save bind
    def save_bind_function(self, eve):
        self.categoryentry.focus_set()
        self.save_new_credit_debit()

    #   Print out
    def print_out(self):
        logo = "img/icon.png"
        treedata = self.tree.get_children()
        desktop_path = platform.node()

        dep = "Department: "+str(self.depid_var.get())
        designation = "Designation: "+str(self.designation_var.get())
        empid = str(self.empid_var.get())
        emptype = "Employee type: "+str(self.emptype_var.get())
        empfather = self.fathername_var.get()
        empname = str(empid)+"  "+str(self.empnaem_var.get())+" S/O "+str(empfather)
        empcnic = "CNIC: "+str(self.empcnic_var.get())
        empcell = "Contact#: "+str(self.empcell_var.get())
        empsalary = "Salary: "+str(self.empsalary_var.get())
        empaddress = "Address: "+str(self.empaddressentry.get("1.0", END))
        
        shorttermbalance = "Shortterm Balance: "+(self.shortterm_var.get())
        longtermbalance = "Longterm Balance: "+(self.longterm_var.get())
        emppic = ""
        a = database_class().database_connection_check()
        if a == True:
            emppic = "EMP-PICS/"+str(empid)+".png"
        else:
            emppic = ""

        pdf = FPDF(orientation='L', unit='mm', format='A4')
        pdf.set_fill_color(250, 250, 250)
        pdf.add_page()
        pdf.set_font("Arial", "B", size=10)
        pdf.cell(100, 8, txt="Littlewood Corporation", ln=0)
        pdf.image(logo, x=51, y=9, w=9, h=9)
        pdf.cell(55, 8, txt="Employee Ledger", ln=0, align="C")
        pdf.ln(10)
        pdf.set_font("Arial", "B", size=8)
        
        pdf.cell(65, 6, txt=str(dep), ln=0, border=True)
        pdf.cell(65, 6, txt=str(designation), ln=0, border=True)
        pdf.cell(65, 6, txt=str(emptype), ln=0, border=True) 
        pdf.cell(80, 6, txt="Print by:   "+str(self.username)+"  "+str(desktop_path), ln=0, border=True)
        pdf.ln()
        pdf.cell(195, 6, txt=str(empname), ln=0, border=True)
        pdf.ln()
        pdf.cell(40, 6, txt=str(empcnic), ln=0, border=True)
        pdf.cell(40, 6, txt=str(empcell), ln=0, border=True)
        pdf.cell(35, 6, txt=str(empsalary), ln=0, border=True)
        pdf.cell(40, 6, txt=str(shorttermbalance), ln=0, border=True)
        pdf.cell(40, 6, txt=str(longtermbalance), ln=0, border=True)
        if emppic:
            pdf.ln()
            pdf.image(emppic, x=210, y=27, w=37, h=30)
        else:
            pass
        pdf.ln(20)

        for data in treedata:
            details = self.tree.item(data)
            allvalues = details["values"]
            if "datefrom" in data:
                pdf.set_font("Arial", "B", size=8)
                pdf.cell(155, 6, txt=str(allvalues[1]), ln=0, border=True, align='L')
                pdf.ln()
                break
        pdf.set_font("Arial", "B", size=8)
        pdf.cell(30, 6, txt=str("Data/ Time"), ln=0, border=True, align='C')
        pdf.cell(125, 6, txt=str("Description"), ln=0, border=True, align='C')
        pdf.cell(30, 6, txt=str("Credit"), ln=0, border=True, align='C')
        pdf.cell(30, 6, txt=str("Debit"), ln=0, border=True, align='C')
        pdf.cell(30, 6, txt=str("balance"), ln=0, border=True, align='C')
        pdf.cell(30, 6, txt=str("Add by"), ln=0, border=True, align='C')
        pdf.ln()

        for data in treedata:
            details = self.tree.item(data)
            allvalues = details["values"]
            if "datefrom" in data:
                pass
            else:
                datatime = str(allvalues[0])
                ledgerdetail = str(allvalues[1])
                credit = str(allvalues[2])
                debit = str(allvalues[3])
                balance = str(allvalues[4])
                addby = str(allvalues[6])

                pdf.set_font("Arial", size=7)
                pdf.cell(30, 6, txt=datatime, ln=0, border=True, align='C')
                pdf.cell(125, 6, txt=ledgerdetail, ln=0, border=True, align='L')
                pdf.cell(30, 6, txt=credit, ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=debit, ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=balance, ln=0, border=True, align='C')
                pdf.cell(30, 6, txt=addby, ln=0, border=True, align='C')
                pdf.ln()


        newpdfsave = filedialog.asksaveasfilename(
                        title=("Save Details"),
                        defaultextension=".pdf",
                        parent=self.root2)
        if newpdfsave:
            pdf.output(newpdfsave)
            messagebox.showinfo(parent=self.root2, title="Saved", message="File saved")
        else:
            pass


