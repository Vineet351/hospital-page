from tkinter import *
from tkinter import messagebox
import ast

# --------- Window Setup ----------
window = Tk()
window.title('Signup')
window.geometry('1000x500')
window.config(bg='white')
window.resizable(False, False)

# --------- Signup Function ----------
def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if username == "" or password == "" or confirm_password == "":
        messagebox.showerror("Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
    else:
        try:
            with open('datasheet.txt', 'a') as file:
                file.write(f"{username},{password}\n")
            messagebox.showinfo("Success", "Signup Successful!")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")

# --------- Background Image ----------
try:
    img1 = PhotoImage(file="C:/Users/ADMIN/Downloads/login.png")
    Label(window, image=img1, border=0, bg='white').place(x=-30, y=-50)
except:
    Label(window, text="(Image Not Found)", bg="white", fg="red").place(x=50, y=50)

# --------- Frame ----------
frame = Frame(window, width=350, height=390, bg='white')
frame.place(x=600, y=50)

headline = Label(window, text='Sign Up', fg='#57a1f8',
                 font=('Microsoft YaHei UI Light', 23, 'bold'), bg="white")
headline.place(x=700, y=20)

# --------- Username Entry ----------
def on_enter_user(e):
    if user.get() == 'username':
        user.delete(0, END)

def on_leave_user(e):
    if user.get() == '':
        user.insert(0, 'username')

user = Entry(frame, width=25, fg='black', border=0, bg='white',
             font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'username')
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# --------- Password Entry ----------
def on_enter_pass(e):
    if code.get() == 'password':
        code.delete(0, END)
        code.config(show="*")

def on_leave_pass(e):
    if code.get() == '':
        code.insert(0, 'password')
        code.config(show="")

code = Entry(frame, width=25, fg='black', border=0, bg='white',
             font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=140)
code.insert(0, 'password')
code.bind("<FocusIn>", on_enter_pass)
code.bind("<FocusOut>", on_leave_pass)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=167)

# --------- Confirm Password Entry ----------
def on_enter_confirm(e):
    if confirm_code.get() == 'confirm password':
        confirm_code.delete(0, END)
        confirm_code.config(show="*")

def on_leave_confirm(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'confirm password')
        confirm_code.config(show="")

confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white',
                     font=('Microsoft YaHei UI Light', 11))
confirm_code.place(x=30, y=200)
confirm_code.insert(0, 'confirm password')
confirm_code.bind("<FocusIn>", on_enter_confirm)
confirm_code.bind("<FocusOut>", on_leave_confirm)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=227)

# --------- Signup Button ----------
Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white',
       border=0, command=signup).place(x=35, y=280)

# --------- Signin Label ----------
label = Label(frame, text="I have an account", fg='black', bg='white',
              font=('Microsoft YaHei UI Light', 9))
label.place(x=90, y=320)

signin = Button(frame, width=6, text='Sign In', border=0, bg='white',
                cursor='hand2', fg='#57a1f8')
signin.place(x=200, y=320)

# --------- Run Window ----------
window.mainloop()
