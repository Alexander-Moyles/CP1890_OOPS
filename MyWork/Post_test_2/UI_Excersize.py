# Monthly Investment / Future Value Program
import locale as lc
import tkinter as tk
from tkinter import ttk


def month_invest():
    month = int(input("Enter monthly investment:\t"))
    return month


def year_int():
    year = float(input("Enter yearly interest rate:\t"))
    return year


def year_num():
    years = int(input("Enter number of years:\t\t"))
    return years


def total_value(monthly_investment, y_interest, years):
    monthly_interest = y_interest / (12 * 100)
    months = years * 12
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        month_interest = future_value * monthly_interest
        future_value += month_interest
    return future_value


def main():
    while True:
        m = month_invest()
        y = year_int()
        yn = year_num()
        print(" ")
        lc.setlocale(lc.LC_ALL, 'en-ca')
        mi = str(lc.currency(m, grouping=True))
        print(f"Monthly investment:\t\t\t{mi}")
        print(f"Yearly interest rate: {y:13}")
        print(f"Years: {yn:28}")

        total = total_value(m, y, yn)
        totali = str(lc.currency(total, grouping=True))
        print(f"{'Future value:':21} {totali:>10}")

        cont = input("Continue? (y/n): ").lower()
        if cont != 'y':
            break


first_window = tk.Tk()
first_window.title("Future value Calculator")
first_window.geometry("400x300")
frame = ttk.Frame(first_window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)

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


def destroy():
    first_window.destroy()


Calculate = ttk.Button(frame, text="Calculate")
Exit = ttk.Button(frame, text="Exit", command=destroy)
Calculate.grid(column=0, row=2, sticky=tk.E)
Exit.grid(column=1, row=2, sticky=tk.E)


if __name__ == "__main__":
    first_window.mainloop()
