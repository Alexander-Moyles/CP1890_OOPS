import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Create an empty window
first_window = tk.Tk()
first_window.title("My First GUI")
first_window.geometry("400x300")


# Adding a frame
frame = ttk.Frame(first_window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)


# Adding button functionality:
"""
message_box(title, message)
"""
def clicked_button1():
    first_window.title("Yes!, I am the cool button")
    name = name_text.get()
    if name == "":
        # messagebox.showerror("Error", "No name entered")
        # messagebox.showwarning("Warning", "Please")
        # messagebox.showinfo("Info", "Hello")
        response = messagebox.askyesno("Are you sure?", "No input entered, proceed?")
        if response == True:
            about_text.set("No name entered, however we continued")
        else:
            about_text.set("Enter a name.")
    else:
        about_text.set(f"{name} is cool")


def clicked_button2():
    first_window.destroy()


# Creating Labels
name_label = ttk.Label(frame, text="Name")
name_label.grid(column=0, row=0, sticky=tk.E)
name_text = tk.StringVar()
name_entry = ttk.Entry(frame, width=25, textvariable=name_text)
name_entry.grid(column=1, row=0, sticky=tk.E)

about_label = ttk.Label(frame, text="About")
about_label.grid(column=0, row=1, sticky=tk.E)
about_text = tk.StringVar()
about_entry = ttk.Entry(frame, width=25, textvariable=about_text, state="readonly")
about_entry.grid(column=1, row=1, sticky=tk.E)


# Adding two buttons
button1 = ttk.Button(frame, text="I'm cool!", command=clicked_button1)
button2 = ttk.Button(frame, text="No, I'M cool!", command=clicked_button2)
button1.grid(column=0, row=2, sticky=tk.E)
button2.grid(column=1, row=2)


for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)

# Running window
first_window.mainloop()