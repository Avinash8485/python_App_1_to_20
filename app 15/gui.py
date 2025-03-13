import tkinter as tk
from tkinter import messagebox
from main import WebAutomation



class App:
    def __init__(self,root):
        self.root = root
        self.root.title("Web Automation GUI")

        #login frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10,pady=10)

        tk.Label(self.login_frame,text ="user Name").grid(row=0,column=0,sticky='w')
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0,column=1,sticky='ew')

        tk.Label(self.login_frame,text ="Password").grid(row=1,column=0,sticky='w')
        self.entry_password = tk.Entry(self.login_frame,show="*")
        self.entry_password.grid(row=1,column=1,sticky='ew')

        #form frame 
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10,pady=10)

        tk.Label(self.form_frame,text ="Full Name").grid(row=0,column=0,sticky='w')
        self.entry_fullname = tk.Entry(self.form_frame)
        self.entry_fullname.grid(row=0,column=1,sticky='ew')

        tk.Label(self.form_frame,text ="Email").grid(row=1,column=0,sticky='w')
        self.entry_email = tk.Entry(self.form_frame)
        self.entry_email.grid(row=1,column=1,sticky='ew')

        tk.Label(self.form_frame,text ="Current Address").grid(row=2,column=0,sticky='w')
        self.entry_curaddress = tk.Entry(self.form_frame)
        self.entry_curaddress.grid(row=2,column=1,sticky='ew')

        tk.Label(self.form_frame,text ="Permanent Address").grid(row=3,column=0,sticky='w')
        self.entry_peraddress = tk.Entry(self.form_frame)
        self.entry_peraddress.grid(row=3,column=1,sticky='ew')

        #buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(padx=10,pady=10)

        tk.Button(self.buttons_frame,text="Submit",command=self.submit_data).grid(row=0,column=0,padx=5)
        tk.Button(self.buttons_frame,text="close",command=self.close).grid(row=0,column=1,padx=5)



    def submit_data(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        fullname = self.entry_fullname.get()
        email = self.entry_email.get()
        curaddress = self.entry_curaddress.get()
        peraddress = self.entry_peraddress.get()

        self.web = WebAutomation()
        self.web.login(username,password)
        self.web.locate(fullname,email,curaddress,peraddress)
        self.web.download()



    def close(self):
        self.web.close()
        messagebox.showinfo("Submitted sucessfully")




root = tk.Tk()
app = App(root)
root.mainloop()