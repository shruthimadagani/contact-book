from tkinter import *
import tkinter.messagebox as mb
import sqlite3



connector = sqlite3.connect('conta.db')
cursor = connector.cursor()

cursor.execute(
"CREATE TABLE IF NOT EXISTS CONTACT_BOOK (S_NO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, EMAIL TEXT, PHONE_NUMBER TEXT,BIRTH TEXT, ADDRESS TEXT,PR TEXT,NOTE TEXT)"
)
class ContactManager:
    global name_strvar, email_strvar, phone_strvar, address_entry,listbox,search_strvar,search_entry
    def __init__(self,root):
        self.root = root
    #root=tk()
        # self.root.title("MINI PROJECT")
        # self.root.geometry('900x750')
        # self.root.resizable(0, 0)

        lf_bg = 'Gray70'  # Lightest Shade
        cf_bg = 'Gray57'
        rf_bg = 'Gray35'  # Darkest Shade

        self.root.title("MINI PROJECT")
        self.root.geometry('900x750')
        self.root.resizable(0, 0)
        frame_font = ("Garamond", 14)

        self.name_strvar = StringVar()
        self.phone_strvar = StringVar()
        self.email_strvar = StringVar()
        self.search_strvar= StringVar()
        self.birth_strvar=StringVar()
        self.pr_strvr=StringVar()

        Label(self.root, text='CONTACT BOOK', font=("Noto Sans CJK TC", 15, "bold"), bg='Black', fg='White').pack(side=TOP, fill=X)
        left_frame = Frame(self.root, bg=lf_bg)
        left_frame.place(relx=0, relheight=1, y=30, relwidth=0.3)
        center_frame = Frame(self.root, bg=cf_bg)
        center_frame.place(relx=0.3, relheight=1, y=30, relwidth=0.3)
        right_frame = Frame(self.root, bg=rf_bg)
        right_frame.place(relx=0.6, relwidth=0.4, relheight=1, y=30)

        Label(left_frame, text='Name', bg=lf_bg, font=frame_font).place(relx=0.1, rely=0.05)
        name_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=self.name_strvar)
        name_entry.place(relx=0.1, rely=0.09)
        Label(left_frame, text='Phone no.', bg=lf_bg, font=frame_font).place(relx=0.1, rely=0.15)
        phone_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=self.phone_strvar)
        phone_entry.place(relx=0.1, rely=0.19)
        Label(left_frame, text='DOB', bg=lf_bg, font=frame_font).place(relx=0.1, rely=0.25)
        birth_entry = Entry(left_frame, width=15, font=("Verdana", 11), textvariable=self.birth_strvar)
        birth_entry.place(relx=0.1, rely=0.29)
        Label(left_frame, text='Email', bg=lf_bg, font=frame_font).place(relx=0.1, rely=0.35)
        email_entry = Entry(left_frame, width=20, font=("Verdana", 11), textvariable=self.email_strvar)
        email_entry.place(relx=0.1, rely=0.39)
        Label(left_frame, text='Address', bg=lf_bg, font=frame_font).place(relx=0.1, rely=0.45)
        self.address_entry = Text(left_frame, width=20, font=("Verdana", 11), height=3)
        self.address_entry.place(relx=0.1, rely=0.49)
        Label(left_frame, text='Profession/Relation', bg=lf_bg, font=frame_font).place(relx=0.1, rely=0.60)
        pr_entry = Entry(left_frame, width=20, font=("Verdana", 11), textvariable=self.pr_strvr)
        pr_entry.place(relx=0.1, rely=0.64)
        Label(left_frame, text='Notes', bg=lf_bg, font=frame_font).place(relx=0.1, rely=0.70)
        self.n_entry = Text(left_frame, width=20, font=("Verdana", 11), height=5)
        self.n_entry.place(relx=0.1, rely=0.74)


        self.search_entry = Entry(center_frame, width=18, font=("Verdana", 12), textvariable=self.search_strvar).place(relx=0.08, rely=0.04)

        Button(center_frame, text='Search', font=frame_font, width=15, command=self.search).place(relx=0.13, rely=0.1)
        Button(center_frame, text='Add Record', font=frame_font, width=15, command=self.submit_record).place(relx=0.13, rely=0.2)
        Button(center_frame, text='View Record', font=frame_font, width=15, command=self.view_record).place(relx=0.13, rely=0.3)
        Button(center_frame, text='Clear Fields', font=frame_font, width=15, command=self.clear_fields).place(relx=0.13, rely=0.4)
        Button(center_frame, text='Delete Record', font=frame_font, width=15, command=self.delete_record).place(relx=0.13, rely=0.5)
        Button(center_frame, text='Delete All Records', font=frame_font, width=15, command=self.delete_all_records).place(relx=0.13, rely=0.6)

        Label(right_frame, text='Saved Contacts', font=("Noto Sans CJK TC", 14), bg=rf_bg).place(relx=0.25, rely=0.05)

        self.listbox = Listbox(right_frame, selectbackground='SkyBlue', bg='Gainsboro', font=('Helvetica', 12), height=20, width=25)
        scroller = Scrollbar(self.listbox, orient=VERTICAL, command=self.listbox.yview)
        scroller.place(relx=0.93, rely=0, relheight=1)
        self.listbox.config(yscrollcommand=scroller.set)
        self.listbox.place(relx=0.1, rely=0.15)

    def submit_record(self):
        global name_strvar, email_strvar, phone_strvar, address_entry,birth_strvar,pr_strvr,n_entry
        global cursor
        name, email, phone,birth, address,pr,n = self.name_strvar.get(), self.email_strvar.get(), self.phone_strvar.get(),self.birth_strvar.get(),self.address_entry.get(1.0, END),self.pr_strvr.get(),self.n_entry.get(1.0,END)

        if name=='' or email=='' or phone==''or birth=='' or address==''or pr==''or n=='':

        #if name=='' or email=='' or phone=='' or address=='':
            mb.showerror('Error!', "Please fill all the fields!")
        else:
            cursor.execute(
            "INSERT INTO CONTACT_BOOK (NAME, EMAIL, PHONE_NUMBER,BIRTH, ADDRESS,PR,NOTE) VALUES (?,?,?,?,?,?,?)", (name, email, phone,birth, address,pr,n))
            connector.commit()
            mb.showinfo('Contact added', 'We have stored the contact successfully!')
            self.listbox.delete(0, END)
            self.list_contacts()
            self.clear_fields()



    def list_contacts(self):
        curr = connector.execute('SELECT NAME FROM CONTACT_BOOK')
        fetch = curr.fetchall()

        for data in fetch:
            self.listbox.insert(END, data)

    def delete_record(self):
    #global listbox, connector, cursor

        if not self.listbox.get(ACTIVE):
            mb.showerror("No item selected", "You have not selected any item!")

        cursor.execute('DELETE FROM CONTACT_BOOK WHERE NAME = ?', (self.listbox.get(ACTIVE)))
        connector.commit()

        mb.showinfo('Contact deleted', 'The desired contact has been deleted')
        self.listbox.delete(0, END)
        self.list_contacts()
        
    def delete_all_records(self):
        cursor.execute('DELETE FROM CONTACT_BOOK')
        connector.commit()

        mb.showinfo("All records deleted", "All the records in your contact book have been deleted")

        self.listbox.delete(0, END)
        self.list_contacts()
        
    def view_record(self):
    #global name_strvar, phone_strvar, email_strvar, address_entry, listbox

        global name_strvar, phone_strvar, email_strvar, address_entry, listbox,pr_entry,n_entry

        curr = cursor.execute('SELECT * FROM CONTACT_BOOK WHERE NAME=?', self.listbox.get(ACTIVE))
        values = curr.fetchall()[0]

        self.name_strvar.set(values[1]);self. phone_strvar.set(values[3]);self.birth_strvar.set(values[4]); self.email_strvar.set(values[2]);self.pr_strvr.set(values[6])

        self.address_entry.delete(1.0, END)
        self.address_entry.insert(END, values[5])
        self.n_entry.delete(1.0,END)
        self.n_entry.insert(END,values[7])


    def clear_fields(self):
    #global name_strvar, phone_strvar, email_strvar, address_entry, listbox

        self.listbox.selection_clear(0, END)

        self.name_strvar.set('')
        self.phone_strvar.set('')
        self.email_strvar.set('')
        self.address_entry.delete(1.0, END)
        self.pr_strvr.set('')
        self.birth_strvar.set('')
        self.n_entry.delete(1.0,END)


    def search(self):
    #global search_strvar
        query = str(self.search_strvar.get())

        if query != '':
                self.listbox.delete(0, END)

        curr = connector.execute('SELECT * FROM CONTACT_BOOK WHERE NAME LIKE ?', ('%'+query+'%', ))
        check = curr.fetchall()

        for data in check:
                self.listbox.insert(END, data[1])


        

        
        

        




class Login:
    def __init__(self, nroot):
        # Initialize the class with the root window passed as an argument
        self.nroot = nroot
        # Set the title of the root window
        self.nroot.title("Contact Book Management System")
        self.nroot.geometry("300x150")
        # Create StringVar variables to store the username and password
        self.username = StringVar()
        self.password = StringVar()

        # Create a label and entry field for the username
        Label(self.nroot, text="Username:").grid(
            row=0, column=0, padx=10, pady=10)
        Entry(self.nroot, textvariable=self.username).grid(
            row=0, column=1, padx=10, pady=10)
        # Create a label and entry field for the password
        Label(self.nroot, text="Password:").grid(
            row=1, column=0, padx=10, pady=10)
        Entry(self.nroot, textvariable=self.password,
              show="*").grid(row=1, column=1, padx=10, pady=10)
        # Create a login button that calls the login method when clicked
        Button(self.nroot, text="Login", command=self.login).grid(
            row=2, column=1, padx=10, pady=10)

    def login(self):
        # Check if the entered username and password are correct
        # You can change the default username and passowrd here !
        if self.username.get() == "admin" and self.password.get() == "pass":
            # If the login is successful, destroy the current window and open a new window
            nroot.destroy()
            root=Tk()
            ContactManager(root)
        else:
            # If the login is unsuccessful, show an error message
            mb.showerror("Error", "Invalid username or password")
nroot = Tk()
obj = Login(nroot)
nroot.mainloop()











