from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1100x600+100+50")
        #self.root.resizable(False, False)
        # ------Background Image---------
        self.bg = ImageTk.PhotoImage(file="bg4.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # ------Login Frame---------
        login_Frame = Frame(self.root, bg="#FF4500")
        login_Frame.place(x=400, y=200, height=380, width=330)
        self.username=StringVar()
        self.password=StringVar()

        self.title = Label(login_Frame, text="Login Here", font=("Century Schoolbook", 35, "bold"), fg="black",
                      bg="#FF4500").place(x=30, y=20)
        self.lbl_user = Label(login_Frame, text="Username:", font=("Century Schoolbook", 15, "bold"), fg="black",
                         bg="#FF4500").place(x=30, y=100)
        self.txt_email = Entry(login_Frame, font=("times new roman", 15), bg="white")
        self.txt_email.place(x=30, y=135, width=260, height=35)



        self.lbl_passwd = Label(login_Frame, text="Password:", font=("Century Schoolbook", 15, "bold"), fg="black",bg="#FF4500").place(x=30, y=190)
        self.passwd = Entry(login_Frame, font=("times new roman", 15), bg="white")
        self.passwd.place(x=30, y=225, width=260, height=35)

        self.signup_btn = Button(login_Frame, text="New User? SignUp",command=self.register_window, font=("helvetica", 15, "bold"), bg="#FF4500",
                            fg="black", bd=0).place(x=30, y=265)

        self.login_btn = Button(login_Frame, text="Login", font=("helvetica", 20, "bold"), bg="white", fg="#FF4500",command=self.login).place(x=110, y=310)

    def register_window(self):
        self.root.destroy()
        import signup

    def login(self):
        if self.txt_email.get()=="" or self.passwd.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="member")
                cur = con.cursor()
                cur.execute("select * from members where emailid=%s and password=%s", (self.txt_email.get(),self.passwd.get()))
                row = cur.fetchone()
                print(row)
                if row == None:
                    messagebox.showerror("Error", "NO SUCH USER EXISTS", parent=self.root)
                else:
                    #messagebox.showerror("Haryana Gym","Welcome to haryana gym",parent=self.root)
                    self.root.destroy()
                    import openingpage

                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)} ", parent=self.root)



root = Tk()
obj = Login(root)
root.mainloop()
