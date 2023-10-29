import tkinter as tk
from tkinter import messagebox
from frame_view import LoginFrame
from student_controller import StudentController


class GUIUniApp:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)


if __name__ == "__main__":
    try:
        root = tk.Tk()
        root.geometry("300x200")
        root.title("UniApp Group11Cmp06")
        root.configure(bg="#607b8d")
        root.resizable(False, False)
        box = LoginFrame(root, StudentController)
        root.mainloop()
    except tk.TclError as e:
        messagebox.showerror("Error", f"A tkinter error occurred: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
