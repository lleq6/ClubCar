# Project CS436 By Baboon Team

from datetime import timedelta
import datetime as date
import random
from subprocess import check_call
import textwrap
from tkinter import messagebox
from tkinter import ttk
from CarOrder import *
from SQLConnect import *
from tkinter import *
from CarInfo import *
from Cart import *
from Account import *
from Payment import *
from Address import *
from checker import Checker

def MainWindow():
    Root = Tk()
    Width = 1280
    Height = 720
    X = Root.winfo_screenwidth() / 2 - Width / 2
    Y = Root.winfo_screenheight() / 2 - Height / 2
    Root.title("Club Car | Final Project CS436 - Baboon Team")
    Root.iconphoto(False, PhotoImage(file="Image/Icon.png"))
    Root.resizable(False, False)
    Root.geometry("%dx%d+%d+%d"%(Width, Height, X, Y))
    Root.configure(bg="#202225")
    Root.rowconfigure(0, weight=1)
    Root.columnconfigure(1, weight=1)
    return Root

global mainFrame
def changeFrame(nextFrame):
    global mainFrame
    mainFrame.destroy()
    mainFrame = nextFrame
    mainFrame.grid(row=0, column=1, sticky='news')

def loginPage():
    loginFrame = Frame(Root, bg='#36393F')
    loginFrame.columnconfigure(0, weight=1)
    loginFrame.rowconfigure(1, weight=2)
    l_usernameInput = StringVar()
    l_passwordInput = StringVar()
    r_usernameInput = StringVar()
    r_passwordInput = StringVar()
    r_firstnameInput = StringVar()
    r_lastnameInput = StringVar()
    r_emailInput = StringVar()
    r_phoneInput = StringVar()
    r_checkState = IntVar()

    def Top():
        global LoginButton
        topFrame = Frame(loginFrame, bg='#0B0B0B')
        topFrame.columnconfigure((0, 1), weight=1)
        Label(topFrame, image=Logo, bg='#0B0B0B').grid(row=0, column=0, sticky="w", padx=80)
        rightFrame = Frame(topFrame, bg='#0B0B0B')
        rightFrame.rowconfigure((0, 1, 2), weight=1)
        Label(rightFrame, image=EntryLogin, bg="#0B0B0B").grid(row=1, column=0, padx=5, sticky='w')
        Label(rightFrame, text='Username', bg='#0B0B0B', fg='#DCDCDC', font=("Helvetica 10 bold")).grid(row=0, column=0, padx=10, sticky='w')
        L_usernameInput = Entry(rightFrame, textvariable=l_usernameInput, font=("Helvetica 10 bold"), borderwidth=0, bg="#252525", fg="#DCDCDC", insertbackground="white", width=22)
        L_usernameInput.grid(row=1, column=0, padx=11, sticky='w')
        Label(rightFrame, image=EntryLogin, bg="#0B0B0B").grid(row=1, column=1, padx=5, sticky='w')
        Label(rightFrame, text='Password', bg='#0B0B0B', fg='#DCDCDC', font=("Helvetica 10 bold")).grid(row=0, column=1, padx=10, sticky='w')
        L_passwordInput = Entry(rightFrame, textvariable=l_passwordInput, font=("Helvetica 10 bold"), borderwidth=0, bg="#252525", fg="#DCDCDC", insertbackground="white", width=22, show="*")
        L_passwordInput.grid(row=1, column=1, padx=11, sticky='w')
        Label(rightFrame, text='Forget Password?', bg='#0B0B0B', fg='#A0A0A0', font=("Helvetica 8 bold")).grid(row=2, column=1, padx=10, sticky='w')
        LoginButton = Button(rightFrame, image=L_image, bg='#0B0B0B', activebackground="#0B0B0B", borderwidth=0, command=lambda:LoginClick(l_usernameInput.get(), l_passwordInput.get()))
        LoginButton.grid(row=0, rowspan=3, column=2, padx=20, sticky='w')
        rightFrame.grid(row=0, column=1, padx=50, pady=17, sticky='e')
        topFrame.grid(row=0, column=0, sticky='news')

    def Main():
        bodyFrame = Frame(loginFrame, bg='#0B0B0B')
        bodyFrame.rowconfigure(0, weight=1)
        bodyFrame.columnconfigure((0, 1), weight=1)
        Label(bodyFrame, image=LoginBG, bg='#0B0B0B', border=0, borderwidth=0).grid(row=0, columnspan=2, pady=7, sticky='news')
        fromFrame = Frame(bodyFrame, bg='#0B0B0B')
        Label(fromFrame, text="BECOME A CLUBCAR MEMBER", bg="#0B0B0B", fg="#F1F1F1", font=("Helvetica 16 bold"), border=0, borderwidth=0).grid(row=0, columnspan=2)
        Label(fromFrame, text="Create your ClubCar Member profile and get first\naccess to the very best of cars inspiration", bg="#0B0B0B", fg="#8E8B8B", font=("Helvetica 10 bold"), border=0, borderwidth=0).grid(row=1, columnspan=2)
        Label(fromFrame, text="", bg="#0B0B0B", fg="#F1F1F1", font=("Helvetica 10 bold"), border=0, borderwidth=0).grid(row=2, columnspan=2, pady=2)
        Label(fromFrame, image=ImgEntry1, bg="#0B0B0B", border=0, borderwidth=0).grid(row=3, columnspan=2, pady=7)
        R_usernameInput = tkEntry(fromFrame, r_usernameInput, 'Username', font=("Helvetica 12"), bg="#0B0B0B", fg="#D4D4D4")
        R_usernameInput["width"] = 35
        R_usernameInput.grid(row=3, columnspan=2, padx=10, pady=7)
        Label(fromFrame, image=ImgEntry1, bg="#0B0B0B", border=0, borderwidth=0).grid(row=4, columnspan=2, pady=7)
        R_passwordInput = tkEntry(fromFrame, r_passwordInput, 'Password', font=("Helvetica 12"), bg="#0B0B0B", fg="#D4D4D4")
        R_passwordInput["width"] = 35
        R_passwordInput.grid(row=4, columnspan=2, padx=10, pady=7)
        Label(fromFrame, image=ImgEntry2, bg="#0B0B0B", border=0, borderwidth=0).grid(row=5, columnspan=2, pady=7)
        R_firstname = tkEntry(fromFrame, r_firstnameInput, 'First Name', font=("Helvetica 12"), bg="#0B0B0B", fg="#D4D4D4")
        R_firstname["width"] = 15
        R_firstname.grid(row=5, column=0, padx=10, pady=7, sticky="w")
        R_lastname = tkEntry(fromFrame, r_lastnameInput, 'Last Name', font=("Helvetica 12"), bg="#0B0B0B", fg="#D4D4D4")
        R_lastname["width"] = 15
        R_lastname.grid(row=5, column=1, padx=12, pady=7, sticky="e")
        Label(fromFrame, image=ImgEntry1, bg="#0B0B0B", border=0, borderwidth=0).grid(row=6, columnspan=2, pady=7)
        R_email = tkEntry(fromFrame, r_emailInput, 'Email', font=("Helvetica 12"), bg="#0B0B0B", fg="#D4D4D4")
        R_email["width"] = 35
        R_email.grid(row=6, columnspan=2, padx=10, pady=7)
        Label(fromFrame, image=ImgEntry1, bg="#0B0B0B", border=0, borderwidth=0).grid(row=7, columnspan=2, pady=7)
        R_number = tkEntry(fromFrame, r_phoneInput, 'Phone Number', font=("Helvetica 12"), bg="#0B0B0B", fg="#D4D4D4")
        R_number["width"] = 35
        R_number.grid(row=7, columnspan=2, padx=10, pady=7)
        data = (r_usernameInput, r_passwordInput, r_firstnameInput, r_lastnameInput, r_emailInput, r_phoneInput)
        state = (R_usernameInput, R_passwordInput, R_firstname, R_lastname, R_email, R_number)
        regCheckbox = Checkbutton(fromFrame, variable=r_checkState, bg="#0B0B0B", activebackground="#0B0B0B", fg="#0B0B0B", border=0, borderwidth=0)
        regCheckbox.grid(row=8, columnspan=2, pady=10, sticky="w")
        Label(fromFrame, text="Sign up for get updates for Club Cars offers and member benefits", bg="#0B0B0B", fg="#8E8B8B", font=("Helvetica 7 bold"), border=0, borderwidth=0).grid(row=8, columnspan=2, padx=10, pady=10, sticky="e")
        registerButton = Button(fromFrame, image=regButtonImg, border=0, borderwidth=0, bg='#0B0B0B', activebackground='#0B0B0B', command=lambda:createAccountClick(data, state))
        registerButton.grid(row=9, columnspan=2, sticky='news')
        fromFrame.grid(row=0, column=1, padx=195, pady=71, sticky='ne')
        bodyFrame.grid(row=1, column=0, sticky='news')
    Top()
    Main()

    def LoginClick(username, password):
        global mainFrame,data1,profileState
        Session = SQLConnect.GetConnect()
        Cursor = Session.cursor()
        with Session:
            sql = f"SELECT * FROM Account WHERE Username='{username}'"
            Cursor.execute(sql)
            data1 = Cursor.fetchone()
        
        if data1 == None:
            messagebox.showerror('ERROR','Username not found!')
            return
        
        if password != data1[2]:
            messagebox.showerror('ERROR', 'Invalid password!')
            return
        Account.UID = data1[0]
        Account.Username = data1[1]
        Account.Password = data1[2]
        Account.Name = data1[3]
        Account.Email = data1[4]
        Account.Number = data1[5]
        Account.Point = data1[6]
        Account.Payment = GetAccountPayment(Account.UID)
        Account.Address = GetAccountAddress(Account.UID)
        Account.discountState = data1[7]
        Cursor.close()
        Session.close()
        messagebox.showinfo('Login', 'Login Complete')
        Root.configure(bg="#202225")
        Root.rowconfigure(0, weight=1)
        Root.columnconfigure(1, weight=1)
        Root.columnconfigure(0, weight=0)
        mainFrame.destroy()
        MenuFrame()
        mainFrame = HomeFrame()
        mainFrame.grid(row=0, column=1, sticky='news')
        profileState = False

    def createAccountClick(data,state):
        global profileState
        data = [i.get() for i in data]
        state = [i.cget('state') for i in state]
        if 'disabled' in state:
            messagebox.showerror('ERROR', 'Please fill all data')
            return
        if '' in data:
            messagebox.showerror('ERROR', 'Please fill data')
            return
        dataStatus = [Checker.usernameCheck(data[0]), Checker.passwordCheck(data[1]), Checker.emailCheck(data[4]), Checker.phoneCheck(data[5])]
        statusText = ['Invalid username\nUsername must be a-z and 0-9','Invalid Password\nPassword can only have 8-30 character!\nPassword must have 3 character 3 numberic atleast\nPlease try again!',
        'Invalid Email please try again!','Invalid phone please try again!']
        for i in range(len(dataStatus)):
            if dataStatus[i] == False:
                messagebox.showerror('Error',statusText[i])
                return
        if r_checkState.get() == 0:
            messagebox.showwarning("Club Car", "Please check get an offer!")
            return
        checkData = [data[0], data[4], data[5]]
        check = ['Username', 'Email', 'Number']
        Session = SQLConnect.GetConnect()
        Cursor = Session.cursor()
        with Session:
            for i in range(len(checkData)):
                sql = f"SELECT * FROM Account WHERE {check[i]}='{checkData[i]}'"
                Cursor.execute(sql)
                if Cursor.fetchall() != []:
                    messagebox.showerror('ERROR',f'{check[i]} is already is use!\nPlease try again!')
                    return

            sql = f"INSERT INTO Account (Username, Password, Name, Email, Number, Point) VALUES ('{data[0]}', '{data[1]}', '{data[2]} {data[3]}', '{data[4]}', '{data[5]}', 0) RETURNING UID"
            Cursor.execute(sql)
            UID = Cursor.lastrowid
            sql = f"INSERT INTO Account_Payment (UID, TransactionId) VALUES ('{UID}', '{tsGenerator()}')"
            Cursor.execute(sql)
            sql = f"INSERT INTO Account_Address (UID) VALUES ('{UID}')"
            Cursor.execute(sql)
            Session.commit()
            Account.UID = UID
            Account.Username = data[0]
            Account.Password = data[1]
            Account.Name = f"{data[2]} {data[3]}"
            Account.Email = data[4]
            Account.Number = data[5]
            Account.Point = 0
            Account.Payment = GetAccountPayment(Account.UID)
            Account.Address = GetAccountAddress(Account.UID)
            messagebox.showinfo('Register', 'Register Complete!')
        Cursor.close()
        Session.close()
        LoginClick(data[0],data[1])
    return loginFrame

def MenuFrame():
    global ButtonHome
    global ButtonCar
    global ButtonCart
    global ButtonOrder
    global ButtonProfile
    Menu = Frame(Root, bg="#202225")
    Menu.rowconfigure(4, weight=1)
    Menu.columnconfigure(0, weight=1)
    ButtonHome = Button(Menu, image=IconHome1, border=0, borderwidth=0, bg="#202225", activebackground="#202225", command=lambda:changeFrame(HomeFrame()))
    ButtonHome.grid(row=0, column=0, pady=10)
    ButtonCar = Button(Menu, image=IconCar1, border=0, borderwidth=0, bg="#202225", activebackground="#202225", command=lambda Cars = GetCars("ALL") : changeFrame(CarsMyRent(Cars)))
    ButtonCar.grid(row=1, column=0, pady=10)
    ButtonCart = Button(Menu, image=IconCart1, border=0, borderwidth=0, bg="#202225", activebackground="#202225", command=lambda:changeFrame(PaymentFrame()))
    ButtonCart.grid(row=2, column=0, pady=10)
    ButtonOrder = Button(Menu, image=IconOrder1, border=0, borderwidth=0, bg="#202225", activebackground="#202225", command=lambda:changeFrame(OrderFrame()))
    ButtonOrder.grid(row=3, column=0, pady=10)
    ButtonProfile = Button(Menu, image=IconProfile1, border=0, borderwidth=0, bg="#202225", activebackground="#202225",command=checkprofile)
    ButtonProfile.grid(row=4, column=0, pady=20, sticky="s")
    Menu.grid(row=0, column=0, sticky="news", ipadx=15)

def profile():
    ButtonProfile["image"] = IconProfile2
    profileframe = Frame(Root, bg="#202225",width=290,height=500)
    profileframe.rowconfigure((0), weight=1)
    profileframe.rowconfigure((1,2), weight=2)
    profileframe.columnconfigure(0, weight=1)
    Frame(profileframe,bg = "#6480B8",width=290,height=100).grid(row=0,column=0,sticky="nwes",pady=10)
    Frame(profileframe,bg = "#6480B8",width=290,height=50).grid(row=0,column=0,sticky="n")
    Label(profileframe,image=profiletest,bg="#6480B8").grid(row=0,column=0,sticky="nw",pady=10)
    PDetailframe = Frame(profileframe,background="white",width=290,height=250)
    PDetailframe.rowconfigure((0,1,2,3,4,5,6), weight=1)
    PDetailframe.columnconfigure(0, weight=1)
    PDetailframe.grid(row=1,column=0,sticky="nwes")
    Label(PDetailframe,image=Dprofile,bg="#202225").grid(row=0,rowspan=7,column=0,sticky="wes")
    Label(PDetailframe,text= data1[3],fg="lightblue",font=("Helvetica 10 bold"),bg="#141416").grid(row=0,column=0,sticky="w",padx=15)
    Label(PDetailframe,text="ชื่อ",fg="white",font=("Helvetica 8 bold"),bg="#141416").grid(row=1,column=0,sticky="w",padx=15)
    Label(PDetailframe,text= data1[3],fg="#C9C9C9",font=("Helvetica 7 bold"),bg="#141416").grid(row=2,column=0,sticky="w",padx=15)
    Label(PDetailframe,text="อีเมล",fg="white",font=("Helvetica 8 bold"),bg="#141416").grid(row=3,column=0,sticky="w",padx=15)
    Label(PDetailframe,text=data1[4],fg="#C9C9C9",font=("Helvetica 7 bold"),bg="#141416").grid(row=4,column=0,sticky="w",padx=15)
    Label(PDetailframe,text="เบอร์โทรศัพท์",fg="white",font=("Helvetica 8 bold"),bg="#141416").grid(row=5,column=0,sticky="w",padx=15)
    Label(PDetailframe,text= data1[5],fg="#C9C9C9",font=("Helvetica 7 bold"),bg="#141416").grid(row=6,column=0,sticky="w",padx=15)
    pointframe = Frame(profileframe,bg="#202225",width=290,height=200)
    pointframe.rowconfigure((0,1), weight=1)
    pointframe.columnconfigure((0,1,2), weight=1)
    pointframe.grid(row=2,column=0,sticky="nwes")
    Point = data1[6]
    Label(pointframe,image=point,bg="#202225").grid(row=0,rowspan=2,columnspan=3,sticky="wes")
    Label(pointframe,text=data1[3],bg="#494949",fg="#FCE07B",image=member,compound=RIGHT,font=("Helvetica 8 bold")).grid(row=0,column=0,sticky="e")
    Label(pointframe,text=Account.Point,bg="#494949",fg="#A07400",image=memberp,compound=CENTER,font=("Helvetica 8")).grid(row=0,column=1,sticky="w")
    dpoint= Button(pointframe,image=discount,borderwidth=0,activebackground="#494949",bg="#494949", command=Dpoint)
    dpoint.grid(row=0,column=2,sticky="w")
    if Account.Point >=100 and Account.discountState == 0:
        dpoint["image"] = discountG
    else:
        dpoint["image"] = discount

    profileframe.place(x=110,y=150)
    return profileframe

def Dpoint():
    if Account.Point < 100:
        messagebox.showerror("Club Car", "You need more 100 point to use discount!")
        return
    elif Account.discountState == 1:
        messagebox.showerror("Club Car", "You alr use discount")
        return
    Account.discountState = 1
    Account.Point -= 100
    con = SQLConnect.GetConnect()
    Cursor = con.cursor()
    sql = "UPDATE Account set Point = ?, DiscountState=? where Username = ?;"
    Cursor.execute(sql,[Account.Point,Account.discountState, Account.Username])
    con.execute(sql,[Account.Point,Account.discountState, Account.Username])
    con.commit()
    con.close()

def checkprofile():
    global profileState, PFrame
    if profileState:
        PFrame.destroy()
        profileState = False
        ButtonProfile["image"] = IconProfile1
    else:
        PFrame = profile()
        profileState = True

def selectionFrameA():
    global BS, BE, BG, SearchBox
    frame = Frame(CarFrame, width=50, background='#2F3136')
    Label(frame, bg='#2F3136',image=sh).grid(row=0,column=0,pady=20)
    Button(frame, bg="#2F3136", image=Search, border=0, borderwidth=0, activebackground="#2F3136", command=OnSearch).grid(row=0,column=0,pady=20, sticky="e", padx=12)
    SearchBox = Entry(frame, bg='#2F3136',borderwidth=0,width=17, fg="white", insertbackground="white", textvariable=SearchName)
    SearchBox.grid(row=0,column=0,padx=20,pady=20,sticky="w")
    Label(frame, text ='Categories Cars', bg='#2F3136',font=("Helvetica 12"),fg="white").grid(row=1, column=0, pady=20)
    BS = Button(frame, text='Super Car',bg="#2F3136",fg="#B9BBBE",border=0,borderwidth=0,activebackground="#2F3136",activeforeground="#B9BBBE",font=("Helvetica 8 bold"),height=2,command=lambda:(Categories(1)))
    BS.grid(row=2, column=0, sticky='news')
    BE = Button(frame, text='Electric Vehicle',bg="#2F3136",fg="#B9BBBE",border=0,borderwidth=0,activebackground="#2F3136",activeforeground="#B9BBBE",font=("Helvetica 8 bold"),height=2,command=lambda:(Categories(2)))
    BE.grid(row=3, column=0, sticky='news')
    BG = Button(frame, text='General Car',bg="#2F3136",fg="#B9BBBE",border=0,borderwidth=0,activebackground="#2F3136",activeforeground="#B9BBBE",font=("Helvetica 8 bold"),height=2,command=lambda:(Categories(3)))
    BG.grid(row=4, column=0, sticky='news')
    return frame

def OnSearch():
    if SearchBox.get() == "":
        messagebox.showwarning("Club Car", "Enter text in searchbox first!")
        SearchBox.focus()
    else:
        Cars = GetCarsBySearch(SearchBox.get())
        if len(Cars) > 0:
            CarsMyRent(Cars)
        else:
            messagebox.showinfo("Club Car", f"'{SearchBox.get()}' Keywords not found.")

def Categories(num):
    if num == 1:
        BS["bg"] = "#474A51"
        BS["fg"] = "white"
        BE["bg"] = "#2F3136"
        BE["fg"] = "#B9BBBE"
        BG["bg"] = "#2F3136"
        BG["fg"] = "#B9BBBE"
        Cars = GetCars("Super Car")
        CarsMyRent(Cars)
    elif num == 2:
        BS["bg"] = "#2F3136"
        BS["fg"] = "#B9BBBE"
        BE["bg"] = "#474A51"
        BE["fg"] = "white"
        BG["bg"] = "#2F3136"
        BG["fg"] = "#B9BBBE"
        Cars = GetCars("Electric Vehicle")
        CarsMyRent(Cars)
    elif num == 3:
        BS["bg"] = "#2F3136"
        BS["fg"] = "#B9BBBE"
        BE["bg"] = "#2F3136"
        BE["fg"] = "#B9BBBE"
        BG["bg"] = "#474A51"
        BG["fg"] = "white"
        Cars = GetCars("General Car")
        CarsMyRent(Cars)

def checkCatagoriesBar():
    global catagoriesBarState, selectionFrame
    if catagoriesBarState:
        selectionFrame.destroy()
        catagoriesBarState = False
    else:
        selectionFrame = selectionFrameA()
        selectionFrame.grid(row=0,column=0, sticky='news', rowspan=10)
        catagoriesBarState = True
    
def CarsMyRent(Cars):
    global SelectPeriod, profileState
    SelectPeriod = "NONE"
    SearchName.set("")
    global catagoriesBarState, selectionFrame, CarFrame
    catagoriesBarState = False
    profileState = False
    ButtonHome["image"] = IconHome1
    ButtonCar["image"] = IconCar2
    ButtonCart["image"] = IconCart1
    ButtonOrder["image"] = IconOrder1
    ButtonProfile["image"] = IconProfile1
    CarFrame = Frame(Root, bg="#36393F")
    CarFrame.rowconfigure(1, weight=1)
    CarFrame.columnconfigure(2, weight=1)
    selectionFrame = selectionFrameA()
    selectionSwitch = Frame(CarFrame, width=50, background='red')
    Button(selectionSwitch,image=btc, borderwidth=0, command=checkCatagoriesBar, bg="#36393F",activebackground="#36393F").pack(fill=BOTH,side=LEFT)
    Label(CarFrame, text="Recommend for you", font=("Helvetica 20 bold"), bg="#36393F", fg="white").grid(row=0, column=2, padx=10, pady=30, sticky="w")
    Body = Canvas(CarFrame, bg="#36393F", highlightbackground="#36393F", border=0, borderwidth=0)
    scrollFrame = Frame(Body, bg="#36393F")
    Row, Column = 1, 0
    for Car in Cars:
        if Car != None:
            GroupFrame = Frame(scrollFrame, bg="#36393F")
            GroupFrame.rowconfigure((0, 1), weight=1)
            GroupFrame.columnconfigure((1, 2, 3), weight=1)
            Label(GroupFrame, image=ImgCars[Car.Id], bg="#36393F").grid(row=Row - 1, column=Column)
            Info = Frame(GroupFrame, bg="#292B2F")
            Info.columnconfigure((0, 1, 2), weight=1)
            Label(Info, text=f"{Car.Name}", bg="#292B2F", fg="white",font=("Helvetica 12 bold")).grid(row=0, columnspan=3, padx=10, pady=5, sticky="w")
            Label(Info, text=f"฿{Car.Price:,.2f} / 1 days", bg="#292B2F", fg="#B9BBBE", font=("Helvetica 14 bold")).grid(row=1, columnspan=3, padx=10, pady=5, sticky="w")
            if Car.Tag == 1:
                Label(GroupFrame, image=TagNew, bg="#292B2F", border=0, borderwidth=0).grid(row=Row - 1, column=Column, sticky="nw")
            if Car.State == 0:
                Button(Info, image=Rent, bg="#292B2F", activebackground="#292B2F", border=0, borderwidth=0, command=lambda Selector = Car : DetailCar(Selector)).grid(row=4, columnspan=3, pady=30)
            elif Car.State == 1:
                Label(GroupFrame, image=Rented, bg="#292B2F", activebackground="#292B2F", border=0, borderwidth=0).grid(row=Row - 1, column=Column, sticky="n", pady=50)
                Label(Info, image=Close, bg="#292B2F", activebackground="#292B2F", border=0, borderwidth=0).grid(row=4, columnspan=3, pady=30)
            Info.grid(row=Row - 1, column=Column, sticky="s", padx=15, pady=5)
            GroupFrame.grid(row=Row, column=Column, sticky="news", padx=10, pady=10)
            Column += 1
            if Column == 3:
                Column = 0
                Row += 2
    Body.create_window((0, 0), window=scrollFrame, anchor="n", width=1100)
    Scroller = Scrollbar(CarFrame, orient=VERTICAL, command=Body.yview)
    Scroller.grid(row=1,column=3, sticky='nes')
    Body.configure(yscrollcommand=Scroller.set)
    scrollFrame.update_idletasks()
    Body.config(scrollregion=Body.bbox("all"))
    Body.grid(row=1, column=2, sticky="news")
    selectionSwitch.grid(row=0,column=1, rowspan=10)
    CarFrame.grid(row=0, column=1, sticky="news")
    return CarFrame

def HomeFrame():
    global SelectPeriod, profileState
    SelectPeriod = "NONE"
    SearchName.set("")
    global SearchBox
    profileState = False
    ButtonHome["image"] = IconHome2
    ButtonCar["image"] = IconCar1
    ButtonCart["image"] = IconCart1
    ButtonOrder["image"] = IconOrder1
    ButtonProfile["image"] = IconProfile1
    Home = Frame(Root, bg="#36393F")
    Home.rowconfigure(0, weight=0)
    Home.rowconfigure(1, weight=1)
    Home.columnconfigure((0, 1), weight=1)
    Body = Canvas(Home, bg="white", highlightbackground="white", border=0, borderwidth=0, height=140)
    CarFrame = Frame(Body, bg="white")
    Column = 0
    for Car in Cars.values():
        if Car != None and Car.State != 1:
            GroupFrame = Frame(CarFrame, bg="white")
            GroupFrame.rowconfigure(0, weight=1)
            Button(GroupFrame, image=ImgModels[Car.Id], bg="white", border=0, borderwidth=0, activebackground="white", command=lambda Selector = Car : DetailCar(Selector)).grid(row=0, column=Column)
            GroupFrame.grid(row=0, column=Column, sticky="news", padx=10)
            Column += 1
    Body.create_window((0, 0), window=CarFrame, anchor="w", height=140)
    Scroller = Scrollbar(Home, orient=HORIZONTAL, command=Body.xview)
    Scroller.grid(row=0, columnspan=2, sticky="wse")
    Body.configure(xscrollcommand=Scroller.set)
    CarFrame.update_idletasks()
    Body.config(scrollregion=Body.bbox("all"))
    Body.grid(row=0, columnspan=2, sticky="news")
    Label(Home, image=homepage, bg="#0E0E0E").grid(row=1, columnspan=2, sticky="n")
    Label(Home, image=BHSearchBox, bg="#0E0E0E").grid(row=1, columnspan=2, sticky="n", pady=200)
    SearchBox = Entry(Home, borderwidth=0, bg="#0E0E0E", fg="white", insertbackground="white", font=("Helvetica 16"), width=36, textvariable=SearchName)
    SearchBox.grid(row=1, columnspan=2, sticky="n", pady=210)
    Button(Home, bg="#0E0E0E", image=Search, border=0, borderwidth=0, activebackground="#0E0E0E", command=OnSearch).grid(row=1, column=1, pady=210, padx=150, sticky="n")
    Home.grid(row=0, column=1, sticky="news")
    return Home

def DetailCar(Car):
    global MainImage
    Detail = Frame(Root, bg="#36393F")
    Detail.rowconfigure((0, 1, 2), weight=1)
    Detail.columnconfigure((0, 1, 2, 3), weight=1)
    Left = Frame(Detail, bg="#36393F")
    Left.columnconfigure(0, weight=1)
    MainImage = Label(Left, image=ImgDetailCar0[Car.Id], bg="#36393F", border=0, borderwidth=0)
    MainImage.grid(row=0, columnspan=4)
    ImageFrame = Frame(Left, bg="#36393F")
    ImageFrame.columnconfigure((0, 1, 2, 3), weight=1)
    Button(ImageFrame, image=ImgCarMini1[Car.Id], bg="#36393F", border=0, borderwidth=0, activebackground="#36393F", command=lambda Id = Car.Id :OnChangeImage(Id, 1)).grid(row=0, column=0, pady=10, sticky="news")
    Button(ImageFrame, image=ImgCarMini2[Car.Id], bg="#36393F", border=0, borderwidth=0, activebackground="#36393F", command=lambda Id = Car.Id :OnChangeImage(Id, 2)).grid(row=0, column=1, pady=10, sticky="news")
    Button(ImageFrame, image=ImgCarMini3[Car.Id], bg="#36393F", border=0, borderwidth=0, activebackground="#36393F", command=lambda Id = Car.Id :OnChangeImage(Id, 3)).grid(row=0, column=2, pady=10, sticky="news")
    Button(ImageFrame, image=ImgCarMini4[Car.Id], bg="#36393F", border=0, borderwidth=0, activebackground="#36393F", command=lambda Id = Car.Id :OnChangeImage(Id, 4)).grid(row=0, column=3, pady=10, sticky="news")
    ImageFrame.grid(row=1, column=0, sticky="news")
    Label(Left, text=" " * 110, bg="#36393F", fg="#454545", font=("Helvetica 13 bold underline")).grid(row=2, column=0)
    Label(Left, text=Car.Name, bg="#36393F", fg="white", font=("Helvetica 26 bold")).grid(row=3, column=0, padx=20)
    Option = Frame(Left, bg="#36393F")
    Option.rowconfigure((0, 1), weight=1)
    Option.columnconfigure((0, 1, 2, 3, 4), weight=1)
    Label(Option, text=f"{Car.Horsepower}", bg="#36393F", fg="white", font=("Helvetica 32 bold")).grid(row=0, column=0)
    Label(Option, text="HORSEPOWER", bg="#36393F", fg="white", font=("Helvetica 10 bold")).grid(row=1, column=0)
    Label(Option, image=Separator, bg="#36393F").grid(row=0, rowspan=2, column=1)
    Label(Option, text=f"{Car.Acceleration:,.1f} s", bg="#36393F", fg="white", font=("Helvetica 32 bold")).grid(row=0, column=2)
    Label(Option, text="ACCELERATION", bg="#36393F", fg="white", font=("Helvetica 10 bold")).grid(row=1, column=2)
    Label(Option, image=Separator, bg="#36393F").grid(row=0, rowspan=2, column=3)
    Label(Option, text=f"{Car.TopSpeed}", bg="#36393F", fg="white", font=("Helvetica 32 bold")).grid(row=0, column=4)
    Label(Option, text="TOP SPEED", bg="#36393F", fg="white", font=("Helvetica 10 bold")).grid(row=1, column=4)
    Option.grid(row=4, column=0, sticky="news")
    Left.grid(row=1, column=1, sticky="news")
    Right = Frame(Detail, bg="#36393F")
    Right.columnconfigure(0, weight=1)
    Label(Right, text=Car.Name, bg="#36393F", fg="white", font=("Helvetica 16 bold")).grid(row=0, column=0, padx=40, pady=5, sticky="w")
    Label(Right, text=f"฿{Car.Price:,.2f}", bg="#36393F", fg="white", font=("Helvetica 12 bold")).grid(row=1, column=0, padx=40, sticky="w")
    Label(Right, text=" " * 110, bg="#36393F", fg="#454545", font=("Helvetica 13 bold underline")).grid(row=2, column=0, padx=40, sticky="w")
    Label(Right, text="Details", bg="#36393F", fg="white", font=("Helvetica 12 bold")).grid(row=3, column=0, padx=40, pady=5, sticky="w")
    Label(Right, image=DescriptionFrame, bg="#36393F").grid(row=4, column=0, pady=5)
    descriptionFrame = Frame(Right, bg="#2F3136")
    descriptionFrame.rowconfigure(0, weight=1)
    descriptionFrame.columnconfigure(0, weight=1)
    Body = Canvas(descriptionFrame, bg="#2F3136", highlightbackground="#2F3136", border=0, borderwidth=0, height=100)
    BoxFrame = Frame(Body, bg="#2F3136")
    Label(BoxFrame, text=f"{textwrap.fill(Car.Description, 60)}", bg="#2F3136", fg="white", font=("Helvetica 12 bold"), justify=LEFT, border=0, borderwidth=0).grid(row=0, column=0, sticky="w")
    Body.create_window((0, 0), window=BoxFrame, anchor="n")
    Scroller = Scrollbar(descriptionFrame, orient=VERTICAL, command=Body.yview)
    Scroller.grid(row=0, column=0, sticky='nes')
    Body.configure(yscrollcommand=Scroller.set)
    BoxFrame.update_idletasks()
    Body.config(scrollregion=Body.bbox("all"))
    Body.grid(row=0, column=0, sticky="news")
    descriptionFrame.grid(row=4, column=0, sticky="news", padx=70, pady=15)
    Label(Right, text="Period Rent", bg="#36393F", fg="white", font=("Helvetica 12 bold")).grid(row=5, column=0, padx=40, pady=5, sticky="w")
    FrameButton = Frame(Right, bg="#36393F")
    FrameButton.rowconfigure((0, 1), weight=1)
    FrameButton.columnconfigure((0, 1, 2), weight=1)
    for i in range(2):
        for j in range(3):
            Period = GetPeriod(i, j)
            ListButton.update({Period : Button(FrameButton, image=ButtonPeriod1, text=f"{Period}", border=0, borderwidth=0, bg="#36393F", activebackground="#36393F", activeforeground="white", compound=CENTER, fg="white", font=("Helvetica 12 bold"), command=lambda i = i, j = j : OnSelectPeriod(i, j))})
            ListButton[Period].grid(row=i, column=j, padx=5, pady=5, sticky="e" if j == 0 else "w" if j == 2 else "ns")
    FrameButton.grid(row=5, column=0, sticky="news")
    Button(Right, image=ButtonContinue, border=0, borderwidth=0, bg="#36393F", activebackground="#36393F", command=lambda:OnPayment(Car)).grid(row=7, column=0, padx=5, pady=20)
    Right.grid(row=1, column=2, sticky="news")
    Detail.grid(row=0, column=1, sticky="news")
    return Detail

def OnChangeImage(Id, Index):
    if Index == 1:
        MainImage["image"] = ImgDetailCar1[Id]
    elif Index == 2:
        MainImage["image"] = ImgDetailCar2[Id]
    elif Index == 3:
        MainImage["image"] = ImgDetailCar3[Id]
    elif Index == 4:
        MainImage["image"] = ImgDetailCar4[Id]

def OnSelectPeriod(i, j):
    global SelectPeriod
    OnResetButton()
    SelectPeriod = GetPeriod(i, j)
    ListButton[SelectPeriod]["image"] = ButtonPeriod2

def OnResetButton():
    for Button in ListButton.values():
        Button["image"] = ButtonPeriod1

def GetPeriod(i, j):
    return "1 Day" if i == 0 and j == 0 else "3 Day" if i == 0 and j == 1 else "5 Day" if i == 0 and j == 2 else "7 Day" if i == 1 and j == 0 else "1 Month" if i == 1 and j == 1 else "3 Month" if i == 1 and j == 2 else ""

def OnPayment(Car):
    if SelectPeriod == "NONE":
        messagebox.showwarning("Club Car", "Please select period rent!")
    else:
        cart.Add(Car, SelectPeriod)
        PaymentFrame()

def PaymentFrame():
    global SelectPayment, DeliveryType, OptionFrame, homeDelivery, pickupInStore, BPay, MPay, GPay, VPay, CPay, labelSelected
    global holderName, cardNumber, expMonthEntry, expYearEntry, cvcEntry, buttonPayment, ConcludeFrame, scrollFrame, Body
    global checkBox, labelPrivacy, selectedPayment, entryFrame, addressFrame, shipFrame, labelPlatter3, labelIconAddress
    global profileState, labelPlatterCard, cardInfoFrame, labelCardType, labelCardNumber, labelIconCard, labelCardNumber2
    global labelCardExpiration, labelTxtExpiration, labelGPay, contactEmail, contactPhone, shippingAddress
    SelectPayment = 2
    DeliveryType = 0
    profileState = False
    checkState.set(0)
    CalculatePayment()
    ButtonHome["image"] = IconHome1
    ButtonCar["image"] = IconCar1
    ButtonCart["image"] = IconCart2
    ButtonOrder["image"] = IconOrder1
    ButtonProfile["image"] = IconProfile1
    PaymentFrame = Frame(Root, bg="#2F2F2F")
    PaymentFrame.rowconfigure((0), weight=1)
    PaymentFrame.columnconfigure(0, weight=0)
    PaymentFrame.columnconfigure(1, weight=2)
    ConcludeFrame = Frame(PaymentFrame, bg="#202020")
    ConcludeFrame.rowconfigure(0, weight=1)
    ConcludeFrame.columnconfigure(0, weight=1)
    Body = Canvas(ConcludeFrame, bg="#202020", highlightbackground="#202020", highlightcolor="#202020", border=0, borderwidth=0)
    scrollFrame = Frame(Body, bg="#202020")
    scrollFrame.rowconfigure((0, 1), weight=1)
    scrollFrame.columnconfigure((0, 1), weight=1)
    Row = 0
    for Car in cart.Items.values():
        InfoFrame = Frame(scrollFrame, bg="#202020")
        InfoFrame.rowconfigure((0, 1, 2), weight=1)
        InfoFrame.columnconfigure((0, 1, 2, 3), weight=1)
        Label(InfoFrame, image=ImgCarMini0[Car.Id], bg="#202020").grid(row=0, rowspan=3, column=0, sticky="nw")
        Label(InfoFrame, text=f"{textwrap.fill(Car.Name, 15)}", bg="#202020", fg="white", font=("Helvetica 10"), justify=LEFT, width=15).grid(row=0, rowspan=3, column=1, sticky="nw")
        Label(InfoFrame, text=f"฿{Car.Price:,.2f}", bg="#202020", fg="white", font=("Helvetica 10")).grid(row=0, column=2, sticky="nw")
        Label(InfoFrame, text=f"Qty: {cart.Periods.get(Car.Id)}", bg="#202020", fg="white", font=("Helvetica 10")).grid(row=1, column=2, sticky="nw")
        Button(InfoFrame, image=IconRemove, bg="#202020", border=0, borderwidth=0, activebackground="#202020", command=lambda Selector = Car:OnRemoveItem(Selector)).grid(row=0, rowspan=3, column=3, sticky="news")
        InfoFrame.grid(row=Row, column=0, sticky="news", padx=10, pady=10)
        Label(scrollFrame, image=Line, bg="#202020").grid(row=Row + 1, columnspan=2, sticky="ew")
        Row += 2
    orderShipping = Frame(scrollFrame, bg="#202020")
    orderShipping.columnconfigure((0, 1), weight=1)
    Label(orderShipping, image=Platter1, bg="#202020").grid(row=0, columnspan=2, sticky="news", pady=20)
    homeDelivery = Button(orderShipping, image=ShippingBorder1, text="Home Delivery", bg="#313131", fg="white", border=0, borderwidth=0, activebackground="#313131", activeforeground="white", compound=CENTER, command=lambda:OnClickShipping(0))
    homeDelivery.grid(row=0, column=0, padx=10, sticky="e")
    pickupInStore = Button(orderShipping, image=ShippingBorder2, text="Pick up in Store", bg="#313131", fg="white", border=0, borderwidth=0, activebackground="#313131", activeforeground="white", compound=CENTER, command=lambda:OnClickShipping(1))
    pickupInStore.grid(row=0, column=1, padx=10, sticky="w")
    addressFrame = Frame(orderShipping, bg="#202020")
    addressFrame.columnconfigure(0, weight=1)
    labelPlatterCard = Label(addressFrame, image=Platter2, bg="#202020", border=0, borderwidth=0, activebackground="#202020")
    labelPlatterCard.grid(row=0, columnspan=2, sticky="news", pady=10)
    cardInfoFrame = Frame(addressFrame, bg="#313131")
    cardInfoFrame.columnconfigure((0, 1), weight=1)
    labelCardType = Label(cardInfoFrame, text=GetCardByType(SelectPayment), bg="#313131", fg="#FFFFFF", font=("Helvetica 10 bold"))
    labelCardType.grid(row=0, column=0, padx=40, sticky="w")
    txtCardNumber = f"{Account.Payment.MCardNumber[0:4]} {Account.Payment.MCardNumber[4:8]} {Account.Payment.MCardNumber[8:12]} {Account.Payment.MCardNumber[12:16]}" if Account.Payment.MCardNumber != "" else "•••• •••• •••• ••••"
    labelCardNumber = Label(cardInfoFrame, text=f"({txtCardNumber})", bg="#313131", fg="white", font=("Helvetica 8 bold"))
    labelCardNumber.grid(row=1, column=0, padx=40, sticky="w")
    Label(cardInfoFrame, text=f"{Account.Address.StreetAddress}, {Account.Address.City} {Account.Address.ZipCode}", bg="#313131", fg="white", font=("Helvetica 8 bold")).grid(row=2, column=0, padx=40, sticky="w")
    cardInfoFrame.grid(row=0, column=0, padx=50, sticky="ew")
    labelIconCard = Label(addressFrame, image=IconMasterCard, bg="#313131")
    labelIconCard.grid(row=0, column=0, padx=50, sticky="w")
    Label(addressFrame, image=Platter2, bg="#202020", border=0, borderwidth=0, activebackground="#202020").grid(row=1, columnspan=2, sticky="news", pady=10)
    contactFrame = Frame(addressFrame, bg="#313131")
    contactFrame.columnconfigure((0, 1), weight=1)
    Label(contactFrame, text="Contact", bg="#313131", fg="#EBEBF5", font=("Helvetica 8 bold")).grid(row=0, column=0, padx=40, sticky="w")
    contactEmail = Label(contactFrame, text=f"{Account.Email}", bg="#313131", fg="white", font=("Helvetica 8 bold"))
    contactEmail.grid(row=1, column=0, padx=40, sticky="w")
    contactPhone = Label(contactFrame, text=f"{Account.Number}", bg="#313131", fg="white", font=("Helvetica 8 bold"))
    contactPhone.grid(row=2, column=0, padx=40, sticky="w")
    Button(contactFrame, image=IconEdit, bg="#313131", border=0, borderwidth=0, activebackground="#313131", command=lambda:OnClickEdit(orderShipping)).grid(row=1, column=1, sticky="e")
    contactFrame.grid(row=1, column=0, padx=50, sticky="ew")
    Label(addressFrame, image=IconContact, bg="#313131").grid(row=1, column=0, padx=50, sticky="w")
    labelPlatter3 = Label(addressFrame, image=Platter3, bg="#202020", border=0, borderwidth=0, activebackground="#202020")
    labelPlatter3.grid(row=2, columnspan=2, sticky="news", pady=10)
    shipFrame = Frame(addressFrame, bg="#313131")
    shipFrame.columnconfigure((0, 1), weight=1)
    Label(shipFrame, text="Ship to", bg="#313131", fg="#EBEBF5", font=("Helvetica 8 bold")).grid(row=0, column=0, padx=40, sticky="w")
    shippingAddress = Label(shipFrame, text=f"{Account.Address.ToString()}", bg="#313131", fg="white", font=("Helvetica 8 bold"), justify=LEFT)
    shippingAddress.grid(row=1, rowspan=2, column=0, padx=40, sticky="w")
    Button(shipFrame, image=IconEdit, bg="#313131", border=0, borderwidth=0, activebackground="#313131", command=lambda:OnClickEdit(orderShipping)).grid(row=1, column=1, sticky="e")
    shipFrame.grid(row=2, column=0, padx=50, sticky="ew")
    labelIconAddress = Label(addressFrame, image=IconAddress, bg="#313131")
    labelIconAddress.grid(row=2, column=0, padx=50, sticky="w")
    addressFrame.grid(row=1, columnspan=2, sticky="news")
    orderShipping.grid(row=Row + 1, columnspan=2, sticky="news")
    Body.create_window((0, 0), window=scrollFrame, anchor="n", width=362)
    Scroller = Scrollbar(ConcludeFrame, orient=VERTICAL, command=Body.yview)
    Scroller.grid(row=0, column=0, sticky='nes')
    Body.configure(yscrollcommand=Scroller.set)
    scrollFrame.update_idletasks()
    Body.config(scrollregion=Body.bbox("all"))
    Body.grid(row=0, column=0, sticky="news")
    sumFrame = Frame(ConcludeFrame, bg="#202020")
    Label(sumFrame, image=IsumFrame, bg="#202020", compound=CENTER).grid(row=0, columnspan=2, sticky="news")
    inSideFrame = Frame(sumFrame, bg="#2C2C2C")
    inSideFrame.rowconfigure((2, 3, 4, 5, 7), weight=1)
    inSideFrame.columnconfigure((0, 1), weight=1)
    Label(inSideFrame, text="Summary", bg="#2C2C2C", fg="white", font=("Helvetica 18 bold")).grid(row=0, column=0, sticky="w", padx=40)
    Label(inSideFrame, text=" " * 74, bg="#2C2C2C", fg="#454545", font=("Helvetica 13 underline")).grid(row=1, columnspan=2)
    Label(inSideFrame, text="", bg="#2C2C2C", fg="white", font=("Helvetica 8")).grid(row=2, columnspan=2)
    Label(inSideFrame, text="SUB TOTAL", bg="#2C2C2C", fg="white", font=("Helvetica 8")).grid(row=3, column=0, sticky="w", padx=40)
    Label(inSideFrame, textvariable=SubTotal, bg="#2C2C2C", fg="white", font=("Helvetica 8")).grid(row=3, column=1, sticky="e", padx=40)
    Label(inSideFrame, text="SHIPPING", bg="#2C2C2C", fg="white", font=("Helvetica 8")).grid(row=4, column=0, sticky="w", padx=40)
    Label(inSideFrame, textvariable=Shipping, bg="#2C2C2C", fg="white", font=("Helvetica 8")).grid(row=4, column=1, sticky="e", padx=40)
    Label(inSideFrame, text="DISCOUNT TOTAL", bg="#2C2C2C", fg="white", font=("Helvetica 8")).grid(row=5, column=0, sticky="w", padx=40)
    Label(inSideFrame, textvariable=Discount, bg="#2C2C2C", fg="white", font=("Helvetica 8")).grid(row=5, column=1, sticky="e", padx=40)
    Label(inSideFrame, text="", bg="#2C2C2C", fg="white", font=("Helvetica 8")).grid(row=6, columnspan=2)
    Label(inSideFrame, text="TOTAL", bg="#2C2C2C", fg="white", font=("Helvetica 10")).grid(row=7, column=0, sticky="w", padx=40)
    Label(inSideFrame, textvariable=Total, bg="#2C2C2C", fg="white", font=("Helvetica 10")).grid(row=7, column=1, sticky="e", padx=40)
    inSideFrame.grid(row=0, column=0, sticky="e")
    sumFrame.grid(row=1, column=0, sticky="news")
    ConcludeFrame.grid(row=0, column=0, sticky="news")
    OptionFrame = Frame(PaymentFrame, bg="#2F2F2F")
    OptionFrame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    CPay = Button(OptionFrame, image=CPay1, bg="#2F2F2F", border=0, borderwidth=0, activebackground="#2F2F2F", command=lambda:OnClickSelect(0))
    CPay.grid(row=0, column=0, padx=5, pady=10)
    VPay = Button(OptionFrame, image=VPay1, bg="#2F2F2F", border=0, borderwidth=0, activebackground="#2F2F2F", command=lambda:OnClickSelect(1))
    VPay.grid(row=0, column=1, padx=5, pady=10)
    MPay = Button(OptionFrame, image=MPay2, bg="#2F2F2F", border=0, borderwidth=0, activebackground="#2F2F2F", command=lambda:OnClickSelect(2))
    MPay.grid(row=0, column=2, padx=5, pady=10)
    GPay = Button(OptionFrame, image=GPay1, bg="#2F2F2F", border=0, borderwidth=0, activebackground="#2F2F2F", command=lambda:OnClickSelect(3))
    GPay.grid(row=0, column=3, padx=5, pady=10)
    BPay = Button(OptionFrame, image=BPay1, bg="#2F2F2F", border=0, borderwidth=0, activebackground="#2F2F2F", command=lambda:OnClickSelect(4))
    BPay.grid(row=0, column=4, padx=5, pady=10)
    labelSelected = Label(OptionFrame, image=IconSelected, bg="#202020", border=0, borderwidth=0)
    labelSelected.grid(row=0, column=2, padx=10, pady=16, sticky="es")
    selectedPayment = Label(OptionFrame, image=MasterCard, bg="#2F2F2F")
    selectedPayment.grid(row=1, columnspan=5, pady=20)
    txtCardNumber2 = f"{Account.Payment.MCardNumber[0:4]} {Account.Payment.MCardNumber[4:8]} {Account.Payment.MCardNumber[8:12]} {Account.Payment.MCardNumber[12:16]}" if Account.Payment.MCardNumber != "" else "••••  ••••  ••••  ••••"
    labelCardNumber2 = Label(OptionFrame, text=f"{txtCardNumber2}", bg="#484206", fg="white", font=("Helvetica 12 bold"))
    labelCardNumber2.grid(row=1, columnspan=3, sticky="ws", padx=40, pady=75)
    labelTxtExpiration = Label(OptionFrame, text="VALID\nTHRU", bg="#484206", fg="white", font=("Helvetica 6 bold"))
    labelTxtExpiration.grid(row=1, columnspan=3, sticky="ws", padx=40, pady=50)
    txtExpriation = f"{Account.Payment.MExpirationMonth}/{Account.Payment.MExpirationYear}" if Account.Payment.MExpirationMonth != "" and Account.Payment.MExpirationYear != "" else "00/00"
    labelCardExpiration = Label(OptionFrame, text=f"{txtExpriation}", bg="#484206", fg="white", font=("Helvetica 8 bold"))
    labelCardExpiration.grid(row=1, columnspan=3, sticky="ws", padx=80, pady=50)
    entryFrame = Frame(OptionFrame, bg="#2F2F2F")
    entryFrame.columnconfigure((0, 1), weight=1)
    Label(entryFrame, image=Entry1, bg="#2F2F2F", border=0, borderwidth=0).grid(row=0, columnspan=2, pady=10)
    holderName = tkEntry(entryFrame, Holdername, "Cardholder name *", font=("Helvetica 10"))
    holderName["width"] = 45
    holderName.grid(row=0, columnspan=2)
    Label(entryFrame, image=Entry1, bg="#2F2F2F", border=0, borderwidth=0).grid(row=1, columnspan=2, pady=10)
    cardNumber = tkEntry(entryFrame, CardNumber, "Card Number *", font=("Helvetica 10"))
    cardNumber["width"] = 45
    cardNumber.grid(row=1, columnspan=2)
    Label(entryFrame, image=Entry2, bg="#2F2F2F", border=0, borderwidth=0).grid(row=2, column=0, pady=10)
    expMonthEntry = tkEntry(entryFrame, ExpMonth, "Expriation Month *", font=("Helvetica 10"))
    expMonthEntry["width"] = 18
    expMonthEntry.grid(row=2, column=0)
    Label(entryFrame, image=Entry2, bg="#2F2F2F", border=0, borderwidth=0).grid(row=2, column=1, pady=10)
    expYearEntry = tkEntry(entryFrame, ExpYear, "Expriation Year *", font=("Helvetica 10"))
    expYearEntry["width"] = 18
    expYearEntry.grid(row=2, column=1)
    Label(entryFrame, image=Entry2, bg="#2F2F2F", border=0, borderwidth=0).grid(row=3, column=0, pady=10)
    cvcEntry = tkEntry(entryFrame, CVC, "CVC *", font=("Helvetica 10"))
    cvcEntry["width"] = 18
    cvcEntry.grid(row=3, column=0)
    checkBox = Checkbutton(OptionFrame, bg="#2F2F2F", activebackground="#2F2F2F", border=0, borderwidth=0, variable=checkState)
    checkBox.grid(row=3, column=0, padx=15, sticky="w")
    labelPrivacy = Label(OptionFrame, text="I agree to Terms & Conditions and Privacy Policy", font=("Helvetica 10"), bg="#2F2F2F", fg="#C8C8C8", justify=LEFT)
    labelPrivacy.grid(row=3, column=0, columnspan=5, padx=45, sticky="e")
    buttonPayment = Button(OptionFrame, image=ImagePayment, bg="#2F2F2F", fg="white", border=0, borderwidth=0, activebackground="#2F2F2F", activeforeground="white", compound=CENTER, text=f"Pay with {GetCardByType(SelectPayment)}", font=("Helvetica 12 bold"), command=OnClickPayment)
    buttonPayment.grid(row=4, columnspan=5, pady=10)
    labelGPay = Label(OptionFrame, text="Press Click Button to Unlock ->", font=("Helvetica 10"), bg="#2F2F2F", fg="white")
    CheckPaymentInfo()
    OptionFrame.grid(row=0, column=1, sticky="ns")
    PaymentFrame.grid(row=0, column=1, sticky="news")
    return PaymentFrame

def OnClickEdit(orderShipping):
    global editFrame, entryFirstname, entryLastname, entryEmail, entryStreetAddress, comboboxState, entryCity, entryZipCode, entryPhone
    addressFrame.grid_forget()
    editFrame = Frame(orderShipping, bg="red")
    editFrame.columnconfigure((0, 1), weight=1)
    Label(editFrame, image=EditFrame, bg="#202020").grid(row=0, columnspan=2, sticky="news")
    etFrame = Frame(editFrame, bg="#313131")
    etFrame.columnconfigure((0, 1), weight=1)
    Label(etFrame, text="Shipping Address", bg="#313131", fg="white", font=("Helvetica 10 bold")).grid(row=0, column=0, pady=2, sticky="w")
    Button(etFrame, image=IconBack, bg="#313131", border=0, borderwidth=0, activebackground="#313131", command=lambda:OnClickBack(editFrame)).grid(row=0, column=1, padx=5, pady=2, sticky="e")
    Label(etFrame, image=EntryFirstname, bg="#313131").grid(row=1, column=0, pady=2, sticky="w")
    e_Firstname.set(Account.Address.Firstname)
    entryFirstname = Entry(etFrame, font=("Helvetica 10 bold"), textvariable=e_Firstname, bg="#313131", fg="white", insertbackground="white", border=0, borderwidth=0, width=17)
    entryFirstname.grid(row=1, column=0, padx=10, pady=13, sticky="ws")
    Label(etFrame, image=EntryLastname, bg="#313131").grid(row=1, column=1, pady=2, sticky="e")
    e_Lastname.set(Account.Address.Lastname)
    entryLastname = Entry(etFrame, font=("Helvetica 10 bold"), textvariable=e_Lastname, bg="#313131", fg="white", insertbackground="white", border=0, borderwidth=0, width=17)
    entryLastname.grid(row=1, column=1, padx=10, pady=13, sticky="ws")
    Label(etFrame, image=EntryEmail, bg="#313131").grid(row=2, columnspan=2, pady=2, sticky="news")
    e_Email.set(Account.Email)
    entryEmail = Entry(etFrame, font=("Helvetica 10 bold"), textvariable=e_Email, bg="#313131", fg="white", insertbackground="white", border=0, borderwidth=0, width=45)
    entryEmail.grid(row=2, columnspan=2, padx=10, pady=13, sticky="ws")
    Label(etFrame, image=EntryStreetAddress, bg="#313131").grid(row=3, columnspan=2, pady=2, sticky="news")
    e_StreetAddress.set(Account.Address.StreetAddress)
    entryStreetAddress = Entry(etFrame, font=("Helvetica 10 bold"), textvariable=e_StreetAddress, bg="#313131", fg="white", insertbackground="white", border=0, borderwidth=0, width=45)
    entryStreetAddress.grid(row=3, columnspan=2, padx=10, pady=13, sticky="ws")
    Label(etFrame, image=EntryState, bg="#313131").grid(row=4, column=0, pady=2, sticky="news")
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="#313131", background="white")
    comboboxState = ttk.Combobox(etFrame, font=("Helvetica 10 bold"), width=14, values=valuesState, textvariable=selectState, foreground="white")
    if Account.Address.State == "":
        comboboxState.set("Thailand")
    else:
        comboboxState.set(Account.Address.State)
    comboboxState.grid(row=4, column=0, padx=10, pady=13, sticky="ws")
    e_City.set(Account.Address.City)
    Label(etFrame, image=EntryCity, bg="#313131").grid(row=4, column=1, pady=2, sticky="news")
    entryCity = Entry(etFrame, font=("Helvetica 10 bold"), textvariable=e_City, bg="#313131", fg="white", insertbackground="white", border=0, borderwidth=0, width=17)
    entryCity.grid(row=4, column=1, padx=10, pady=13, sticky="ws")
    e_ZipCode.set(Account.Address.ZipCode)
    Label(etFrame, image=EntryZipCode, bg="#313131").grid(row=5, column=0, pady=2, sticky="news")
    entryZipCode = Entry(etFrame, font=("Helvetica 10 bold"), textvariable=e_ZipCode, bg="#313131", fg="white", insertbackground="white", border=0, borderwidth=0, width=17)
    entryZipCode.grid(row=5, column=0, padx=10, pady=13, sticky="ws")
    e_Phone.set(Account.Number)
    Label(etFrame, image=EntryPhone, bg="#313131").grid(row=5, column=1, pady=2, sticky="news")
    entryPhone = Entry(etFrame, font=("Helvetica 10 bold"), textvariable=e_Phone, bg="#313131", fg="white", insertbackground="white", border=0, borderwidth=0, width=17)
    entryPhone.grid(row=5, column=1, padx=10, pady=13, sticky="ws")
    Button(etFrame, image=ButtonSave, text="SAVE", fg="white", font=("Helvetica 12 bold"), bg="#313131", border=0, borderwidth=0, activebackground="#313131", activeforeground="white", compound=CENTER, command=OnClickSave).grid(row=6, columnspan=2, pady=10, sticky="news")
    etFrame.grid(row=0, columnspan=2, sticky="news", padx=40, pady=15)
    editFrame.grid(row=1, columnspan=2, sticky="news")
    UpdateFrame()

def UpdateFrame():
    Body.grid_forget()
    scrollFrame.grid_forget()
    Body.create_window((0, 0), window=scrollFrame, anchor="n", width=362)
    Scroller = Scrollbar(ConcludeFrame, orient=VERTICAL, command=Body.yview)
    Scroller.grid(row=0, column=0, sticky='nes')
    Body.configure(yscrollcommand=Scroller.set)
    scrollFrame.update_idletasks()
    Body.config(scrollregion=Body.bbox("all"))
    Body.grid(row=0, column=0, sticky="news")

def OnClickBack(editFrame):
    editFrame.grid_forget()
    editFrame.update_idletasks()
    UpdateFrame()
    addressFrame.grid(row=1, columnspan=2, sticky="news")

def OnClickSave():
    if entryFirstname.get() == "":
        messagebox.showwarning("Club Car", "Please enter Firstname first!")
    elif entryLastname.get() == "":
        messagebox.showwarning("Club Car", "Please enter Lastname first!")
    elif entryEmail.get() == "":
        messagebox.showwarning("Club Car", "Please enter Email first!")
    elif entryStreetAddress.get() == "":
        messagebox.showwarning("Club Car", "Please enter Street Address first!")
    elif comboboxState.get() == "" and comboboxState.get() not in valuesState:
        messagebox.showwarning("Club Car", "Please select State/Province first!")
    elif entryCity.get() == "":
        messagebox.showwarning("Club Car", "Please enter City first!")
    elif entryZipCode.get() == "":
        messagebox.showwarning("Club Car", "Please enter Zip Code first!")
    elif entryPhone.get() == "":
        messagebox.showwarning("Club Car", "Please enter Phone first!")
    else:
        Session = SQLConnect.GetConnect()
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Account SET Email='{e_Email.get()}', Number='{e_Phone.get()}' WHERE UID = '{Account.UID}'")
        Cursor.execute(f"UPDATE Account_Address SET Firstname='{e_Firstname.get()}', Lastname='{e_Lastname.get()}', StreetAddress='{e_StreetAddress.get()}', State='{selectState.get()}', City='{e_City.get()}', ZipCode='{e_ZipCode.get()}' WHERE UID = '{Account.UID}'")
        Session.commit()
        Account.Email = e_Email.get()
        Account.Number = e_Phone.get()
        Account.Address.Firstname = e_Firstname.get()
        Account.Address.Lastname = e_Lastname.get()
        Account.Address.StreetAddress = e_StreetAddress.get()
        Account.Address.State = selectState.get()
        Account.Address.City = e_City.get()
        Account.Address.ZipCode = e_ZipCode.get()
        Cursor.close()
        Session.close()
        contactEmail["text"] = Account.Email
        contactPhone["text"] = Account.Number
        shippingAddress["text"] = Account.Address.ToString()
        e_Phone.set(Account.Number)
        messagebox.showinfo("Club Car", "Save success.")

def OnClickPayment():
    Point = 0
    if DeliveryType == 0 and Account.Address.IsEmpty():
        messagebox.showwarning("Club Car", "Please enter delivery location information.")
    elif Account.Payment.IsEmpty(SelectPayment):
        if holderName.get() == "" or holderName.get() == "Cardholder name *":
            messagebox.showwarning("Club Car", "Please enter Cardholder name first!")
        elif cardNumber.get() == "" or cardNumber.get() == "Card Number *":
            messagebox.showwarning("Club Car", "Please enter Card number first!")
        elif expMonthEntry.get() == "" or expMonthEntry.get() == "Expriation Month *":
            messagebox.showwarning("Club Car", "Please enter expiration month first!")
        elif expYearEntry.get() == "" or expYearEntry.get() == "Expriation Year *":
            messagebox.showwarning("Club Car", "Please enter expiration year first!")
        elif cvcEntry.get() == "" or cvcEntry.get() == "CVC *":
            messagebox.showwarning("Club Car", "Please enter CVC first!")
        else:
            if len(CardNumber.get()) < 16 or len(CardNumber.get()) > 16:
                messagebox.showwarning("Club Car", f"Card Number length not met or out of range [16:{len(CardNumber.get())}]")
            elif len(ExpMonth.get()) < 2 or len(ExpMonth.get()) > 2:
                messagebox.showwarning("Club Car", f"Month length not met or out of range [2:{len(ExpMonth.get())}]")
            elif len(ExpYear.get()) < 2 or len(ExpYear.get()) > 2:
                messagebox.showwarning("Club Car", f"Year length not met or out of range [2:{len(ExpYear.get())}]")
            elif int(ExpMonth.get()) < 1 or int(ExpMonth.get()) > 12:
                messagebox.showwarning("Club Car", f"Month out of range 01 - 12 [{ExpMonth.get()}]")
            elif (len(CVC.get()) < 3 or len(CVC.get()) > 3):
                messagebox.showwarning("Club Car", f"CVC length not met or out of range [3:{len(ExpMonth.get())}]")
            else:
                Session = SQLConnect.GetConnect()
                Cursor = Session.cursor()
                if SelectPayment == 1:
                    Account.Payment.VCardHoldername = Holdername.get()
                    Account.Payment.VCardNumber = CardNumber.get()
                    Account.Payment.VExpirationMonth = ExpMonth.get()
                    Account.Payment.VExpirationYear = ExpYear.get()
                    Account.Payment.VCVC = CVC.get()
                    Cursor.execute(f"UPDATE Account_Payment SET VCardHoldername='{Holdername.get()}', VCardNumber='{CardNumber.get()}', VExpirationMonth='{ExpMonth.get()}', VExpirationYear='{ExpYear.get()}', VCVC='{CVC.get()}' WHERE UID = '{Account.UID}'")
                elif SelectPayment == 2:
                    Account.Payment.MCardHoldername = Holdername.get()
                    Account.Payment.MCardNumber = CardNumber.get()
                    Account.Payment.MExpirationMonth = ExpMonth.get()
                    Account.Payment.MExpirationYear = ExpYear.get()
                    Account.Payment.MCVC = CVC.get()
                    Cursor.execute(f"UPDATE Account_Payment SET MCardHoldername='{Holdername.get()}', MCardNumber='{CardNumber.get()}', MExpirationMonth='{ExpMonth.get()}', MExpirationYear='{ExpYear.get()}', MCVC='{CVC.get()}' WHERE UID = '{Account.UID}'")
                Session.commit()
                Cursor.close()
                Session.close()
                Point = OnSaveCardInfo()
    else:
        Point = OnSaveCardInfo()

    Account.Point += Point
    Session = SQLConnect.GetConnect()
    Cursor = Session.cursor()
    Cursor.execute(f"UPDATE Account SET Point='{Account.Point}' WHERE UID = '{Account.UID}'")
    Session.commit()
    Cursor.close()
    Session.close()
    
    if Account.discountState == 1:
        Account.discountState = 0
        Session = SQLConnect.GetConnect()
        Cursor = Session.cursor()
        Cursor.execute(f"UPDATE Account SET DiscountState='0' WHERE UID = '{Account.UID}'")
        Session.commit()
        Cursor.close()
        Session.close()

def OnSaveCardInfo():
    Point = 0
    if checkState.get() == 0 and (checkBox.cget('state') == 'normal' or checkBox.cget('state') == 'active'):
        messagebox.showwarning("Club Car", "Please accept Terms & Conditions and Privacy Policy")
    else:
        if len(cart.Items.values()) < 1:
            messagebox.showwarning("Club Car", "Please select the car you wish to rent.")
        for Car in cart.Items.values():
            Point += 10
            UpdateStateCar(Car)
            CreateLog(Car)
        cart.Clear()
    return Point

def UpdateStateCar(Car):
    Cars[Car.Id].State = 1
    Session = SQLConnect.GetConnect()
    Cursor = Session.cursor()
    Cursor.execute(f"UPDATE Car SET State='1' WHERE ID = '{Car.Id}'")
    Session.commit()
    Cursor.close()
    Session.close()

def CreateLog(Car):
    TimeNow = date.datetime.now().strftime("%Y%m%d%H%M%S")
    RentDate = date.datetime.now().strftime("%d %b %Y (%H:%M)")
    Days = GetDayOfPeriod(cart.Periods.get(Car.Id))
    EndDate = (date.datetime.now() + timedelta(days=Days)).strftime("%d %b %Y (%H:%M)")
    Session = SQLConnect.GetConnect()
    Cursor = Session.cursor()
    Cursor.execute(f"INSERT INTO Rent_Log (OrderID, CarID, UID, Rent_Date, End_Date) VALUES ('CC{Car.Id:02d}{Account.UID:04d}{TimeNow}', '{Car.Id}', '{Account.UID}', '{RentDate}', '{EndDate}') RETURNING OrderID")
    OrderID = Cursor.fetchone()[0]
    Session.commit()
    Cursor.close()
    Session.close()
    if OrderID != "":
        Order = CarOrder()
        Order.ID = OrderID
        Order.CarID = Car.Id
        Order.UID = Account.UID
        Order.RentDate = RentDate
        Order.EndDate = EndDate
        changeFrame(SuccessFrame(OrderID))

def SuccessFrame(OrderID):
    scFrame = Frame(Root, bg="#2E2E2E")
    scFrame.rowconfigure((0, 1, 2), weight=1)
    scFrame.columnconfigure((0, 1, 2), weight=1)
    infoFrame = Frame(scFrame, bg="#2E2E2E")
    infoFrame.columnconfigure(0, weight=1)
    Label(infoFrame, text="Thank You For Your Purchase", font=("Helvetica 20 bold"), bg="#2E2E2E", fg="white").grid(row=0, column=0, pady=30)
    Label(infoFrame, image=IconDone, bg="#2E2E2E").grid(row=1, column=0)
    Label(infoFrame, text=f"Order #{OrderID} Confirmed", font=("Helvetica 20 bold"), bg="#2E2E2E", fg="white").grid(row=2, column=0, pady=30)
    Button(infoFrame, image=BackToMain, text="Back to Main", font=("Helvetica 12 bold"), bg="#2E2E2E", fg="black", border=0, borderwidth=0, activebackground="#2E2E2E", activeforeground="black", compound=CENTER, command=lambda:OnBackToMain(0)).grid(row=3, column=0)
    Button(infoFrame, image=RentAnAddition, text="Rent an additional car", font=("Helvetica 12 bold"), bg="#2E2E2E", fg="white", border=0, borderwidth=0, activebackground="#2E2E2E", activeforeground="white", compound=CENTER, command=lambda:OnBackToMain(1)).grid(row=4, column=0, pady=10)
    infoFrame.grid(row=1, column=1, sticky="news")
    scFrame.grid(row=0, columnspan=2, sticky="news")
    return scFrame

def OnBackToMain(Type):
    MenuFrame()
    if Type == 0:
        HomeFrame()
    elif Type == 1:
        Cars = GetCars("ALL")
        CarsMyRent(Cars)

def OrderFrame():
    global profileState
    profileState = False
    ButtonHome["image"] = IconHome1
    ButtonCar["image"] = IconCar1
    ButtonCart["image"] = IconCart1
    ButtonOrder["image"] = IconOrder2
    ButtonProfile["image"] = IconProfile1
    listOrder = Frame(Root, bg="#2F2F2F")
    listOrder.rowconfigure((1), weight=3)
    listOrder.columnconfigure((0), weight=1)
    rentalName, rentalDetail = GetRental()

    if rentalName == []:
        Label(listOrder,image=dontHaveOrder,bg="#2F2F2F").grid(row=0,rowspan=2,column=0)
    else :
        Head = Frame(listOrder,bg="#2F2F2F")
        Head.columnconfigure((0, 1), weight=1)
        Label(Head,bg="#2F2F2F",text="List Rental Cars",font=("Helvetica 20 bold"),fg="white").grid(row=1,column=0,sticky="w",padx=10)
        Label(Head,bg="#2F2F2F",text="The vehicle your rent on the clubcar marketplace",font=("Helvetica 14"),fg="white").grid(row=2,column=0,sticky="w",padx=10)
        Label(Head,bg="#2F2F2F",text= f"{len(rentalName)} Vehicle",font=("Helvetica 12"),fg="white",image=vehicle,compound=CENTER).grid(row=2,column=1,sticky="e",padx=10)
    
        Body = Canvas(listOrder, bg="#2F2F2F", highlightbackground="#2F2F2F", border=0, borderwidth=0)
        scrollFrame = Frame(Body, bg="#2F2F2F")
        Row, Column = 1, 0
        for Car in zip(rentalName, rentalDetail):
            GroupFrame = Frame(scrollFrame, bg="#2F2F2F")
            GroupFrame.rowconfigure((0), weight=1)
            GroupFrame.columnconfigure((0,1), weight=1)
            Label(GroupFrame,image=FCar,bg="#2F2F2F",).grid(row=0,column=0,columnspan=2,sticky="news")
            Label(GroupFrame,bg="#3B3B3B",image=ImgCarMidle[Car[1][1]]).grid(row=0,column=0)
            Dateframe = Frame(GroupFrame,bg="#2F2F2F")
            Dateframe.rowconfigure((0, 1, 2, 3, 4), weight=1)
            Dateframe.columnconfigure((0, 1), weight=1)
            Label(Dateframe,image=Ddate,bg="#3B3B3B",height=150,anchor=E).grid(row=0,rowspan=4,columnspan=2,sticky="e")
            Label(Dateframe,text=f"{Car[0]}",bg="#292929",font=("Helvetica 12"),fg="white").grid(row=0,column=0,columnspan=2,sticky="sw",padx=10)
            Label(Dateframe,text="Started :",bg="#292929",font=("Helvetica 9"),fg="#D8D8D8").grid(row=1,column=0,sticky="w",padx=10)
            Label(Dateframe,text="Ending :",bg="#292929",font=("Helvetica 9"),fg="#D8D8D8").grid(row=1,column=1,sticky="w",padx=10)
            Label(Dateframe,text=Car[1][3],bg="#292929",font=("Helvetica 8"),fg="#D8D8D8").grid(row=2,column=0,sticky="nw",padx=10)
            Label(Dateframe,text=Car[1][4],bg="#292929",font=("Helvetica 8"),fg="#D8D8D8").grid(row=2,column=1,sticky="nw",padx=10)           
            Label(Dateframe,text=Car[1][0],bg="#202020",font=("Helvetica 9 bold"),fg="#D1D1D1").grid(row=3,column=0,columnspan=2,sticky="nw",padx=10)
            Dateframe.grid(row=0,column=1)
            GroupFrame.grid(row=Row, column=Column, sticky="news",pady=10,padx=12)
            Column += 1
            if Column == 2:
                Column = 0
                Row += 2
        Head.grid(row=0,column=0,sticky="news", padx=20, pady=20)
        Body.create_window((0, 0), window=scrollFrame, anchor="n")
        Scroller = Scrollbar(listOrder, orient=VERTICAL, command=Body.yview)
        Scroller.grid(row=1,column=3, sticky='nes')
        Body.configure(yscrollcommand=Scroller.set)
        scrollFrame.update_idletasks()
        Body.config(scrollregion=Body.bbox("all"))
        Body.grid(row=1, column=0, sticky="news")
    listOrder.grid(row=0, column=1, sticky="news")
    return listOrder

def OnClickShipping(Type):
    global DeliveryType, pickUpCarFrame, labelFooter, labelShowCode, labelAsk
    DeliveryType = Type
    if Type == 0:
        homeDelivery["image"] = ShippingBorder1
        pickupInStore["image"] = ShippingBorder2
        shipFrame.grid(row=2, column=0, padx=50, sticky="ew")
        labelPlatter3["image"] = Platter3
        labelPlatter3.grid(row=2, columnspan=2, sticky="news", pady=10)
        labelIconAddress.grid(row=2, column=0, padx=50, sticky="w")
        addressFrame.grid(row=1, columnspan=2, sticky="news")
        if SelectPayment == 1 or SelectPayment == 2:
            labelPlatterCard.grid(row=0, columnspan=2, sticky="news", pady=10)
            labelIconCard.grid(row=0, column=0, padx=50, sticky="w")
            cardInfoFrame.grid(row=0, column=0, padx=50, sticky="ew")
        try:
            pickUpCarFrame.grid_forget()
            labelFooter.grid_forget()
            labelShowCode.grid_forget()
            labelAsk.grid_forget()
        except:
            pass
    elif Type == 1:
        cardInfoFrame.grid_forget()
        labelIconCard.grid_forget()
        labelPlatterCard.grid_forget()
        homeDelivery["image"] = ShippingBorder2
        pickupInStore["image"] = ShippingBorder1
        shipFrame.grid_forget()
        labelIconAddress.grid_forget()
        labelPlatter3["image"] = pickUpFrame
        labelPlatter3.grid(row=2, columnspan=2, sticky="news", pady=10)
        pickUpCarFrame = Frame(addressFrame, bg="#313131")
        pickUpCarFrame.columnconfigure((0, 1), weight=1)
        Label(pickUpCarFrame, text="Pick up Car", font=("Helvetica 10 bold"), fg="white", bg="#313131").grid(row=0, column=0, padx=10, sticky="w")
        Label(pickUpCarFrame, text="-" * 150, font=("Helvetica 8 bold"), fg="white", bg="#313131").grid(row=1, column=0, sticky="w")
        Label(pickUpCarFrame, text="•  Directly applied at the checkout, every rental.", font=("Helvetica 8"), fg="white", bg="#313131").grid(row=2, columnspan=2, padx=10, sticky="w")
        Label(pickUpCarFrame, text="•  Payment must be before the vehicle can be picked up.", font=("Helvetica 8"), fg="white", bg="#313131").grid(row=3, columnspan=2, padx=10, sticky="w")
        pickUpCarFrame.grid(row=2, column=0, padx=32, pady=15, sticky="news")
        labelFooter = Label(addressFrame, image=footerPickUpFrame, bg="#202020", border=0, borderwidth=0)
        labelFooter.grid(row=2, columnspan=2, sticky="s")
        labelShowCode = Label(addressFrame, text="Show your code to the team at Flagship Store", font=("Helvetica 7"), bg="#292929", fg="white", border=0, borderwidth=0)
        labelShowCode.grid(row=2, column=0, padx=40, pady=5, sticky="ws")
        labelAsk = Label(addressFrame, text="Ask a Specialist", font=("Helvetica 7 underline"), bg="#292929", fg="#4687FF", border=0, borderwidth=0, activebackground="#292929", activeforeground="#4687FF")
        labelAsk.grid(row=2, column=0, padx=40, pady=3, sticky="es")

def OnClickSelect(Type):
    global SelectPayment, BTCFrame
    SelectPayment = Type
    buttonPayment["text"] = f"Pay with {GetCardByType(SelectPayment)}"
    labelCardType["text"] = GetCardByType(SelectPayment)
    ResetSelect()
    selectedPayment.grid(row=1, columnspan=5, pady=20)
    buttonPayment.grid(row=4, columnspan=5, pady=10)
    labelGPay.grid_forget()
    labelPlatterCard.grid_forget()
    labelIconCard.grid_forget()
    cardInfoFrame.grid_forget()
    labelCardNumber2.grid_forget()
    labelCardExpiration.grid_forget()
    labelTxtExpiration.grid_forget()
    try:
        BTCFrame.grid_forget()
    except:
        pass
    if Type == 0:
        CPay["image"] = CPay2 
        selectedPayment["image"] = CashPayment
        buttonPayment["text"] = f"Cash on Delivery {Total.get()}"
        buttonPayment["image"] = ButtonCashPayment
    elif Type == 1:
        VPay["image"] = VPay2 
        selectedPayment["image"] = Visa
        buttonPayment["image"] = ImagePayment
        txtCardNumber = f"{Account.Payment.VCardNumber[0:4]} {Account.Payment.VCardNumber[4:8]} {Account.Payment.VCardNumber[8:12]} {Account.Payment.VCardNumber[12:16]}" if Account.Payment.VCardNumber != "" else "**** **** **** ****"
        labelCardNumber["text"] = f"({txtCardNumber})"
        labelIconCard["image"] = IconVISA
        if DeliveryType == 0:
            labelPlatterCard.grid(row=0, columnspan=2, sticky="news", pady=10)
            labelIconCard.grid(row=0, column=0, padx=50, sticky="w")
            cardInfoFrame.grid(row=0, column=0, padx=50, sticky="ew")
        labelCardNumber2["bg"] = "#8241BE"
        txtCardNumber2 = f"{Account.Payment.VCardNumber[0:4]} {Account.Payment.VCardNumber[4:8]} {Account.Payment.VCardNumber[8:12]} {Account.Payment.VCardNumber[12:16]}" if Account.Payment.VCardNumber != "" else "****  ****  ****  ****"
        labelCardNumber2["text"] = f"{txtCardNumber2}"
        labelCardNumber2.grid(row=1, columnspan=3, sticky="ws", padx=35, pady=90)
        labelTxtExpiration["bg"] = "#8241BE"
        txtCardHoldername = Account.Payment.VCardHoldername if Account.Payment.VCardHoldername != "" else "****** ******"
        labelTxtExpiration["text"] = f"{txtCardHoldername}"
        labelTxtExpiration["font"] = "Helvetica 8 bold"
        labelTxtExpiration.grid(row=1, columnspan=3, sticky="ws", padx=35, pady=35)
        labelCardExpiration["bg"] = "#8241BE"
        txtExpriation = f"{Account.Payment.VExpirationMonth}/{Account.Payment.VExpirationYear}" if Account.Payment.VExpirationMonth != "" and Account.Payment.VExpirationYear != "" else "00/00"
        labelCardExpiration["text"] = f"{txtExpriation}"
        labelCardExpiration.grid(row=1, column=1, columnspan=4, sticky="ws", padx=107, pady=35)
    elif Type == 2:
        MPay["image"] = MPay2
        selectedPayment["image"] = MasterCard
        buttonPayment["image"] = ImagePayment
        txtCardNumber = f"{Account.Payment.MCardNumber[0:4]} {Account.Payment.MCardNumber[4:8]} {Account.Payment.MCardNumber[8:12]} {Account.Payment.MCardNumber[12:16]}" if Account.Payment.MCardNumber != "" else "•••• •••• •••• ••••"
        labelCardNumber["text"] = f"({txtCardNumber})"
        labelIconCard["image"] = IconMasterCard
        labelCardNumber2["bg"] = "#484206"
        txtCardNumber2 = f"{Account.Payment.MCardNumber[0:4]}  {Account.Payment.MCardNumber[4:8]}  {Account.Payment.MCardNumber[8:12]}  {Account.Payment.MCardNumber[12:16]}" if Account.Payment.MCardNumber != "" else "••••  ••••  ••••  ••••"
        labelCardNumber2["text"] = f"{txtCardNumber2}"
        labelCardNumber2.grid(row=1, columnspan=3, sticky="ws", padx=40, pady=75)
        labelTxtExpiration["bg"] = "#484206"
        labelTxtExpiration["text"] = "VALID\nTHRU"
        labelTxtExpiration["font"] = "Helvetica 6 bold"
        labelTxtExpiration.grid(row=1, columnspan=3, sticky="ws", padx=40, pady=50)
        labelCardExpiration["bg"] = "#484206"
        txtExpriation = f"{Account.Payment.MExpirationMonth}/{Account.Payment.MExpirationYear}" if Account.Payment.MExpirationMonth != "" and Account.Payment.MExpirationYear != "" else "00/00"
        labelCardExpiration["text"] = f"{txtExpriation}"
        labelCardExpiration.grid(row=1, columnspan=3, sticky="ws", padx=80, pady=50)
        if DeliveryType == 0:
            labelPlatterCard.grid(row=0, columnspan=2, sticky="news", pady=10)
            labelIconCard.grid(row=0, column=0, padx=50, sticky="w")
            cardInfoFrame.grid(row=0, column=0, padx=50, sticky="ew")
    elif Type == 3:
        GPay["image"] = GPay2
        selectedPayment["image"] = GooglePay
        buttonPayment["image"] = ImagePayment
        labelGPay.grid(row=2, columnspan=5, sticky="n")
    elif Type == 4:
        BPay["image"] = BPay2
        buttonPayment["image"] = ImagePayment
        selectedPayment.grid_forget()
        buttonPayment.grid_forget()
        BTCFrame = Frame(OptionFrame, bg="#2F2F2F")
        BTCFrame.columnconfigure(0, weight=1)
        Label(BTCFrame, image=BTCPayFrame, bg="#2F2F2F").grid(row=0, column=0, sticky="news")
        infoFrame = Frame(BTCFrame, bg="#262625")
        infoFrame.columnconfigure((0, 1), weight=1)
        Label(infoFrame, text="BTC", font=("Helvetica 12 bold"), image=IconBTC, compound=LEFT, bg="#262625", fg="white", padx=10).grid(row=0, column=0, sticky="nw")
        Label(infoFrame, image=IconBTC2, bg="#262625").grid(row=0, column=1, sticky="ne")
        Label(infoFrame, image=Platter_BTC, bg="#262625").grid(row=1, columnspan=2, pady=5, sticky="ew")
        addressReferral = Frame(infoFrame, bg="#313131")
        addressReferral.columnconfigure((0, 1), weight=1)
        Label(addressReferral, text="ClubCar Address Referral", font=("Helvetica 10 bold"), bg="#313131", fg="#939398").grid(row=0, column=0, sticky="w")
        Label(addressReferral, text="0x9876543210135", font=("Helvetica 10 bold"), bg="#313131", fg="white").grid(row=1, column=0, sticky="w")
        Button(addressReferral, image=IconCopy, bg="#313131", border=0, borderwidth=0, activebackground="#313131", command=lambda:OnClickCopy("0x9876543210135")).grid(row=0, rowspan=2, column=1, sticky="e")
        addressReferral.grid(row=1, columnspan=2, padx=10, pady=10, sticky="ew")
        Label(infoFrame, image=Platter_BTC, bg="#262625").grid(row=2, columnspan=2, pady=5, sticky="ew")
        transactionFrame = Frame(infoFrame, bg="#313131")
        transactionFrame.columnconfigure((0, 1), weight=1)
        Label(transactionFrame, text="Transaction Id", font=("Helvetica 10 bold"), bg="#313131", fg="#939398").grid(row=0, column=0, sticky="w")
        Label(transactionFrame, text=f"{Account.Payment.TransactionId}", font=("Helvetica 10 bold"), bg="#313131", fg="white").grid(row=1, column=0, sticky="w")
        transactionFrame.grid(row=2, columnspan=2, padx=10, pady=10, sticky="ew")
        infoFrame.grid(row=0, columnspan=2, sticky="news", padx=20, pady=20)
        Label(BTCFrame, image=FooterPlatter_BTC, bg="#313131", border=0, borderwidth=0).grid(row=0, columnspan=2, pady=20, sticky="s")
        totalFrame = Frame(BTCFrame, bg="#202020")
        totalFrame.columnconfigure((0, 1), weight=1)
        Label(totalFrame, text="Total payable BTC amount", font=("Helvetica 8 bold"), bg="#202020", fg="#939398").grid(row=0, column=0, padx=20, sticky="w")
        Label(totalFrame, text="0.005397", font=("Helvetica 16 bold"), bg="#202020", fg="white").grid(row=1, column=0, padx=20, sticky="w")
        Button(totalFrame, image=IconCopy, bg="#202020", border=0, borderwidth=0, activebackground="#202020", command=lambda:OnClickCopy("0.005397")).grid(row=0, rowspan=2, column=1, padx=25, sticky="e")
        Label(totalFrame, text=" " * 128, font=("Helvetica 8 underline"), bg="#202020", fg="#545458", border=0, borderwidth=0).grid(row=2, columnspan=2, sticky="ew")
        Label(totalFrame, image=IconExchange, bg="#202020", border=0, borderwidth=0).grid(row=3, columnspan=2)
        Label(totalFrame, text="Pay with BTC on Cryptocurrency Exchanges ", font=("Helvetica 8 bold"), bg="#202020", fg="#939398").grid(row=4, columnspan=2)
        totalFrame.grid(row=0, columnspan=2, sticky="ews", padx=3, pady=10)
        BTCFrame.grid(row=1, columnspan=5, sticky="news", pady=20)
    CheckPaymentInfo()
    labelSelected.grid_forget()
    labelSelected.grid(row=0, column=Type, padx=10, pady=16, sticky="es")

def CheckPaymentInfo():
    if not Account.Payment.IsEmpty(SelectPayment):
        entryFrame.grid_forget()
        if SelectPayment == 1 or SelectPayment == 2 or SelectPayment == 3 or SelectPayment == 4:
            checkBox.grid_forget()
            checkBox.configure(state='disable')
            labelPrivacy.grid_forget()
        else:
            checkBox.grid(row=3, column=0, padx=15, sticky="w")
            checkBox.configure(state='active')
            labelPrivacy.grid(row=3, column=0, columnspan=5, padx=45, sticky="e")
    else:
        checkBox.grid(row=3, column=0, padx=15, sticky="w")
        checkBox.configure(state='active')
        labelPrivacy.grid(row=3, column=0, columnspan=5, padx=45, sticky="e")
        entryFrame.grid(row=2, columnspan=5, sticky="news")

def ResetSelect():
    CPay["image"] = CPay1
    VPay["image"] = VPay1
    MPay["image"] = MPay1
    GPay["image"] = GPay1
    BPay["image"] = BPay1

def CalculatePayment():
    subTotal, shipping, discount = 0.0, 0.0, 0.0
    for Car in cart.Items.values():
        subTotal += Car.Price * GetDayOfPeriod(cart.Periods.get(Car.Id))
    SubTotal.set(f"฿{subTotal:,.2f}")
    if Account.discountState == 1:
        discount = subTotal*0.10
        Discount.set(f"{discount:,.2f}")
    Total.set(f"฿{(subTotal + shipping - discount):,.2f}")

def GetDayOfPeriod(Period):
    if Period == "1 Day":
        return 1.0
    elif Period == "3 Day":
        return 3.0
    elif Period == "5 Day":
        return 5.0
    elif Period == "7 Day":
        return 7.0
    elif Period == "1 Month":
        return 30.0
    elif Period == "3 Month":
        return 90.0
    return 1.0

def GetCardByType(Type):
    if Type == 0:
        return "Cash"
    elif Type == 1:
        return "VISA"
    elif Type == 2:
        return "Mastercard"
    elif Type == 3:
        return "Google Pay"
    elif Type == 4:
        return "Apple Pay"
    return "None"

def OnRemoveItem(Car):
    cart.Remove(Car)
    PaymentFrame()

def LoadCarsInfo():
    Session = SQLConnect.GetConnect()
    Cursor = Session.cursor()
    Cursor.execute("SELECT * FROM Car ORDER BY Tag DESC")
    Lists = Cursor.fetchall()
    if Lists:
        for Data in Lists:
            Car = CarInfo()
            Car.Id = Data[0]
            Car.Name = Data[1]
            Car.Type = Data[2]
            Car.Tag = Data[3]
            Car.Image = Data[4]
            Car.DetailImage0 = Data[5]
            Car.DetailImage1 = Data[6]
            Car.DetailImage2 = Data[7]
            Car.DetailImage3 = Data[8]
            Car.DetailImage4 = Data[9]
            Car.ModelImage = Data[10]
            Car.Description = Data[11]
            Car.Price = Data[12]
            Car.State = Data[13]
            Car.Horsepower = Data[14]
            Car.Acceleration = Data[15]
            Car.TopSpeed = Data[16]
            Cars.update({Car.Id : Car})
    Lists.clear()
    Cursor.close()
    Session.close()

def LoadImagesCar():
    for Car in Cars.values():
        try:
            ImgCars.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.Image}").subsample(2, 2)})
        except:
            ImgCars.update({Car.Id : PhotoImage(file=f"ImageCar/CCar0.png").subsample(2, 2)})
        try:
            ImgModels.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.ModelImage}")})
        except:
            ImgModels.update({Car.Id : PhotoImage(file=f"Image/ImageNotFound.png").subsample(5, 5)})
        try:
            ImgCarMini0.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.DetailImage0}").subsample(10, 10)})
            ImgDetailCar0.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.DetailImage0}").subsample(2, 2)})
            ImgCarMidle.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.DetailImage0}").subsample(4, 4)})
        except:
            ImgCarMini0.update({Car.Id : PhotoImage(file=f"Image/ImageNotFound.png").subsample(10, 10)})
            ImgDetailCar0.update({Car.Id : PhotoImage(file=f"Image/ImageNotFound.png").subsample(2, 2)})
        try:
            ImgCarMini1.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.DetailImage1}").subsample(10, 10)})
            ImgDetailCar1.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.DetailImage1}").subsample(2, 2)})
        except:
            ImgCarMini1.update({Car.Id : PhotoImage(file=f"Image/ImageNotFound.png").subsample(10, 10)})
            ImgDetailCar1.update({Car.Id : PhotoImage(file=f"Image/ImageNotFound.png").subsample(2, 2)})
        try:
            ImgCarMini2.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.DetailImage2}").subsample(10, 10)})
            ImgDetailCar2.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.DetailImage2}").subsample(2, 2)})
        except:
            ImgCarMini2.update({Car.Id : PhotoImage(file=f"Image/ImageNotFound.png").subsample(10, 10)})
            ImgDetailCar2.update({Car.Id : PhotoImage(file=f"Image/ImageNotFound.png").subsample(2, 2)})
        try:
            ImgCarMini3.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.DetailImage3}").subsample(10, 10)})
            ImgDetailCar3.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.DetailImage3}").subsample(2, 2)})
        except:
            ImgCarMini3.update({Car.Id : PhotoImage(file=f"Image/ImageNotFound.png").subsample(10, 10)})
            ImgDetailCar3.update({Car.Id : PhotoImage(file=f"Image/ImageNotFound.png").subsample(2, 2)})
        try:
            ImgCarMini4.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.DetailImage4}").subsample(10, 10)})
            ImgDetailCar4.update({Car.Id : PhotoImage(file=f"ImageCar/{Car.DetailImage4}").subsample(2, 2)})
        except:
            ImgCarMini4.update({Car.Id : PhotoImage(file=f"Image/ImageNotFound.png").subsample(10, 10)})
            ImgDetailCar4.update({Car.Id : PhotoImage(file=f"Image/ImageNotFound.png").subsample(2, 2)})

def GetCars(Type):
    Result = []
    for Car in Cars.values():
        if Car != None and (Car.Type == Type or Type == "ALL"):
            Result.append(Car)
    return Result

def GetRental():
    Result = []
    CarName = []
    Session = SQLConnect.GetConnect()
    Cursor = Session.cursor()
    Cursor.execute("SELECT * FROM Rent_Log")
    List = Cursor.fetchall()
    for i in List:
        if i[2] == Account.UID:
            for Car in Cars.values():
                if Car.Id == i[1]:
                    CarName.append(i)
                    Result.append(Car.Name)
                    break
    Cursor.close()
    Session.close()
    return (Result, CarName)


def GetCarsBySearch(Name):
    Result = []
    Session = SQLConnect.GetConnect()
    Cursor = Session.cursor()
    Cursor.execute(f"SELECT * FROM Car WHERE Name LIKE '%{Name}%' ORDER BY Id ASC")
    Lists = Cursor.fetchall()
    if Lists:
        for Data in Lists:
            Car = CarInfo()
            Car.Id = Data[0]
            Car.Name = Data[1]
            Car.Type = Data[2]
            Car.Tag = Data[3]
            Car.Image = Data[4]
            Car.DetailImage0 = Data[5]
            Car.DetailImage1 = Data[6]
            Car.DetailImage2 = Data[7]
            Car.DetailImage3 = Data[8]
            Car.DetailImage4 = Data[9]
            Car.ModelImage = Data[10]
            Car.Description = Data[11]
            Car.Price = Data[12]
            Car.State = Data[13]
            Car.Horsepower = Data[14]
            Car.Acceleration = Data[15]
            Car.TopSpeed = Data[16]
            Result.append(Car)
    Lists.clear()
    Cursor.close()
    Session.close()
    return Result

def tkEntry(master, textvar=None, placeholder='', font=None, bg="#2F2F2F", fg="white"):
        def on_focus_in(entry):
            if entry.cget('state') == 'disabled':
                entry.configure(state='normal')
                entry.delete(0, 'end')

        def on_focus_out(entry, placeholder):
                if entry.get() == "":
                    entry.insert(0, placeholder)
                    entry.configure(state='disabled')

        entry = Entry(master, textvariable=textvar, border=0, borderwidth=0, bg=bg, fg=fg, insertbackground=fg, disabledbackground=bg, disabledforeground=fg)
        entry.delete(0, 'end')
        entry.insert(0, placeholder)
        entry.configure(state='disabled')
        entry.bind('<Button-1>', lambda x: on_focus_in(entry))
        entry.bind('<FocusOut>', lambda x: on_focus_out(entry, placeholder))

        if font != None:
            entry.config(font=font)

        return entry

def GetAccountPayment(UID):
    if UID == 0:
        return None
    Session = SQLConnect.GetConnect()
    Cursor = Session.cursor()
    Cursor.execute(f"SELECT * FROM Account_Payment WHERE UID = '{UID}'")
    Data = Cursor.fetchone()
    if Data:
        payment = Payment()
        payment.MCardHoldername = Data[1]
        payment.MCardNumber = Data[2]
        payment.MExpirationMonth = Data[3]
        payment.MExpirationYear = Data[4]
        payment.MCVC = Data[5]
        payment.VCardHoldername = Data[6]
        payment.VCardNumber = Data[7]
        payment.VExpirationMonth = Data[8]
        payment.VExpirationYear = Data[9]
        payment.VCVC = Data[10]
        payment.TransactionId = Data[11]
        Cursor.close()
        Session.close()
        return payment
    return None

def GetAccountAddress(UID):
    if UID == 0:
        return None
    Session = SQLConnect.GetConnect()
    Cursor = Session.cursor()
    Cursor.execute(f"SELECT * FROM Account_Address WHERE UID = '{UID}'")
    Data = Cursor.fetchone()
    if Data:
        address = Address()
        address.Firstname = Data[1]
        address.Lastname = Data[2]
        address.StreetAddress = Data[3]
        address.State = Data[4]
        address.City = Data[5]
        address.ZipCode = Data[6]
        Cursor.close()
        Session.close()
        return address
    return None

def tsGenerator(size=13, chars="ABCDEFabcdef0123456789"):
    return ''.join(random.choice(chars) for _ in range(size))
    
def OnClickCopy(txt):
    cmd='echo ' + txt.strip() + '|clip'
    messagebox.showinfo("Club Car", f"Copied '{txt}' to clipboard.")
    return check_call(cmd, shell=True)

Root = MainWindow()
ImgEntry1 = PhotoImage(file="Image/ImgEntry1.png").subsample(2, 2)
ImgEntry2 = PhotoImage(file="Image/ImgEntry2.png").subsample(2, 2)
EntryLogin = PhotoImage(file="Image/EntryLogin.png").subsample(2, 2)
IconCart1 = PhotoImage(file="Image/Cart_1.png").subsample(3, 3)
IconCart2 = PhotoImage(file="Image/Cart_2.png").subsample(3, 3)
IconHome1 = PhotoImage(file="Image/Home_1.png").subsample(3, 3)
IconHome2 = PhotoImage(file="Image/Home_2.png").subsample(3, 3)
IconCar1 = PhotoImage(file="Image/Car_1.png").subsample(3, 3)
IconCar2 = PhotoImage(file="Image/Car_2.png").subsample(3, 3)
IconOrder1 = PhotoImage(file="Image/Order_2.png").subsample(3, 3)
IconOrder2 = PhotoImage(file="Image/Order_1.png").subsample(3, 3)
IconProfile1 = PhotoImage(file="Image/Profile_1.png").subsample(5, 5)
IconProfile2 = PhotoImage(file="Image/Profile_2.png").subsample(5, 5)
ImageNotFound = PhotoImage(file="Image/ImageNotFound.png")
homepage = PhotoImage(file="Image/homepage.png")
BHSearchBox = PhotoImage(file="Image/HSearchBox.png").subsample(2, 2)
Rent = PhotoImage(file="Image/Rent.png").subsample(3, 3)
Close = PhotoImage(file="Image/Close.png").subsample(3, 3)
Search = PhotoImage(file="Image/Search.png").subsample(2, 2)
Rented = PhotoImage(file="Image/Rented.png").subsample(4, 4)
TagNew = PhotoImage(file="Image/TagNew.png").subsample(2, 2)
DescriptionFrame = PhotoImage(file="Image/DescriptionFrame.png")
ButtonPeriod1 = PhotoImage(file="Image/ButtonPeriod_1.png")
ButtonPeriod2 = PhotoImage(file="Image/ButtonPeriod_2.png")
ButtonContinue = PhotoImage(file="Image/ButtonContinue.png")
Separator = PhotoImage(file="Image/Separator.png").subsample(2, 2)
btc = PhotoImage(file="Image/btc.png").subsample(6, 6)
sh = PhotoImage(file="Image/sh.png").subsample(3, 3)
BPay1 = PhotoImage(file="Payment/BPay_1.png").subsample(2, 2)
BPay2 = PhotoImage(file="Payment/BPay_1.png")
GPay1 = PhotoImage(file="Payment/GPay_1.png").subsample(2, 2)
GPay2 = PhotoImage(file="Payment/GPay_1.png")
MPay1 = PhotoImage(file="Payment/MPay_1.png").subsample(2, 2)
MPay2 = PhotoImage(file="Payment/MPay_1.png")
CPay1 = PhotoImage(file="Payment/CPay_1.png").subsample(2, 2)
CPay2 = PhotoImage(file="Payment/CPay_1.png")
VPay1 = PhotoImage(file="Payment/VPay_1.png").subsample(2, 2)
VPay2 = PhotoImage(file="Payment/VPay_1.png")
MasterCard = PhotoImage(file="Payment/MasterCard.png").subsample(2, 2)
Visa = PhotoImage(file="Payment/VISA.png").subsample(2, 2)
GooglePay = PhotoImage(file="Payment/GooglePay.png").subsample(2, 2)
IsumFrame = PhotoImage(file="Image/sumFrame.png")
Line = PhotoImage(file="Image/Line.png")
Platter1 = PhotoImage(file="Image/Platter1.png").subsample(2, 2)
Platter2 = PhotoImage(file="Image/Platter2.png").subsample(2, 2)
Platter3 = PhotoImage(file="Image/Platter3.png").subsample(2, 2)
Platter_BTC = PhotoImage(file="Image/Platter_BTC.png").subsample(2, 2)
ShippingBorder1 = PhotoImage(file="Image/ShippingBorder1.png").subsample(3, 3)
ShippingBorder2 = PhotoImage(file="Image/ShippingBorder2.png").subsample(3, 3)
IconContact = PhotoImage(file="Image/IconContact.png").subsample(3, 3)
IconAddress = PhotoImage(file="Image/IconAddress.png").subsample(3, 3)
IconSelected = PhotoImage(file="Image/IconSelected.png").subsample(3, 3)
IconRemove = PhotoImage(file="Image/IconRemove.png").subsample(3, 3)
IconEdit = PhotoImage(file="Image/IconEdit.png").subsample(2, 2)
IconBack = PhotoImage(file="Image/IconBack.png").subsample(2, 2)
IconCopy = PhotoImage(file="Image/IconCopy.png").subsample(2, 2)
IconExchange = PhotoImage(file="Image/IconExchange.png").subsample(2, 2)
Entry1 = PhotoImage(file="Image/Entry1.png")
Entry2 = PhotoImage(file="Image/Entry2.png")
ImagePayment = PhotoImage(file="Image/ImagePayment.png").subsample(3, 3)
IconDone = PhotoImage(file="Image/IconDone.png").subsample(2, 2)
BackToMain = PhotoImage(file="Image/BackToMain.png")
RentAnAddition = PhotoImage(file="Image/RentAnAddition.png")
regButtonImg = PhotoImage(file='image/regButtonImg.png').subsample(2, 2)
L_image = PhotoImage(file= 'image/Login.png').subsample(2, 2)
CashPayment = PhotoImage(file= 'image/CashPayment.png').subsample(2, 2)
ButtonCashPayment = PhotoImage(file= 'image/ButtonCashPayment.png').subsample(3, 3)
EditFrame = PhotoImage(file= 'image/EditFrame.png').subsample(2, 2)
EntryFirstname = PhotoImage(file= 'image/EntryFirstname.png')
EntryLastname = PhotoImage(file= 'image/EntryLastname.png')
EntryEmail = PhotoImage(file= 'image/EntryEmail.png')
EntryStreetAddress = PhotoImage(file= 'image/EntryStreetAddress.png')
EntryState = PhotoImage(file= 'image/EntryState.png')
EntryCity = PhotoImage(file= 'image/EntryCity.png')
EntryZipCode = PhotoImage(file= 'image/EntryZipCode.png')
EntryPhone = PhotoImage(file= 'image/EntryPhone.png')
ButtonSave = PhotoImage(file="Image/ButtonSave.png")
pickUpFrame = PhotoImage(file="Image/pickUpFrame.png").subsample(2, 2)
footerPickUpFrame = PhotoImage(file="Image/footerPickUpFrame.png").subsample(2, 2)
BTCPayFrame = PhotoImage(file="Image/BTCPayFrame.png").subsample(2, 2)
FooterPlatter_BTC = PhotoImage(file="Image/FooterPlatter_BTC.png").subsample(2, 2)
IconBTC = PhotoImage(file="Image/IconBTC.png").subsample(2, 2)
IconBTC2 = PhotoImage(file="Image/IconBTC2.png").subsample(2, 2)
point = PhotoImage(file= 'image/point.png').subsample(1,1)
discount = PhotoImage(file= 'image/discount.png').subsample(1,1)
discountG = PhotoImage(file= 'image/discountG.png').subsample(1,1)
member = PhotoImage(file= 'image/member.png').subsample(1,1)
memberp = PhotoImage(file= 'image/memberp.png').subsample(1,1)
profiletest = PhotoImage(file= 'image/profiletest.png').subsample(1,1)
FCar = PhotoImage(file= 'image/FCar.png').subsample(1,1)
Ddate = PhotoImage(file= 'image/Date.png').subsample(1,1)
vehicle = PhotoImage(file= 'image/vehicle.png').subsample(1,1)
dontHaveOrder = PhotoImage(file= 'Image/dontHaveOrder.png').subsample(1,1)
Dprofile = PhotoImage(file= 'image/Dprofile.png').subsample(1,1)
IconMasterCard = PhotoImage(file= 'Payment/IconMasterCard.png').subsample(3, 3)
IconVISA = PhotoImage(file= 'Payment/IconVISA.png').subsample(3, 3)
Logo = PhotoImage(file= "Image/Logo.png").subsample(2, 2)
LoginBG = PhotoImage(file= "Image/LoginBG.png")

Cars = {}
LoadCarsInfo()
ImgCars = {}
ImgModels = {}
ImgCarMini0 = {}
ImgCarMini1 = {}
ImgCarMini2 = {}
ImgCarMini3 = {}
ImgCarMini4 = {}
ImgDetailCar0 = {}
ImgDetailCar1 = {}
ImgDetailCar2 = {}
ImgDetailCar3 = {}
ImgDetailCar4 = {}
ImgCarMidle = {}
LoadImagesCar()
ListButton = {}
SearchName = StringVar()
SubTotal = StringVar()
SubTotal.set("฿0.00")
Discount = StringVar()
Discount.set("฿0.00")
Shipping = StringVar()
Shipping.set("฿0.00")
Total = StringVar()
Total.set("฿0.00")
SelectPeriod = "NONE"
SelectPayment = 2
DeliveryType = 0
valuesState = ['Andorra', 'Albania', 'Austria', 'Belgium', 'Bulgaria', 'Belarus', 'Czech Republic', 'Germany', 
'Denmark', 'Estonia', 'Finland', 'France', 'Greece', 'Hungary', 'Republic of Ireland', 'Iceland', 'Italy', 
'Liechtenstein', 'Lithuania', 'Luxembourg', 'Latvia', 'Macedonia', 'Malta', 'Kingdom of the Netherlands', 
'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Sweden', 'Slovenia', 'Slovakia', 'San Marino', 
'Ukraine', 'Vatican City', 'Bosnia and Herzegovina', 'Croatia', 'Moldova', 'Monaco', 'Montenegro', 
'Serbia', 'Spain', 'Switzerland', 'United Kingdom', 'Afghanistan', 'Armenia', 'Azerbaijan', 'Bangladesh', 
'Bahrain', 'Brunei Darussalam', 'Bhutan', "People's Republic of China", 'Cyprus', 'Georgia', 'Indonesia', 
'Israel', 'India', 'Iraq', 'Iran', 'Jordan', 'Japan', 'Kyrgyzstan', 'North Korea', 'South Korea', 'Kuwait', 
'Lebanon', 'Myanmar', 'Mongolia', 'Maldives', 'Malaysia', 'Nepal', 'Oman', 'Philippines', 'Pakistan', 'Qatar', 
'Saudi Arabia', 'Singapore', 'Syria', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Turkey', 'Uzbekistan', 'Vietnam', 
'Yemen', 'Cambodia', 'East Timor', 'Kazakhstan', 'Laos', 'Sri Lanka', 'United Arab Emirates', 'Antigua and Barbuda', 
'Barbados', 'Bahamas', 'Belize', 'Canada', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'Guatemala', 'Haiti', 
'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Trinidad and Tobago', 'United States', 'El Salvador', 'Grenada', 
'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Angola', 'Burkina Faso', 'Burundi', 'Benin', 
'Botswana', 'Democratic Republic of the Congo', 'Republic of the Congo', 'Ivory Coast', 'Cameroon', 'Cape Verde', 'Djibouti', 
'Egypt', 'Eritrea', 'Ethiopia', 'Gabon', 'Ghana', 'The Gambia', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Liberia', 'Lesotho', 
'Libya', 'Madagascar', 'Mali', 'Mauritania', 'Mauritius', 'Malawi', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 
'Seychelles', 'Sudan', 'Sierra Leone', 'Senegal', 'Somalia', 'Sao Tome and Principe', 'Togo', 'Tunisia', 'Tanzania', 
'Uganda', 'Zambia', 'Zimbabwe', 'Algeria', 'Central African Republic', 'Chad', 'Comoros', 'Equatorial Guinea', 
'Morocco', 'South Africa', 'Swaziland', 'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 
'Peru', 'Paraguay', 'Suriname', 'Uruguay', 'Venezuela', 'Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Nauru', 
'New Zealand', 'Papua New Guinea', 'Palau', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu', 'Federated States of Micronesia', 'Samoa']
valuesState.sort()
cart = Cart()
Account = Account()
Holdername = StringVar()
CardNumber = StringVar()
ExpMonth = StringVar()
ExpYear = StringVar()
CVC = StringVar()
e_Firstname = StringVar()
e_Lastname = StringVar()
e_Email = StringVar()
e_StreetAddress = StringVar()
selectState = StringVar()
e_City = StringVar()
e_ZipCode = StringVar()
e_Phone = StringVar()
checkState = IntVar()
mainFrame = loginPage()
mainFrame.grid(row=0, columnspan=2, sticky='news')
Root.mainloop()