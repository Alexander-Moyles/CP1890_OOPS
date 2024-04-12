"""
Assignment 3

Question 4
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import sqrt as square_root


def get_sides():
    """
    Gets and validates user input for sides a and b.
    Uses these values to get and return c.
    """
    err = 0
    try:
        a = int(side_a_text.get())
        b = int(side_b_text.get())
    except ValueError:
        err = 1
        messagebox.showerror("Error", "Please Enter Proper Integers")
    finally:
        if err == 0:
            c = square_root(a**2 + b**2)
            return c


def calc_button():
    """
    Checks user input for sides a and b, then calculates and displays c.
    """
    c_value = get_sides()
    side_c_text.set(f"{c_value:.3f}")
    

def exit_button():
    """
    Closes GUI window.
    """
    calc_window.destroy()


# Window
calc_window = tk.Tk()
calc_window.title("Right Triangle Calculator")
calc_window.geometry("300x140")

frame = ttk.Frame(calc_window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)


# Side a
side_a = ttk.Label(frame, text="Side A: ")
side_a.grid(column=0, row=0, sticky=tk.E)
side_a_text = tk.StringVar()
side_a_entry = ttk.Entry(frame, width=35, textvariable=side_a_text)
side_a_entry.grid(column=1, row=0, columnspan=2, sticky=tk.E)


# Side b
side_b = ttk.Label(frame, text="Side B: ")
side_b.grid(column=0, row=1, sticky=tk.E)
side_b_text = tk.StringVar()
side_b_entry = ttk.Entry(frame, width=35, textvariable=side_b_text)
side_b_entry.grid(column=1, row=1, columnspan=2, sticky=tk.E)


# side c
side_c = ttk.Label(frame, text="Side C: ")
side_c.grid(column=0, row=2, sticky=tk.E)
side_c_text = tk.StringVar()
side_c_entry = ttk.Entry(frame, width=35, textvariable=side_c_text, state="readonly")
side_c_entry.grid(column=1, row=2, columnspan=2, sticky=tk.E)


# Buttons
calculate = ttk.Button(frame, text="Calculate", command=calc_button)
end = ttk.Button(frame, text="Exit", command=exit_button)
calculate.grid(column=1, row=3, sticky=tk.E)
end.grid(column=2, row=3, sticky=tk.W)


# Padding
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)
    

if __name__ == "__main__":
    calc_window.mainloop()
