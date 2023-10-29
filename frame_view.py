from subject_controller import SubjectController
import tkinter as tk
import tkinter.messagebox as mb


class LoginFrame(tk.LabelFrame):
    def clear(self):
        self.emailField.delete(0, tk.END)
        self.passwordField.delete(0, tk.END)

    def login(self, master, model):
        validationMsg = "Incorrect email or password format"
        if not model.checkFormat(self.emailText.get(), self.passwordTxt.get()):
            mb.showerror(title="Login Error", message=validationMsg)
            self.clear()
            return

        student = model.login(self.emailText.get(), self.passwordTxt.get())

        if student != None:
            info = f"Welcome {student.name}"
            EnrollmentWindow(master, student)
            self.clear()
        else:
            info = "Student does not exist"
            mb.showerror(title="Login Error", message=info)
            self.clear()

    def __init__(self, master, model) -> None:
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
            command=lambda: self.login(master, model),
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

        info = f"of {model.name}!"
        self.title("Enrollment " + info)
        self.geometry("400x300")
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("+%d+%d" % (x + 300, y))
        self.configure(bg="#607b8d")
        self.resizable(False, False)

        # enrolled subjects label & listbox
        enrollLbl = tk.Label(
            self,
            text="Enrolled subjects",
            justify="left",
            fg="#ffc107",
            font="Helvetica 12 bold",
            bg="#607b8d",
        )
        enrollLbl.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

        enrolled_subjects = SubjectController.enrolledSubjects(model)

        enrolllistVar = tk.Variable(value=enrolled_subjects)
        enrolledList = tk.Listbox(
            self, listvariable=enrolllistVar, selectmode=tk.SINGLE
        )
        enrolledList.grid(column=0, row=1, padx=5, pady=5)

        # all subjects label & listbox
        allsubjectLbl = tk.Label(
            self,
            text="All subjects",
            justify="left",
            fg="#ffc107",
            font="Helvetica 12 bold",
            bg="#607b8d",
        )
        allsubjectLbl.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)

        all_subjects = SubjectController.getAllSubjects()
        listVar = tk.Variable(value=all_subjects)
        allList = tk.Listbox(self, listvariable=listVar, selectmode=tk.SINGLE)
        allList.select_set(0)
        allList.grid(column=1, row=1, padx=5, pady=5)

        # enroll button
        enrollBtn = tk.Button(
            self,
            text="Enroll",
            bg="#252525",
            fg="#ffc107",
            font="Helvetica 10 bold",
            command=lambda: self.enroll(master, model, allList, enrolledList),
        )
        enrollBtn.grid(column=0, row=2, columnspan=2, padx=5, pady=5)

        # remove subject button
        removeBtn = tk.Button(
            self,
            text="Remove",
            bg="#252525",
            fg="#ffc107",
            font="Helvetica 10 bold",
            command=lambda: self.remove(master, model, allList, enrolledList),
        )
        removeBtn.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

    def enroll(self, master, model, allList, enrolledList):
        if SubjectController.checkLimit(model):
            if allList.curselection():
                idx = allList.curselection()
                temp = allList.get(idx)
                answer = mb.askyesno(
                    title="confirmation",
                    message=f"Are you sure that you want to enroll {temp}?",
                )
                if answer:
                    allList.delete(idx)
                    enrolledList.insert("end", temp)
                    splitString = temp.split("-")
                    subjectID = splitString[-1]
                    subject = SubjectController.createSubjectCustomID(subjectID)
                    SubjectController.enrollSubject(model, subject)
            else:
                info = "Please select from all subject then enroll!"
                mb.showerror(title="Enroll Error", message=info)
        else:
            info = "Students are allowed to enroll in 4 subjects only"
            mb.showerror(title="Enroll Error", message=info)

    def remove(self, master, model, allList, enrolledList):
        if enrolledList.curselection():
            idx = enrolledList.curselection()
            temp = enrolledList.get(idx)
            answer = mb.askyesno(
                title="confirmation",
                message=f"Are you sure that you want to remove {temp}?",
            )
            if answer:
                enrolledList.delete(idx)
                allList.insert("end", temp)
                splitString = temp.split("-")
                subjectID = splitString[-1]
                SubjectController.removeSubject(model, subjectID)
        else:
            info = "Please select enrolled subject then remove!"
            mb.showerror(title="Remove Error", message=info)


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
