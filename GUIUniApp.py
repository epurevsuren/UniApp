import tkinter as tk
from frame_view import LoginFrame
from student_controller import StudentController


class GUIUniApp:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")
    root.title("UniApp Group11Cmp06")
    root.configure(bg="#607b8d")
    root.resizable(False, False)
    box = LoginFrame(root, StudentController)
    root.mainloop()
