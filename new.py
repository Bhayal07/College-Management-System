from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import datetime
import Fee_Backend


class Fee():
    def __init__(self, master):
        self.master = master
        self.master.title('Fee Report')
        self.master.geometry('1350x750')
        self.master.config(bg='Navajo white')

        # ==================================================Variables=================================================
        self.recpt = StringVar()
        self.name = StringVar()
        self.admsn = StringVar()
        self.date = StringVar()
        self.branch = StringVar()
        self.sem = StringVar()
        self.total = DoubleVar()
        self.paid = DoubleVar()
        self.due = DoubleVar()

        # ==================================================Functions=================================================
        def Tuple(event):
            try:
                global st
                index = self.list.curselection()[0]
                st = self.list.get(index)

                self.recpt_entry.delete(0, END)
                self.recpt_entry.insert(END, st[1])
                self.name_entry.delete(0, END)
                self.name_entry.insert(END, st[2])
                self.admsn_entry.delete(0, END)
                self.admsn_entry.insert(END, st[3])
                self.Date_entry.delete(0, END)
                self.Date_entry.insert(END, st[4])
                self.branch_entry.delete(0, END)
                self.branch_entry.insert(END, st[5])
                self.sem_entry.delete(0, END)
                self.sem_entry.insert(END, st[6])
                self.total_entry.delete(0, END)
                self.total_entry.insert(END, st[7])
                self.paid_entry.delete(0, END)
                self.paid_entry.insert(END, st[8])
                self.due_entry.delete(0, END)
                self.due_entry.insert(END, st[9])
            except IndexError:
                pass

        def Insert():
            if (len(self.admsn.get()) != 0):
                Fee_Backend.insert(self.recpt.get(), self.name.get(), self.admsn.get(), self.date.get(),self.branch.get(), self.sem.get(), self.total.get(), self.paid.get(), self.due.get())
                self.list.delete(0, END)
                self.list.insert(END, (self.recpt.get(), self.name.get(), self.admsn.get(), self.date.get(), self.branch.get(), self.sem.get(), self.total.get(), self.paid.get(), self.due.get()))

        def View():
            self.list.delete(0, END)
            for row in Fee_Backend.view():
                self.list.insert(END, row, str(' '))

        def Reset():
            self.recpt.set(' ')
            self.name.set(' ')
            self.admsn.set(' ')
            #self.date.set(' ')
            self.branch.set(' ')
            self.sem.set(' ')
            self.paid.set(' ')
            self.due.set(' ')
            self.Display.delete('1.0', END)
            self.list.delete(0, END)

        def Delete():
            Fee_Backend.delete(st[0])
            Reset()
            View()

        def Receipt():
            self.Display.delete('1.0', END)
            self.Display.insert(END, '\t\tRECEIPT' + '\n\n')
            self.Display.insert(
                END, '\tReceipt No.\t     :' + self.recpt.get() + '\n')
            self.Display.insert(END, '\tStudent Name  :' +
                                self.name.get() + '\n')
            self.Display.insert(END, '\tAdmission No.\t:' +
                                self.admsn.get() + '\n')
            self.Display.insert(
                END, '\tDate\t          :' + self.date.get() + '\n')
            self.Display.insert(
                END, '\tBranch\t          :' + self.branch.get() + '\n')
            self.Display.insert(
                END, '\tSemester \t        :' + self.sem.get() + '\n\n')

            x1 = (self.var_1.get())
            x2 = (self.paid.get())
            x3 = (x1 - x2)

            self.Display.insert(END, '\tTotal Amount  :' + str(x1) + '\n')
            self.Display.insert(END, '\tPaid Amount   :' + str(x2) + '\n')
            self.Display.insert(END, '\tBalance\t         :' + str(x3) + '\n')

            self.due.set(x3)

        def Search():
            self.list.delete(0, END)
            for row in Fee_Backend.search(self.recpt.get(), self.name.get(), self.admsn.get(), self.date.get(),self.branch.get(), self.sem.get(), self.total.get(), self.paid.get(), self.due.get()):
                self.list.insert(END, row, str(' '))

        def Update():
            Fee_Backend.delete(st[0])
            Insert()

        def Exit():
            Exit = tkinter.messagebox.askyesno(
                'Attention', 'Confirm, if you want to Exit')
            if Exit > 0:
                root.destroy()
                return

        # ==================================================Frames===================================================
        Main_Frame = Frame(self.master, bg='Navajo white')
        Main_Frame.grid()

        Title_Frame = LabelFrame(
            Main_Frame, width=1350, height=100, bg='Navajo white', relief='ridge', bd=15)
        Title_Frame.pack(side=TOP)

        self.lblTitle = Label(Title_Frame, font=('arial', 40, 'bold'), text='FEE REPORT',bg='navajowhite', padx=13)
        self.lblTitle.grid(padx=400)

        Data_Frame = Frame(Main_Frame, width=1350, height=350,bg='Navajo white', relief='ridge', bd=15)
        Data_Frame.pack(side=TOP, padx=15)

        Frame_1 = LabelFrame(Data_Frame, width=850, height=350, bg='Navajo white', relief='ridge', bd=8,text='Informations', font=('arial', 15, 'bold'))
        Frame_1.pack(side=LEFT, padx=10)

        Frame_2 = LabelFrame(Data_Frame, width=495, height=350, bg='Navajo white', relief='ridge', bd=8,text='Fee Receipt', font=('arial', 15, 'bold'))
        Frame_2.pack(side=RIGHT, padx=10)

        List_Frame = Frame(Main_Frame, width=1350, height=150,bg='Navajo white', relief='ridge', bd=15)
        List_Frame.pack(side=TOP, padx=15)

        Button_Frame = Frame(Main_Frame, width=1350, height=80,bg='Navajo white', relief='ridge', bd=15)
        Button_Frame.pack(side=TOP)

        # ===================================================Labels================================================
        self.recpt_label = Label(Frame_1, text='Receipt No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.recpt_label.grid(row=0, column=0, padx=15, sticky=W)

        self.name_label = Label(Frame_1, text='Student Name : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.name_label.grid(row=1, column=0, padx=15, sticky=W)

        self.admsn_label = Label(Frame_1, text='Admission No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.admsn_label.grid(row=2, column=0, padx=15, sticky=W)

        self.Date_label = Label(Frame_1, text='Date : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.Date_label.grid(row=3, column=0, padx=15, sticky=W)

        self.branch_label = Label(Frame_1, text='Branch : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.branch_label.grid(row=4, column=0, padx=15, sticky=W)

        self.sem_label = Label(Frame_1, text='Semester : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.sem_label.grid(row=5, column=0, padx=15, sticky=W)

        self.total_label = Label(Frame_1, text='TOTAL AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.total_label.grid(row=2, column=2, padx=5, sticky=W)

        self.paid_label = Label(Frame_1, text='PAID AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.paid_label.grid(row=3, column=2, padx=5, sticky=W)

        self.due_label = Label(Frame_1, text='BALANCE : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.due_label.grid(row=4, column=2, padx=5, sticky=W)

        # ==================================================Entries=================================================
        self.var_1 = DoubleVar(Frame_1, value='36265')
        d1 = datetime.date.today()
        self.date.set(d1)

        self.recpt_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.recpt)
        self.recpt_entry.grid(row=0, column=1, padx=15, pady=5)

        self.name_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.name)
        self.name_entry.grid(row=1, column=1, padx=15, pady=5)

        self.admsn_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.admsn)
        self.admsn_entry.grid(row=2, column=1, padx=15, pady=5)

        self.Date_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.date)
        self.Date_entry.grid(row=3, column=1, padx=15, pady=5)

        self.branch_entry = ttk.Combobox(Frame_1, values=(' ', 'CSE', 'IT', 'ETC/ET&T', 'Mechanical', 'Civil', 'EE', 'EEE'),font=('arial', 14), width=19, textvariable=self.branch)
        self.branch_entry.grid(row=4, column=1, padx=15, pady=5)

        self.sem_entry = ttk.Combobox(Frame_1, values=(' ', 'FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH','SEVENTH', 'EIGHTH'), font=('arial', 14), width=19,textvariable=self.sem)
        self.sem_entry.grid(row=5, column=1, padx=15, pady=5)

        self.total_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.var_1, state='readonly')
        self.total_entry.grid(row=2, column=3, padx=8, pady=5)

        self.paid_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.paid)
        self.paid_entry.grid(row=3, column=3, pady=5)

        self.due_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.due)
        self.due_entry.grid(row=4, column=3, pady=7)

        # ==================================================Frame_2=================================================
        self.Display = Text(Frame_2, width=42, height=12,
                            font=('arial', 14, 'bold'))
        self.Display.grid(row=0, column=0, padx=3)

        # =============================================List box and scrollbar===========================================
        sb = Scrollbar(List_Frame)
        sb.grid(row=0, column=1, sticky='ns')

        self.list = Listbox(List_Frame, font=(
            'arial', 13, 'bold'), width=140, height=8)
        self.list.bind('<<ListboxSelect>>', Tuple)
        self.list.grid(row=0, column=0)
        sb.config(command=self.list.yview)

        # ==================================================Buttons=================================================
        btnSave = Button(Button_Frame, text='SAVE', font=(
            'arial', 14, 'bold'), width=10, command=Insert)
        btnSave.grid(row=0, column=0, padx=5, pady=5)

        btnDisplay = Button(Button_Frame, text='DISPLAY', font=(
            'arial', 14, 'bold'), width=10, command=View)
        btnDisplay.grid(row=0, column=1, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='RESET', font=(
            'arial', 14, 'bold'), width=10, command=Reset)
        btnReset.grid(row=0, column=2, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='UPDATE', font=(
            'arial', 14, 'bold'), width=10, command=Update)
        btnReset.grid(row=0, column=3, padx=5, pady=5)

        btnSearch = Button(Button_Frame, text='SEARCH', font=(
            'arial', 14, 'bold'), width=10, command=Search)
        btnSearch.grid(row=0, column=4, padx=5, pady=5)

        btnDelete = Button(Button_Frame, text='DELETE', font=(
            'arial', 14, 'bold'), width=10, command=Delete)
        btnDelete.grid(row=0, column=5, padx=5, pady=5)

        btnReceipt = Button(Button_Frame, text='RECEIPT', font=(
            'arial', 14, 'bold'), width=10, command=Receipt)
        btnReceipt.grid(row=0, column=6, padx=5, pady=5)

        btnExit = Button(Button_Frame, text='EXIT', font=(
            'arial', 14, 'bold'), width=10, command=Exit)
        btnExit.grid(row=0, column=7, padx=5, pady=5)


root = Tk()
obj = Fee(root)
root.mainloop()

import sqlite3

def connect():
    con = sqlite3.connect('fee.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS fee(id INTEGER PRIMARY KEY, recpt integer, name text, admsn text, date integer, branch text, sem text, total integer, paid integer, due integer)')

    con.commit()
    con.close()

def insert(recpt = ' ', name = ' ', admsn = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
    con = sqlite3.connect('fee.db')
    cur = con.cursor()

    cur.execute('INSERT INTO fee VALUES (NULL,?,?,?,?,?,?,?,?,?)',(recpt,name,admsn,date,branch,sem,total,paid,due))

    con.commit()
    con.close()

def view():
    con = sqlite3.connect('fee.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM fee')
    row = cur.fetchall()
    return row

    con.commit()
    

def delete(id):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('DELETE FROM fee WHERE id = ?',(id,))

       con.commit()
       con.close()

def update(id,recpt = ' ', name = ' ', admsn = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('UPDATE fee SET recpt = ? OR name = ? OR admsn = ? OR date = ? OR branch = ? OR sem = ? OR total = ? OR paid = ? OR due = ?',(recpt,name,admsn,date,branch,sem,total,paid,due))


       con.commit()
       con.close()

def search(recpt = ' ', name = ' ', admsn = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = sqlite3.connect('fee.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM fee WHERE  recpt = ? OR name = ? OR admsn = ? OR date = ? OR branch = ? OR sem = ? OR total = ? OR paid = ? OR due = ?',(recpt,name,admsn,date,branch,sem,total,paid,due))
       row = cur.fetchall()
       return row

       con.commit()
       
connect()

import sqlite3

def connect():
       con = sqlite3.connect('library.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS library(x INTEGER PRIMARY KEY, Mtype text, refno integer, fname text, \
                     surname text, address text, post integer, mobno integer, ID text, title text, author text, \
                     borrow integer, due integer, loan integer)')


       con.commit()
       con.close()

def insert(Mtype = ' ', refno = ' ', fname = ' ', surname = ' ', address = ' ', post = ' ', mobno = ' ', ID = ' ', title = ' ', author = ' ', borrow = ' ', due = ' ', loan = ' '):
       con = sqlite3.connect('library.db')
       cur = con.cursor()

       cur.execute('INSERT INTO library VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)',(Mtype,refno,fname,surname,address,post, mobno,ID,title,author,borrow,due,loan))

       con.commit()
       con.close()

def view():
       con = sqlite3.connect('library.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM library')
       row = cur.fetchall()
       return row

       con.close()
def delete(x):
       con = sqlite3.connect('library.db')
       cur = con.cursor()

       cur.execute('DELETE FROM library WHERE x = ?',(x,))
       
       con.commit()
       con.close()
       
def update(x, Mtype = ' ', refno = ' ', fname = ' ', surname = ' ', address = ' ', post = ' ', mobno = ' ', ID = ' ', title = ' ', author = ' ', borrow = ' ', due = ' ', loan = ' '):
       con = sqlite3.connect('library.db')
       cur = con.cursor()

       cur.execute('UPDATE library SET Mtype = ? OR refno = ? OR fname = ? OR surname = ? OR address = ? OR post = ? OR \
       mobno = ? OR ID = ? OR title = ? OR author = ? OR borrow = ? OR due = ? OR loan = ?',(Mtype,refno,fname,surname,address, post,mobno,ID,title,author,borrow,due,loan))
       con.commit()
       con.close()

def search(Mtype = ' ', refno = ' ', fname = ' ', surname = ' ', address = ' ', post = ' ', mobno = ' ', ID = ' ', title = ' ', author = ' ', borrow = ' ', due = ' ', loan = ' '):
       con = sqlite3.connect('library.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM library WHERE Mtype = ? OR refno = ? OR fname = ? OR surname = ? OR address = ? OR \
       post = ? OR mobno = ? OR ID = ? OR title = ? OR author = ? OR borrow = ? OR due = ? OR loan = ?',(Mtype,refno,\
                                                                                                        fname,surname,\
                                                                                                        address,post,mobno,\
                                                                                                        ID,title,author,\
                                                                                                        borrow,due,loan))
       row = cur.fetchall()
       return row
       con.close()


connect()

from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox
import Library_Backend

class Library:
       
       def __init__(self, root):
              self.root = root
              self.root.title('Library Management System')
              self.root.geometry('1350x750')
              self.root.config(bg = 'navajowhite')

       #===================================================Variables===================================================
              self.Mtype = StringVar()
              self.refno = StringVar()
              self.fname = StringVar()
              self.surname = StringVar()
              self.address = StringVar()
              self.post = StringVar()
              self.mobno = StringVar()
              self.ID = StringVar()
              self.title = StringVar()
              self.author = StringVar()
              self.borrow = StringVar()
              self.due = StringVar()
              self.loan = StringVar()
              self.yop = StringVar()
              self.edsn = StringVar()
              


       #================================================Functions======================================================
              def BookRec(event):
                     try:
                            global selected_tuple
                            index = self.Listbox_2.curselection()[0]
                            selected_tuple = self.Listbox_2.get(index)

                            self.Entry_0.delete(0, END)
                            self.Entry_0.insert(END, selected_tuple[1])  
                            self.Entry_1.delete(0, END)
                            self.Entry_1.insert(END, selected_tuple[2])                           
                            self.Entry_2.delete(0, END)
                            self.Entry_2.insert(END, selected_tuple[3])
                            self.Entry_3.delete(0, END)
                            self.Entry_3.insert(END, selected_tuple[4])
                            self.Entry_4.delete(0, END)
                            self.Entry_4.insert(END, selected_tuple[5])
                            self.Entry_5.delete(0, END)
                            self.Entry_5.insert(END, selected_tuple[6])
                            self.Entry_6.delete(0, END)
                            self.Entry_6.insert(END, selected_tuple[7])
                            self.Entry_7.delete(0, END)
                            self.Entry_7.insert(END, selected_tuple[8])
                            self.Entry_8.delete(0, END)
                            self.Entry_8.insert(END, selected_tuple[9])
                            self.Entry_9.delete(0, END)
                            self.Entry_9.insert(END, selected_tuple[10])
                            self.Entry_10.delete(0, END)
                            self.Entry_10.insert(END, selected_tuple[11])
                            self.Entry_11.delete(0, END)
                            self.Entry_11.insert(END, selected_tuple[12])
                            self.Entry_12.delete(0, END)
                            self.Entry_12.insert(END, selected_tuple[13])

                     except IndexError:
                            pass
              def Insert():
                     if(len(self.refno.get()) != 0):
                            Library_Backend.insert(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get(), self.address.get(), self.post.get(), self.mobno.get(), self.ID.get(), self.title.get(), self.author.get(), self.borrow.get(), self.due.get(), self.loan.get())
                            self.Listbox_2.delete(0, END)
                            self.Listbox_2.insert(END , (self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get(), self.address.get(), self.post.get(), self.mobno.get(), self.ID.get(), self.title.get(), self.author.get(), self.borrow.get(), self.due.get(), self.loan.get()))
                            

              def Display():
                     self.Listbox_2.delete(0, END)
                     for row in Library_Backend.view():
                            self.Listbox_2.insert(END, row, str(' '))  
              def Exit():
                     Exit = tkinter.messagebox.askyesno('Library Management System','Confirm if you want to Exit')
                     if Exit > 0:
                            root.destroy()
                            return
              def Reset():
                     self.Mtype.set('')
                     self.refno.set('')
                     self.fname.set('')
                     self.surname.set('')
                     self.address.set('')
                     self.post.set('')
                     self.mobno.set('')
                     self.ID.set('')
                     self.title.set('')
                     self.author.set('')
                     self.borrow.set('')
                     self.due.set('')
                     self.loan.set('')
                     self.Display.delete('1.0',END)
                     self.Listbox_2.delete(0, END)

              def Delete():
                     Library_Backend.delete(selected_tuple[0])
                     Reset()
                     Display()

              def Update():
                     Library_Backend.delete(selected_tuple[0])
                     Library_Backend.insert(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get(), self.address.get(), self.post.get(), self.mobno.get(), self.ID.get(), self.title.get(), self.author.get(), self.borrow.get(), self.due.get(), self.loan.get())
                     self.Listbox_2.delete(0, END)
                     self.Listbox_2.insert(END,(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get()\
                                                 , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get()\
                                                 , self.title.get(), self.author.get(), self.borrow.get(), self.due.get()\
                                                 , self.loan.get()))

              def Search():
                     self.Listbox_2.delete(0, END)
                     for row in Library_Backend.search(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get()\
                                                 , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get()\
                                                 , self.title.get(), self.author.get(), self.borrow.get(), self.due.get()\
                                                 , self.loan.get()):
                            self.Listbox_2.insert(END, row, str(' '))

              def Details():
                     self.Display.delete('1.0',END)
                     self.Display.insert(END, 'Book ID: ' + self.ID.get() + '\n')
                     self.Display.insert(END, 'Title: ' + self.title.get() + '\n')
                     self.Display.insert(END, 'Author:  ' +  self.author.get() + '\n')
                     self.Display.insert(END, 'Edition: ' + self.edsn.get() + '\n')
                     self.Display.insert(END, 'Year of Publision: \t' + self.yop.get() + '\n')
                     self.Display.insert(END, 'Date Borrowed: ' + self.borrow.get() + '\n')
                     self.Display.insert(END, 'Date Due:' + self.due.get() + '\n')
                     self.Display.insert(END, 'Days in Loan: ' + self.loan.get() + '\n')


       #=====================================================Frames=====================================================
              Main_Frame = Frame(self.root, bg = 'navajowhite')
              Main_Frame.grid()

              Title_Frame_1 = Frame(Main_Frame, width = 1350, bg = 'navajowhite', relief = RIDGE, bd = 15, padx = 20)
              Title_Frame_1.pack(side = TOP)

              self.lblTitle = Label(Title_Frame_1, font = ('arial',40,'bold'), text = '\tLibrary Management System\t', \
                                   bg = 'navajowhite', padx = 13)
              self.lblTitle.grid()

              Button_Frame = Frame(Main_Frame, width = 1350, height = 50, relief = RIDGE, bd = 10, bg = 'navajowhite')
              Button_Frame.pack(side = BOTTOM)

              Detail_Frame = Frame(Main_Frame, width = 1350, height = 100, relief = RIDGE, bd = 10, bg = 'navajowhite')
              Detail_Frame.pack(side = BOTTOM)

              Data_Frame = Frame(Main_Frame, width = 1350, height = 400, relief = RIDGE, bd = 15, bg = 'navajowhite')
              Data_Frame.pack(side = BOTTOM)

              Frame_1 = LabelFrame(Data_Frame, width = 800, height = 400, relief = RIDGE, bd = 10, bg = 'navajowhite', \
                            text = "Library Membership Info:", padx = 20, font = ('arial',15,'bold'))
              Frame_1.pack(side = LEFT, padx = 3)

              Frame_2 = LabelFrame(Data_Frame, width = 550, height = 400, relief = RIDGE, bd = 10, bg = 'navajowhite', text = "Book Details:", padx = 20, font = ('arial',15,'bold'))
              Frame_2.pack(side = RIGHT)


       #================================================Labels========================================================
              self.Label_1 = Label(Frame_1, text = 'Member type', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_1.grid(row = 0, column = 0, sticky = W)
              self.Label_2 = Label(Frame_1, text = 'Reference No.', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_2.grid(row = 1, column = 0, sticky = W)
              self.Label_3 = Label(Frame_1, text = 'First Name', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_3.grid(row = 2, column = 0, sticky = W)
              self.Label_4 = Label(Frame_1, text = 'Surname', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_4.grid(row = 3, column = 0, sticky = W)
              self.Label_5 = Label(Frame_1, text = 'Address', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_5.grid(row = 4, column = 0, sticky = W)
              self.Label_6 = Label(Frame_1, text = 'Post Code', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_6.grid(row = 5, column = 0, sticky = W)
              self.Label_7 = Label(Frame_1, text = 'Mobile No.', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_7.grid(row = 6, column = 0, sticky = W)
              self.Label_8 = Label(Frame_1, text = 'Book ID', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_8.grid(row = 0, column = 2, sticky = W)
              self.Label_9 = Label(Frame_1, text = 'Book Title', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_9.grid(row = 1, column = 2, sticky = W)
              self.Label_10 = Label(Frame_1, text = 'Author', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_10.grid(row = 2, column = 2, sticky = W)
              self.Label_11 = Label(Frame_1, text = 'Date Borrowed', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_11.grid(row = 3, column = 2, sticky = W)
              self.Label_13 = Label(Frame_1, text = 'Date Due', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_13.grid(row = 4, column = 2, sticky = W)
              self.Label_13 = Label(Frame_1, text = 'Days in Loan', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_13.grid(row = 5, column = 2, sticky = W)
              


       #================================================Entries========================================================
              self.Entry_0 = ttk.Combobox(Frame_1, values = (' ','Student','Faculty','Staff Member'), \
                                          font = ('arial',13,'bold'), width = 23, textvariable = self.Mtype )
              self.Entry_0.grid(row = 0, column = 1)
              self.Entry_1 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.refno )
              self.Entry_1.grid(row = 1, column = 1, padx = 15)
              self.Entry_2 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.fname)
              self.Entry_2.grid(row = 2, column = 1, padx = 15)
              self.Entry_3 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.surname)
              self.Entry_3.grid(row = 3, column = 1, padx = 15)
              self.Entry_4 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.address)
              self.Entry_4.grid(row = 4, column = 1, padx = 15)
              self.Entry_5 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.post)
              self.Entry_5.grid(row = 5, column = 1, padx = 15)
              self.Entry_6 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.mobno)
              self.Entry_6.grid(row = 6, column = 1, padx = 15)
              self.Entry_7 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.ID)
              self.Entry_7.grid(row = 0, column = 4, padx = 15)
              self.Entry_8 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.title)
              self.Entry_8.grid(row = 1, column = 4, padx = 15)
              self.Entry_9 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.author)
              self.Entry_9.grid(row = 2, column = 4, padx = 15)
              self.Entry_10 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.borrow)
              self.Entry_10.grid(row = 3, column = 4, padx = 15)
              self.Entry_11 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.due)
              self.Entry_11.grid(row = 4, column = 4, padx = 15)
              self.Entry_12 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.loan)
              self.Entry_12.grid(row = 5, column = 4, padx = 15)                                        


       #=============================================Widgets=========================================================
              self.Display = Text(Frame_2, font = ('arial',13,'bold'), width = 28, height = 11)
              self.Display.grid(row = 0, column = 2)


              List_of_Books = [' C',' C++',' Java',' Python',' PHP',' Java Script',' My SQL',' Data Structure',' Linux',\
                            ' Operating System',' Web Developement',' Data Science',' Algorithms',' Android', \
                            ' VB.net']


       #===========================================Function for Books Details=========================================
              def SelectedBook(event):
                     value = str(self.Listbox_1.get(self.Listbox_1.curselection()))
                     v = value

                     if (v == ' C'):
                            self.ID.set('ISBN 525341')
                            self.title.set('Programming using C')
                            self.author.set('Yashwant Kanetkar')
                            self.yop.set('2019')
                            self.edsn.set('5th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 14)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('14')
                            self.due.set(d3)
                            Details()
                     elif (v == ' C++'):
                            self.ID.set('ISBN 345687')
                            self.title.set('Programming using C++')
                            self.author.set('Yashwant Kanetkar')
                            self.yop.set('2019')
                            self.edsn.set('4th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 10)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('10')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Java'):
                            self.ID.set('ISBN 643842')
                            self.title.set('Java Programming')
                            self.author.set('Joshua Bloch')
                            self.yop.set('2019')
                            self.edsn.set('7th')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('13')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Python'):
                            self.ID.set('ISBN 564524')
                            self.title.set('Python Programming')
                            self.author.set('John Zelle')
                            self.yop.set('2019')
                            self.edsn.set('3rd')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('13')
                            self.due.set(d3)
                            Details()
                     elif (v == ' PHP'):
                            self.ID.set('ISBN 735893')
                            self.title.set('PHP Programming')
                            self.author.set('Alan Forbes')
                            self.yop.set('2019')
                            self.edsn.set('5th')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 15)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('15')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Java Script'):
                            self.ID.set('ISBN 643842')
                            self.title.set('Java Script Programming')
                            self.author.set('Jon Duckett.')
                            self.yop.set('2019')
                            self.edsn.set('4th')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('13')
                            self.due.set(d3)
                            Details()
                     elif (v == ' My SQL'):
                            self.ID.set('ISBN 649635')
                            self.title.set('My SQL Programming')
                            self.author.set('Groff James')
                            self.yop.set('2019')
                            self.edsn.set('3rd')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 20)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('20')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Data Structure'):
                            self.ID.set('ISBN 531588')
                            self.title.set('Data Structure')
                            self.author.set('Karumanchi Narasimha')
                            self.yop.set('2019')
                            self.edsn.set('5th')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 11)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('11')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Linux'):
                            self.ID.set('ISBN 356853')
                            self.title.set('Linux Administration')
                            self.author.set('SOYINKA')
                            self.yop.set('2019')
                            self.edsn.set('1st')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 6)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('6')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Operating System'):
                            self.ID.set('ISBN 536453')
                            self.title.set('OS Concepts ')
                            self.author.set('Silberschatz Abraham')
                            self.yop.set('2019')
                            self.edsn.set('4th')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 12)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('12')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Web Developement'):
                            self.ID.set('ISBN 543548')
                            self.title.set('Web Developement ')
                            self.author.set('Paul McFedries')
                            self.yop.set('2019')
                            self.edsn.set('3rd')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 15)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('15')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Data Science'):
                            self.ID.set('ISBN 835764')
                            self.title.set('Data Science Concept ')
                            self.author.set('David Stephenson')
                            self.yop.set('2019')
                            self.edsn.set('3rd')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 15)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('15')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Algorithms'):
                            self.ID.set('ISBN 535674')
                            self.title.set('Basics of Algorithm ')
                            self.author.set('Karumanchi Narasimha')
                            self.yop.set('2019')
                            self.edsn.set('7th')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 10)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('10')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Android'):
                            self.ID.set('ISBN 356452')
                            self.title.set('Android Programming')
                            self.author.set('Harwani B. M')
                            self.yop.set('2019')
                            self.edsn.set('4th')

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 9)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('9')
                            self.due.set(d3)
                            Details()
                            
       #===========================================List Box and Scroll Bar==========================================                    
              sb_1 = Scrollbar(Frame_2)
              sb_1.grid(row =0, column = 1, sticky = 'ns')

              self.Listbox_1 = Listbox(Frame_2, font = ('arial',13,'bold'), width = 20, height = 10)
              self.Listbox_1.bind('<<ListboxSelect>>', SelectedBook)
              self.Listbox_1.grid(row = 0, column = 0)
              sb_1.config(command = self.Listbox_1.yview)

              
              sb_2 = Scrollbar(Detail_Frame)
              sb_2.grid(row = 1, column = 1, sticky = 'ns')

              self.Listbox_2 = Listbox(Detail_Frame, font = ('arial',13,'bold'), width = 144, height = 11)
              self.Listbox_2.bind('<<ListboxSelect>>', BookRec)
              self.Listbox_2.grid(row = 1, column = 0)
              sb_2.config(command = self.Listbox_2.yview)

              for items in List_of_Books:
                     self.Listbox_1.insert(END, items)


       #=============================================Buttons=========================================================
              Button_1 = Button(Button_Frame, text = 'SAVE', font = ('arial',15,'bold'), width = 10, command = Insert)
              Button_1.grid(row = 0, column = 0, padx = 8, pady = 5)
              Button_2 = Button(Button_Frame, text = 'DISPLAY', font = ('arial',15,'bold'), width = 10, command = Display)
              Button_2.grid(row = 0, column = 1, padx = 8)
              Button_3 = Button(Button_Frame, text = 'RESET', font = ('arial',15,'bold'), width = 10, command = Reset)
              Button_3.grid(row = 0, column = 2, padx = 8)
              Button_4 = Button(Button_Frame, text = 'UPDATE', font = ('arial',15,'bold'), width = 10, command = Update)
              Button_4.grid(row = 0, column = 3, padx = 8)
              Button_5 = Button(Button_Frame, text = 'SEARCH', font = ('arial',15,'bold'), width = 10, command = Search)
              Button_5.grid(row = 0, column = 4, padx = 8)
              Button_6 = Button(Button_Frame, text = 'DELETE', font = ('arial',15,'bold'), width = 10, command = Delete)
              Button_6.grid(row = 0, column = 5, padx = 8)
              Button_7 = Button(Button_Frame, text = 'EXIT', font = ('arial',15,'bold'), width = 10, command = Exit)
              Button_7.grid(row = 0, column = 6, padx = 8)

              

if __name__ == '__main__':
       root = Tk()
       applicaton = Library(root)
       root.mainloop()


from tkinter import*
import tkinter.messagebox                               # for messagebox
import os                                               # for stringvariable
from tkinter import ttk                                 # for combobox
import random                                           # for reference
import time
import datetime

def main():
    root = Tk()
    app = Window_1(root)


class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('1350x750')
        self.master.config(bg = 'lightskyblue')
        self.Frame = Frame(self.master, bg = 'lightskyblue')
        self.Frame.pack()


        self.Username = StringVar()                             # x = StringVar()  Holds a string; default value is " "
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text = 'Login Menu', font = ('arial',55,'bold'), bg = 'lightskyblue', fg = 'Black')
        self.Lbl_Title.grid(row = 0, column = 0, columnspan =3, pady = 40)
        
        self.Login_Frame_1 = LabelFrame(self.Frame, width = 1350, height = 600, relief = 'ridge', bg = 'lightskyblue', bd = 15,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_1.grid(row = 1, column =0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width = 1000, height = 600, relief = 'ridge',bg = 'lightskyblue', bd = 15,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_2.grid(row = 2, column = 0)


        #===================================================LABEL and ENTRIES=======================================================================
        self.Label_Username = Label(self.Login_Frame_1, text = 'Username', font = ('arial',20,'bold'), bg = 'lightskyblue', bd = 20)
        self.Label_Username.grid(row = 0, column = 0)
        self.text_Username = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), textvariable = self.Username)
        self.text_Username.grid(row = 0, column = 1, padx = 50)                       
        
        self.Label_Password = Label(self.Login_Frame_1, text = 'Password', font = ('arial',20,'bold'), bg = 'lightskyblue', bd = 20)
        self.Label_Password.grid(row = 1, column = 0)
        self.text_Password = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), show = '*', textvariable = self.Password)
        self.text_Password.grid(row = 1, column = 1) 
        
        
        #=============================================================BUTTONS=======================================================================
        self.btnLogin = Button(self.Login_Frame_2, text = 'Login', width = 10, font = ('airia',15,'bold'), command = self.Login)
        self.btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

        self.btnReset = Button(self.Login_Frame_2, text = 'Reset', width = 10, font = ('airia',15,'bold'), command = self.Reset)
        self.btnReset.grid(row = 3, column = 1, padx = 8, pady = 20)

        self.btnExit = Button(self.Login_Frame_2, text = 'Exit', width = 10, font = ('airia',15,'bold'), command = self.Exit)
        self.btnExit.grid(row = 3, column = 2, padx = 8, pady = 20)


        #======================================================Code for Login Button==================================================================
    def Login(self):
        u = (self.Username.get())
        p = (self.Password.get())

        if (u == str('Prashant') and p == str(12345678)):
            self.__menu__()
        else:
            tkinter.messagebox.askyesno("Login","Error : Wrong Password")
            self.Username.set("")
            self.Password.set("")
            #self.text_Username.focus()

        
        #======================================================Code for Reset Button==================================================================
    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.text_Username.focus()


        #======================================================Code for Exit Button==================================================================

    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()
            return

    def __menu__(self):
        filename = 'Menu.py'
        os.system(filename)
        os.system('notepad'+filename)

    '''def new_window(self):
        self.new_Window = Toplevel(self.master)
        self.app = Window_2(self.new_Window)'''

class Window_2:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Main Menu")
        self.master.geometry('1350x750')
        self.master.config(bg = 'sky blue')
        self.Frame = Frame(self.master, bg = 'lightskyblue')
        self.Frame.pack()

    

if __name__ == '__main__':                                    # https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
    main()


from tkinter import*
import sqlite3

def connect():
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS Marks (id INTEGER PRIMARY KEY, name text, roll integer, fname text, mname \
                     text, DOB integer, gender text, scl text, email text, m1 integer, m2 integer, m3 integer, m4 integer, \
                     m5 integer, gt integer, per integer, cgpa integer, grade text, div text, result text)')

       con.commit()
       con.close()

def insert(name = ' ',roll = ' ',fname = ' ',mname = ' ',DOB = ' ',gender = ' ',scl = ' ',email = ' ',m1 = ' ',m2 = ' ', \
       m3 = ' ',m4 = ' ',m5 = ' ',gt = ' ',per = ' ',cgpa = ' ',grade = ' ', div = ' ', result = ' '):
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('INSERT INTO Marks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(name,roll,fname,mname,DOB,gender, \
                                                                                    scl,email,m1,m2,m3,m4,m5,gt,per,\
                                                                                    cgpa,grade,div,result))

       con.commit()
       con.close()

'''def view():
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM Marks')

       con.commit()
       con.close()

def delete(id):
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('DELETE FROM Marks WHERE id = ?)',(id,))

       con.commit()
       con.close()'''

def update(id,name = ' ',roll = ' ',fname = ' ',mname = ' ',DOB = ' ',gender = ' ',scl = ' ',email = ' ',m1 = ' ',m2 = ' ', \
       m3 = ' ',m4 = ' ',m5 = ' ',gt = ' ',per = ' ',cgpa = ' ',grade = ' ', div = ' ', result = ' '):
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('UPDATE Marks SET name = ? OR roll = ? OR fname =  ? OR mname = ? OR DOB = ? OR gender = ? OR \
                     scl = ? OR email = ? OR m1 = ? OR m2 = ? OR  m3 = ? OR m4 = ? OR m5 = ? OR gt = ? OR per = ? OR \
                     cgpa = ? OR grade = ? OR div = ? OR result = ?',(name,roll,fname,mname,DOB,gender,scl,email,m1,m2,m3, \
                                                                      m4,m5,gt,per,cgpa,grade))

       con.commit()
       con.close()

def search(roll):
       con = sqlite3.connect('Marks.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM Marks WHERE roll = ?',(roll,))
       row = cur.fetchall()
       return row

connect()

from tkinter import *
import random
import Marksheet_Backend
import tkinter.messagebox
from tkinter import ttk

def marksheet():
       root = Tk()
       root.title('Marksheet')
       root.geometry('1350x750')
       root.config(bg = 'Navajo white')

       #================================================Variables======================================================
       name = StringVar()
       roll = StringVar()
       fname = StringVar()
       mname = StringVar()
       DOB = StringVar()
       gender = StringVar()
       scl = StringVar()
       email = StringVar()
       m1 = DoubleVar()
       m2 = DoubleVar()
       m3 = DoubleVar()
       m4 = DoubleVar()
       m5 = DoubleVar()
       gt = DoubleVar()
       per = DoubleVar()
       cgpa = DoubleVar()
       grade = StringVar()
       div = StringVar()
       result = StringVar()


       #==============================================Functions==========================================================
       def Add():
              if (len(roll.get()) != 0):
                     Marksheet_Backend.insert(name.get(),roll.get(),fname.get(),mname.get(),DOB.get(),gender.get(), \
                                          scl.get(),email.get(),m1.get(),m2.get(),m3.get(),m4.get(),m5.get(), \
                                          gt.get(),per.get(),cgpa.get(),grade.get(),div.get(),result.get())

       def Update():
              if (len(roll.get()) != 0):
                     Marksheet_Backend.update(name.get(),roll.get(),fname.get(),mname.get(),DOB.get(),gender.get(), \
                                          scl.get(),email.get(),m1.get(),m2.get(),m3.get(),m4.get(),m5.get(), \
                                          gt.get(),per.get(),cgpa.get(),grade.get(),div.get(),result.get())
       
       def Exit():
              Exit = tkinter.messagebox.askyesno('Marksheet','Confirm if you want to Exit')
              if Exit > 0:
                     root.destroy()
                     return

       
       def Compute():
              x1 = (m1.get());      x2 = (m2.get());    x3 = (m3.get());      x4 = (m4.get());    x5 = (m5.get())

              if x1 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x2 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x3 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x4 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x5 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
                     
       
              tot = x1+x2+x3+x4+x5
              gt.set(tot)
              
              Per = ((x1+x2+x3+x4+x5) * 100)/500
              per.set(Per)


              cg = (((x1+x2+x3+x4+x5) * 100)/500) / 9.5
              cgpa.set(round(cg,1))

              if cg > 10:
                     cgpa.set(10)


              if (((x1+x2+x3+x4+x5) * 100)/500) <= 40:
                     grd = 'G'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 50:
                     grd = 'F'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 60:
                     grd = 'E'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 70:
                     grd = 'D'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 80:
                     grd = 'C'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 90:
                     grd = 'B'
              else:
                     grd = 'A'

              grade.set(grd)

              count = 0
              if x1 < 33:
                     count = count + 1
              if x2 < 33:
                     count = count + 1
              if x3 < 33:
                     count = count + 1
              if x4 < 33:
                     count = count + 1
              if x5 < 33:
                     count = count + 1

              if (count == 0):
                     result.set('PASS')
              elif (count == 1 or count == 2 ):
                     result.set('SUPPLY')
              else:
                     result.set('FAIL')

              if Per <= 45 and result != "FAIL":
                     div.set('THIRD')
              elif Per <= 60 and result != "FAIL":
                     div.set('SECOND')
              elif Per <= 100:
                     div.set('FIRST')

       def Reset():
              name.set(' ')
              roll.set(' ')
              fname.set(' ')
              mname.set(' ')
              DOB.set(' ')
              gender.set(' ')
              scl.set(' ')
              email.set(' ')
              m1.set(' ')
              m2.set(' ')
              m3.set(' ')
              m4.set(' ')
              m5.set(' ')
              gt.set(' ')
              per.set(' ')
              cgpa.set(' ')
              grade.set(' ')
              div.set(' ')
              result.set(' ')  
       

       #========================================================Frame_1===============================================================
       
       Frame_1 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'Navajo white', bd = 10, \
                            text = 'Student Details', relief = 'ridge')
       Frame_1.grid(row = 1, column = 0, pady = 20, padx = 20)


       #=================================================Labels and Entries for Frame_1===============================================
       Label_Name = Label(Frame_1, text = 'Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Name.grid(row = 0, column = 0, padx = 80)
       Entry_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = name)
       Entry_Name.grid(row = 0, column = 1, padx = 5, pady = 5)

       Label_Roll_no = Label(Frame_1, text = 'Roll Number', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Roll_no.grid(row = 0, column = 3, padx = 80)
       Entry_Roll_no = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = roll)
       Entry_Roll_no.grid(row = 0, column = 4, padx = 40)

       Label_Father_Name = Label(Frame_1, text = 'Father Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Father_Name.grid(row = 1, column = 0, padx = 80)
       Entry_Father_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = fname)
       Entry_Father_Name.grid(row = 1, column = 1, padx = 5, pady = 10)

       Label_Mother_Name = Label(Frame_1, text = 'Mother Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Mother_Name.grid(row = 1, column = 3, padx = 80)
       Entry_Mother_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = mname)
       Entry_Mother_Name.grid(row = 1, column = 4, padx = 5)

       Label_DOB = Label(Frame_1, text = 'Date of Birth', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_DOB.grid(row = 2, column = 0, padx = 80)
       Entry_DOB = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = DOB)
       Entry_DOB.grid(row = 2, column = 1, padx = 5, pady = 5)

       Label_Gender = Label(Frame_1, text = 'Gender', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Gender.grid(row = 2, column = 3, padx = 80)
       Entry_Gender = ttk.Combobox(Frame_1, values = (' ','Male','Female','Others'), font = ('arial',15), width = 23, textvariable = gender)
       Entry_Gender.grid(row = 2, column = 4, padx = 5, pady = 5)


       Label_School = Label(Frame_1, text = 'School Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_School.grid(row = 3, column = 0, padx = 80)
       Entry_School = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = scl)
       Entry_School.grid(row = 3, column = 1, padx = 5, pady = 5)

       Label_Email = Label(Frame_1, text = 'Email ID', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Email.grid(row = 3, column = 3, padx = 80)
       Entry_Email = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = email)
       Entry_Email.grid(row = 3, column = 4, padx = 5, pady = 5)



       #========================================================Frame_2==================================================================       
       Frame_2 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'Navajo white', bd = 10 \
                            , text = 'Grades Point Obtained', relief = 'ridge')
       Frame_2.grid(row = 3, column = 0)



       #======================================================Labels of Frame_2===========================================================

       Label_Subject = Label(Frame_2, text = 'SUBJECT', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_Subject.grid(row = 3, column = 0, padx = 50, pady = 10)

       Label_obt_Marks = Label(Frame_2, text = 'MARKS OBTAINED', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_obt_Marks.grid(row = 3, column = 1, padx = 20)

       Label_Subject = Label(Frame_2, text = 'PASSING MARKS', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_Subject.grid(row = 3, column = 2, padx = 20)

       Label_obt_Marks = Label(Frame_2, text = 'TOTAL MARKS', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_obt_Marks.grid(row = 3, column = 3, padx = 20)

       Label_1 = Label(Frame_2, text = 'MATHEMATICS', font = ('arial',14), bg = 'Navajo white')
       Label_1.grid(row = 4, column = 0)
       Label_2 = Label(Frame_2, text = 'PHYSICS', font = ('arial',14), bg = 'Navajo white')
       Label_2.grid(row = 5, column = 0)
       Label_3 = Label(Frame_2, text = 'CHEMISTRY', font = ('arial',14), bg = 'Navajo white')
       Label_3.grid(row = 6, column = 0)
       Label_4 = Label(Frame_2, text = 'HINDI', font = ('arial',14), bg = 'Navajo white')
       Label_4.grid(row = 7, column = 0)
       Label_5 = Label(Frame_2, text = 'ENGLISH', font = ('arial',14), bg = 'Navajo white')
       Label_5.grid(row = 8, column = 0)
       Label_6 = Label(Frame_2, text = 'GRAND TOTAL', font = ('arial',16), bg = 'Navajo white')
       Label_6.grid(row = 9, column = 0)
       Label_7 = Label(Frame_2, text = 'PERCENTAGE', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_7.grid(row = 10, column = 0)
       Label_8 = Label(Frame_2, text = 'CGPA', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_8.grid(row = 10, column = 2)
       Label_9 = Label(Frame_2, text = 'GRADE', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_9.grid(row = 10, column = 4)
       Label_10 = Label(Frame_2, text = 'DIVISION', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_10.grid(row = 11, column = 0)
       Label_10 = Label(Frame_2, text = 'RESULT', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_10.grid(row = 11, column = 2)
       
       #======================================================Entries of Frame_2===========================================================
       var_1 = StringVar(Frame_2, value = '33')
       var_2 = StringVar(Frame_2, value = '100')
       var_3 = StringVar(Frame_2, value = '500')

       Entry__1 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m1)
       Entry__1.grid(row = 4, column = 1)
       Entry__2 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m2)
       Entry__2.grid(row = 5, column = 1)
       Entry__3 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m3)
       Entry__3.grid(row = 6, column = 1)
       Entry__4 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m4)
       Entry__4.grid(row = 7, column = 1)
       Entry__5 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m5)
       Entry__5.grid(row = 8, column = 1)
       Entry__6 = Entry(Frame_2, font = ('arial',14), width = 5, textvariable = gt, state = 'readonly')
       Entry__6.grid(row = 9, column = 1, pady = 8)
       Entry__7 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = per, state = 'readonly')
       Entry__7.grid(row = 10, column = 1, pady = 8)
       Entry__8 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = cgpa, state = 'readonly')
       Entry__8.grid(row = 10, column = 3, pady = 8)
       Entry__9 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = grade, state = 'readonly')
       Entry__9.grid(row = 10, column = 5, padx = 20, pady = 8)
       Entry__10 = Entry(Frame_2, font = ('arial',14,'bold'), width = 8, textvariable = div, state = 'readonly')
       Entry__10.grid(row = 11, column = 1, padx = 20, pady = 8)
       Entry__11 = Entry(Frame_2, font = ('arial',14,'bold'), width = 7, textvariable = result, state = 'readonly')
       Entry__11.grid(row = 11, column = 3, padx = 20, pady = 8)
       
       Entry_1_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_1_2.grid(row = 4, column = 2, pady = 5)
       Entry_1_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_1_3.grid(row = 4, column = 3)
       Entry_2_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_2_2.grid(row = 5, column = 2, pady = 5)
       Entry_2_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_2_3.grid(row = 5, column = 3)
       Entry_3_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_3_2.grid(row = 6, column = 2, pady = 5)
       Entry_3_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_3_3.grid(row = 6, column = 3)
       Entry_4_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_4_2.grid(row = 7, column = 2, pady = 5)
       Entry_4_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_4_3.grid(row = 7, column = 3)
       Entry_5_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_5_2.grid(row = 8, column = 2, pady = 5)
       Entry_5_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_5_3.grid(row = 8, column = 3)
       Entry_6_3 = Entry(Frame_2, textvariable = var_3, font = ('arial',16), width = 5, state = 'readonly')
       Entry_6_3.grid(row = 9, column = 3)
       


       #======================================================Buttons===========================================================
       Btn_Compute = Button(Frame_2, text = 'COMPUTE', font = ('arial',12,'bold'), width = 10, command = Compute)
       Btn_Compute.grid(row = 4, column = 4, padx = 50, pady = 6)
       Btn_Save = Button(Frame_2, text = 'SAVE', font = ('arial',12,'bold'), width = 10, command = Add)
       Btn_Save.grid(row = 5, column = 4, padx = 50, pady = 6)
       Btn_Update = Button(Frame_2, text = 'UPDATE', font = ('arial',12,'bold'), width = 10, command = Update)
       Btn_Update.grid(row = 6, column = 4, padx = 50, pady = 6)
       Btn_Cancel = Button(Frame_2, text = 'RESET', font = ('arial',12,'bold'), width = 10, command = Reset)
       Btn_Cancel.grid(row = 7, column = 4, padx = 50, pady = 6)
       Btn_Exit = Button(Frame_2, text = 'EXIT', font = ('arial',12,'bold'), width = 10, command = Exit)
       Btn_Exit.grid(row = 8, column = 4, padx = 50, pady = 6)


       root.mainloop()


def search_result_marksheet(row):
       root = Tk()
       root.title('Marksheet')
       root.geometry('1350x750')
       root.config(bg = 'Navajo white')

       
       #==============================================Functions==========================================================             
       
       def Compute():
              x1 = (m1.get());      x2 = (m2.get());    x3 = (m3.get());      x4 = (m4.get());    x5 = (m5.get())                                   
       
              tot = x1+x2+x3+x4+x5
              gt.set(tot)
              
              Per = ((x1+x2+x3+x4+x5) * 100)/500
              per.set(Per)


              cg = (((x1+x2+x3+x4+x5) * 100)/500) / 9.5
              cgpa.set(round(cg,1))


              if (((x1+x2+x3+x4+x5) * 100)/500) <= 40:
                     grd = 'G'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 50:
                     grd = 'F'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 60:
                     grd = 'E'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 70:
                     grd = 'D'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 80:
                     grd = 'C'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 90:
                     grd = 'B'
              else:
                     grd = 'A'

              grade.set(grd)

              count = 0
              if x1 < 33:
                     count = count + 1
              if x2 < 33:
                     count = count + 1
              if x3 < 33:
                     count = count + 1
              if x4 < 33:
                     count = count + 1
              if x5 < 33:
                     count = count + 1

              if (count == 0):
                     result.set('PASS')
              elif (count == 1 or count == 2 ):
                     result.set('SUPPLY')
              else:
                     result.set('FAIL')

              if Per <= 45 and result != "FAIL":
                     div.set('THIRD')
              elif Per <= 60 and result != "FAIL":
                     div.set('SECOND')
              elif Per <= 100:
                     div.set('FIRST')     

       
       

       #========================================================Frame_1===============================================================
       
       Frame_1 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'Navajo white', bd = 10, \
                            text = 'Student Details', relief = 'ridge')
       Frame_1.grid(row = 1, column = 0, pady = 20, padx = 20)

       name = StringVar(Frame_1,value=row[0][1])
       roll = StringVar(Frame_1,value=row[0][2])
       fname = StringVar(Frame_1,value=row[0][3])
       mname = StringVar(Frame_1,value=row[0][4])
       DOB = StringVar(Frame_1,value=row[0][5])
       gender = StringVar(Frame_1,value=row[0][6])
       scl = StringVar(Frame_1,value=row[0][7])
       email = StringVar(Frame_1,value=row[0][8])
       


       #=================================================Labels and Entries for Frame_1===============================================
       Label_Name = Label(Frame_1, text = 'Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Name.grid(row = 0, column = 0, padx = 80)
       Entry_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = name)
       Entry_Name.grid(row = 0, column = 1, padx = 5, pady = 5)

       Label_Roll_no = Label(Frame_1, text = 'Roll Number', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Roll_no.grid(row = 0, column = 3, padx = 80)
       Entry_Roll_no = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = roll)
       Entry_Roll_no.grid(row = 0, column = 4, padx = 40)

       Label_Father_Name = Label(Frame_1, text = 'Father Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Father_Name.grid(row = 1, column = 0, padx = 80)
       Entry_Father_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = fname)
       Entry_Father_Name.grid(row = 1, column = 1, padx = 5, pady = 10)

       Label_Mother_Name = Label(Frame_1, text = 'Mother Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Mother_Name.grid(row = 1, column = 3, padx = 80)
       Entry_Mother_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = mname)
       Entry_Mother_Name.grid(row = 1, column = 4, padx = 5)

       Label_DOB = Label(Frame_1, text = 'Date of Birth', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_DOB.grid(row = 2, column = 0, padx = 80)
       Entry_DOB = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = DOB)
       Entry_DOB.grid(row = 2, column = 1, padx = 5, pady = 5)

       Label_Gender = Label(Frame_1, text = 'Gender', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Gender.grid(row = 2, column = 3, padx = 80)
       Entry_Gender = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = gender)
       Entry_Gender.grid(row = 2, column = 4, padx = 5, pady = 5)


       Label_School = Label(Frame_1, text = 'School Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_School.grid(row = 3, column = 0, padx = 80)
       Entry_School = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = scl)
       Entry_School.grid(row = 3, column = 1, padx = 5, pady = 5)

       Label_Email = Label(Frame_1, text = 'Email ID', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Email.grid(row = 3, column = 3, padx = 80)
       Entry_Email = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = email)
       Entry_Email.grid(row = 3, column = 4, padx = 5, pady = 5)



       #========================================================Frame_2==================================================================       
       Frame_2 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'Navajo white', bd = 10 \
                            , text = 'Grades Point Obtained', relief = 'ridge')
       Frame_2.grid(row = 3, column = 0)

       m1 = DoubleVar(Frame_2,row[0][9])
       m2 = DoubleVar(Frame_2,row[0][10])
       m3 = DoubleVar(Frame_2,row[0][11])
       m4 = DoubleVar(Frame_2,row[0][12])
       m5 = DoubleVar(Frame_2,row[0][13])
       gt = DoubleVar(Frame_2,row[0][14])
       per = DoubleVar(Frame_2,row[0][15])
       cgpa = DoubleVar(Frame_2,row[0][16])
       grade = StringVar(Frame_2,row[0][17])
       div = StringVar(Frame_2,row[0][18])
       result = StringVar(Frame_2,row[0][19])

       #======================================================Labels of Frame_2===========================================================

       Label_Subject = Label(Frame_2, text = 'SUBJECT', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_Subject.grid(row = 3, column = 0, padx = 50, pady = 10)

       Label_obt_Marks = Label(Frame_2, text = 'MARKS OBTAINED', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_obt_Marks.grid(row = 3, column = 1, padx = 20)

       Label_Subject = Label(Frame_2, text = 'PASSING MARKS', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_Subject.grid(row = 3, column = 2, padx = 20)

       Label_obt_Marks = Label(Frame_2, text = 'TOTAL MARKS', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_obt_Marks.grid(row = 3, column = 3, padx = 20)

       Label_1 = Label(Frame_2, text = 'MATHEMATICS', font = ('arial',14), bg = 'Navajo white')
       Label_1.grid(row = 4, column = 0)
       Label_2 = Label(Frame_2, text = 'PHYSICS', font = ('arial',14), bg = 'Navajo white')
       Label_2.grid(row = 5, column = 0)
       Label_3 = Label(Frame_2, text = 'CHEMISTRY', font = ('arial',14), bg = 'Navajo white')
       Label_3.grid(row = 6, column = 0)
       Label_4 = Label(Frame_2, text = 'HINDI', font = ('arial',14), bg = 'Navajo white')
       Label_4.grid(row = 7, column = 0)
       Label_5 = Label(Frame_2, text = 'ENGLISH', font = ('arial',14), bg = 'Navajo white')
       Label_5.grid(row = 8, column = 0)
       Label_6 = Label(Frame_2, text = 'GRAND TOTAL', font = ('arial',16), bg = 'Navajo white')
       Label_6.grid(row = 9, column = 0)
       Label_7 = Label(Frame_2, text = 'PERCENTAGE', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_7.grid(row = 10, column = 0)
       Label_8 = Label(Frame_2, text = 'CGPA', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_8.grid(row = 10, column = 2)
       Label_9 = Label(Frame_2, text = 'GRADE', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_9.grid(row = 10, column = 4)
       Label_10 = Label(Frame_2, text = 'DIVISION', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_10.grid(row = 11, column = 0)
       Label_10 = Label(Frame_2, text = 'RESULT', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_10.grid(row = 11, column = 2)
       
       #======================================================Entries of Frame_2===========================================================
       var_1 = StringVar(Frame_2, value = '33')
       var_2 = StringVar(Frame_2, value = '100')
       var_3 = StringVar(Frame_2, value = '500')

       Entry__1 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m1)
       Entry__1.grid(row = 4, column = 1)
       Entry__2 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m2)
       Entry__2.grid(row = 5, column = 1)
       Entry__3 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m3)
       Entry__3.grid(row = 6, column = 1)
       Entry__4 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m4)
       Entry__4.grid(row = 7, column = 1)
       Entry__5 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = m5)
       Entry__5.grid(row = 8, column = 1)
       Entry__6 = Entry(Frame_2, font = ('arial',14), width = 5, textvariable = gt)
       Entry__6.grid(row = 9, column = 1, pady = 8)
       Entry__7 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = per)
       Entry__7.grid(row = 10, column = 1, pady = 8)
       Entry__8 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = cgpa)
       Entry__8.grid(row = 10, column = 3, pady = 8)
       Entry__9 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = grade)
       Entry__9.grid(row = 10, column = 5, padx = 20, pady = 8)
       Entry__10 = Entry(Frame_2, font = ('arial',14,'bold'), width = 8, textvariable = div)
       Entry__10.grid(row = 11, column = 1, padx = 20, pady = 8)
       Entry__11 = Entry(Frame_2, font = ('arial',14,'bold'), width = 7, textvariable = result)
       Entry__11.grid(row = 11, column = 3, padx = 20, pady = 8)
       
       Entry_1_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5)
       Entry_1_2.grid(row = 4, column = 2, pady = 5)
       Entry_1_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5)
       Entry_1_3.grid(row = 4, column = 3)
       Entry_2_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5)
       Entry_2_2.grid(row = 5, column = 2, pady = 5)
       Entry_2_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5)
       Entry_2_3.grid(row = 5, column = 3)
       Entry_3_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5)
       Entry_3_2.grid(row = 6, column = 2, pady = 5)
       Entry_3_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5)
       Entry_3_3.grid(row = 6, column = 3)
       Entry_4_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5)
       Entry_4_2.grid(row = 7, column = 2, pady = 5)
       Entry_4_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5)
       Entry_4_3.grid(row = 7, column = 3)
       Entry_5_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5)
       Entry_5_2.grid(row = 8, column = 2, pady = 5)
       Entry_5_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5)
       Entry_5_3.grid(row = 8, column = 3)
       Entry_6_3 = Entry(Frame_2, textvariable = var_3, font = ('arial',16), width = 5)
       Entry_6_3.grid(row = 9, column = 3)
              


       #======================================================Buttons===========================================================
       
       Btn_Exit = Button(Frame_2, text = 'EXIT', font = ('arial',12,'bold'), width = 10, command = root.destroy)
       Btn_Exit.grid(row = 8, column = 4, padx = 50, pady = 6)

       
       root.mainloop()

if __name__ == '__main__':
       marksheet()
from tkinter import*
import random
import os

def __marksheet__():
       filename = 'Search_Page.py'
       os.system(filename)
       os.system('notepad'+filename)

def __Library__():
       filename = 'Library_Frontend.py'
       os.system(filename)
       os.system('notepad'+filename)

def __information__():
       filename = 'Std_info_FrontEnd.py'
       os.system(filename)
       os.system('notepad'+filename)

def __FeeReport__():
       filename = 'Fee_Frontend.py'
       os.system(filename)
       os.system('notepad'+filename)
       
       
def menu():
       root = Tk()
       root.title('Menu')
       root.geometry('1350x750')
       root.config(bg = 'navajo white')
       
       title_Frame = LabelFrame(root, font = ('arial',50,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'raise', bd = 13)
       title_Frame.grid(row = 0, column = 0, pady = 50)
       
       title_Label = Label(title_Frame, text = 'MENU', font = ('arial',30,'bold'), bg = 'navajo white')
       title_Label.grid(row = 0, column = 0, padx = 150)


       #========================================================FRAMES===================================================================
       Frame_1 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
       Frame_1.grid(row = 1, column = 0, padx = 280)
       Frame_2 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
       Frame_2.grid(row = 2, column = 0, padx = 130, pady = 7)
       Frame_3 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
       Frame_3.grid(row = 3, column = 0, pady = 7)
       Frame_4 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
       Frame_4.grid(row = 4, column = 0, pady = 7)
       


       #========================================================LABELS===================================================================
       Label_1 = Label(Frame_1, text = 'STUDENT PROFILE', font = ('arial',25,'bold'), bg = 'navajo white')
       Label_1.grid(row = 0, column = 0, padx = 50, pady = 5)
       Label_2 = Label(Frame_2, text = 'FEE REPORT', font = ('arial',25,'bold'), bg = 'navajo white')
       Label_2.grid(row = 0, column = 0, padx = 100, pady = 5)
       Label_3 = Label(Frame_3, text = 'LIBRARY SYSTEM', font = ('arial',25,'bold'), bg = 'navajo white')
       Label_3.grid(row = 0, column = 0, padx = 60, pady = 5)
       Label_4 = Label(Frame_4, text = 'MARKSHEET', font = ('arial',25,'bold'), bg = 'navajo white')
       Label_4.grid(row = 0, column = 0, padx = 101, pady = 5)
       


       #========================================================BUTTONS===================================================================
       Button_1 = Button(Frame_1, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __information__)
       Button_1.grid(row = 0, column = 3, padx = 50)
       Button_2 = Button(Frame_2, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __FeeReport__)
       Button_2.grid(row = 0, column = 3, padx = 50)
       Button_3 = Button(Frame_3, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __Library__)
       Button_3.grid(row = 0, column = 3, padx = 50)
       Button_4 = Button(Frame_4, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __marksheet__)
       Button_4.grid(row = 0, column = 3, padx = 50)
       
       

       root.mainloop()


       
       
if __name__ == '__main__':
       menu()


from tkinter import *  
import random
import Marksheet_Backend
import Marksheet_Frontend
import tkinter.messagebox
import os

class Window_1():
       def __init__(self, master):
              self.master = master
              self.master.title('Search Page')
              self.master.geometry('1360x750')
              self.master.config(bg = 'navajowhite')

              self.roll = StringVar()
              frame = LabelFrame(self.master, width = 1000, height = 100, font = ('arial',30,'bold'), relief = 'ridge', bd = 15, bg = 'wheat')
              frame.grid(row = 1, column = 0, padx = 200, pady = 200)

              label = Label(frame, text = 'Enter Roll Number', font = ('arial',25,'bold'), bg = 'wheat' )
              label.grid(row = 0, column = 0, padx = 100, pady = 10)

              entry = Entry(frame, font = ('arial',25,'bold'), textvariable = self.roll)
              entry.grid(row = 0, column = 1, padx = 30, pady = 20)

              def Search():
                     if(len(self.roll.get()) != 0):
                            row = Marksheet_Backend.search(int(self.roll.get()))
                            print(row)
                            Marksheet_Frontend.search_result_marksheet(row)
                     else:
                            tkinter.messagebox.askokcancel('Attention','Please enter valid Roll No.')
                            return

              def new():
                     filename = 'Marksheet_Frontend.py'
                     os.system(filename)
                     os.system('notepad'+filename)
                     

              btnSearch = Button(frame, text = 'SEARCH', width = 15, font = ('arial',15,'bold'), command=Search)
              btnSearch.grid(row = 1, column = 0, padx = 50)
              btnNew = Button(frame, text = 'CREATE NEW', width = 15, font = ('arial',15,'bold'), command=new)
              btnNew.grid(row = 1, column = 1, padx = 50, pady = 20 )




root = Tk()
root.title("Login Form")
Window_1(root)
root.mainloop()


from tkinter import *  
import random
import Marksheet_Backend
import Marksheet_Frontend
import tkinter.messagebox
import os

class Window_1():
       def __init__(self, master):
              self.master = master
              self.master.title('Search Page')
              self.master.geometry('1360x750')
              self.master.config(bg = 'navajowhite')

              self.roll = StringVar()
              frame = LabelFrame(self.master, width = 1000, height = 100, font = ('arial',30,'bold'), relief = 'ridge', bd = 15, bg = 'wheat')
              frame.grid(row = 1, column = 0, padx = 200, pady = 200)

              label = Label(frame, text = 'Enter Roll Number', font = ('arial',25,'bold'), bg = 'wheat' )
              label.grid(row = 0, column = 0, padx = 100, pady = 10)

              entry = Entry(frame, font = ('arial',25,'bold'), textvariable = self.roll)
              entry.grid(row = 0, column = 1, padx = 30, pady = 20)

              def Search():
                     if(len(self.roll.get()) != 0):
                            row = Marksheet_Backend.search(int(self.roll.get()))
                            print(row)
                            Marksheet_Frontend.search_result_marksheet(row)
                     else:
                            tkinter.messagebox.askokcancel('Attention','Please enter valid Roll No.')
                            return

              def new():
                     filename = 'Marksheet_Frontend.py'
                     os.system(filename)
                     os.system('notepad'+filename)
                     

              btnSearch = Button(frame, text = 'SEARCH', width = 15, font = ('arial',15,'bold'), command=Search)
              btnSearch.grid(row = 1, column = 0, padx = 50)
              btnNew = Button(frame, text = 'CREATE NEW', width = 15, font = ('arial',15,'bold'), command=new)
              btnNew.grid(row = 1, column = 1, padx = 50, pady = 20 )




root = Tk()
root.title("Login Form")
Window_1(root)
root.mainloop()


import sqlite3

def connect():
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name text, fname text, mname text, \
                     address text, mobno integer,email text, dob integer, gender text)")

       conn.commit()
       conn.close()

def insert(name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)", (name, fname, mname, address , mobno, email, dob, gender))

       conn.commit()
       conn.close()
                                                                      

def view():
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM student")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(id):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM student WHERE id = ?", (id,))

       conn.commit()
       conn.close()

def update(id,name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("UPDATE student SET name = ? OR fname = ? OR mname = ? OR address = ? OR mobno = ? OR email = ? OR dob = ? OR gender = ?", \
              (name, fname, mname, address , mobno, email, dob, gender))

       conn.commit()
       conn.close()

def search(name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " "):
       conn = sqlite3.connect("student.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM student WHERE name = ? OR fname = ? OR mname = ? OR address = ? OR mobno = ? OR email = ? OR dob = ? \
                     OR gender = ?", (name, fname, mname, address , mobno, email, dob, gender))
       rows = cur.fetchall()
       return rows
       
       conn.close()

                                                               
connect()
       


from tkinter import*
import tkinter.messagebox  
import random
import Std_info_BackEnd
from tkinter import ttk

class Std_info():
       def __init__(self, master):
              self.master = master
              self.master.title('Student Information')
              self.master.geometry('1350x750')
              self.master.config(bg = 'navajowhite')
              
              def information():
              #========================================================Variables=====================================================================
                     self.name = StringVar()
                     self.fname = StringVar()
                     self.mname = StringVar()
                     self.address = StringVar()
                     self.mobno = StringVar()
                     self.email = StringVar()
                     self.dob = StringVar()
                     self.gender = StringVar()
                     


              #==========================================================Functions====================================================================
                     def StudentRec(event):
                            try: 
                                   global selected_tuple
                                   
                                   index = self.listbox.curselection()[0]
                                   selected_tuple = self.listbox.get(index)

                                   self.Entry_name.delete(0, END)
                                   self.Entry_name.insert(END, selected_tuple[1])
                                   self.Entry_fname.delete(0, END)
                                   self.Entry_fname.insert(END, selected_tuple[2])
                                   self.Entry_mname.delete(0, END)
                                   self.Entry_mname.insert(END, selected_tuple[3])
                                   self.Entry_address.delete(0, END)
                                   self.Entry_address.insert(END, selected_tuple[4])
                                   self.Entry_mobno.delete(0, END)
                                   self.Entry_mobno.insert(END, selected_tuple[5])
                                   self.Entry_emailID.delete(0, END)
                                   self.Entry_emailID.insert(END, selected_tuple[6])
                                   self.Entry_dob.delete(0, END)
                                   self.Entry_dob.insert(END, selected_tuple[7])
                                   self.Entry_gender.delete(0, END)
                                   self.Entry_gender.insert(END, selected_tuple[8])
                            except IndexError:
                                   pass


                     def Add():
                            if(len(self.name.get()) != 0):
                                   Std_info_BackEnd.insert(self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                                                 self.gender.get())
                                   self.listbox.delete(0, END)
                                   self.listbox.insert(END, (self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                                                 self.gender.get()))

                     def Display():
                                   self.listbox.delete(0, END)
                                   for row in Std_info_BackEnd.view():
                                          self.listbox.insert(END, row, str(' '))


                     def Exit():
                            Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
                            if Exit > 0:
                                   self.master.destroy()
                                   return
                            

                     def Reset():
                            self.name.set('')
                            self.fname.set('')
                            self.mname.set('')
                            self.address.set('')
                            self.mobno.set('')
                            self.email.set('')
                            self.dob.set('')
                            self.gender.set('')
                            self.listbox.delete(0, END)

                     

                     def Delete():
                            if(len(self.name.get()) != 0):
                                   Std_info_BackEnd.delete(selected_tuple[0])
                                   Reset()
                                   Display()


                     def Search():
                            self.listbox.delete(0, END)
                            for row in Std_info_BackEnd.search(self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(),self.gender.get()):
                                   self.listbox.insert(END, row, str(' '))
                                   

                     def Update():
                            if(len(self.name.get()) != 0):
                                   Std_info_BackEnd.delete(selected_tuple[0])
                            if(len(self.name.get()) != 0):
                                   Std_info_BackEnd.insert(self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                                                        self.gender.get())

                            self.listbox.delete(0, END)
                            self.listbox.insert(END, (self.name.get(), self.fname.get(), self.mname.get(), self.address.get(), self.mobno.get(), self.email.get(), self.dob.get(), \
                                                 self.gender.get()))
                     


                     #============================================================Frames=====================================================================

                     self.Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial',20,'bold'), \
                                                 bg = 'navajowhite',bd = 15, relief = 'ridge')
                     self.Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

                     self.Frame_1 = LabelFrame(self.Main_Frame, width = 600, height = 400, font = ('arial',15,'bold'), \
                                          relief = 'ridge', bd = 10, bg = 'navajowhite', text = 'STUDENT INFORMATION ')
                     self.Frame_1.grid(row = 1, column = 0, padx = 10)

                     self.Frame_2 = LabelFrame(self.Main_Frame, width = 750, height = 400, font = ('arial',15,'bold'), \
                                          relief = 'ridge', bd = 10, bg = 'navajowhite', text = 'STUDENT DATABASE')
                     self.Frame_2.grid(row = 1, column = 1, padx = 5)                  
                     
                     self.Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('arial',10,'bold'), \
                                          bg = 'navajowhite', relief = 'ridge', bd = 13)
                     self.Frame_3.grid(row = 2, column = 0, pady = 10)


                     
                     #========================================================Labels of Frame_1========================================================
                     self.Label_name = Label(self.Frame_1, text = 'Name', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_name.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
                     self.Label_fname = Label(self.Frame_1, text = 'Father Name', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_fname.grid(row = 1, column = 0, sticky = W, padx = 20)
                     self.Label_mname = Label(self.Frame_1, text = 'Mother Name', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_mname.grid(row = 2, column = 0, sticky = W, padx = 20)
                     self.Label_address = Label(self.Frame_1, text = 'Address', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_address.grid(row = 3, column = 0, sticky = W, padx = 20)
                     self.Label_mobno = Label(self.Frame_1, text = 'Mobile Number', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_mobno.grid(row = 4, column = 0, sticky = W, padx = 20)
                     self.Label_emailID = Label(self.Frame_1, text = 'Email ID', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_emailID.grid(row = 5, column = 0, sticky = W, padx = 20)
                     self.Label_dob = Label(self.Frame_1, text = 'Date of Birth', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_dob.grid(row = 6, column = 0, sticky = W, padx = 20)
                     self.Label_gender = Label(self.Frame_1, text = 'Gender', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_gender.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 10)


                     #========================================================Entries of Frame_1========================================================
                     self.Entry_name = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.name)
                     self.Entry_name.grid(row = 0, column = 1, padx = 10, pady = 5)
                     self.Entry_fname = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.fname)
                     self.Entry_fname.grid(row = 1, column = 1, padx = 10, pady = 5)
                     self.Entry_mname = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.mname)
                     self.Entry_mname.grid(row = 2, column = 1, padx = 10, pady = 5)
                     self.Entry_address = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.address)
                     self.Entry_address.grid(row = 3, column = 1, padx = 10, pady = 5)
                     self.Entry_mobno = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.mobno)
                     self.Entry_mobno.grid(row = 4, column = 1, padx = 10, pady = 5)
                     self.Entry_emailID = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.email)
                     self.Entry_emailID.grid(row = 5, column = 1, padx = 10, pady = 5)
                     self.Entry_dob = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.dob)
                     self.Entry_dob.grid(row = 6, column = 1, padx = 10, pady = 5)
                     self.Entry_gender = ttk.Combobox(self.Frame_1, values = (' ','Male','Female','Others'),\
                                                 font = ('arial',17,'bold'), textvariable = self.gender, width = 19)
                     self.Entry_gender.grid(row = 7, column = 1, padx = 10, pady = 5)




                     #========================================================Buttons of self.Frame_3=========================================================
                     self.btnSave = Button(self.Frame_3, text = 'SAVE', font = ('arial',17,'bold'), width = 8, command = Add)
                     self.btnSave.grid(row = 0, column = 0, padx = 10, pady = 10)
                     self.btnDisplay = Button(self.Frame_3, text = 'DISPLAY', font = ('arial',17,'bold'), width = 8, command = Display)
                     self.btnDisplay.grid(row = 0, column = 1, padx = 10, pady = 10)
                     self.btnReset = Button(self.Frame_3, text = 'RESET', font = ('arial',17,'bold'), width = 8, command = Reset)
                     self.btnReset.grid(row = 0, column = 2, padx = 10, pady = 10)
                     self.btnUpdate = Button(self.Frame_3, text = 'UPDATE', font = ('arial',17,'bold'), width = 8, command = Update)
                     self.btnUpdate.grid(row = 0, column = 3, padx = 10, pady = 10)
                     self.btnDelete = Button(self.Frame_3, text = 'DELETE', font = ('arial',17,'bold'), width = 8, command = Delete)
                     self.btnDelete.grid(row = 0, column = 4, padx = 10, pady = 10)
                     self.btnSearch = Button(self.Frame_3, text = 'SEARCH', font = ('arial',17,'bold'), width = 8, command = Search )
                     self.btnSearch.grid(row = 0, column = 5, padx = 10, pady = 10)
                     self.btnExit = Button(self.Frame_3, text = 'EXIT', font = ('arial',17,'bold'), width = 8, command = Exit)
                     self.btnExit.grid(row = 0, column = 6, padx = 10, pady = 10)



                     #===============================================List Box and self.scrollbar========================================================
                     self.scrollbar = Scrollbar(self.Frame_2)
                     self.scrollbar.grid(row = 0, column = 1, sticky = 'ns')

                     self.listbox = Listbox(self.Frame_2, width = 75, height = 20 , font = ('arial',12,'bold'))
                     self.listbox.bind('<<ListboxSelect>>', StudentRec)
                     self.listbox.grid(row = 0, column = 0)
                     self.scrollbar.config(command = self.listbox.yview)
                            
              information()
                     

root = Tk()
obj = Std_info(root)
root.mainloop()

from tkinter import Tk, ttk, filedialog, simpledialog
from tkinter.messagebox import askyesno, showinfo, WARNING


def main():
    root = Tk()
    root.title("Csv To Excel")
    root.geometry("300x150")

    def select_file():
        file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            entry_path.delete(0, "end")
            entry_path.insert(0, file_path)

    def convert_to_excel():
        file_path = entry_path.get()
        if file_path:
            if file_path.endswith(".csv"):
                save_path = filedialog.asksaveasfilename(title="Save as Excel file", defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
                if save_path:
                    # Convert CSV to Excel here
                    showinfo("Success", "File converted successfully!")
            else:
                showinfo("Error", "Please select a CSV file!")
        else:
            showinfo("Error", "Please select a file!")

    def quit_app():
        if askyesno("Quit", "Are you sure you want to quit?"):
            root.destroy()

    entry_path = ttk.Entry(root, width=50)
    entry_path.pack(pady=20)

    frame_buttons = ttk.Frame(root)
    frame_buttons.pack()

    button_browse = ttk.Button(frame_buttons, text="Browse", command=select_file)
    button_browse.pack(side="left", padx=10)

    button_convert = ttk.Button(frame_buttons, text="Convert to Excel", command=convert_to_excel)
    button_convert.pack(side="left", padx=10)

    button_quit = ttk.Button(frame_buttons, text="Quit", command=quit_app)
    button_quit.pack(side="left", padx=10)

    root.mainloop()


if __name__ == "__main__":
    main()