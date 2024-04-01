import tkinter as tk
from tkinter import ttk
import sqlite3
from dataclasses import dataclass


@dataclass
class Player:
    playerID: int
    batOrder: int
    firstName: str = ''
    lastName: str = ''
    position: str = ''
    atBats: int = 0
    hits: int = 0

    @property
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @property
    def battingAvg(self) -> float:
        try:
            avg = self.hits / self.atBats
            return avg
        except ZeroDivisionError:
            return 0.0

    def __str__(self):
        return f"{self.playerID:5}{self.batOrder:5}{self.fullName:40}{self.position:6}{self.atBats:>6d}{self.hits:>8d}{self.avg:>10.3f}"


class Lineup:
    def __init__(self):
        self.__players = []

        conn = sqlite3.connect('Baseball.sqlite')
        c = conn.cursor()
        c.execute("select * from Player")
        rows = c.fetchall()
        conn.close

        for row in rows:
            if row is not None:
                self.__players.append(row)

    @property
    def player_count(self):
        return len(self.__players)

    def __iter__(self):
        for player in self.__players:
            yield str(player)



def title():
    print("=" * 75)
    print("\t\t\t\t\tBaseball Team Manager")

    print("MENU OPTIONS")
    print("1 - Display lineup\n2 - Add player\n3 - Remove player")
    print("4 - Update batting order\n5 - Update player data\n6 - Exit\n")
    position = "positions\nC, 1B, 2B, 3b, ss, lf, cf, rf, f"
    print(position.upper())
    print("=" * 75)


def get_pos():
    pos_list = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'F']
    while True:
        pos = input("Position: ").upper()
        if pos not in pos_list:
            print(f"Invalid position.\n Valid positions: {pos_list}")
        else:
            return pos


def get_at_bats():
    while True:
        try:
            at_bats = int(input("At Bats: "))
        except ValueError:
            print("Invalid integer.")
            continue

        if at_bats < 0 or at_bats > 5000:
            print("Invalid entry.")
        else:
            return at_bats


def get_hits(at_bats):
    while True:
        try:
            hits = int(input("Hits: "))
        except ValueError:
            print("Invalid integer.")
            continue

        if hits < 0 or hits > at_bats:
            print("Invalid entry.")
        else:
            return hits


def add():
    lineup = Lineup()
    first_name = str(input("First name: "))
    last_name = str(input("Last name: "))
    pos = get_pos()
    bats = get_at_bats()
    hits = get_hits(bats)

    newid = lineup.player_count + 1

    query2 = f"INSERT INTO Player VALUES ({newid}, {newid}, '{first_name}', '{last_name}', '{pos}', {bats}, {hits});"

    conn = sqlite3.connect('Baseball.sqlite')
    c = conn.cursor()
    c.execute(query2)
    conn.commit()
    conn.close()

    print("Player was added.")

def player_list():
    print(f"{'ID':5}{'BO':5}{'Fname':12}{'Lname':12}{'POS':>6}{'AB':>8}{'H':>10}")
    print("-" * 75)

    conn = sqlite3.connect('Baseball.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM Player;")
    rows = c.fetchall()
    conn.close()

    for row in rows:
        if row != None:
            print(f"{row[0]:<5}{row[1]:<5}{row[2]:12}{row[3]:12}{row[4]:>6}{row[5]:>8}{row[6]:>10}")
    print()


def num(check):
    if check == 1:
        prnt = "Enter player ID: "
    elif check == 2:
        prnt = "Enter new bat order number: "

    while True:
        try:
            player_id = int(input(prnt))
            break
        except ValueError:
            print("Invalid integer.")
            continue

    return player_id


def update_bat():
    player_id = num(1)
    new_order = num(2)

    query = f"UPDATE Player SET batOrder = {new_order} WHERE playerID = {player_id}"

    conn = sqlite3.connect('Baseball.sqlite')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

    print("\nBat Order Updated")


def update_stat():
    player_id = num(1)
    pos = get_pos()
    bats = get_at_bats()
    hits = get_hits(bats)

    query = f"UPDATE Player SET position = '{pos}', atBats = {bats}, hits = {hits} WHERE playerID = {player_id}"

    conn = sqlite3.connect('Baseball.sqlite')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

    print("\nPlayer Stats Updated")


def remove():
    player_id = num(1)
    query = "DELETE FROM Player WHERE playerID = '{}'".format(player_id)

    conn = sqlite3.connect('Baseball.sqlite')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

    print("Player Deleted")


def main():
    title()
    print("")
    menu = 0
    while menu != 6:
        menu = int(input("Menu option: "))
        if menu == 1:
            # Display Lineup
            print()
            player_list()
        elif menu == 2:
            # Add Player
            print()
            add()
        elif menu == 3:
            # Remove Player
            print()
            remove()
        elif menu == 4:
            # Update batting order
            print()
            update_bat()
        elif menu == 5:
            # Update player data
            print()
            update_stat()
        elif menu == 6:
            # Exit
            break
        else:
            print("Invalid entry, please try again.")
            menu = int(input("\nMenu option: "))
    print("Bye!")


if __name__ == "__main__":
    main()
