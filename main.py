from tkinter import *
import os

def main():
    root = Tk()
    LoginPage(root, 'Login or Register', '300x200')
    return None

class LoginPage:
    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        self.main_screen()


        self.root.mainloop()

    def delete1(self):
        self.root.destroy()

    def delete2(self):
        self.root2.destroy()

    def delete3(self):
        self.root3.destroy()
        Game()

    def delete4(self):
        self.root4.destroy()

    def delete5(self):
        self.root5.destroy()

    def main_screen(self):
        self.login_or_register = Label(text="Login or Register", bg="grey", width="300", height="2", font=("Calibre", 13)).pack()
        self.label = Label(text="").pack()
        self.login_button = Button(text="Login", height="2", width="30", command=self.login).pack()
        self.label2 = Label(text="").pack()
        self.register_button = Button(text="Register", height="2", width="30", command=self.register).pack()

    def register(self):
        self.master = Toplevel()
        self.root2 = self.master
        # APPLYING VARIABLES
        self.root2.title("Register")
        self.root2.geometry("300x250")


        self.username = StringVar()
        self.password = StringVar()

        self.label3 = Label(self.root2, text="Please enter details below").pack()
        self.label4 = Label(self.root2, text="").pack()
        self.label5 = Label(self.root2, text="Username * ").pack()

        self.username_entry = Entry(self.root2, textvariable=self.username)
        self.username_entry.pack()
        self.label6 = Label(self.root2, text="Password * ").pack()
        self.password_entry = Entry(self.root2, textvariable=self.password)
        self.password_entry.pack()
        Label(self.root2, text="").pack()
        Button(self.root2, text="Register", width=10, height=1, command=self.register_user).pack()

    def register_user(self):
        print("working")

        self.username_info = self.username.get()
        password_info = self.password.get()

        self.file = open(self.username_info, "w")
        self.file.write(self.username_info + "\n")
        self.file.write(password_info)
        self.file.close()

        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        Label(self.root2, text="Registration Success", fg="green", font=("calibre", 11)).pack()
        self.root2.after(3000, self.delete2)

    def login_success(self):
        self.master = Toplevel()
        self.root3 = self.master
        self.root3.title("Success")
        self.root3.geometry("150x100")
        Label(self.root3, text="Login Success").pack()
        Button(self.root3, text="OK", command=self.delete3).pack()

    def password_not_recognised(self):
        self.master = Toplevel()
        self.root4 = self.master
        self.root4.title("Failed")
        self.root4.geometry("150x100")
        Label(self.root4, text="Password Error").pack()
        Button(self.root4, text="OK", command=self.delete4).pack()

    def user_not_found(self):
        self.master = Toplevel()
        self.root5 = self.master
        self.root5.title("Failed")
        self.root5.geometry("150x100")
        self.label7 = Label(self.root5, text="User Not Found").pack()
        Button(self.root5, text="OK", command=self.delete5).pack()

    def login_verify(self):
        self.username1 = self.username_verify.get()
        self.password1 = self.password_verify.get()
        self.username_entry1.delete(0, END)
        self.password_entry1.delete(0, END)

        self.list_of_files = os.listdir()
        if self.username1 in self.list_of_files:
            self.file1 = open(self.username1, "r")
            self.verify = self.file1.read().splitlines()
            if self.password1 in self.verify:
                self.login_success()
            else:
                self.password_not_recognised()

        else:
            self.user_not_found()



    def login(self):
        self.root2 = Toplevel()
        self.root2.title("Login")
        self.root2.geometry("300x250")
        self.label8 = Label(self.root2, text="Please enter details below to login").pack()
        self.label9 = Label(self.root2, text="").pack()

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        self.label10 = Label(self.root2, text="Username * ").pack()
        self.username_entry1 = Entry(self.root2, textvariable=self.username_verify)
        self.username_entry1.pack()
        self.label11 = Label(self.root2, text="").pack()
        self.label12 = Label(self.root2, text="Password * ").pack()
        self.password_entry1 = Entry(self.root2, textvariable=self.password_verify)
        self.password_entry1.pack()
        self.label13 = Label(self.root2, text="").pack()
        self.login_login_button = Button(self.root2, text="Login", width=10, height=1, command=self.login_verify).pack()

class Game:
    def __init__(self):
        self.master = Toplevel()
        self.game_root = self.master
        # APPLYING VARIABLES
        self.game_root.title('WordBomb')
        self.game_root.geometry('600x600')
        self.widgets2()

    def widgets2(self):
        myfile = open("Josh", "rt")  # open lorem.txt for reading text
        contents = myfile.read()  # read the entire file to string
        myfile.close()  # close the file
        print(contents)

main()