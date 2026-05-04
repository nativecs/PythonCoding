import tkinter as tk
from tkinterweb import HtmlFrame

root = tk.Tk()
root.title("Joshua's Hotel Booking System")
root.geometry("640x480")

# Create HTML frame
frame = HtmlFrame(root)
frame.pack(fill="both", expand=True)

# HTML content
html_content = """
<h1 style='color:blue;'>Welcome to Joshua's Hotel Booking System</h1>
<p>This is my test program for OCR H446</p>

<button onclick="alert('Entering system...')">Enter</button>
"""

# Load HTML into the frame
frame.set_content(html_content)

root.mainloop()