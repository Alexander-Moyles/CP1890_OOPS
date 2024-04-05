import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


def length():
    lineup = []
    conn = sqlite3.connect('Baseball.sqlite')
    c = conn.cursor()
    c.execute("select * from Player")
    rows = c.fetchall()
    conn.close

    for row in rows:
        if row is not None:
            lineup.append(row)

    return len(lineup)


def value_err(lineup):
    messagebox.showerror("Player ID not found.", f"Please enter a valid integer,\nthere are {lineup} players.")
    player_id_text.set("")
    first_name_text.set("")
    last_name_text.set("")
    position_text.set("")
    atbat_text.set("")
    hits_text.set("")


def get_player_button():
    lineup = length()
    player_id_entry.config(state=tk.DISABLED)
    try:
        player = int(player_id_text.get())
        if player > int(lineup):
            value_err(lineup)
        else:
            query = "select * from Player where playerID = '{}'".format(player)

            conn = sqlite3.connect('Baseball.sqlite')
            c = conn.cursor()
            c.execute(query)
            conn.commit()
            rows = c.fetchall()
            conn.close()

            for row in rows:
                avg = (row[6] / row[5])

                first_name_text.set(row[2])
                last_name_text.set(row[3])
                position_text.set(row[4])
                atbat_text.set(row[5])
                hits_text.set(row[6])
                bat_avg_text.set(f"{avg:.3f}")

    except ValueError:
        value_err(lineup)


def save_button():
    player_id_entry.config(state=tk.NORMAL)
    try:
        new_fname = first_name_text.get()
        new_lname = last_name_text.get()
        new_pos = position_text.get()
        new_atbat = atbat_text.get()
        new_hits = hits_text.get()

        player = int(player_id_text.get())
        query = f"""update Player set
        firstName = '{new_fname}',
        lastName = '{new_lname}',
        position = '{new_pos}',
        atbats = '{new_atbat}',
        hits = '{new_hits}'
        where playerID = '{player}'
        """

        conn = sqlite3.connect('Baseball.sqlite')
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        conn.close()

        player_id_text.set("")
        first_name_text.set("")
        last_name_text.set("")
        position_text.set("")
        atbat_text.set("")
        hits_text.set("")
        bat_avg_text.set("")

    except ValueError:
        messagebox.showerror("Player ID not found.", "Please enter a valid integer.")


# Window
GUI_win = tk.Tk()
GUI_win.title("Player")
GUI_win.geometry("350x250")
frame = ttk.Frame(GUI_win, padding="10 10 10 10")
frame.pack()

# Buttons
get_player = tk.Button(frame, text="Get Player", command=get_player_button)
save = tk.Button(frame, text="Save Changes", command=save_button)
cancel = tk.Button(frame, text="Cancel", command=get_player_button, padx=10)
get_player.grid(row=0, column=2, sticky=tk.E)
save.grid(row=7, column=1, sticky=tk.W)
cancel.grid(row=7, column=1, sticky=tk.E)

# Player ID
player_id = ttk.Label(frame, text="Player ID:")
player_id.grid(column=0, row=0, sticky=tk.E)
player_id_text = tk.StringVar()
player_id_entry = ttk.Entry(frame, width=25, textvariable=player_id_text)
player_id_entry.grid(column=1, row=0, sticky=tk.E)

# First Name
first_name = ttk.Label(frame, text="First Name:")
first_name.grid(column=0, row=1, sticky=tk.E)
first_name_text = tk.StringVar()
first_name_entry = ttk.Entry(frame, width=25, textvariable=first_name_text)
first_name_entry.grid(column=1, row=1, sticky=tk.E)

# Last Name
last_name = ttk.Label(frame, text="Last Name:")
last_name.grid(column=0, row=2, sticky=tk.E)
last_name_text = tk.StringVar()
last_name_entry = ttk.Entry(frame, width=25, textvariable=last_name_text)
last_name_entry.grid(column=1, row=2, sticky=tk.E)

# Position
position = ttk.Label(frame, text="Position:")
position.grid(column=0, row=3, sticky=tk.E)
position_text = tk.StringVar()
position_entry = ttk.Entry(frame, width=25, textvariable=position_text)
position_entry.grid(column=1, row=3, sticky=tk.E)

# At bats
atbat = ttk.Label(frame, text="At bats:")
atbat.grid(column=0, row=4, sticky=tk.E)
atbat_text = tk.StringVar()
atbat_entry = ttk.Entry(frame, width=25, textvariable=atbat_text)
atbat_entry.grid(column=1, row=4, sticky=tk.E)

# Hits
hits = ttk.Label(frame, text="Hits:")
hits.grid(column=0, row=5, sticky=tk.E)
hits_text = tk.StringVar()
hits_entry = ttk.Entry(frame, width=25, textvariable=hits_text)
hits_entry.grid(column=1, row=5, sticky=tk.E)

# Batting Avg
bat_avg = ttk.Label(frame, text="Batting Avg:")
bat_avg.grid(column=0, row=6, sticky=tk.E)
bat_avg_text = tk.StringVar()
bat_avg_entry = ttk.Entry(frame, width=25, textvariable=bat_avg_text, state='readonly')
bat_avg_entry.grid(column=1, row=6, sticky=tk.E)


for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)


if __name__ == "__main__":
    GUI_win.mainloop()
