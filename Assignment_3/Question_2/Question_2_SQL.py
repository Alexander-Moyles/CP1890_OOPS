"""
Assignment 3

Question 2 - SQL related Functions / Commands.
"""

import sqlite3


def view():
    """
    Selects all players from the database by highest wins.
    """
    conn = sqlite3.connect('Question2_Supporting_Files/player_db.sqlite')
    c = conn.cursor()
    c.execute("SELECT * from Player order by wins desc;")
    rows = c.fetchall()
    conn.close()

    return rows


def add(player_name, player_wins, player_losses, player_ties):
    """
    Adds a player to the database.
    """
    query = f"""INSERT INTO Player (name, wins, losses, ties)
    VALUES ('{player_name}', '{player_wins}', '{player_losses}', '{player_ties}')
    """

    conn = sqlite3.connect('Question2_Supporting_Files/player_db.sqlite')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


def delete(player_name):
    """
    Deletes a player from the database.
    """
    query = f"DELETE from Player WHERE name = '{player_name}'"

    conn = sqlite3.connect('Question2_Supporting_Files/player_db.sqlite')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


def update(player_name, player_wins, player_losses, player_ties):
    """
    Updates a player's stats.
    """
    query = f"""update Player set
    wins = '{player_wins}',
    losses = '{player_losses}',
    ties = '{player_ties}'
    where name = '{player_name}'"""

    conn = sqlite3.connect('Question2_Supporting_Files/player_db.sqlite')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()
