import tkinter as tk

root = tk.Tk()
root.title("Welcome to Joshua's Hotel Booking System!")
root.geometry("640x480")

tk.Label(root, text="This is my test program for hotel booking system OCR H446").pack(pady=50)
tk.Button(root, text="Enter", command=root.destroy).pack()

root.mainloop()
