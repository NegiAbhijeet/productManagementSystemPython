import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

class application:
    def __init__(self,root):
        p=database()
        p.conn()

        root.title("Management System")
        root.geometry("1300x700")

        pid=StringVar()
        name=StringVar()
        price=StringVar()
        qty=StringVar()
        company=StringVar()
        contact=StringVar()

        def clear():
            close=tk.messagebox.askyesno("Product Management System","Do you want to close")
            if close>0:
                root.destroy()
        def reset():
            entId.delete(0,END)
            entName.delete(0,END)
            entPrice.delete(0,END)
            entQty.delete(0,END)
            entCompany.delete(0,END)
            entContact.delete(0,END)
        def insert():
            if (len(pid.get())!=0):
                p.insert(pid.get(),name.get(),price.get(),qty.get(),company.get(),contact.get())
                productlist.delete(0,END)
                productlist.insert(pid.get(),name.get(),price.get(),qty.get(),company.get(),contact.get())
                show()
            else:
                print("bekar")
        def show():
            productlist.delete(0,END)
            for row in p.show():
                productlist.insert(END,row,str(""))
        def proRec(event):
            global pd 
            searchPd=productlist.curselection()[0]
            pd = productlist.get(searchPd)
            
            entId.delete(0,END)
            entId.insert(END,pd[0])

            entName.delete(0,END)
            entName.insert(END,pd[1])

            entPrice.delete(0,END)
            entPrice.insert(END,pd[2])

            entQty.delete(0,END)
            entQty.insert(END,pd[3])

            entCompany.delete(0,END)
            entCompany.insert(END,pd[4])

            entContact.delete(0,END)
            entContact.insert(END,pd[5])
        def delete():
            if (len(pid.get())!=0):
                p.delete(pd[0])
                reset()
                show()
        def search():
            productlist.delete(0,END)
            for row in p.search(pid.get(),name.get(),price.get(),qty.get(),company.get(),contact.get()):
                productlist.insert(END,row,str(""))
        def update():
            if (len(pid.get())!=0):
                p.delete(pd[0])
            if (len(pid.get())!=0):
                p.insert(pid.get(),name.get(),price.get(),qty.get(),company.get(),contact.get())
                productlist.delete(0,END)
                productlist.insert(END,pid.get(),name.get(),price.get(),qty.get(),company.get(),contact.get())

        canvas=tk.Canvas(root,bg="#3939ac")
        canvas.place(relheight=1,relwidth=1)

        headFrame=tk.Frame(canvas,bg="#3939ac")
        headLabel=tk.Label(headFrame,text="Product Management System",font=('arial',55,'bold'),bg="red")
        headLabel.pack()
        headFrame.place(relwidth=0.8,relx=0.1)

        bodyFrame=tk.Frame(canvas,bg="#3939ac")
        leftFrame=tk.Frame(bodyFrame,bg="yellow")
        leftFrame.place(relwidth=0.55,relx=0.01,relheight=1)
        leftLable=tk.Label(leftFrame,text="Products",bg="#3939ac",fg="white",font=('arial',30,'bold'))
        leftLable.pack()
        rightFrame=tk.Frame(bodyFrame,bg="yellow")
        rightFrame.place(relwidth=0.42,relx=0.57,relheight=1)
        rightLable=tk.Label(rightFrame,text="All Products",bg="#3939ac",fg="white",font=('arial',30,'bold'))
        scroll=tk.Scrollbar(rightFrame)
        scroll.place(rely=0.2,relheight=0.7,relx=0.9)
        productlist=tk.Listbox(rightFrame,font=('arial',15,'bold'),yscrollcommand=scroll.set)
        productlist.bind('<<ListboxSelect>>',proRec)
        productlist.place(rely=0.2,relheight=0.7,relwidth=0.8,relx=0.1)
        scroll.config(command=productlist.yview)
        
        
        rightLable.pack()
        bodyFrame.place(relwidth=1,relheight=0.7,rely=0.15)

        opFrame=tk.Frame(canvas,bg="yellow")
        bt1=tk.Button(opFrame,bg="#3939ac",fg="white",bd=10,font=('arial',18,'bold'),text="Save",command=insert)
        bt1.place(relheight=0.8,relwidth=0.12,rely=0.1,relx=0.02)
        bt1=tk.Button(opFrame,bg="#3939ac",fg="white",bd=10,font=('arial',14,'bold'),text="Show Data",command=show)
        bt1.place(relheight=0.8,relwidth=0.12,rely=0.1,relx=0.16)
        bt1=tk.Button(opFrame,bg="#3939ac",fg="white",bd=10,font=('arial',18,'bold'),text="Reset",command=reset)
        bt1.place(relheight=0.8,relwidth=0.12,rely=0.1,relx=0.30)
        bt1=tk.Button(opFrame,bg="#3939ac",fg="white",bd=10,font=('arial',18,'bold'),text="Delete",command=delete)
        bt1.place(relheight=0.8,relwidth=0.12,rely=0.1,relx=0.44)
        bt1=tk.Button(opFrame,bg="#3939ac",fg="white",bd=10,font=('arial',18,'bold'),text="Search",command=search)
        bt1.place(relheight=0.8,relwidth=0.12,rely=0.1,relx=0.58)
        bt1=tk.Button(opFrame,bg="#3939ac",fg="white",bd=10,font=('arial',18,'bold'),text="Update",command=update)
        bt1.place(relheight=0.8,relwidth=0.12,rely=0.1,relx=0.72)
        bt1=tk.Button(opFrame,bg="#3939ac",fg="white",bd=10,font=('arial',18,'bold'),text="Close",command=clear)
        bt1.place(relheight=0.8,relwidth=0.12,rely=0.1,relx=0.86)
        opFrame.place(relwidth=0.8,relheight=0.1,relx=0.1,rely=0.88)

        labelId=tk.Label(leftFrame,text="Product Id",font=('arial',15,'bold'),bd=4,bg="#3939ac",fg="white")
        labelId.place(relx=0.1,relwidth=0.25,rely=0.25)
        entId=tk.Entry(leftFrame,textvariable=pid,font=('arial',15,'bold'),bd=5)
        entId.place(relx=0.38,relwidth=0.5,rely=0.25)

        labelId=tk.Label(leftFrame,text="Product Name",font=('arial',15,'bold'),bd=4,bg="#3939ac",fg="white")
        labelId.place(relx=0.1,relwidth=0.25,rely=0.35)
        entName=tk.Entry(leftFrame,textvariable=name,font=('arial',15,'bold'),bd=5)
        entName.place(relx=0.38,relwidth=0.5,rely=0.35)

        labelId=tk.Label(leftFrame,text="Product Price",font=('arial',15,'bold'),bd=4,bg="#3939ac",fg="white")
        labelId.place(relx=0.1,relwidth=0.25,rely=0.45)
        entPrice=tk.Entry(leftFrame,textvariable=price,font=('arial',15,'bold'),bd=5)
        entPrice.place(relx=0.38,relwidth=0.5,rely=0.45)

        labelId=tk.Label(leftFrame,text="Product Quantity",font=('arial',15,'bold'),bd=4,bg="#3939ac",fg="white")
        labelId.place(relx=0.1,relwidth=0.25,rely=0.55)
        entQty=tk.Entry(leftFrame,textvariable=qty,font=('arial',15,'bold'),bd=5)
        entQty.place(relx=0.38,relwidth=0.5,rely=0.55)

        labelId=tk.Label(leftFrame,text="Product Company",font=('arial',15,'bold'),bd=4,bg="#3939ac",fg="white")
        labelId.place(relx=0.1,relwidth=0.25,rely=0.65)
        entCompany=tk.Entry(leftFrame,textvariable=company,font=('arial',15,'bold'),bd=5)
        entCompany.place(relx=0.38,relwidth=0.5,rely=0.65)

        labelId=tk.Label(leftFrame,text="Contact",font=('arial',15,'bold'),bd=4,bg="#3939ac",fg="white")
        labelId.place(relx=0.1,relwidth=0.25,rely=0.75)
        entContact=tk.Entry(leftFrame,textvariable=contact,font=('arial',15,'bold'),bd=5)
        entContact.place(relx=0.38,relwidth=0.5,rely=0.75)

class database:
    def conn(self):
        print("database called")
        con=sqlite3.connect("management.db")
        cur=con.cursor()
        query="create table if not exists product(pid integer primary key,name text,price text,qty text,company text,contact text)"
        cur.execute(query)
        con.commit()
        con.close()
    def insert(self,pid,name,price,qty,company,contact):
        con=sqlite3.connect("management.db")
        cur=con.cursor()
        query="insert into product values(?,?,?,?,?,?)"
        cur.execute(query,(pid,name,price,qty,company,contact))
        con.commit()
        con.commit()
    def show(self):
        con=sqlite3.connect("management.db")
        cur=con.cursor()
        query="select * from product"
        cur.execute(query)
        rows=cur.fetchall()
        con.commit()
        con.commit()
        return rows
    def delete(self,pid):
        con=sqlite3.connect("management.db")
        cur=con.cursor()
        cur.execute("delete from product where pid=?",(pid,))
        con.commit()
        con.close()
    def search(self,pid="",name="",price="",qty="",company="",contact=""):
        con=sqlite3.connect("management.db")
        cur=con.cursor()
        query="select * from product where pid=? or name=? or price=? or qty=? or company =? or contact=?"
        cur.execute(query,(pid,name,price,qty,company,contact))
        rows=cur.fetchall()
        con.commit()
        return rows
    def update(self,pid="",name="",price="",qty="",company="",contact=""):
        con=sqlite3.connect("management.db")
        cur=con.cursor()
        query="update product set pid=? or name=? or price=? or qty=? or company =? or contact=?"
        cur.execute(query,(pid,name,price,qty,company,contact))
        con.commit()
        con.commit()

if __name__=='__main__':
    root=tk.Tk()
    pd=[]
    application=application(root)
    root.mainloop()