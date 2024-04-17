import tkinter as tk
from tkinter import ttk

preferences = tk.Tk()
preferences.title("Preferences")
preferences.geometry("400x150")

frame = ttk.Frame(preferences, padding="10 10 10 10")
frame.pack()


def reader():
    rows = []
    file_name = "pref.txt"
    with open(file_name, "r") as file:
        for row in file:
            rows.append(row)

    if rows != []:
        name_text.set(rows[0])
        language_text.set(rows[1])
        autosave_text.set(rows[2])



def writer():
    check_autosave = 0
    check_name = 0
    check_language = 0
    try:
        autosave = int(autosave_text.get())
        check_autosave = 1
    except ValueError:
        preferences.geometry("500x150")
        autosave_err = ttk.Label(frame, text="Must be valid integer.")
        autosave_err.grid(column=3, row=2, sticky=tk.W)

    if name_text.get() == "":
        preferences.geometry("500x150")
        name_err = ttk.Label(frame, text="Required.")
        name_err.grid(column=3, row=0, sticky=tk.W)
        check_name = 1

    if language_text.get() == "":
        preferences.geometry("500x150")
        language_err = ttk.Label(frame, text="Required.")
        language_err.grid(column=3, row=1, sticky=tk.W)
        check_language = 1

    if check_autosave == 1 and check_name == 1 and check_language == 1:
        file_name = "pref.txt"
        with open(file_name, "w") as file:
            file.writelines(f"{[str(name_text.get()),str(language_text.get()),int(autosave)]}")


# Button Functionality
def save_button():
    writer() # <= Was not able to make write to file, can read from files just fine however.
    preferences.destroy()


def cancel_button():
    preferences.destroy()


# Name
name = ttk.Label(frame, text="Name: ")
name.grid(column=0, row=0, sticky=tk.E)
name_text = tk.StringVar()
name_entry = ttk.Entry(frame, width=25, textvariable=name_text)
name_entry.grid(column=1, row=0)

# Language
language = ttk.Label(frame, text="Language: ")
language.grid(column=0, row=1, sticky=tk.E)
language_text = tk.StringVar()
language_entry = ttk.Entry(frame, width=25, textvariable=language_text)
language_entry.grid(column=1, row=1)

# Auto Save
autosave = ttk.Label(frame, text="Auto Save Every X Minutes: ")
autosave.grid(column=0, row=2, sticky=tk.E)
autosave_text = tk.StringVar()
autosave_entry = ttk.Entry(frame, width=25, textvariable=autosave_text)
autosave_entry.grid(column=1, row=2)

# Buttons
save = ttk.Button(frame, text="Save", command=save_button)
save.grid(column=1, row=3, sticky=tk.W)
Cancel = ttk.Button(frame, text="Cancel", command=cancel_button)
Cancel.grid(column=1, row=3, sticky=tk.E)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

if __name__ == "__main__":
    try:
        reader()
    except FileNotFoundError:
        file_name = "pref.txt"
        name_text.set("")
        language_text.set("")
    finally:
        preferences.mainloop()
