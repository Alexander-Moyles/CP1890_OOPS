import sqlite3


def view_prod(cat: int):
    """
    Returns all products in database based on category.

    :param cat:
    :return rows:
    """
    conn = sqlite3.connect('SQL/guitar_shop.sqlite')
    c = conn.cursor()
    c.execute(f"SELECT productCode, productName, listPrice FROM Product where categoryID = {cat}")
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


def update(code, price):
    """
    Updates the price for the selected product based on code.

    :param code:
    :param price:
    """
    conn = sqlite3.connect('SQL/guitar_shop.sqlite')
    c = conn.cursor()
    c.execute(f"update Product set listPrice = {price} where productCode = '{code}'")
    conn.commit()
    conn.close()


def product_codes():
    """
    Returns all products in database based on category.

    :param cat:
    :return rows:
    """
    conn = sqlite3.connect('SQL/guitar_shop.sqlite')
    c = conn.cursor()
    c.execute(f"SELECT productCode FROM Product")
    rows = c.fetchall()
    conn.close()
    return rows
