from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("SignUp Page")
        self.root.geometry("1100x600+100+50")
        # ------Background Image---------
        self.bg = ImageTk.PhotoImage(file="s5.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # ------Login Frame---------
        login_Frame = Frame(self.root, bg="#FF4500")
        login_Frame.place(x=100, y=100, height=440, width=660)

        title = Label(login_Frame, text="SignUp Here", font=("Century Schoolbook", 30, "bold"), fg="black",
                      bg="#FF4500").place(x=140, y=40)

        # ---------Name--------------------
        lbl_fname = Label(login_Frame, text="First Name:", font=("Century Schoolbook", 15, "bold"), fg="black",
                          bg="#FF4500").place(x=30, y=100)
        self.txt_fname = Entry(login_Frame, font=("times new roman", 15), bg="white")
        self.txt_fname.place(x=30, y=125, width=260, height=35)

        lbl_lname = Label(login_Frame, text="Last Name:", font=("Century Schoolbook", 15, "bold"), fg="black",
                          bg="#FF4500").place(x=320, y=100)
        self.txt_lname = Entry(login_Frame, font=("times new roman", 15), bg="white")
        self.txt_lname.place(x=320, y=125, width=260, height=35)

        # -----------Username and Age----------------
        lbl_email = Label(login_Frame, text="Username/Email:", font=("Century Schoolbook", 15, "bold"), fg="black",
                          bg="#FF4500").place(x=30, y=175)
        self.txt_email = Entry(login_Frame, font=("times new roman", 15), bg="white")
        self.txt_email.place(x=30, y=200, width=260, height=35)

        lbl_age = Label(login_Frame, text="Age:", font=("Century Schoolbook", 15, "bold"), fg="black",
                        bg="#FF4500").place(x=320, y=175)
        self.txt_age = Entry(login_Frame, font=("times new roman", 15), bg="white")
        self.txt_age.place(x=320, y=200, width=260, height=35)

        # -------------Password------------------------------------------
        lbl_passwd = Label(login_Frame, text="Password:", font=("Century Schoolbook", 15, "bold"), fg="black",
                           bg="#FF4500").place(x=30, y=250)
        self.txt_passwd = Entry(login_Frame, font=("times new roman", 15), bg="white")
        self.txt_passwd.place(x=30, y=275, width=260, height=35)

        lbl_confirm = Label(login_Frame, text="Confirm:", font=("Century Schoolbook", 15, "bold"), fg="black",
                            bg="#FF4500").place(x=320, y=250)
        self.txt_confirm = Entry(login_Frame, font=("times new roman", 15), bg="white")
        self.txt_confirm.place(x=320, y=275, width=260, height=35)

        login_btn = Button(login_Frame, text="Already User? Login",command=self.login_window, font=("helvetica", 15, "bold"), bg="#FF4500",
                            fg="black", bd=0).place(x=30, y=310)

        signup_btn = Button(login_Frame, command=self.register_data, text="SignUp", font=("helvetica", 20, "bold"),
                           bg="white", fg="#FF4500").place(x=260, y=360)
    def login_window(self):
        self.root.destroy()
        import LOGIN 
                            

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_age.delete(0,END)
        self.txt_passwd.delete(0,END)
        self.txt_confirm.delete(0,END)


    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_email.get()=="" or  self.txt_age.get()=="" or self.txt_passwd.get()=="" or self.txt_confirm.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_passwd.get() != self.txt_confirm.get():
            messagebox.showerror("Error", "Passwords don't match", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="member")
                cur=con.cursor()
                cur.execute("select * from members where emailid=%s",self.txt_email.get())
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error", "User Already Exists,Please Try With Another Name", parent=self.root)
                else:
                    cur.execute("insert into members(fname,lname,emailid,age,password)values(%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_email.get(),
                                 self.txt_age.get(),
                                 self.txt_passwd.get()
                                 ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
                    self.root.destroy()
                    import openingpage  
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)} ", parent=self.root)









root = Tk()
obj = Login(root)
root.mainloop()