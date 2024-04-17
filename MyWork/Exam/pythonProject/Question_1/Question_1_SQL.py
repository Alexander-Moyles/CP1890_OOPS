import sqlite3


def view_prod(cat: int):
    """
    Returns all products in database based on category.

    :param cat:
    :return rows:
    """
    conn = sqlite3.connect('SQL/guitar_shop.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM Product where categoryID = {cat}")
    rows = c.fetchall()
    conn.close()
    return rows


def get_categories():
    """
    Returns all categories in database.

    :return rows:
    """
    conn = sqlite3.connect('SQL/guitar_shop.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM Category")
    rows = c.fetchall()
    conn.close()
    return rows


def update():
    pass
