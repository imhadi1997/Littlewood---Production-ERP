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


class receipt_system:
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
            self.root2.resizable(False, False)
            self.root2.iconphoto(False, icon_photo)
            
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

            self.receipt_system_frame()
        else:
            messagebox.showerror(parent=self.root,title="Server Respone", message="Database connection lost")

    #   Receipt System Frame
    def receipt_system_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            self.root2backgroundphoto = Image.open("img/background.png")
            self.makereceipt = Image.open("img/receipt.png")
            self.subreceitpphoto = Image.open("img/subreceipt.png")
            self.clearreceiptphoto = Image.open("img/clear_receipt_icon.png")
            self.ordericonphoto = Image.open("img/order_icon.png")

            self.bg_photo = ImageTk.PhotoImage(self.root2backgroundphoto)
            self.bg_label = Label(self.root2, image=self.bg_photo, width=1500, height=116)
            self.bg_label.place(x=0, y=0)

            self.blankhomeframe = Frame(self.root2, width=1500, bd=3, bg=self.bgcolor, relief=FLAT)
            self.blankhomeframe.place(x=1, y=117, height=770)


            #   Make Receipt
            self.receipticon = ImageTk.PhotoImage(self.makereceipt)
            self.makereceiptbutton = Button(self.blankhomeframe, width=130,  text="New\nReceipt",font=("Time new rooman", 9, "bold", "italic"), image=self.receipticon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=make_receipt_class(self.root2, self.username, self.root).make_receipt_frame)
            self.makereceiptbutton.place(x=10, y=0, height=65)

            #   Job Card
            self.subreceipticon = ImageTk.PhotoImage(self.subreceitpphoto)
            self.subreceiptbutton = Button(self.blankhomeframe, width=130,  text="New\nSub\nReceipt",font=("Time new rooman", 9, "bold", "italic"), image=self.subreceipticon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=make_job_card_class(self.root2, self.username, self.root).job_card_frame)
            self.subreceiptbutton.place(x=150, y=0, height=65)

            #   Clear Receipt
            self.clearreceipticon = ImageTk.PhotoImage(self.clearreceiptphoto)
            self.clearreceiptbutton = Button(self.blankhomeframe, width=130,  text="Clear\nReceipt",font=("Time new rooman", 9, "bold", "italic"), image=self.clearreceipticon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=clear_receipt_class(self.root2, self.username, self.root).clear_receipt_frame)
            self.clearreceiptbutton.place(x=290, y=0, height=65)

            """
            #   Order Button
            self.ordericon = ImageTk.PhotoImage(self.ordericonphoto)
            self.addorderbutton = Button(self.blankhomeframe, width=130, text="Order\nDetails", font=("Time new rooman", 9, "bold", "italic"), image=self.ordericon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=order_class(self.root2, self.username, self.root).add_order_frame)
            self.addorderbutton.place(x=430, y=2, height=65)

            #   Department Button
            self.depicon = ImageTk.PhotoImage(self.depiconphoto)
            self.departmentbutton = Button(self.blankhomeframe, width=130,  text="Department",font=("Time new rooman", 9, "bold", "italic"), image=self.depicon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=departments_class(self.root2, self.username, self.root).add_department_frame)
            self.departmentbutton.place(x=10, y=0, height=65)

            #   Employee
            self.empicon = ImageTk.PhotoImage(self.empiconphoto)
            self.addemployeebutton = Button(self.blankhomeframe, width=130, text="Employee", font=("Time new rooman", 9, "bold", "italic"), image=self.empicon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=employee_class(self.root2, self.username, self.root).add_employee_frame)
            self.addemployeebutton.place(x=150, y=0, height=65)

            #   Order Rate Button
            self.orderrateicon = ImageTk.PhotoImage(self.orderrateiconphoto)
            self.orderratebutton = Button(self.blankhomeframe, width=130, text="Order\nRate/Process", font=("Time new rooman", 9, "bold", "italic"), image=self.orderrateicon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=order_rate_and_process(self.root2, self.username, self.root).order_rate_frame)
            self.orderratebutton.place(x=430, y=2, height=65)

            #   Requisition Button
            self.requesticon = ImageTk.PhotoImage(self.requesticonphoto)
            self.requestbutton = Button(self.blankhomeframe, width=130, text="Purchase\nRequisition", font=("Time new rooman", 9, "bold", "italic"), image=self.requesticon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=requsition_class(self.root2, self.username, self.root).requisition_frame)
            self.requestbutton.place(x=570, y=2, height=65)

            #   Inventory Data
            self.storeicon = ImageTk.PhotoImage(self.storeiconphoto)
            self.storebutton = Button(self.blankhomeframe, width=130,  text="Raw\nMaterial",font=("Time new rooman", 9, "bold", "italic"), image=self.storeicon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=raw_material_class(self.root2, self.username, self.root).raw_material_frame)
            self.storebutton.place(x=710, y=2, height=65)

            #   Average Button
            self.avgicon = ImageTk.PhotoImage(self.avgiconphoto)
            self.avgbutton = Button(self.blankhomeframe, width=130,  text="Estimated\nAverage",font=("Time new rooman", 9, "bold", "italic"), image=self.avgicon, compound=LEFT, fg=self.black,  bg=self.bgcolor, activebackground=self.powderblue, relief=GROOVE, command=order_stimated_avg(self.root2, self.username, self.root).order_estimated_avg_frame)
            self.avgbutton.place(x=850, y=2, height=65)"""

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

#   Make Receipt Class
class make_receipt_class(receipt_system):
    #   init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)

    #   Make Receipt Frae
    def make_receipt_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.matinfoframe = Frame(self.newdepinfoframemain, width=1450, bg=self.gray, bd=4, relief=FLAT)
            self.matinfoframe.place(x=0, y=0, height=50)
            self.newempinfoframe3 = Frame(self.newdepinfoframemain, width=725, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe3.place(x=0, y=51, height=172)
            self.newempinfoframe4 = Frame(self.newdepinfoframemain, width=725, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe4.place(x=742, y=51, height=440)

            #   Label
            self.addnewemployeelabel = Label(self.matinfoframe, text="      New Wages Receipt", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=550, y=0)
            self.addnewemployeelabel = Label(self.newempinfoframe3, text=" Order Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=250, y=0)
            self.depidlabel = Label(self.newempinfoframe3, text="Order id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.newempinfoframe3, text="Factory-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=318, y=26)
            self.empidlabel = Label(self.newempinfoframe3, text="Customer-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=3, y=61)
            self.emptypelabel = Label(self.newempinfoframe3, text="Description:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=318, y=61)
            self.empidlabel = Label(self.newempinfoframe3, text="Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=14, y=96)
            self.depnamelabel = Label(self.newempinfoframe3, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=321, y=96)
            self.empidlabel = Label(self.newempinfoframe3, text="Department:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=11, y=131)

            self.addnewemployeelabel = Label(self.newempinfoframe4, text="Article of Order Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=250, y=0)
            self.depidlabel = Label(self.newempinfoframe4, text="Artical id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=12, y=26)
            self.depidlabel = Label(self.newempinfoframe4, text="Product No:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=318, y=26)
            self.depnamelabel = Label(self.newempinfoframe4, text="Size:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=21, y=61)
            self.depnamelabel = Label(self.newempinfoframe4, text="Color:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=328, y=61)
            self.empidlabel = Label(self.newempinfoframe4, text="Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=14, y=96)
            self.empidlabel = Label(self.newempinfoframe4, text="Remain:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=325, y=96)
            self.empidlabel = Label(self.newempinfoframe4, text="Add Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=6, y=131)
            self.empidlabel = Label(self.newempinfoframe4, text="Comments:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=321, y=131)
            
            self.depnamelabel = Label(self.newempinfoframe4, text="Employee id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=7, y=166)
            self.empidlabel = Label(self.newempinfoframe4, text="Search Employee:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=315, y=166)
            self.depnamelabel = Label(self.newempinfoframe4, text="Employee Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=5, y=201)
            self.depidlabel = Label(self.newempinfoframe4, text="Receipt#:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=15, y=236)
            self.empidlabel = Label(self.matinfoframe, text="Select Order:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=2, y=4)

            existingorders = customer_order_database().pending_orders()
            d = [""]
            s = [""]
            for i in existingorders:
                a = str(i[0])+"-"+str(i[1])+" / "+str(i[2])
                s.append(a)

            #   Variables
            self.searchorderid_var = StringVar()

            self.orderid_var = StringVar()
            self.factorypo_var = StringVar()
            self.customerpo_var = StringVar()
            self.description_var = StringVar()
            self.orderqty_var = StringVar()
            self.ordertype_var = StringVar()

            self.articalid_var = StringVar()
            self.productno_var = StringVar()
            self.size_var = StringVar()
            self.color_var = StringVar()
            self.arttotalqty_var = StringVar()
            self.artremainqty_var = StringVar()
            self.depid_var = StringVar()
            self.newqtyfordep_var = StringVar()

            self.searchemp_var = StringVar()
            self.empid_var = StringVar()
            self.empname_var = StringVar()
            self.comments_var = StringVar()

            self.receiptno_var = StringVar()
            
            #   Order Entry
            self.orderidentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.orderid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.orderidentry.place(x=130, y=30, height=24, width=170)
            self.factorypoentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.factorypo_var, state="readonly", readonlybackground=self.white)
            self.factorypoentry.place(x=440, y=30, height=24, width=170)
            self.customerpoentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.customerpo_var, state="readonly", readonlybackground=self.white)
            self.customerpoentry.place(x=130, y=65, height=24, width=170)
            self.orderdescriptionentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.description_var, state="readonly", readonlybackground=self.white)
            self.orderdescriptionentry.place(x=440, y=65, height=24, width=170)
            self.orderqtyentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.orderqty_var, font=("Time new rooman", 10, "bold"), state="readonly", readonlybackground=self.white)
            self.orderqtyentry.place(x=130, y=100, height=24, width=170)
            self.orrdertypeentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.ordertype_var, font=("Time new rooman", 10, "bold"), state="readonly", readonlybackground=self.white)
            self.orrdertypeentry.place(x=440, y=100, height=24, width=170)

            self.articalidentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.articalid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articalidentry.place(x=130, y=30, height=24, width=170)
            self.productnoentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.productno_var, state="readonly", readonlybackground=self.white)
            self.productnoentry.place(x=440, y=30, height=24, width=170)
            self.sizeentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.size_var, state="readonly", readonlybackground=self.white)
            self.sizeentry.place(x=130, y=65, height=24, width=170)
            self.colorentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.color_var, state="readonly", readonlybackground=self.white)
            self.colorentry.place(x=440, y=65, height=24, width=170)
            self.arttotalqtyentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.arttotalqty_var, state="readonly", readonlybackground=self.white)
            self.arttotalqtyentry.place(x=130, y=100, height=24, width=170)
            self.artremainqtyentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.lightred, fg=self.black,font=("Time new rooman", 9, "bold"),  textvariable=self.artremainqty_var, state="readonly", readonlybackground=self.lightred)
            self.artremainqtyentry.place(x=440, y=100, height=24, width=170)
            self.newqtyfordepentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black, font=("Time new rooman", 9, "bold"), textvariable=self.newqtyfordep_var)
            self.newqtyfordepentry.place(x=130, y=135, height=24, width=170)
            self.commentsentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.comments_var)
            self.commentsentry.place(x=440, y=135, height=24, width=170)

            self.empidentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.empid_var, state="readonly", readonlybackground=self.white)
            self.empidentry.place(x=130, y=170, height=24, width=170)
            self.empnameentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.empname_var, state="readonly", readonlybackground=self.white)
            self.empnameentry.place(x=130, y=205, height=24, width=482)
            self.orderdepentry = Combobox(self.newempinfoframe3, values=d, textvariable=self.depid_var,  state="readonly")
            self.orderdepentry.place(x=130, y=135, height=24, width=482)
            self.emppicentry = Text(self.newempinfoframe4, font=("Time new rooman", 10, "bold"),bd=2, relief=GROOVE, bg=self.bgcolor, fg=self.black, state=DISABLED)
            self.emppicentry.place(x=360, y=234, height=200, width=250)
            self.receiptidentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.receiptno_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.receiptidentry.place(x=130, y=240, height=24, width=170)
            
            #   Search Order Entry
            self.searchorderidentry = Combobox(self.matinfoframe, values=s, textvariable=self.searchorderid_var,  state="readonly")
            self.searchorderidentry.place(x=130, y=8, height=24, width=170)
            self.searchempbarentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchemp_var)
            self.searchempbarentry.place(x=440, y=170, height=24, width=170)
            
            #   Tree
            self.v2 = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v2.pack(side=RIGHT, fill=Y)
            self.v2.place(x=728, y=225, height=267)

            self.tree2 = Treeview(self.newdepinfoframemain, height=12, columns=("C1", "C2", "C3", "C4", "C5"), show="headings", yscrollcommand=self.v2.set)
            self.tree2.place(x=1, y=225, width=725)

            self.tree2.column("#1", anchor="nw", width=10)
            self.tree2.column("#2", anchor="nw", width=80)
            self.tree2.column("#3", anchor=CENTER, width=20)
            self.tree2.column("#4", anchor="nw", width=90)
            self.tree2.column("#5", anchor=CENTER, width=45)

            self.tree2.heading("#1", text="id")
            self.tree2.heading("#2", text="Product No")
            self.tree2.heading("#3", text="Size")
            self.tree2.heading("#4", text="Color")
            self.tree2.heading("#5", text="Quantity")

            self.v2.config(command=self.tree2.yview)

            #   Tree 4
            self.v3 = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v3.pack(side=RIGHT, fill=Y)
            self.v3.place(x=1469, y=502, height=350)

            self.tree3 = Treeview(self.newdepinfoframemain, height=16, columns=("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"), show="headings", yscrollcommand=self.v3.set)
            self.tree3.place(x=1, y=502, width=1466)

            self.tree3.column("#1", anchor=CENTER, width=30)
            self.tree3.column("#2", anchor=CENTER, width=80)
            self.tree3.column("#3", anchor="nw", width=400)
            self.tree3.column("#4", anchor=CENTER, width=90)
            self.tree3.column("#5", anchor=CENTER, width=100)
            self.tree3.column("#6", anchor=CENTER, width=90)
            self.tree3.column("#7", anchor=CENTER, width=100)
            self.tree3.column("#8", anchor=CENTER, width=90)

            self.tree3.heading("#1", text="Receipt#")
            self.tree3.heading("#2", text="Emp-id")
            self.tree3.heading("#3", text="Employee Name")
            self.tree3.heading("#4", text="Quantity")
            self.tree3.heading("#5", text="Date / Time")
            self.tree3.heading("#6", text="Add By")
            self.tree3.heading("#7", text="Clear Date / Time")
            self.tree3.heading("#8", text="Clear By")

            self.v3.config(command=self.tree3.yview)
            
            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.saveicon = ImageTk.PhotoImage(self.saveiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            self.editicon = ImageTk.PhotoImage(self.editiconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)

            self.searchbutton = Button(self.matinfoframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_order, bd=2)
            self.searchbutton.place(x=310, y=8, height=25)
            self.searchbutton1 = Button(self.newempinfoframe4, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_emp, bd=2)
            self.searchbutton1.place(x=620, y=170, height=25)
            
            self.savebutton = Button(self.newempinfoframe4, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_in_dep, bd=2)
            self.savebutton.place(x=190, y=290, height=40)
            self.backbutton = Button(self.newempinfoframe4, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.receipt_system_frame, bd=2)
            self.backbutton.place(x=10, y=290, height=40)
            self.clearbutton = Button(self.newempinfoframe4, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen, bd=2)
            self.clearbutton.place(x=100, y=290, height=40)

            #   Bind
            self.root2.bind("<Control-f>", self.bind_search_order)
            self.root2.bind("<Alt-f>", self.bind_search_emp)
            self.root2.bind("<Control-s>", self.bind_save_dep)
            self.tree2.bind("<Double-Button-1>", self.select_article)
            self.orderdepentry.bind("<<ComboboxSelected>>", self.on_combobox_select)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.bind_back)
            
        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Bind Back
    def bind_back(self, eve):
        self.receipt_system_frame()

    #   Bind Search Order
    def bind_search_order(self, eve):
        self.searchorderidentry.focus_set()
        self.search_order()

    #   Bind Save
    def bind_save_dep(self, eve):
        self.save_in_dep()

    #   Bind Search Employee
    def bind_search_emp(self, eve):
        self.searchempbarentry.focus_set()
        self.search_emp()

    #   Clear Screen
    def clear_screen(self):
        self.clear_screen1()
        self.clear_screen2()
        self.clear_screen3()
        self.searchorderidentry.focus_set()
        self.searchorderid_var.set("")

    #   Clear Screen 1
    def clear_screen1(self):
        self.orderid_var.set("")
        self.factorypo_var.set("")
        self.customerpo_var.set("")
        self.description_var.set("")
        self.orderqty_var.set("")
        self.ordertype_var.set("")
        self.tree2.delete(*self.tree2.get_children())
        self.tree3.delete(*self.tree3.get_children())

        self.articalid_var.set("")
        self.productno_var.set("")
        self.size_var.set("")
        self.color_var.set("")
        self.arttotalqty_var.set("")
        self.artremainqty_var.set("")
        self.orderdepentry.config(values=[""])
        self.depid_var.set("")
        self.comments_var.set("")
        self.newqtyfordep_var.set("")

    #   Clear Screen 2
    def clear_screen2(self):
        self.articalid_var.set("")
        self.productno_var.set("")
        self.size_var.set("")
        self.color_var.set("")
        self.arttotalqty_var.set("")
        self.artremainqty_var.set("")
        self.comments_var.set("")
        self.tree3.delete(*self.tree3.get_children())

    #   Clear Screen 3
    def clear_screen3(self):
        self.searchemp_var.set("")
        self.empid_var.set("")
        self.empname_var.set("")
        self.comments_var.set("")
        self.emppicentry.config(state=NORMAL)
        self.emppicentry.delete("1.0", END)
        self.emppicentry.config(state=DISABLED)

    #   Combo Box bind
    def on_combobox_select(self, eve):
        self.clear_screen2()

    #   Search Order
    def search_order(self):
        searchbar = (self.searchorderid_var.get()).capitalize()
        if searchbar:
            allorderdetailsandrates = order_receipts().order_details_and_rate_database(searchbar)
            ratefordepartment = order_receipts().order_all_rate_database(searchbar)
            if allorderdetailsandrates == False or ratefordepartment == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif allorderdetailsandrates != []:
                self.clear_screen1()
                for i in allorderdetailsandrates:
                    orderid = i[0]
                    factorypo = i[1]
                    customerpo = i[2]
                    description = i[3]
                    orderqty = i[4]
                    ordertype = i[5]
                    self.orderid_var.set(orderid)
                    self.factorypo_var.set(factorypo)
                    self.customerpo_var.set(customerpo)
                    self.description_var.set(description)
                    self.orderqty_var.set(orderqty)
                    self.ordertype_var.set(ordertype)
                    artid = str(i[13])
                    prono = str(i[15])
                    size = str(i[16])
                    color = str(i[17])
                    qty = str(i[18])
                    self.tree2.insert("", END, iid=artid, values=(artid, prono, size, color, qty))

                d = [""]
                if ratefordepartment == []:
                    d = [""]
                elif ratefordepartment != []:
                    for i in ratefordepartment:
                        rateid = i[1]
                        details = i[4]
                        dep = str(i[3])+" "+str(i[7])

                        n = str(rateid)+"|"+str(dep)+"|"+str(details)
                        d.append(n)
                self.orderdepentry.config(values=d)

        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Seacrh details are empty") 

    #   Select Article
    def select_article(self, eve):
        r_id = self.tree2.focus()
        details = self.tree2.item(r_id)
        row = details['values']
        x = self.tree2.selection()
        orderid = self.orderid_var.get()
        if row != '' and x and orderid:
            self.clear_screen2()
            depid = self.depid_var.get()
            if depid:
                self.tree2.selection_remove(row[0])
                self.articalid_var.set(row[0])
                self.productno_var.set(row[1])
                self.size_var.set(row[2])
                self.color_var.set(row[3])
                self.arttotalqty_var.set(row[4])
                artid = row[0]
                self.geting_info(artid, depid, row[4])
            else:
                messagebox.showwarning(parent=self.root2,title="Department", message="Select department first") 
        else:
            pass

    #   Save in department
    def save_in_dep(self):
        depid = self.depid_var.get()
        artid = self.articalid_var.get()
        user = self.username
        remain = self.artremainqty_var.get()
        newqty = self.newqtyfordep_var.get()
        makedate = self.current_date()
        maketime = str(self.current_time())
        empid = self.empid_var.get()
        comments = (self.comments_var.get()).capitalize()
        receiptno = self.receiptno_var.get()
        artqty = self.arttotalqty_var.get()
        if depid and artid and remain and newqty and empid and receiptno:
            if newqty.isdigit() == True:
                if int(newqty) <= int(remain) and int(newqty) != 0:
                    n = receiptno.split("-")
                    databsereceiptno = n[2]
                    saveartindep = order_receipts().save_art_in_dep_database(depid, artid, user,newqty, receiptno, databsereceiptno, empid, makedate, maketime, comments)
                    if saveartindep == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif saveartindep == "Empty":
                        messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
                    elif saveartindep == "Save":
                        self.geting_info(artid, depid, artqty)
                        messagebox.showinfo(parent=self.root2, title="Saved", message="Article has been saved in "+str(depid))
                        
                else:
                    messagebox.showerror(parent=self.root2, title="Quantity", message="Quantity can't be greater then remain & can't be 0")
            else:
                messagebox.showwarning(parent=self.root2, title="Error", message="Quantity must be int")
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")

    #   Search emp
    def search_emp(self):
        searchemp = self.searchemp_var.get()
        if searchemp:
            empdetails = employee_database().search_by_id(searchemp)
            if empdetails == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif empdetails == []:
                messagebox.showerror(parent=self.root2,title="No match", message="No match found")
            elif empdetails != []:
                empid = ""
                empname = ""
                emppic = ""
                emptype = ""
                for i in empdetails:
                    empid = i[1]
                    empname = str(i[2])+" S/O "+str(i[3])
                    emppic = i[7]
                    emptype = i[8]
                    self.empid_var.set(empid)
                    self.empname_var.set(empname)
                    self.emppicentry.config(state=NORMAL)
                    self.emppicentry.delete("1.0", END)
                    img = ImageTk.PhotoImage(Image.open(emppic))
                    self.emppicentry.imgtk = img
                    self.emppicentry.image_create(END, image=img)
                    self.emppicentry.config(state=DISABLED)
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Seacrh details are empty") 

    #   Getting Info
    def geting_info(self, artid, depid, q):
        if depid:
            totalartindep = order_receipts().check_article_in_department_database(artid, depid)
            databsereceiptno = order_receipts().new_receipt_id(artid)
            alreadysaveddata = order_receipts().already_saved_selected_process(artid, depid)
            if totalartindep == False or databsereceiptno == False or alreadysaveddata == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif totalartindep == "Empty":
                messagebox.showwarning(parent=self.root2,title="Empty", message="Require fields are empty")
            elif totalartindep != []:
                parts = self.username.split("-")
                u = parts[0]
                receiptno = str(artid)+"-"+str(databsereceiptno)
                artqtyt = q
                t = 0
                
                for i in totalartindep:
                    if i[0] == None:
                        t = 0
                    else:
                        t = i[0]
                
                if int(t) == 0:
                    self.artremainqty_var.set(artqtyt)
                else:
                    remain = int(artqtyt) - int(t)
                    self.artremainqty_var.set(remain)
                self.receiptno_var.set(receiptno)
                self.newqtyfordepentry.focus_set()

                self.tree3.delete(*self.tree3.get_children())
                if alreadysaveddata == [] or alreadysaveddata == "Empty":
                    pass
                elif alreadysaveddata != []:
                    if alreadysaveddata == None:
                        pass
                    else:
                        for i in alreadysaveddata:
                            empname = str(i[17])+" S/O "+str(i[18])
                            addeddate = str(i[9])+" / "+str(i[10])
                            username = str(i[7])+"-"+str(i[19])
                            cleardatetime = str(i[13])+" / "+str(i[14])
                            clearby = str(i[15])+"-"+str(i[20])
                            self.tree3.insert("", END, iid=i[1], values=(i[1], i[8], empname, i[5], addeddate, username, cleardatetime, clearby))
                        
        else:
            messagebox.showwarning(parent=self.root2,title="Department", message="Select department first") 

#   Job Done
class make_job_card_class(receipt_system):
    #   init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)

    #   Job Card Frame
    def job_card_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.matinfoframe = Frame(self.newdepinfoframemain, width=1450, bg=self.gray, bd=4, relief=FLAT)
            self.matinfoframe.place(x=0, y=0, height=50)
            self.newempinfoframe4 = Frame(self.newdepinfoframemain, width=700, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe4.place(x=0, y=205, height=440)
            self.newempinfoframe3 = Frame(self.newdepinfoframemain, width=700, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe3.place(x=0, y=51, height=172)
            self.newempinfoframe5 = Frame(self.newdepinfoframemain, width=725, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe5.place(x=704, y=320, height=440)

            #   Label
            self.addnewemployeelabel = Label(self.matinfoframe, text="      Job Card Receipt", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=550, y=0)
            self.addnewemployeelabel = Label(self.newempinfoframe3, text=" Receipt Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=250, y=0)
            self.depidlabel = Label(self.newempinfoframe3, text="Order id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.newempinfoframe3, text="Factory-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=318, y=26)
            self.empidlabel = Label(self.newempinfoframe3, text="Customer-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=3, y=61)
            self.emptypelabel = Label(self.newempinfoframe3, text="Description:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=318, y=61)
            self.empidlabel = Label(self.newempinfoframe3, text="Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=14, y=96)
            self.depnamelabel = Label(self.newempinfoframe3, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=321, y=96)
            self.empidlabel = Label(self.newempinfoframe3, text="Department:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=11, y=131)

            self.depidlabel = Label(self.newempinfoframe4, text="Artical id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=12, y=26)
            self.depidlabel = Label(self.newempinfoframe4, text="Product No:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=318, y=26)
            self.depnamelabel = Label(self.newempinfoframe4, text="Size:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=21, y=61)
            self.depnamelabel = Label(self.newempinfoframe4, text="Color:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=328, y=61)
            self.empidlabel = Label(self.newempinfoframe4, text="Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=14, y=96)
            self.empidlabel = Label(self.newempinfoframe4, text="Remain:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=325, y=96)
            self.empidlabel = Label(self.newempinfoframe4, text="Comments:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=321, y=131)

            self.depnamelabel = Label(self.newempinfoframe4, text="Employee id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=7, y=131)
            self.depnamelabel = Label(self.newempinfoframe4, text="Employee Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=5, y=166)
            self.empidlabel = Label(self.newempinfoframe4, text="Added by:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=15, y=201)
            self.depidlabel = Label(self.newempinfoframe4, text="Receipt#:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=15, y=236)

            self.addnewemployeelabel = Label(self.newempinfoframe5, text="New Job Card Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=200, y=0)
            self.depidlabel = Label(self.newempinfoframe5, text="id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=24, y=26)
            self.depidlabel = Label(self.newempinfoframe5, text="Sub-Receipt#:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=5, y=61)
            self.depidlabel = Label(self.newempinfoframe5, text="Process id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=7, y=96)
            self.empidlabel = Label(self.newempinfoframe5, text="Process Details", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=2, y=131)
            self.depnamelabel = Label(self.newempinfoframe5, text="Employee id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=7, y=166)
            self.depnamelabel = Label(self.newempinfoframe5, text="Employee Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=5, y=201)
            self.empidlabel = Label(self.newempinfoframe5, text="Add Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=6, y=236)
            self.empidlabel = Label(self.newempinfoframe5, text="Comments:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=10, y=271)

            #   Search Label
            self.empidlabel = Label(self.matinfoframe, text="Search Receipt:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=2, y=4)
            self.empidlabel = Label(self.matinfoframe, text="Process Details", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=980, y=18)
            self.empidlabel = Label(self.newempinfoframe5, text="Search Worker:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=318, y=236)

            #   Variables
            self.orderid_var = StringVar()
            self.factorypo_var = StringVar()
            self.customerpo_var = StringVar()
            self.description_var = StringVar()
            self.orderqty_var = StringVar()
            self.ordertype_var = StringVar()

            self.articalid_var = StringVar()
            self.productno_var = StringVar()
            self.size_var = StringVar()
            self.color_var = StringVar()
            self.arttotalqty_var = StringVar()
            self.artremainqty_var = StringVar()
            self.depid_var = StringVar()
            
            self.empid_var = StringVar()
            self.empname_var = StringVar()
            self.comments_var = StringVar()
            self.receiptno_var = StringVar()
            self.addby_var = StringVar()
            
            self.saecrhreceipt_var = StringVar()
            self.searchemp_var = StringVar()

            self.newid_var = StringVar()
            self.subreceiptno_var = StringVar()
            self.subprocessid_var = StringVar()
            self.subprodetails_var = StringVar()
            self.newqtyfordep_var = StringVar()
            self.empid1_var = StringVar()
            self.empname1_var = StringVar()
            self.comments1_var = StringVar()

            #   Order Entry
            self.orderidentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.orderid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.orderidentry.place(x=130, y=30, height=24, width=170)
            self.factorypoentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.factorypo_var, state="readonly", readonlybackground=self.white)
            self.factorypoentry.place(x=440, y=30, height=24, width=170)
            self.customerpoentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.customerpo_var, state="readonly", readonlybackground=self.white)
            self.customerpoentry.place(x=130, y=65, height=24, width=170)
            self.orderdescriptionentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.description_var, state="readonly", readonlybackground=self.white)
            self.orderdescriptionentry.place(x=440, y=65, height=24, width=170)
            self.orderqtyentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.orderqty_var, font=("Time new rooman", 10, "bold"), state="readonly", readonlybackground=self.white)
            self.orderqtyentry.place(x=130, y=100, height=24, width=170)
            self.orrdertypeentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.ordertype_var, font=("Time new rooman", 10, "bold"), state="readonly", readonlybackground=self.white)
            self.orrdertypeentry.place(x=440, y=100, height=24, width=170)

            self.articalidentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.articalid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.articalidentry.place(x=130, y=30, height=24, width=170)
            self.productnoentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.productno_var, state="readonly", readonlybackground=self.white)
            self.productnoentry.place(x=440, y=30, height=24, width=170)
            self.sizeentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.size_var, state="readonly", readonlybackground=self.white)
            self.sizeentry.place(x=130, y=65, height=24, width=170)
            self.colorentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.color_var, state="readonly", readonlybackground=self.white)
            self.colorentry.place(x=440, y=65, height=24, width=170)
            self.arttotalqtyentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, font=("Time new rooman", 9, "bold"), textvariable=self.arttotalqty_var, state="readonly", readonlybackground=self.white)
            self.arttotalqtyentry.place(x=130, y=100, height=24, width=170)
            self.artremainqtyentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.lightred, fg=self.black,font=("Time new rooman", 9, "bold"),  textvariable=self.artremainqty_var, state="readonly", readonlybackground=self.lightred)
            self.artremainqtyentry.place(x=440, y=100, height=24, width=170)
            self.commentsentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.comments_var, state="readonly", readonlybackground=self.white)
            self.commentsentry.place(x=440, y=135, height=24, width=170)
            self.receiptmakebyentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.addby_var, state="readonly", readonlybackground=self.white)
            self.receiptmakebyentry.place(x=130, y=205, height=24, width=482)

            self.empidentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.empid_var, state="readonly", readonlybackground=self.white)
            self.empidentry.place(x=130, y=135, height=24, width=170)
            self.empnameentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.empname_var, state="readonly", readonlybackground=self.white)
            self.empnameentry.place(x=130, y=170, height=24, width=482)
            self.orderdepentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.depid_var, state="readonly", readonlybackground=self.white)
            self.orderdepentry.place(x=130, y=135, height=24, width=482)
            self.emppicentry = Text(self.newempinfoframe4, font=("Time new rooman", 10, "bold"),bd=2, relief=GROOVE, bg=self.bgcolor, fg=self.black, state=DISABLED)
            self.emppicentry.place(x=360, y=234, height=200, width=250)
            self.receiptidentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.receiptno_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.receiptidentry.place(x=130, y=240, height=24, width=170)

            self.subreceiptidentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.newid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.subreceiptidentry.place(x=130, y=30, height=24, width=170)
            self.subreceiptnoentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.subreceiptno_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.subreceiptnoentry.place(x=130, y=65, height=24, width=170)
            self.subprocessidentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.subprocessid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.subprocessidentry.place(x=130, y=100, height=24, width=170)
            self.subprocessdetailsentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.subprodetails_var, state="readonly", readonlybackground=self.white)
            self.subprocessdetailsentry.place(x=130, y=135, height=24, width=300)
            self.empidentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.empid1_var, state="readonly", readonlybackground=self.white)
            self.empidentry.place(x=130, y=170, height=24, width=170)
            self.empnameentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.empname1_var, state="readonly", readonlybackground=self.white)
            self.empnameentry.place(x=130, y=205, height=24, width=300)
            self.newqtyfordepentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black, font=("Time new rooman", 9, "bold"), textvariable=self.newqtyfordep_var)
            self.newqtyfordepentry.place(x=130, y=240, height=24, width=170)
            self.subcommentsentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.comments1_var)
            self.subcommentsentry.place(x=130, y=275, height=24, width=170)
            self.emppicentry1 = Text(self.newempinfoframe5, font=("Time new rooman", 10, "bold"),bd=2, relief=GROOVE, bg=self.bgcolor, fg=self.black, state=DISABLED)
            self.emppicentry1.place(x=455, y=5, height=200, width=250)

            self.searchempbarentry = Entry(self.matinfoframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.saecrhreceipt_var)
            self.searchempbarentry.place(x=130, y=8, height=24, width=170)
            self.searchempbarentry.focus_set()
            self.searchempbarentry1 = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.searchemp_var)
            self.searchempbarentry1.place(x=440, y=240, height=24, width=170)

            #   Tree
            self.v2 = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v2.pack(side=RIGHT, fill=Y)
            self.v2.place(x=1432, y=51, height=267)

            self.tree2 = Treeview(self.newdepinfoframemain, height=12, columns=("C1", "C2", "C3", "C4", "C5", "C6"), show="headings", yscrollcommand=self.v2.set)
            self.tree2.place(x=704, y=51, width=725)

            self.tree2.column("#1", anchor=CENTER, width=50)
            self.tree2.column("#2", anchor="nw", width=150)
            self.tree2.column("#3", anchor=CENTER, width=45)
            self.tree2.column("#4", anchor=CENTER, width=45)
            self.tree2.column("#5", anchor=CENTER, width=45)
            self.tree2.column("#6", anchor=CENTER, width=45)

            self.tree2.heading("#1", text="id")
            self.tree2.heading("#2", text="Details")
            self.tree2.heading("#3", text="Rate")
            self.tree2.heading("#4", text="Total")
            self.tree2.heading("#5", text="Resereved")
            self.tree2.heading("#6", text="Remain")

            self.v2.config(command=self.tree2.yview)

            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.saveicon = ImageTk.PhotoImage(self.saveiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.printicon = ImageTk.PhotoImage(self.printiconphoto)

            self.searchbutton2 = Button(self.matinfoframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_receipt, bd=2)
            self.searchbutton2.place(x=315, y=8, height=25)
            self.searchbutton1 = Button(self.newempinfoframe5, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_emp, bd=2)
            self.searchbutton1.place(x=625, y=240, height=25)
            self.backbutton = Button(self.newempinfoframe5, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.receipt_system_frame, bd=2)
            self.backbutton.place(x=180, y=310, height=40)
            self.savebutton = Button(self.newempinfoframe5, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_sub_receipt, bd=2)
            self.savebutton.place(x=280, y=310, height=40)
            self.clearbutton = Button(self.newempinfoframe5, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen, bd=2)
            self.clearbutton.place(x=380, y=310, height=40)

            #   Bind
            self.root2.bind("<Control-f>", self.bind_search)
            self.root2.bind("<Control-s>", self.bind_save_dep)
            self.root2.bind("<Alt-f>", self.bind_search_emp)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.bind_back)
            self.tree2.bind("<Double-Button-1>", self.select_process)
        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Clear Screen
    def clear_screen(self):
        self.receiptno_var.set("")
        self.empid_var.set("")
        self.empname_var.set("")
        self.empid1_var.set("")
        self.empname1_var.set("")
        self.searchempbarentry.focus_set()
        self.saecrhreceipt_var.set("")
        self.searchemp_var.set("")
        self.emppicentry1.config(state=NORMAL)
        self.emppicentry1.delete("1.0", END)
        self.emppicentry1.config(state=DISABLED)
        self.clear_screen1()
        self.clear_screen2()
        self.clear_screen2()

    #   Clear Screen 1
    def clear_screen1(self):
        self.orderid_var.set("")
        self.factorypo_var.set("")
        self.customerpo_var.set("")
        self.description_var.set("")
        self.orderqty_var.set("")
        self.ordertype_var.set("")
        self.tree2.delete(*self.tree2.get_children())

        self.articalid_var.set("")
        self.productno_var.set("")
        self.size_var.set("")
        self.color_var.set("")
        self.arttotalqty_var.set("")
        self.artremainqty_var.set("")
        self.depid_var.set("")
        self.comments_var.set("")
        self.newqtyfordep_var.set("")
        self.addby_var.set("")

        self.emppicentry.config(state=NORMAL)
        self.emppicentry.delete("1.0", END)
        self.emppicentry.config(state=DISABLED)

        self.newid_var.set("")
        self.subreceiptno_var.set("")
        self.newqtyfordep_var.set("")
        self.subprocessid_var.set("")
        self.subprodetails_var.set("")
        self.comments1_var.set("")

    #   Clear Scree 2
    def clear_screen2(self):
        self.newid_var.set("")
        self.subreceiptno_var.set("")
        self.newqtyfordep_var.set("")
        self.subprocessid_var.set("")
        self.subprodetails_var.set("")
        self.artremainqty_var.set("")
        self.comments1_var.set("")

    #   Bind Search
    def bind_search(self, eve):
        self.searchempbarentry.focus_set()
        self.search_receipt()

    #   Bind Back
    def bind_back(self, eve):
        self.receipt_system_frame()
   
    #   Bind Save
    def bind_save_dep(self, eve):
        self.save_sub_receipt()

    #   Bind Search Employee
    def bind_search_emp(self, eve):
        self.searchempbarentry1.focus_set()
        self.search_emp()

    #   Search Receipt
    def search_receipt(self):
        searchreceipt = self.saecrhreceipt_var.get()
        if searchreceipt:
            showreceiptinfodatabase = order_receipts().seacrh_receipt_for_work_booking(searchreceipt)
            if showreceiptinfodatabase == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif showreceiptinfodatabase == []:
                messagebox.showerror(parent=self.root2,title="No match", message="No match found")
            elif showreceiptinfodatabase != []:
                self.clear_screen1()
                selectedpro = ""
                for i in showreceiptinfodatabase:
                    self.receiptno_var.set(i[1])
                    selectedpro = i[2]
                    prono = str(i[2])+" | "+str(i[3])+" "+str(i[18])+" | "+str(i[17])
                    self.depid_var.set(prono)
                    self.articalid_var.set(i[4])
                    self.productno_var.set(i[20])
                    self.size_var.set(i[21])
                    self.color_var.set(i[22])
                    addedby = str(i[9])+" | "+str(i[10])+"\tuser: "+str(i[7])+"-"+str(i[23])
                    self.addby_var.set(addedby)
                    empid = i[8]
                    empname = str(i[24])+" S/O "+str(i[25])
                    emppic = i[26]
                    self.empid_var.set(empid)
                    self.empname_var.set(empname)
                    self.orderid_var.set(i[27])
                    self.factorypo_var.set(i[28])
                    self.customerpo_var.set(i[29])
                    self.description_var.set(i[30])
                    self.ordertype_var.set(i[31])
                    self.emppicentry.config(state=NORMAL)
                    img = ImageTk.PhotoImage(Image.open(emppic))
                    self.emppicentry.imgtk = img
                    self.emppicentry.image_create(END, image=img)
                    self.emppicentry.config(state=DISABLED)
                    self.comments_var.set(i[11])
                    self.arttotalqty_var.set(i[5])
                    self.orderqty_var.set(i[28])

                receipt = self.receiptno_var.get()
                if selectedpro == "":
                    pass
                else:
                    savedallsubprocess = customer_order_process_database().all_sub_process(selectedpro)
                    if savedallsubprocess == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif savedallsubprocess == []:
                        pass
                    elif savedallsubprocess != []:
                        for i in savedallsubprocess:
                            totalqty = self.arttotalqty_var.get()
                            alreadyinprocess = order_receipts().check_already_qty_subreceipt_dataabse(receipt, i[1])
                            if alreadyinprocess == []:
                                self.tree2.insert("", END, iid=i[1], values=(i[1], i[3], i[5], totalqty, 0, totalqty))
                            elif alreadyinprocess != []:
                                tp = 0
                                for j in alreadyinprocess:
                                    tp = tp + j[0]
                                
                                reservedremain = int(totalqty) - int(tp)
                                self.tree2.insert("", END, iid=i[1], values=(i[1], i[3], i[5], totalqty, tp, reservedremain))
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Seacrh details are empty")

    #   Select Process
    def select_process(self, eve):
        r_id = self.tree2.focus()
        details = self.tree2.item(r_id)
        row = details['values']
        x = self.tree2.selection()
        orderid = self.receiptno_var.get()
        if row != '' and x and orderid:
            self.clear_screen2()
            self.tree2.selection_remove(row[0])
            processid = row[0]
            q = row[5]
            sd = str(row[1])+"   | Rate: "+str(row[2])
            self.subprocessid_var.set(processid)
            self.subprodetails_var.set(sd)
            self.artremainqty_var.set(q)
            self.newqtyfordepentry.focus_set()
            self.geting_info(processid, q)
        else:
            pass

    #   getting Information
    def geting_info(self, processid, q):
        receiptno = self.receiptno_var.get()
        if processid and receiptno:
            newreceiptno = order_receipts().new_sub_receipt_no(receiptno)
            processdetails = order_receipts().check_already_qty_subreceipt_dataabse(receiptno, processid)
            if newreceiptno == False or processdetails == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            else:
                reqid = str(newreceiptno)
                m = str(receiptno)+"-"+str(reqid)
                self.newid_var.set(reqid)
                self.subreceiptno_var.set(m)
                if processdetails == []:
                    self.artremainqty_var.set(q)
                elif processdetails != []:
                    r = 0
                    for i in processdetails:
                        r = r + i[0]

                    c = int(self.arttotalqty_var.get()) - int(r)
                    self.artremainqty_var.set(c)
                self.newqtyfordepentry.focus_set()
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")

    #   Save Sub Receipt
    def save_sub_receipt(self):
        receiptno = self.receiptno_var.get()
        subproid = self.subprocessid_var.get()
        empid = self.empid1_var.get()
        qty = self.newqtyfordep_var.get()
        newid = self.newid_var.get()
        subreceiptid = self.subreceiptno_var.get()
        adddate = self.current_date()
        addtime = self.current_time()
        user = self.username
        comments = (self.comments1_var.get()).capitalize()
        remain = self.artremainqty_var.get()
        pcqty = self.arttotalqty_var.get()
        if receiptno and subproid and empid and qty and newid and subreceiptid and remain and pcqty:
            if qty.isdigit() == True:
                if int(qty) <= int(remain) and int(qty) != 0 and int(qty) <= int(pcqty):
                    n = user.split("-")
                    userid = n[0]
                    saveartindep = order_receipts().save_sub_receipt_in_database(receiptno, subproid, empid, qty, newid, subreceiptid, adddate, addtime, userid, comments)
                    if saveartindep == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif saveartindep == "Empty":
                        messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
                    elif saveartindep == "Save":
                        self.saecrhreceipt_var.set(receiptno)
                        self.search_receipt()
                        messagebox.showinfo(parent=self.root2, title="Saved", message="Job Card "+str(subproid)+" | "+str(self.subprodetails_var.get())+" of receipt no: "+str(receiptno)+" has been saved")
                else:
                    messagebox.showerror(parent=self.root2, title="Quantity", message="Quantity can't be greater then remain & total pc / can't be 0")
            else:
                messagebox.showwarning(parent=self.root2, title="Error", message="Quantity must be int")
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")

    #   Search emp
    def search_emp(self):
        searchemp = self.searchemp_var.get()
        if searchemp:
            empdetails = employee_database().search_by_id(searchemp)
            if empdetails == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif empdetails == []:
                messagebox.showerror(parent=self.root2,title="No match", message="No match found")
            elif empdetails != []:
                empid = ""
                empname = ""
                emppic = ""
                emptype = ""
                for i in empdetails:
                    empid = i[1]
                    empname = str(i[2])+" S/O "+str(i[3])
                    emppic = i[7]
                    emptype = i[8]
                if emptype == "Salary":
                    messagebox.showwarning(parent=self.root2, title="Salary Base", message="You can't select salarybase employee")
                elif emptype == "Contractor" or emptype == "Maker":
                    self.empid1_var.set(empid)
                    self.empname1_var.set(empname)
                    self.emppicentry1.config(state=NORMAL)
                    self.emppicentry1.delete("1.0", END)
                    img = ImageTk.PhotoImage(Image.open(emppic))
                    self.emppicentry1.imgtk = img
                    self.emppicentry1.image_create(END, image=img)
                    self.emppicentry1.config(state=DISABLED)
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Seacrh details are empty") 

#   Clear receipt
class clear_receipt_class(receipt_system):
    #   init
    def __init__(self, root2, username, root):
        self.root2 = root2
        self.username = username
        self.root = root
        super().__init__(self.root, self.username)

    #   Job Card Frame
    def clear_receipt_frame(self):
        a = database_class().database_connection_check()
        if a == True:
            #   FRAMES
            self.newdepinfoframemain = Frame(self.root2, width=1500, bg=self.gray, bd=5, relief=FLAT)
            self.newdepinfoframemain.place(x=0, y=0, height=885)
            self.matinfoframe = Frame(self.newdepinfoframemain, width=1450, bg=self.gray, bd=4, relief=FLAT)
            self.matinfoframe.place(x=0, y=0, height=50)
            self.newempinfoframe4 = Frame(self.newdepinfoframemain, width=900, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe4.place(x=0, y=205, height=440)
            self.newempinfoframe3 = Frame(self.newdepinfoframemain, width=700, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe3.place(x=0, y=51, height=172)
            self.newempinfoframe5 = Frame(self.newdepinfoframemain, width=900, bg=self.gray, bd=4, relief=FLAT)
            self.newempinfoframe5.place(x=0, y=480, height=255)

            #   Label
            self.addnewemployeelabel = Label(self.matinfoframe, text="      Clear Job Card/Receipt", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=550, y=0)
            self.addnewemployeelabel = Label(self.newempinfoframe3, text=" Receipt Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=250, y=0)
            self.depidlabel = Label(self.newempinfoframe3, text="Order id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=14, y=26)
            self.depnamelabel = Label(self.newempinfoframe3, text="Factory-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=318, y=26)
            self.empidlabel = Label(self.newempinfoframe3, text="Customer-Po:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=3, y=61)
            self.emptypelabel = Label(self.newempinfoframe3, text="Description:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.emptypelabel.place(x=318, y=61)
            self.empidlabel = Label(self.newempinfoframe3, text="Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=14, y=96)
            self.depnamelabel = Label(self.newempinfoframe3, text="Category:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=321, y=96)
            self.empidlabel = Label(self.newempinfoframe3, text="Department:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=11, y=131)

            self.depidlabel = Label(self.newempinfoframe4, text="Artical id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=12, y=26)
            self.depidlabel = Label(self.newempinfoframe4, text="Product No:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=318, y=26)
            self.depnamelabel = Label(self.newempinfoframe4, text="Size:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=21, y=61)
            self.depnamelabel = Label(self.newempinfoframe4, text="Color:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=328, y=61)
            self.empidlabel = Label(self.newempinfoframe4, text="Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=14, y=96)
            self.empidlabel = Label(self.newempinfoframe4, text="Remain:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=325, y=96)
            self.empidlabel = Label(self.newempinfoframe4, text="Comments:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=321, y=131)

            self.depnamelabel = Label(self.newempinfoframe4, text="Employee id:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=7, y=131)
            self.depnamelabel = Label(self.newempinfoframe4, text="Employee Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=5, y=166)
            self.empidlabel = Label(self.newempinfoframe4, text="Added by:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=15, y=201)
            self.depidlabel = Label(self.newempinfoframe4, text="Receipt#:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=15, y=236)
            self.depidlabel = Label(self.newempinfoframe4, text="Sub-Receipt#:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depidlabel.place(x=321, y=236)

            self.addnewemployeelabel = Label(self.newempinfoframe5, text="    Job Card Information", font=("Time new rooman", 11, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.addnewemployeelabel.place(x=250, y=0)

            self.empidlabel = Label(self.newempinfoframe5, text="Process Details", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=2, y=26)
            self.depnamelabel = Label(self.newempinfoframe5, text="Employee Name:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.depnamelabel.place(x=5, y=61)
            self.empidlabel = Label(self.newempinfoframe5, text="Added by:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=15, y=96)
            self.empidlabel = Label(self.newempinfoframe5, text="Add Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=6, y=131)
            self.empidlabel = Label(self.newempinfoframe5, text="Comments:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=321, y=131)
            self.empidlabel = Label(self.newempinfoframe5, text="Clear Quantity:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=4, y=166)


            #   Search Label
            self.empidlabel = Label(self.matinfoframe, text="Search Receipt:", font=("Time new rooman", 9, "bold"), fg=self.black, bg=self.gray, bd=4, pady=4, padx=4)
            self.empidlabel.place(x=2, y=4)

            #   Variables
            self.orderid_var = StringVar()
            self.factorypo_var = StringVar()
            self.customerpo_var = StringVar()
            self.description_var = StringVar()
            self.orderqty_var = StringVar()
            self.ordertype_var = StringVar()

            self.articalid_var = StringVar()
            self.productno_var = StringVar()
            self.size_var = StringVar()
            self.color_var = StringVar()
            self.arttotalqty_var = StringVar()
            self.artremainqty_var = StringVar()
            self.depid_var = StringVar()
            
            self.empid_var = StringVar()
            self.empname_var = StringVar()
            self.comments_var = StringVar()
            self.receiptno_var = StringVar()
            self.addby_var = StringVar()

            self.subreceiptno_var = StringVar()
            self.subprodetails_var = StringVar()
            self.newqtyfordep_var = StringVar()
            self.empid1_var = StringVar()
            self.empname1_var = StringVar()
            self.comments1_var = StringVar()
            self.addby1_var = StringVar()
            self.clearqty_var = StringVar()

            self.saecrhreceipt_var = StringVar()
            #   Order Entry
            self.orderidentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.orderid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.white)
            self.orderidentry.place(x=130, y=30, height=24, width=170)
            self.factorypoentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.factorypo_var, state="readonly", readonlybackground=self.white)
            self.factorypoentry.place(x=440, y=30, height=24, width=170)
            self.customerpoentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.customerpo_var, state="readonly", readonlybackground=self.white)
            self.customerpoentry.place(x=130, y=65, height=24, width=170)
            self.orderdescriptionentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.description_var, state="readonly", readonlybackground=self.white)
            self.orderdescriptionentry.place(x=440, y=65, height=24, width=170)
            self.orderqtyentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.orderqty_var, font=("Time new rooman", 10, "bold"), state="readonly", readonlybackground=self.white)
            self.orderqtyentry.place(x=130, y=100, height=24, width=170)
            self.orrdertypeentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black,textvariable=self.ordertype_var, font=("Time new rooman", 10, "bold"), state="readonly", readonlybackground=self.white)
            self.orrdertypeentry.place(x=440, y=100, height=24, width=170)

            #   Article Entry
            self.articalidentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.articalid_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.white)
            self.articalidentry.place(x=130, y=30, height=24, width=170)
            self.productnoentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.productno_var, state="readonly", readonlybackground=self.white)
            self.productnoentry.place(x=440, y=30, height=24, width=170)
            self.sizeentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.size_var, state="readonly", readonlybackground=self.white)
            self.sizeentry.place(x=130, y=65, height=24, width=170)
            self.colorentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.color_var, state="readonly", readonlybackground=self.white)
            self.colorentry.place(x=440, y=65, height=24, width=170)
            self.arttotalqtyentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, font=("Time new rooman", 9, "bold"), textvariable=self.arttotalqty_var, state="readonly", readonlybackground=self.white)
            self.arttotalqtyentry.place(x=130, y=100, height=24, width=170)
            self.artremainqtyentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.lightred, fg=self.black,font=("Time new rooman", 9, "bold"),  textvariable=self.artremainqty_var, state="readonly", readonlybackground=self.lightred)
            self.artremainqtyentry.place(x=440, y=100, height=24, width=170)
            self.commentsentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.comments_var, state="readonly", readonlybackground=self.white)
            self.commentsentry.place(x=440, y=135, height=24, width=170)
            self.receiptmakebyentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.addby_var, state="readonly", readonlybackground=self.white)
            self.receiptmakebyentry.place(x=130, y=205, height=24, width=482)

            #   Employee Entry
            self.empidentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.empid_var, state="readonly", readonlybackground=self.white)
            self.empidentry.place(x=130, y=135, height=24, width=170)
            self.empnameentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.empname_var, state="readonly", readonlybackground=self.white)
            self.empnameentry.place(x=130, y=170, height=24, width=482)
            self.orderdepentry = Entry(self.newempinfoframe3,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.depid_var, state="readonly", readonlybackground=self.white)
            self.orderdepentry.place(x=130, y=135, height=24, width=482)
            self.emppicentry = Text(self.newempinfoframe4, font=("Time new rooman", 10, "bold"),bd=2, relief=GROOVE, bg=self.bgcolor, fg=self.black, state=DISABLED)
            self.emppicentry.place(x=625, y=30, height=200, width=250)
            self.receiptidentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.receiptno_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.receiptidentry.place(x=130, y=240, height=24, width=170)
            self.subreceiptnoentry = Entry(self.newempinfoframe4,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.subreceiptno_var, font=("Time new rooman", 9, "bold"), state="readonly", readonlybackground=self.bgcolor)
            self.subreceiptnoentry.place(x=440, y=240, height=24, width=170)

            #   Sub-Receipt Entry
            self.subprocessdetailsentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.subprodetails_var, state="readonly", readonlybackground=self.white)
            self.subprocessdetailsentry.place(x=130, y=30, height=24, width=482)
            self.empidentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.empid1_var, state="readonly", readonlybackground=self.white)
            self.empidentry.place(x=130, y=61, height=24, width=482)
            self.receiptmakebyentry1 = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", fg=self.black, textvariable=self.addby1_var, state="readonly", readonlybackground=self.white)
            self.receiptmakebyentry1.place(x=130, y=96, height=24, width=482)
            self.newqtyfordepentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black, font=("Time new rooman", 9, "bold"), textvariable=self.newqtyfordep_var, state="readonly", readonlybackground=self.bgcolor)
            self.newqtyfordepentry.place(x=130, y=135, height=24, width=170)
            self.subcommentsentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", bg=self.white, fg=self.black, textvariable=self.comments1_var, state="readonly", readonlybackground=self.white)
            self.subcommentsentry.place(x=440, y=135, height=24, width=170)
            self.emppicentry1 = Text(self.newempinfoframe5, font=("Time new rooman", 10, "bold"),bd=2, relief=GROOVE, bg=self.bgcolor, fg=self.black, state=DISABLED)
            self.emppicentry1.place(x=625, y=0, height=200, width=250)
            self.clearqtyentry = Entry(self.newempinfoframe5,bd=2, relief=SUNKEN, justify="left", bg=self.lightgreen, fg=self.black, textvariable=self.clearqty_var)
            self.clearqtyentry.place(x=130, y=170, height=24, width=170)

            #   Tree
            self.v3 = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v3.pack(side=RIGHT, fill=Y)
            self.v3.place(x=1469, y=30, height=180)

            self.tree3 = Treeview(self.newdepinfoframemain, height=8, columns=("C1", "C2", "C3", "C4", "C5"), show="headings", yscrollcommand=self.v3.set)
            self.tree3.place(x=625, y=30, width=848)

            self.tree3.column("#1", anchor=CENTER, width=50)
            self.tree3.column("#2", anchor="nw", width=220)
            self.tree3.column("#3", anchor=CENTER, width=50)
            self.tree3.column("#4", anchor=CENTER, width=50)
            self.tree3.column("#5", anchor=CENTER, width=50)

            self.tree3.heading("#1", text="Receipt#")
            self.tree3.heading("#2", text="Employee Name")
            self.tree3.heading("#3", text="Quantity")
            self.tree3.heading("#4", text="Clear")
            self.tree3.heading("#5", text="Remain")

            self.v3.config(command=self.tree3.yview)


            self.v2 = Scrollbar(self.newdepinfoframemain, orient='vertical')
            self.v2.pack(side=RIGHT, fill=Y)
            self.v2.place(x=1456, y=240, height=230)

            self.tree2 = Treeview(self.newdepinfoframemain, height=10, columns=("C1", "C2", "C3"), show="headings", yscrollcommand=self.v2.set)
            self.tree2.place(x=903, y=240, width=550)

            self.tree2.column("#1", anchor=CENTER, width=80)
            self.tree2.column("#2", anchor=CENTER, width=80)
            self.tree2.column("#3", anchor=CENTER, width=80)

            self.tree2.heading("#1", text="Quantity")
            self.tree2.heading("#2", text="Date / Time")
            self.tree2.heading("#3", text="User")

            self.v2.config(command=self.tree2.yview)

            #   Seacrh
            self.searchempbarentry = Entry(self.matinfoframe,bd=2, relief=SUNKEN, justify="left",bg=self.powderblue, fg=self.black, textvariable=self.saecrhreceipt_var)
            self.searchempbarentry.place(x=130, y=8, height=24, width=170)
            self.searchempbarentry.focus_set()

            #   Button
            self.backicon = ImageTk.PhotoImage(self.backiconphoto)
            self.saveicon = ImageTk.PhotoImage(self.saveiconphoto)
            self.clearicon = ImageTk.PhotoImage(self.cleariconphoto)
            self.searchicon = ImageTk.PhotoImage(self.searchiconphoto)
            self.printicon = ImageTk.PhotoImage(self.printiconphoto)

            self.searchbutton2 = Button(self.matinfoframe, width=60, text="Search", font=("Time new rooman", 9, "bold", "italic"), image=self.searchicon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.search_receipt, bd=2)
            self.searchbutton2.place(x=315, y=8, height=25)
            self.backbutton = Button(self.newempinfoframe5, width=73, text="Back", font=("Time new rooman", 9, "bold", "italic"), image=self.backicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.receipt_system_frame, bd=2)
            self.backbutton.place(x=180, y=205, height=40)
            self.savebutton = Button(self.newempinfoframe5, width=73, text="Save", font=("Time new rooman", 9, "bold", "italic"), image=self.saveicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.save_receipt_qty, bd=2)
            self.savebutton.place(x=280, y=205, height=40)
            self.clearbutton = Button(self.newempinfoframe5, width=73, text="Clear", font=("Time new rooman", 9, "bold", "italic"), image=self.clearicon, compound=LEFT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=self.clear_screen1, bd=2)
            self.clearbutton.place(x=380, y=205, height=40)

            #   Bind
            self.root2.bind("<Control-f>", self.bind_search)
            self.root2.bind("<Control-KeyPress-BackSpace>", self.bind_back)
            self.root2.bind("<Control-s>", self.bind_save_dep)

        else:
            messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")

    #   Clear Screen 1
    def clear_screen1(self):
        self.orderid_var.set("")
        self.factorypo_var.set("")
        self.customerpo_var.set("")
        self.description_var.set("")
        self.orderqty_var.set("")
        self.ordertype_var.set("")
        self.tree2.delete(*self.tree2.get_children())
        self.tree3.delete(*self.tree3.get_children())

        self.articalid_var.set("")
        self.productno_var.set("")
        self.size_var.set("")
        self.color_var.set("")
        self.arttotalqty_var.set("")
        self.artremainqty_var.set("")
        self.depid_var.set("")
        self.comments_var.set("")
        self.newqtyfordep_var.set("")
        self.addby_var.set("")

        self.emppicentry.config(state=NORMAL)
        self.emppicentry.delete("1.0", END)
        self.emppicentry.config(state=DISABLED)

        self.emppicentry1.config(state=NORMAL)
        self.emppicentry1.delete("1.0", END)
        self.emppicentry1.config(state=DISABLED)

        self.subreceiptno_var.set("")
        self.newqtyfordep_var.set("")
        self.subprodetails_var.set("")
        self.comments1_var.set("")
        self.addby1_var.set("")
        self.clearqty_var.set("")

        self.receiptno_var.set("")
        self.empid_var.set("")
        self.empname_var.set("")
        self.empid1_var.set("")

    #   Bind Search
    def bind_search(self, eve):
        self.searchempbarentry.focus_set()
        self.search_receipt()

    #   Bind Back
    def bind_back(self, eve):
        self.receipt_system_frame()
   
    #   Bind Save
    def bind_save_dep(self, eve):
        self.clearqtyentry.focus_set()
        self.save_receipt_qty()

    #   Search Receipt
    def search_receipt(self):
        searchreceipt = self.saecrhreceipt_var.get()
        if searchreceipt:
            showsubreceiptinfo = order_receipts().check_subreceipt_database(searchreceipt)
            if showsubreceiptinfo == False:
                messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
            elif showsubreceiptinfo == []:
                messagebox.showerror(parent=self.root2,title="No match", message="No match found")
            elif showsubreceiptinfo != []:
                self.clear_screen1()
                subproidcheck = ""
                for j in showsubreceiptinfo:
                    self.receiptno_var.set(j[1])
                    self.subreceiptno_var.set(j[6])
                    subproidcheck = j[2]
                    subproid = str(j[2])+" | "+str(j[12])+" | Rate: "+str(j[13])
                    self.subprodetails_var.set(subproid)
                    self.newqtyfordep_var.set(j[4])
                    self.comments1_var.set(j[10])
                    addby = str(j[7])+" | "+str(j[8])+"\tuser: "+str(j[9])+"-"+str(j[14])
                    self.addby1_var.set(addby)
                    empname = str(j[3])+" | "+str(j[15])+" S/O "+str(j[16])
                    emppic1 = j[17]
                    self.empid1_var.set(empname)
                    self.emppicentry1.config(state=NORMAL)
                    img = ImageTk.PhotoImage(Image.open(emppic1))
                    self.emppicentry1.imgtk = img
                    self.emppicentry1.image_create(END, image=img)
                    self.emppicentry1.config(state=DISABLED)

                receiptno = self.receiptno_var.get()
                subreceiptno = self.subreceiptno_var.get()
                showreceiptinfodatabase = order_receipts().seacrh_receipt_for_work_booking(receiptno)
                subreqqtydetails =  order_receipts().sub_receipt_details_database(subreceiptno)
                if showreceiptinfodatabase == False or subreqqtydetails == False:
                    messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                elif showreceiptinfodatabase != []:
                    selectedpro = ""
                    for i in showreceiptinfodatabase:
                        self.receiptno_var.set(i[1])
                        selectedpro = i[2]
                        prono = str(i[2])+" | "+str(i[3])+" "+str(i[18])+" | "+str(i[17])
                        self.depid_var.set(prono)
                        self.articalid_var.set(i[4])
                        self.productno_var.set(i[20])
                        self.size_var.set(i[21])
                        self.color_var.set(i[22])
                        addedby = str(i[9])+" | "+str(i[10])+"\tuser: "+str(i[7])+"-"+str(i[23])
                        self.addby_var.set(addedby)
                        empid = i[8]
                        empname = str(i[24])+" S/O "+str(i[25])
                        emppic = i[26]
                        self.empid_var.set(empid)
                        self.empname_var.set(empname)
                        self.orderid_var.set(i[27])
                        self.factorypo_var.set(i[28])
                        self.customerpo_var.set(i[29])
                        self.description_var.set(i[30])
                        self.ordertype_var.set(i[31])
                        self.emppicentry.config(state=NORMAL)
                        img = ImageTk.PhotoImage(Image.open(emppic))
                        self.emppicentry.imgtk = img
                        self.emppicentry.image_create(END, image=img)
                        self.emppicentry.config(state=DISABLED)
                        self.comments_var.set(i[11])
                        self.arttotalqty_var.set(i[5])
                        self.orderqty_var.set(i[28])
                    
                    subreqqty = self.newqtyfordep_var.get()
                    if subreqqtydetails != []:
                        totalsaved = 0
                        for k in subreqqtydetails:
                            adddate = str(k[3])+" / "+str(k[4])
                            username = str(k[5])+"-"+str(k[9])
                            totalsaved = totalsaved + k[2]
                            self.tree2.insert("", END, iid=k[0], values=(k[2], adddate, username))

                        remain = int(subreqqty) - int(totalsaved)
                        self.artremainqty_var.set(remain)
                    elif subreqqtydetails == []:
                        self.artremainqty_var.set(subreqqty)

                    checkallreceiptsofsubpro = order_receipts().check_all_sub_receipts_numbers(subproidcheck, receiptno)
                    if checkallreceiptsofsubpro == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif checkallreceiptsofsubpro == []:
                        pass
                    elif checkallreceiptsofsubpro != []:
                        for k in checkallreceiptsofsubpro:
                            reqid = k[0]
                            reqemp = str(k[1])+" | "+str(k[4])+" S/O "+str(k[5])
                            reqqty = k[2]
                            if k[3] == None:
                                comp = 0
                            else:    
                                comp = k[3]
                            
                            r = int(reqqty) - int(comp)
                            self.tree3.insert("", END, iid=reqid, values=(reqid, reqemp, reqqty, comp, r))
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Seacrh details are empty")

    #   Save Receipt Qty
    def save_receipt_qty(self):
        subreceiptid = self.subreceiptno_var.get()
        adddate = self.current_date()
        addtime = self.current_time()
        user = self.username
        pcqty = self.clearqty_var.get()
        remain = self.artremainqty_var.get()
        reqqty = self.newqtyfordep_var.get()
        if subreceiptid and pcqty:
            if pcqty.isdigit() == True:
                if int(pcqty) <= int(remain) and int(pcqty) != 0 and int(pcqty) <= int(reqqty):
                    n = user.split("-")
                    userid = n[0]
                    saveartindep = order_receipts().save_sub_req_qty_database(subreceiptid,adddate, addtime,  userid, pcqty)
                    if saveartindep == False:
                        messagebox.showerror(parent=self.root2,title="Server Respone", message="Database connection lost")
                    elif saveartindep == "Empty":
                        messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")
                    elif saveartindep == "Save":
                        self.saecrhreceipt_var.set(subreceiptid)
                        self.search_receipt()
                        messagebox.showinfo(parent=self.root2, title="Saved", message="Quantity of receipt no: "+str(subreceiptid)+" has been saved")
                else:
                    messagebox.showerror(parent=self.root2, title="Quantity", message="Quantity can't be greater then remain & total pc / can't be 0")
            else:
                messagebox.showwarning(parent=self.root2, title="Error", message="Quantity must be int")
        else:
            messagebox.showerror(parent=self.root2,title="Empty", message="Fill required fields")



































































































































































































































