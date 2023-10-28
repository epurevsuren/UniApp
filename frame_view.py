# from controller import Controller
from utils import Utils
import tkinter as tk
import tkinter.messagebox as mb


class ConfirmationView(tk.Toplevel):
    def __init__(self, master, msg):
        super().__init__(master=master)
        self.title("Confirmation Window")
        self.geometry("300x200")
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("+%d+%d" % (x + 300, y))
        self.configure(bg="#607b8d")
        self.resizable(False, False)
        label = tk.Label(
            self, text=msg, fg="#ffc107", font="Helvetica 12 bold", bg="#607b8d"
        )
        label.place(relx=0.5, rely=0.5, anchor="center")
        closeBtn = tk.Button(
            self,
            text="Close",
            bg="#252525",
            fg="#ffc107",
            font="Helvetica 10 bold",
            command=lambda: self.destroy(),
        )
        closeBtn.pack(padx=5, pady=5, side="bottom")


class LoginFrame(tk.LabelFrame):
    def clear(self):
        self.emailField.delete(0, tk.END)
        self.passwordField.delete(0, tk.END)

    def login(self, master, db):
        validationMsg = "Incorrect email or password format"
        if not Utils.is_valid_email(self.emailText.get()):
            mb.showerror(title="Login Error", message=validationMsg)
            self.clear()
            return

        if not Utils.is_valid_password(self.passwordTxt.get()):
            mb.showerror(title="Login Error", message=validationMsg)
            self.clear()
            return

        student = db.match(self.emailText.get(), self.passwordTxt.get())

        if student != None:
            info = f"Welcome {student.name}"
            EnrollmentWindow(master, student)
            # ConfirmationView(master, info)
            # Controller.save(student.name)
            self.clear()
        else:
            info = "Student does not exist"
            mb.showerror(title="Login Error", message=info)
            self.clear()

    def __init__(self, master, db) -> None:
        super().__init__(master)
        box = tk.LabelFrame(
            master,
            text="Sign In",
            bg="#607b8d",
            fg="white",
            padx=11,
            pady=11,
            font="Helvetica 10 bold",
        )
        box.columnconfigure(0, weight=1)
        box.columnconfigure(1, weight=3)
        box.place(rely=0.5, relx=0.5, anchor="center")

        self.emailLbl = tk.Label(
            box,
            text="Email:",
            justify="left",
            fg="#ffc107",
            font="Helvetica 12 bold",
            bg="#607b8d",
        )
        self.emailLbl.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

        passwordLbl = tk.Label(
            box, text="Password:", fg="#ffc107", font="Helvetica 12 bold", bg="#607b8d"
        )
        passwordLbl.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

        self.emailText = tk.StringVar()
        self.emailField = tk.Entry(box, textvariable=self.emailText)
        self.emailField.grid(column=1, row=0, padx=5, pady=5)
        self.emailField.focus()

        self.passwordTxt = tk.StringVar()
        self.passwordField = tk.Entry(box, textvariable=self.passwordTxt, show="*")
        self.passwordField.grid(column=1, row=1, padx=5, pady=5)

        self.loginBtn = tk.Button(
            box,
            text="Login",
            bg="#252525",
            fg="#ffc107",
            font="Helvetica 10 bold",
            command=lambda: self.login(master, db),
        )
        self.loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.cancelBtn = tk.Button(
            box,
            bg="#252525",
            fg="#ffc107",
            font="Helvetica 10 bold",
            text="Cancel",
            command=lambda: master.quit(),
        )
        self.cancelBtn.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)


class EnrollmentWindow(tk.Toplevel):
    def __init__(self, master, model):
        super().__init__(master=master)

        self.title("GUIUniApp - Enrollment")
        self.geometry("300x200")
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("+%d+%d" % (x + 300, y))
        self.configure(bg="#607b8d")
        self.resizable(False, False)

        label = tk.Label(
            self,
            text=f"Welcome {model.name} \n Press button to enroll in subjects",
            fg="#ffc107",
            font="Helvetica 12 bold",
            bg="#607b8d",
        )
        label.place(relx=0.5, rely=0.5, anchor="center")

        enrollBtn = tk.Button(
            self,
            text="Enroll",
            bg="#252525",
            fg="#ffc107",
            font="Helvetica 10 bold",
            command=lambda: self.enroll(master, model),
        )
        enrollBtn.pack(padx=5, pady=5, side="bottom")

    def enroll(self, master, model):
        if len(model.subjects) < 4:
            subject = Subject()
            model.subjects.append(subject)
            SubjectWindow(master, model)
        else:
            info = "Students are allowed to enroll in 4 subjects only"
            mb.showerror(title="Enroll Error", message=info)


# need to fix the enroll button logic >> add subject to the list


class SubjectWindow(tk.Toplevel):
    def __init__(self, master, model):
        super().__init__(master=master)
        self.title("GUIUniApp - Subject List")
        self.geometry("300x300")
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("+%d+%d" % (x + 600, y))
        self.configure(bg="#607b8d")
        self.resizable(False, False)

        # listVar = tk.Variable(value=model.subjects.id)
        # subjectList = tk.Listbox(master,listvariable=listVar)
        # subjectList.pack(fill=tk.BOTH,expand=True,padx=20,pady=40)
        abc = model.show_subjects()

        subjectList = tk.Label(
            self, text=f"{abc}", font="Helvetica 12 bold", bg="#607b8d"
        )
        subjectList.place(relx=0.5, rely=0.5, anchor="center")

        closeBtn = tk.Button(
            self,
            text="Close",
            bg="#252525",
            fg="#ffc107",
            font="Helvetica 12 bold",
            command=lambda: self.destroy(),
        )
        closeBtn.pack(padx=5, pady=20, side="bottom")


class ExceptionWindow:
    pass
