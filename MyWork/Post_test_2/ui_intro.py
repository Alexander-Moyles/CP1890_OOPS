import tkinter as tk
from tkinter import ttk


# Create an empty window
first_window = tk.Tk()
first_window.title("My First GUI")
first_window.geometry("400x300")


# Adding a frame
frame = ttk.Frame(first_window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)


# Adding button functionality:
def clicked_button1():
    first_window.title("Yes!, I am the cool button")
    name = name_text.get()
    about_text.set(f"{name} is cool")


def clicked_button2():
    first_window.destroy()


# Creating Labels
name_label = ttk.Label(frame, text="Name")
name_label.pack()
name_text = tk.StringVar()
name_entry = ttk.Entry(frame, width=25, textvariable=name_text)
name_entry.pack()

about_label = ttk.Label(frame, text="About")
about_label.pack()
about_text = tk.StringVar()
about_entry = ttk.Entry(frame, width=25, textvariable=about_text, state="readonly")
about_entry.pack()


# Adding two buttons
button1 = ttk.Button(frame, text="I'm cool!", command=clicked_button1)
button2 = ttk.Button(frame, text="No, I'M cool!", command=clicked_button2)
button1.pack()
button2.pack()


# Running window
first_window.mainloop()
