#   Tkinter Import
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from database import database_class
from Directors import director_class
from Main_Store import main_store_class
from Receipts import receipt_system
from data_entry import data_entry_class
from Payment import payment_systemn
import babel.numbers


class start:
    #   init
    def __init__(self):
        self.black = "black"
        self.white = "white"
        self.gray = "#ededf0"
        self.bgcolor = "#E6E7E8"
        self.powderblue = "powder blue"
        self.lightgreen = "#cdfac5"
        self.lightred = "#fac5d5"
        self.green = "green"
        self.red = "red"

        self.loginbackgroundphoto = Image.open("img/login.png")
        self.appiconphoto = Image.open("img/icon.png")
        self.entericonphoto = Image.open("img/enter_button.png")

    #   DataBase Connection
    def first_root(self):
        self.root = Tk()
        self.root.geometry("400x550")
        self.root.title("Littlewood Corporation(pvt) - ERP")
        icon_photo = ImageTk.PhotoImage(self.appiconphoto)
        self.root.iconphoto(False, icon_photo)
        self.root.resizable(False, False)
        self.bglabel = ImageTk.PhotoImage(self.loginbackgroundphoto)
        self.backgroundlabel = Label(self.root, image=self.bglabel, width=400, height=550)
        self.backgroundlabel.place(x=0, y=0)

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Time new rooman", 8, "bold", "italic"), foreground="black", background="gray", relief="groove")
        

        self.user = StringVar()
        self.password = StringVar()
        
        self.userentry =  Entry(self.root ,bd=2, relief=SUNKEN, justify="left", fg="black", textvariable=self.user, bg="#ede9dd", font=("Time new rooman", 11, "bold"))
        self.userentry.place(x=180, y=278, height=27, width=170)
        self.passwordentry = Entry(self.root ,bd=2, relief=SUNKEN, justify="left", fg="black", textvariable=self.password, bg="#ede9dd", font=("Time new rooman", 14, "bold"), show="*")
        self.passwordentry.place(x=180, y=341, height=27, width=170)
        self.userentry.focus_set()
        self.userentry.insert(1, "hamza")
        self.passwordentry.insert(1, "123")
        self.entericon = ImageTk.PhotoImage(self.entericonphoto)
        self.entrbutton = Button(self.root, width=73, text="Enter", font=("Time new rooman", 8, "bold", "italic"), image=self.entericon, compound=RIGHT, fg=self.black, bg=self.gray, activebackground=self.powderblue, relief=GROOVE, command=lambda:self.check(None), bd=2)
        self.entrbutton.place(x=180, y=395, height=35)
        self.root.bind("<Return>", self.check)

        self.root.mainloop()

    #   Check
    def check(self, eve):
        a = database_class().database_connection_check()
        if a == True:
            u = (self.user.get()).lower()
            p = self.password.get()
            if u and p:
                checkuser = database_class().user_checking(user=u, password=p)
                if checkuser == False:
                    messagebox.showerror(parent=self.root,title="Server Respone", message="Database connection lost")
                elif checkuser == []:
                    messagebox.showerror(parent=self.root, title="User", message="User not found")
                elif checkuser == "NO MATCH":
                    messagebox.showerror(parent=self.root, title="invalid login", message="User not add in database. Contact Admin")
                elif checkuser != []:
                    u = ""
                    cat = ""
                    for i in checkuser:
                        u = str(i[0])+"-"+str(i[1])
                        cat = i[4]
                    if cat == "Director":
                        self.root.withdraw()
                        self.password.set("")
                        director_class(self.root, u).new_window()
                    elif cat == "Main Store":
                        self.root.withdraw()
                        self.password.set("")
                        main_store_class(self.root, u).new_window()
                    elif cat == "Receipt":
                        self.root.withdraw()
                        self.password.set("")
                        receipt_system(self.root, u).new_window()
                    elif cat == "Data Entry":
                        self.root.withdraw()
                        self.password.set("")
                        data_entry_class(self.root, u).new_window()
                    elif cat == "Payment":
                        self.root.withdraw()
                        self.password.set("")
                        payment_systemn(self.root, u).new_window()

            else:
              messagebox.showwarning(parent=self.root,title="Empty", message="UserName/Password empty")      
        else:
            messagebox.showerror(parent=self.root,title="Server Respone", message="Database connection lost")



start().first_root()

