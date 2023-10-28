import tkinter as tk
from _frameview import LoginFrame
from database import Database

root = tk.Tk()
root.geometry("300x200")
root.title("GUIUniApp")
root.configure(bg='#607b8d')
root.resizable(False, False)

database = Database()
box = LoginFrame(root, database)

root.mainloop()

