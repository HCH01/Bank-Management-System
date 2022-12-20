from tkinter import *
from tkinter import font
import mysql.connector as a
bank = a.connect(host='localhost',user='root',passwd='1234',database='Bank')
mycr = bank.cursor()
p = Tk()
p.title(" Bank Management System ")
p.geometry("730x600")
can = Canvas(p ,width="700" ,height="600")
f = PhotoImage(file="C:\\Users\\Himanshu-PC\\Desktop\\Py\\BG1.png")
b = Label(can, image=f).place(width="700",height="600")
rkg = PhotoImage(file="C:\\Users\\Himanshu-PC\\Desktop\\Py\\RKGIT_logo.png")
Label(p, image=rkg ).place(x=250,y=10)
can.pack()
bnk = PhotoImage(file="C:\\Users\\Himanshu-PC\\Desktop\\Py\\BG3.png")
Label(p, image=bnk).place(x=0,y=500)

def btn():
    b1 = Button(p, text="New Account", command= newAcc, width="25", borderwidth="5").place(x=267,y=250)
    b2 = Button(p, text="Deposite Money", command= deposite, width="25",borderwidth="5" ).place(x=267,y=290)
    b3 = Button(p, text="Withdraw Amount", command= withdraw, width="25",borderwidth="5"  ).place(x=267,y=330)
    b4 = Button(p, text="Balance Enquiry", command= enquiry, width="25",borderwidth="5" ).place(x=267,y=370)
    b5 = Button(p, text="Display Customer Details", command= details, width="25",borderwidth="5" ).place(x=267,y=410)
    b6 = Button(p, text="Close Account", command= close, width="25",borderwidth="5" ).place(x=267,y=450)

def newAcc():
    t=Toplevel()
    t.title("Make new acount")
    t.geometry("750x600")
    Label(t ,text="Name ", font="10").place(x=100,y=100)
    Label(t ,text="Account Number", font="10").place(x=100,y=140)
    Label(t ,text="Date of Birth", font="10").place(x=100,y=180)
    Label(t ,text="Address ", font="10").place(x=100,y=220)
    Label(t ,text="Phone Number   ", font="10").place(x=100,y=260)
    Label(t ,text="Open Balance Amount", font="10").place(x=100,y=300)
    l1 =Entry(t ,width=40, borderwidth=6 , font="8")
    l1.place(x=300,y=100)
    l2 =Entry(t ,width=40, borderwidth=6 , font="8")
    l2.place(x=300,y=140)
    l3 =Entry(t ,width=40, borderwidth=6 , font="8")
    l3.place(x=300,y=180)
    l4 =Entry(t ,width=40, borderwidth=6 , font="8")
    l4.place(x=300,y=220)
    l5 =Entry(t ,width=40, borderwidth=6 , font="8")
    l5.place(x=300,y=260)
    l6 =Entry(t ,width=40, borderwidth=6 , font="8")
    l6.place(x=300,y=300)

    list_l = [l1 ,l2 ,l3 ,l4 ,l5 ,l6]

    def summit():
        data = (l1.get(), l2.get(), l3.get(), l4.get(), l5.get(), l6.get())
        data1 = (l1.get(), l2.get(), l6.get())
        sql = "INSERT INTO account VALUES(%s,%s,%s,%s,%s,%s)"
        sql1 = "INSERT INTO amount VALUES(%s,%s,%s)"
        mycr.execute(sql, data)
        mycr.execute(sql1, data1)
       
        bank.commit()

        l1.delete(0, END)
        l2.delete(0, END)
        l3.delete(0, END)
        l4.delete(0, END)
        l5.delete(0, END)
        l6.delete(0, END)
        
        Label(t ,text="Your Account has been created !").place(x=300,y=460)
    

    def go_to_next_entry(event, list , this_index):
        next_index = (this_index + 1)
        list[next_index].focus_set()

    entries = [a for a in t.winfo_children() if isinstance(a, Entry)]
    for idx, entry in enumerate(entries):
        entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

    Button(t ,text="Submit", command=summit, width="10",borderwidth="5" ).place(x=450,y=350)
    
    t.mainloop()

def deposite():
    d=Toplevel()    
    d.title("Deposite your amount")
    d.geometry("750x600")
    Label(d, text="Enter your account number ", font="10").place(x=100,y=150)
    Label(d, text="Enter amount to deposite ", font="10").place(x=100,y=230)
    q1 = Entry(d, width="50", borderwidth="10")
    q1.place(x=330,y=145)
    q2 = Entry(d, width="50", borderwidth="10")
    q2.place(x=330,y=225)
    list_q = [q1 ,q2]
    
    def dpbtn():
        acc = q1.get()
        am = int(q2.get())
        f = "select Balance from amount where accno=%s"
        data = (acc,)
        mycr.execute(f,data)
        result = mycr.fetchone()
        newam = result[0]+am
        update = "update amount set Balance=%s where accno=%s"
        data1 = (newam,acc)
        mycr.execute(update,data1)
        bank.commit()

        q1.delete(0 ,END)
        q2.delete(0 ,END)

        Label(d, text="Your amount has been added into your account").place(x=330,y=350)

    def go_to_next_entry(event, list , this_index):
        next_index = (this_index + 1)
        list[next_index].focus_set()

    entries = [a for a in d.winfo_children() if isinstance(a, Entry)]
    for idx, entry in enumerate(entries):
        entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

    Button(d, text="Deposite", width="10",borderwidth="5", command=dpbtn).place(x=450,y=300)

def withdraw():
    d=Toplevel()    
    d.title("Withdraw your amount")
    d.geometry("750x600")
    Label(d, text="Enter your account number ", font="10").place(x=100,y=150)
    Label(d, text="Enter amount to withdraw ", font="10").place(x=100,y=230)
    q1 = Entry(d, width="50", borderwidth="10")
    q1.place(x=330,y=145)
    q2 = Entry(d, width="50", borderwidth="10")
    q2.place(x=330,y=225)
    list_q = [q1 ,q2]

    def wthbt():
        acc = q1.get()
        am = int(q2.get())
        f = "select Balance from amount where accno=%s"
        data = (acc,)
        mycr.execute(f,data)
        result = mycr.fetchone()
        newam = result[0]-am
        update = "update amount set Balance=%s where accno=%s"
        data1 = (newam,acc)
        mycr.execute(update,data1)
        bank.commit()

        q1.delete(0 ,END)
        q2.delete(0 ,END)

        Label(d, text="Your amount has been withdrawn from your account").place(x=330,y=350)

    def go_to_next_entry(event, list , this_index):
        next_index = (this_index + 1)
        list[next_index].focus_set()

    entries = [a for a in d.winfo_children() if isinstance(a, Entry)]
    for idx, entry in enumerate(entries):
        entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

    Button(d, text="withdraw", width="10",borderwidth="5", command=wthbt).place(x=450,y=300)

def enquiry():
     d=Toplevel()    
     d.title("Balance Enquiry")
     d.geometry("650x300")
     Label(d, text="Enter your account number ", font="9").place(x=50,y=40)
     q1 = Entry(d, width="50", borderwidth="10")
     q1.place(x=270,y=35)

     def enq():
        acc = q1.get()
        sql = "select balance from amount where accno=%s"
        data = (acc,)
        mycr.execute(sql,data)
        bal = mycr.fetchone()
        Label(d, text="Balance in your account is : "+ str(bal[0]), font="9" ).place(x=50,y=200)
    
     Button(d, text="See Details", width="10",borderwidth="5", command=enq).place(x=300,y=110)

def details():
     d=Toplevel()    
     d.title("Your account deatils")
     d.geometry("720x550")
     c = Canvas(d, width="720", height="550")
     c.pack()
     Label(d, text="Enter your account number ", font="9").place(x=50,y=40)
     q1 = Entry(d, width="50", borderwidth="10")
     q1.place(x=270,y=35)

     def det():
        acc = q1.get()
        sql = "select * from account where accno=%s"
        data = (acc,)
        mycr.execute(sql,data)
        f = mycr.fetchone()
        list_f = list(f)
        for i in range(6):
           Label(d, text=list_f[i] ).place(x=180,y=200+50*i)
        Label (d, text="NAME").place(x=50,y=200)
        Label (d, text="ACCOUNT NO.").place(x=50,y=250)
        Label (d, text="DOB").place(x=50,y=300)
        Label (d, text="ADDRESS").place(x=50,y=350)
        Label (d, text="PHONE NO.").place(x=50,y=400)
        Label (d, text="OPENING BALANCE").place(x=50,y=450)
        c.create_rectangle(40 ,190 ,680 ,480)
        c.create_line(170,190,170,480)
        c.create_line(40,240,680,240)
        c.create_line(40,290,680,290)
        c.create_line(40,335,680,335)
        c.create_line(40,380,680,380)
        c.create_line(40,430,680,430)
                   
     Button(d, text="see details", width="10", borderwidth="5", command=det).place(x=300,y=110)

def close():
     d=Toplevel()    
     d.title("Clsoe your accont")
     d.geometry("650x300")
     Label(d, text="Enter your account number ", font="9").place(x=50,y=40)
     q1 = Entry(d, width="50", borderwidth="10")
     q1.place(x=270,y=35)
     
     def clc():
         acc = q1.get()
         sql1 = "delete from account where accno=%s"
         sql2 = "delete from amount where accno=%s"
         data = (acc,)
         mycr.execute(sql1,data)
         mycr.execute(sql2,data)
         bank.commit()
         Label(d, text="Your account has been deleted !",font="9" ).place(x=50,y=200) 
    
     Button(d, text="Delete", width="10", borderwidth="5", command=clc).place(x=300,y=110)

btn()

p.mainloop()
