import random
from tkinter import *
import os
from PIL import ImageTk


# from PyDictionary import *
# from PyDictionary.test_pydictionary import dictionary

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

        self.turn = 1

        if self.turn == 1:
            self.bomb_time = random.randint(5, 30)
        elif self.turn == 2:
            self.bomb_time = random.randint(5, 30)
        elif self.turn == 3:
            self.bomb_time = random.randint(5, 30)
        elif self.turn == 4:
            self.bomb_time = random.randint(5, 30)

        self.root.mainloop()

    def delete1(self):
        self.root.destroy()

    def delete2(self):
        self.root2.destroy()

    def delete3(self):
        self.root3.destroy()
        self.choose_players()

    def delete4(self):
        self.root4.destroy()

    def delete5(self):
        self.root5.destroy()

    def main_screen(self):
        self.login_or_register = Label(text="Login or Register", bg="grey", width="300", height="2",
                                       font=("Calibre", 13)).pack()
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
        Button(self.root3, text="OK", command=self.choose_players).pack()

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

    def choose_players(self):
        self.master = Toplevel()
        self.root8 = self.master
        self.root8.title('Players')
        self.root8.geometry("300x300")

        self.player1_name = StringVar()
        self.player2_name = StringVar()
        self.player3_name = StringVar()
        self.player4_name = StringVar()
        self.player5_name = StringVar()
        self.player6_name = StringVar()
        self.player7_name = StringVar()
        self.player8_name = StringVar()

        self.choose_p1_label = Label(self.root8, text='Player 1', font=('Arial', 15))
        self.choose_p1_label.place(x=10, y=10)
        self.player1_entry = Entry(self.root8, textvariable=self.player1_name, font=('Arial', 15))
        self.player1_entry.place(x=10, y=40)
        self.choose_p2_label = Label(self.root8, text='Player 2', font=('Arial', 15))
        self.choose_p2_label.place(x=10, y=70)
        self.player2_entry = Entry(self.root8, textvariable=self.player2_name, font=('Arial', 15))
        self.player2_entry.place(x=10, y=100)
        self.choose_p3_label = Label(self.root8, text='Player 3', font=('Arial', 15))
        self.choose_p3_label.place(x=10, y=130)
        self.player3_entry = Entry(self.root8, textvariable=self.player3_name, font=('Arial', 15))
        self.player3_entry.place(x=10, y=160)
        self.choose_p4_label = Label(self.root8, text='Player 4', font=('Arial', 15))
        self.choose_p4_label.place(x=10, y=190)
        self.player4_entry = Entry(self.root8, textvariable=self.player4_name, font=('Arial', 15))
        self.player4_entry.place(x=10, y=220)
        self.next_button = Button(self.root8, text='Continue to Game', command=self.next)
        self.next_button.place(x=95, y=260)

    def next(self):
        self.master = Toplevel()
        self.root9 = self.master
        self.root9.title('BOMB PARTY')
        self.root9.geometry('600x600')

        if self.turn == 1:
            self.timer()
            self.green_image = ImageTk.PhotoImage(file=r'C:\\Users\\jlnelson\\Pictures\\Saved Pictures\\greenlight.jpg')
            self.image_label = Label(self.root9, image=self.green_image, height=20, width=20)
            self.image_label.place(x=170, y=32.5)

            with open("combinations.txt", "r") as file:
                self.allText = file.read()
                self.combinations = list(map(str, self.allText.split()))

                # print random string
                self.rand_combination = (random.choice(self.combinations))
                self.rand_combination_label = Label(self.root9, text=self.rand_combination, font=('Arial', 15))
                self.rand_combination_label.place(x=280, y=240)

        self.player1_label = Label(self.root9, text=self.player1_name.get(), font=('Arial', 15))
        self.player1_label.place(x=10, y=10)
        self.player1_word_entry = Entry(self.root9, font=('Arial', 10))
        self.player1_word_entry.bind("<Return>", self.onReturn1)
        self.player1_word_entry.place(x=10, y=35)

        if self.turn == 2:
            with open("combinations.txt", "r") as file:
                self.allText = file.read()
                self.combinations = list(map(str, self.allText.split()))

                # print random string
                self.rand_combination = (random.choice(self.combinations))
                self.rand_combination_label.config(text=self.rand_combination)

        self.player2_label = Label(self.root9, text=self.player2_name.get(), font=('Arial', 15))
        self.player2_label.place(x=10, y=150)
        self.player2_word_entry = Entry(self.root9, font=('Arial', 10))
        self.player2_word_entry.bind("<Return>", self.onReturn2)
        self.player2_word_entry.place(x=10, y=175)

        if self.turn == 3:
            with open("combinations.txt", "r") as file:
                self.allText = file.read()
                self.combinations = list(map(str, self.allText.split()))

                # print random string
                self.rand_combination = (random.choice(self.combinations))
                self.rand_combination_label.config(text=self.rand_combination)

        self.player3_label = Label(self.root9, text=self.player3_name.get(), font=('Arial', 15))
        self.player3_label.place(x=10, y=290)
        self.player3_word_entry = Entry(self.root9, font=('Arial', 10))
        self.player3_word_entry.bind("<Return>", self.onReturn3)
        self.player3_word_entry.place(x=10, y=315)

        if self.turn == 4:
            self.image_label.place(x=170, y=452.5)

            with open("combinations.txt", "r") as file:
                self.allText = file.read()
                self.combinations = list(map(str, self.allText.split()))

                # print random string
                self.rand_combination = (random.choice(self.combinations))
                self.rand_combination_label.config(text=self.rand_combination)

        self.player4_label = Label(self.root9, text=self.player4_name.get(), font=('Arial', 15))
        self.player4_label.place(x=10, y=430)
        self.player4_word_entry = Entry(self.root9, font=('Arial', 10))
        self.player4_word_entry.bind("<Return>", self.onReturn4)
        self.player4_word_entry.place(x=10, y=455)

    def onReturn1(self, *args):
        if self.turn == 1:
            self.update_time = self.root9.after(1000, self.timer)
        if self.bomb_time == 0:
            self.turn += 1
            self.onReturn2()
            with open('words.txt', 'r') as file:
                self.words = [line.strip('\n') for line in file.readlines()]
            while True:  # or whatever the game loop is
                self.user_input = self.player1_word_entry.get().upper()
                if self.user_input in self.words:
                    if self.rand_combination in self.user_input:
                            self.turn += 1
                            self.image_label.place(x=170, y=172.5)
                            self.player1_last_word = Label(self.root9, text=self.player1_word_entry.get().upper(),
                                                           font=('Arial', 13))
                            self.player1_last_word.place(x=10, y=55)
                            self.rand_combination = (random.choice(self.combinations))
                            self.rand_combination_label.config(text=self.rand_combination)
                            break
                    else:
                        print("word doesn't contain combination")
                        break
                else:
                    print('not a word')
                    break

    def onReturn2(self, *args):
        if self.turn == 2:
            self.bomb_time = random.randint(5, 30)
            self.update_time = self.root9.after(1000, self.timer)

            with open('words.txt', 'r') as file:
                self.words = [line.strip('\n') for line in file.readlines()]
            while True:  # or whatever the game loop is
                self.user_input = self.player2_word_entry.get().upper()
                if self.user_input in self.words:
                    if self.rand_combination in self.user_input:
                        self.turn += 1
                        self.image_label.place(x=170, y=312.5)
                        self.player2_last_word = Label(self.root9, text=self.player2_word_entry.get().upper(),
                                                       font=('Arial', 13))
                        self.player2_last_word.place(x=10, y=195)
                        self.rand_combination = (random.choice(self.combinations))
                        self.rand_combination_label.config(text=self.rand_combination)
                        break
                    else:
                        print("word doesn't contain combination")
                        break
                else:
                    print('not a word')
                    break

    def onReturn3(self, *args):
        self.update_time = self.root9.after(1000, self.timer)
        if self.turn == 3:
            with open('words.txt', 'r') as file:
                self.words = [line.strip('\n') for line in file.readlines()]
            while True:  # or whatever the game loop is
                self.user_input = self.player3_word_entry.get().upper()
                if self.user_input in self.words:
                    if self.rand_combination in self.user_input:
                        self.image_label.place(x=170, y=452.5)
                        self.turn += 1
                        self.player3_last_word = Label(self.root9, text=self.player3_word_entry.get().upper(),
                                                       font=('Arial', 13))
                        self.player3_last_word.place(x=10, y=335)
                        self.rand_combination = (random.choice(self.combinations))
                        self.rand_combination_label.config(text=self.rand_combination)
                        break
                    else:
                        print("word doesn't contain combination")
                        break
                else:
                    print('not a word')
                    break

    def onReturn4(self, *args):
        self.update_time = self.root9.after(1000, self.timer)
        if self.turn == 4:
            with open('words.txt', 'r') as file:
                self.words = [line.strip('\n') for line in file.readlines()]
            while True:  # or whatever the game loop is
                self.user_input = self.player4_word_entry.get().upper()
                if self.user_input in self.words:
                    if self.rand_combination in self.user_input:
                        self.image_label.place(x=170, y=32.5)
                        self.turn += 1
                        self.player4_last_word = Label(self.root9, text=self.player4_word_entry.get().upper(),
                                                       font=('Arial', 13))
                        self.player4_last_word.place(x=10, y=475)
                        self.rand_combination = (random.choice(self.combinations))
                        self.rand_combination_label.config(text=self.rand_combination)
                        break
                    else:
                        print("word doesn't contain combination")
                        break
                else:
                    print('not a word')
                    break

    def timer(self):
        if self.turn == 1:
            if self.bomb_time > 0:
                self.bomb_time -= 1
                print(self.bomb_time)
                self.root9.after(1000, self.timer)
            elif self.bomb_time <= 0:
                self.onReturn2()
                return


main()
