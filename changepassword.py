from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox

class ChangePasswordFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.style = Style()

        self.style.configure('TFrame', background='white')

        self.place(relx=.5,rely=.5,anchor=CENTER)

        self.old_password_label = Label(self,text="Old Password:")
        self.old_password_label.grid(row=0,column=0)

        self.old_password_entry = Entry(self,show='*')
        self.old_password_entry.grid(row=0,column=1)

        self.new_password_label = Label(self, text="New Password:")
        self.new_password_label.grid(row=1, column=0)

        self.new_password_entry = Entry(self,show='*')
        self.new_password_entry.grid(row=1, column=1)

        self.confirm_password_label = Label(self, text="Confirm Password:")
        self.confirm_password_label.grid(row=2, column=0)

        self.confirm_password_entry = Entry(self,show='*')
        self.confirm_password_entry.grid(row=2, column=1)

        self.change_password_button = Button(self,text="Change",
        command=self.change_password_button_click)
        self.change_password_button.grid(row=3,column=1)

    def change_password_button_click(self):
        con = connect('mycontacts.db')
        cur = con.cursor()
        cur.execute("select * from Login where Password = '{0}'".format(
            self.old_password_entry.get()
        ))
        row = cur.fetchone()
        if row is not None:
            new_password = self.new_password_entry.get()
            confirm_password = self.confirm_password_entry.get()
            if new_password == confirm_password:
                cur.execute("""update Login set Password = '{0}' 
                where Password = '{1}'
                """.format(
                    self.new_password_entry.get(),
                    self.old_password_entry.get()
                ))
                con.commit()
                messagebox.showinfo("Success Message",
                "Your password is changed successfully")
            else:
                messagebox.showerror("Error Message",
                "New and confirm password didn't match")
        else:
            messagebox.showerror("Error Message","Incorrect old password")