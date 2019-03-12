from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import *
from tkinter import filedialog


class ManageContactsFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.style = Style()

        self.style.configure('TFrame', background='white')

        self.pack(fill=BOTH,expand=TRUE)

        self.create_view_all_contacts_frame()

    def create_view_all_contacts_frame(self):
        self.view_all_contacts_frame = Frame(self)
        self.view_all_contacts_frame.place(relx=.5,rely=.5,anchor=CENTER)

        self.style.configure('TButton',font=(NONE,15))

        self.add_new_contact_button = Button(self.view_all_contacts_frame,
        text="Add New Contact",width=15,command=self.create_add_new_contact_frame)
        self.add_new_contact_button.grid(row=0,column=1,pady=25,sticky=E)

        self.style.configure('TLabel',background='white',font=(NONE,15))

        self.name_label = Label(self.view_all_contacts_frame,text="Name:",width=10)
        self.name_label.grid(row=1,column=0,sticky=W)

        self.name_entry = Entry(self.view_all_contacts_frame,width=60,font=(NONE,15))
        self.name_entry.grid(row=1,column=1,sticky=W,pady=25)

        self.style.configure('Treeview.Heading',font=(NONE,15))
        self.style.configure('Treeview',font=(NONE,13))

        self.contacts_treeview = Treeview(self.view_all_contacts_frame,
        columns=('name','phone_number','email_id','city'),show='headings')
        self.contacts_treeview.grid(row=2,column=0,columnspan=2,pady=25)
        self.contacts_treeview.heading('name',text="Name",anchor=W)
        self.contacts_treeview.heading('phone_number',text="Phone Number",anchor=W)
        self.contacts_treeview.heading('email_id',text="Email Id",anchor=W)
        self.contacts_treeview.heading('city',text="City",anchor=W)

        self.contacts_treeview.insert("",END,values=('Rajeev Mehra','+91-9823114521','rajeev.mehra@gmail.com','Greater Noida'))
        self.contacts_treeview.insert("", END, values=(
        'Rajeev Mehra', '+91-9823114521', 'rajeev.mehra@gmail.com', 'Greater Noida'))
        self.contacts_treeview.insert("", END, values=(
        'Rajeev Mehra', '+91-9823114521', 'rajeev.mehra@gmail.com', 'Greater Noida'))
        self.contacts_treeview.insert("", END, values=(
        'Rajeev Mehra', '+91-9823114521', 'rajeev.mehra@gmail.com', 'Greater Noida'))
        self.contacts_treeview.insert("", END, values=(
        'Rajeev Mehra', '+91-9823114521', 'rajeev.mehra@gmail.com', 'Greater Noida'))

    def create_add_new_contact_frame(self):
        self.view_all_contacts_frame.destroy()
        self.add_new_contact_frame = Frame(self)
        self.add_new_contact_frame.place(relx=.5,rely=.5,anchor=CENTER)

        self.style.configure('TLabel',background='white',font=(NONE,15))

        self.name_label = Label(self.add_new_contact_frame,text="Name:")
        self.name_label.grid(row=0,column=0,pady=10)

        self.phone_number_label = Label(self.add_new_contact_frame, text="Phone Number:")
        self.phone_number_label.grid(row=1, column=0, pady=10)

        self.email_id_label = Label(self.add_new_contact_frame, text="Email Id:")
        self.email_id_label.grid(row=2, column=0, pady=10)

        self.city_label = Label(self.add_new_contact_frame, text="City:")
        self.city_label.grid(row=3, column=0, pady=10)

        self.profile_pic_label = Label(self.add_new_contact_frame, text="Profile Pic:")
        self.profile_pic_label.grid(row=4, column=0, pady=10)

        self.name_entry = Entry(self.add_new_contact_frame,font=(NONE,15))
        self.name_entry.grid(row=0,column=1)

        self.phone_number_entry = Entry(self.add_new_contact_frame, font=(NONE, 15))
        self.phone_number_entry.grid(row=1,column=1)

        self.email_id_entry = Entry(self.add_new_contact_frame, font=(NONE, 15))
        self.email_id_entry.grid(row=2,column=1)

        self.city_combobox = Combobox(self.add_new_contact_frame,font=(NONE,15),
        values=('Noida','Greater Noida','Delhi','Mumbai','Banglore'))
        self.city_combobox.grid(row=3,column=1)

        self.style.configure('TButton',font=(NONE,15),width=20)

        self.profile_pic_button = Button(self.add_new_contact_frame,
        text="Choose Your Profile Pic",command=self.profile_pic_button_click)
        self.profile_pic_button.grid(row=4,column=1)

        self.add_button = Button(self.add_new_contact_frame,text="Add")
        self.add_button.grid(row=5,column=1)

    def profile_pic_button_click(self):
        filedialog.askopenfilename()
