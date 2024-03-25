# Monthly Investment / Future Value Program
import locale as lc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def month_invest():
    try:
        month = int(month_text.get())
        return month
    except ValueError:
        messagebox.showerror("Monthly Investment Error", "Please Enter a Proper Integer")
        future_text.set("Please Enter Proper Data")


def year_int():
    try:
        year = float(year_text.get())
        year_text.set(str(year))
        return year
    except ValueError:
        messagebox.showerror("Yearly Interest Error", "Please Enter a Proper Float/Decimal Number")
        future_text.set("Please Enter Proper Data")


def year_num():
    try:
        years = int(years_text.get())
        return years
    except ValueError:
        messagebox.showerror("Years Error", "Please Enter a Proper Integer")
        future_text.set("Please Enter Proper Data")


def total_value(monthly_investment, y_interest, years):
    monthly_interest = y_interest / (12 * 100)
    months = years * 12
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        month_interest = future_value * monthly_interest
        future_value += month_interest
    return future_value


def calculate_button():
    m = month_invest()
    y = year_int()
    yn = year_num()

    lc.setlocale(lc.LC_ALL, 'en-ca')
    total = total_value(m, y, yn)
    calc = str(lc.currency(total, grouping=True))
    future_text.set(calc)


# Window:
first_window = tk.Tk()
first_window.title("Future Value Calculator")
first_window.geometry("300x165")
frame = ttk.Frame(first_window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)

# Monthly Investment:
month_label = ttk.Label(frame, text="Monthly Investment:", padding="5")
month_label.grid(column=0, row=0, sticky=tk.E)
month_text = tk.StringVar()
month_entry = ttk.Entry(frame, width=25, textvariable=month_text)
month_entry.grid(column=1, row=0, sticky=tk.E)

# Yearly Interest Rate
year_label = ttk.Label(frame, text="Yearly Interest Rate:", padding="5")
year_label.grid(column=0, row=1, sticky=tk.E)
year_text = tk.StringVar()
year_entry = ttk.Entry(frame, width=25, textvariable=year_text)
year_entry.grid(column=1, row=1, sticky=tk.E)

# Years:
years_label = ttk.Label(frame, text="Years:", padding="5")
years_label.grid(column=0, row=2, sticky=tk.E)
years_text = tk.StringVar()
years_entry = ttk.Entry(frame, width=25, textvariable=years_text)
years_entry.grid(column=1, row=2, sticky=tk.E)

# Future Value:
future_label = ttk.Label(frame, text="Future Value:", padding="5")
future_label.grid(column=0, row=3, sticky=tk.E)
future_text = tk.StringVar()
future_entry = ttk.Entry(frame, width=25, textvariable=future_text, state="readonly")
future_entry.grid(column=1, row=3, sticky=tk.E)


def destroy():
    first_window.destroy()


# Buttons:
Calculate = ttk.Button(frame, text="Calculate", command=calculate_button)
Exit = ttk.Button(frame, text="Exit", command=destroy)
Calculate.grid(column=1, row=4, sticky=tk.W)
Exit.grid(column=1, row=4, sticky=tk.E)


if __name__ == "__main__":
    first_window.mainloop()
