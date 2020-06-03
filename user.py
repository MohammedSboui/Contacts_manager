from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import datetime
conn = sqlite3.connect("contacts.db")
c=conn.cursor()
def refresh(window,username,passwd):
    window.destroy()
    User(username,passwd)

def ajouter(nom,prenom,tel,dep,window,username,passwd):
    nomm=nom.get()
    prenomm=prenom.get()
    tell=tel.get()
    depp=dep.get()
    if nomm =='' or prenomm =='' or tell=='' or depp=='':
        messagebox.showerror("Error","please fill all the entries !")
        return
    for cc in ['0','1','2','3','4','5','6','7','8','9']:
        if cc in nomm or cc in prenomm or cc in depp:
            messagebox.showerror("Error","Nom ou prenom ou departement can't have digits")
    if(len(tell)!=8):
        messagebox.showerror("Error","give valid tel number")
    for cc in tell:
        if(cc>'9' or cc < '0'):
            messagebox.showerror("Error","give valid tel number")
            
        
            
    c.execute("""INSERT INTO allcontacts (nom,prenom,tel,dep) VALUES(?,?,?,?)""",(nomm,prenomm,tell,depp))
    conn.commit()
    nom.delete(0, END)
    prenom.delete(0, END)
    tel.delete(0, END)
    dep.delete(0, END)
    messagebox.showinfo("Success","contact registred !")
    refresh(window,username,passwd)

def User(username,passwd):
    window = Tk()
    window.geometry("950x950")
    window.resizable(False,False)
    window.configure(bg="steelblue")
    window.title("User")
    tree=ttk.Treeview(window,columns=("a","b","c"))
    tree.heading('#0', text="Nom")
    tree.heading('#1', text="Prenom")
    tree.heading('#2', text="Tel")
    tree.heading('#3', text="Departement")

    tree.column("#0", width=120)
    tree.column("#1", width=120)
    tree.column("#2", width=120)
    tree.column("#3", width=120)

    tree.place(x=300,y=200)
    
    
    bar = Frame(window,width=950,height=140,bg="lightblue")
    bar.place(x=0,y=0)
    welcome = Label(window,text="Welcome "+username+"!",font=('arial 35'),bg="lightblue",fg="black")
    welcome.place(x=350,y=15)
    contacts = Label(window,text="Contacts",font=('arial 12'),bg="steelblue",fg="black")
    contacts.place(x=450,y=170)
    
    
    
    

    c.execute("""Select * from allcontacts""") 
    all_contacts = c.fetchall()
    for elem in all_contacts:
        tree.insert("", "end",text=elem[0],values=(elem[1],elem[2],elem[3]))
    
    nom = Label(window,text="nom",font=('arial 12'),bg="steelblue",fg="black")
    prenom = Label(window,text="prenom",font=('arial 12'),bg="steelblue",fg="black")
    tel = Label(window,text="Tel",font=('arial 12'),bg="steelblue",fg="black")
    dep = Label(window,text="departement",font=('arial 12'),bg="steelblue",fg="black")
    nom_box = Entry(window)
    nom_box.bind('<Return>', ajouter)

    prenom_box = Entry(window)
    prenom_box.bind('<Return>', ajouter)

    
    tel_box = Entry(window)
    tel_box.bind('<Return>', ajouter)

    
    dep_box = Entry(window)
    dep_box.bind('<Return>', ajouter)

    add = Button(window, text='Ajouter', command=lambda:ajouter(nom_box,prenom_box,tel_box,dep_box,window,username,passwd),bg="lightblue",width=20)
    add.bind('<Return>', ajouter)

    nom.place(x=15,y=200)
    nom_box.place(x=15,y=225)
    prenom.place(x=15,y=250)
    prenom_box.place(x=15,y=275)
    tel.place(x=15,y=300)
    tel_box.place(x=15,y=325)
    dep.place(x=15,y=350)
    dep_box.place(x=15,y=375)
    add.place(x=15,y=410)

    
    
    window.mainloop()