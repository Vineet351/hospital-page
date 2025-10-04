from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1200x700")

        # Variables
        self.tabletname = StringVar()
        self.doctorname = StringVar()
        self.patientage = StringVar()
        self.addmission = StringVar()
        self.father = StringVar()
        self.mother = StringVar()
        self.address = StringVar()
        self.patientipd = StringVar()
        self.dob = StringVar()
        self.dd = StringVar()
        self.digonuses = StringVar()
        self.ward = StringVar()

        # Title
        title = Label(self.root, text="HOSPITAL MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"),
                      bg="white", fg="red", bd=10, relief=RIDGE)
        title.pack(side=TOP, fill=X)

        # Frame
        data_frame = Frame(self.root, bd=20, relief=RIDGE)
        data_frame.place(x=0, y=70, width=1200, height=350)

        # Left Frame
        left_frame = LabelFrame(data_frame, text="Patient Information", font=("arial", 12, "bold"), bd=10, relief=RIDGE)
        left_frame.place(x=0, y=0, width=750, height=330)

        # Right Frame
        right_frame = LabelFrame(data_frame, text="Prescription", font=("arial", 12, "bold"), bd=10, relief=RIDGE)
        right_frame.place(x=760, y=0, width=400, height=330)

        # Labels & Entries
        Label(left_frame, text="Patient Name", font=("arial", 12, "bold")).grid(row=0, column=0, sticky=W, padx=5, pady=5)
        txt_name = Entry(left_frame, textvariable=self.tabletname, font=("arial", 12), width=30)
        txt_name.grid(row=0, column=1, padx=5, pady=5)

        Label(left_frame, text="Doctor Name", font=("arial", 12, "bold")).grid(row=1, column=0, sticky=W, padx=5, pady=5)
        txt_doc = Entry(left_frame, textvariable=self.doctorname, font=("arial", 12), width=30)
        txt_doc.grid(row=1, column=1, padx=5, pady=5)

        Label(left_frame, text="Age", font=("arial", 12, "bold")).grid(row=2, column=0, sticky=W, padx=5, pady=5)
        txt_age = Entry(left_frame, textvariable=self.patientage, font=("arial", 12), width=30)
        txt_age.grid(row=2, column=1, padx=5, pady=5)

        Label(left_frame, text="Date of Admit", font=("arial", 12, "bold")).grid(row=3, column=0, sticky=W, padx=5, pady=5)
        txt_admit = Entry(left_frame, textvariable=self.addmission, font=("arial", 12), width=30)
        txt_admit.grid(row=3, column=1, padx=5, pady=5)

        # Prescription Text
        self.txtPrescription = Text(right_frame, font=("arial", 12), width=45, height=15)
        self.txtPrescription.pack()

        # Buttons
        btn_frame = Frame(self.root, bd=10, relief=RIDGE)
        btn_frame.place(x=0, y=430, width=1200, height=60)

        Button(btn_frame, text="Prescription", command=self.iprescription, bg="red", fg="white",
               font=("arial", 12, "bold"), width=15).grid(row=0, column=0, padx=10)

        Button(btn_frame, text="Insert", command=self.insert_data, bg="green", fg="white",
               font=("arial", 12, "bold"), width=15).grid(row=0, column=1, padx=10)

        Button(btn_frame, text="Clear", command=self.clear, bg="blue", fg="white",
               font=("arial", 12, "bold"), width=15).grid(row=0, column=2, padx=10)

        Button(btn_frame, text="Exit", command=self.iexit, bg="black", fg="white",
               font=("arial", 12, "bold"), width=15).grid(row=0, column=3, padx=10)

    # Functions
    def iprescription(self):
        self.txtPrescription.insert(END, f"Patient Name:\t{self.tabletname.get()}\n")
        self.txtPrescription.insert(END, f"Doctor Name:\t{self.doctorname.get()}\n")
        self.txtPrescription.insert(END, f"Age:\t{self.patientage.get()}\n")
        self.txtPrescription.insert(END, f"Date of Admit:\t{self.addmission.get()}\n")

    def insert_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="vineet", password="saini@12345", database="mywork")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO hospital (patientname, doctorname, patientage, addmission) VALUES (%s,%s,%s,%s)",
                           (self.tabletname.get(), self.doctorname.get(), self.patientage.get(), self.addmission.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record Inserted Successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")

    def clear(self):
        self.tabletname.set("")
        self.doctorname.set("")
        self.patientage.set("")
        self.addmission.set("")
        self.txtPrescription.delete("1.0", END)

    def iexit(self):
        confirm = messagebox.askyesno("Exit", "Do you want to exit?")
        if confirm:
            self.root.destroy()


root = Tk()
app = HospitalApp(root)
root.mainloop()
