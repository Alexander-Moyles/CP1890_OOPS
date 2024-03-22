import sqlite3


conn = sqlite3.connect('movies.sqlite')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='movies';")
result = c.fetchall()

if result == [('movies',)]:
    conn.close()
else:
    query = "CREATE TABLE IF NOT EXISTS movies (id INTEGER AUTO INCREMENT PRIMARY KEY, `name` TEXT, year INTEGER, minutes INTEGER, category TEXT);"
    c.execute(query)

    # len = 32
    c.execute("""insert into movies (id, name, year, minutes, category)
    values (1, 'Spirit: Stallion of the Cimarron', 2002, 83, 'Animation'),
    (2, 'Spirited Away', 2001, 125, 'Animation'),
    (3, 'Aladdin', 1992, 90, 'Animation'),
    (4, 'Ice Age', 2002, 81, 'Animation'),
    (5, 'Toy Story', 1995, 81, 'Animation'),
    (6, 'Titanic', 1998, 93, 'History'),
    (7, 'Transformers', 2005, 100, 'Comedy'),
    (8, 'Spooky Movie', 1995, 81, 'Comedy'),
    (9, 'Spookier Movie', 1999, 95, 'Comedy'),
    (10, 'Spookiest Movie', 2003, 94, 'Comedy'),
    (11, 'WWII: A History', 2006, 109, 'History'),
    (12, 'Movie Title', 2007, 100, 'Comedy'),
    (13, 'Why 13', 2009, 86, 'Comedy');""")
    conn.commit()
    conn.close()


def menu():
    print("\nCOMMAND MENU")
    print("cat - View movies by category")
    print("year - View movies by year")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")


def categories():
    print("\nCATEGORIES")
    print("1. Animation\n2. Comedy\n3. History")


def main():
    print("The Movie List Program")

    menu()
    categories()

    while True:
        com = input("\nCommand: ")
        if com == "cat":
            sort_cat()
        elif com == "year":
            sort_year()
        elif com == "add":
            add_movie()
        elif com == "del":
            del_movie()
        elif com == "exit":
            break
        else:
            print("\nInvalid input, try again")

def sort_cat():
    qcheck = 0
    while qcheck == 0:
        id = input("Category ID: ")
        if id == '1':
            query2 = "select * from movies where category = 'Animation';"
            qcheck = 1
        elif id == '2':
            query2 = "SELECT * FROM movies WHERE category = 'Comedy';"
            qcheck = 2
        elif id == '3':
            query2 = "SELECT * FROM movies WHERE category = 'History';"
            qcheck = 3
        else:
            print("\nInvalid input, try again")
    conn = sqlite3.connect('movies.sqlite')
    c = conn.cursor()
    c.execute(query2)
    rows = c.fetchall()
    conn.close

    if qcheck == 1:
        cat = "Animation"
    elif qcheck == 2:
        cat = "Comedy"
    elif qcheck == 3:
        cat = "History"

    print(f"MOVIES {cat}")
    print(f"{'ID':<5}{'Name':<36}{'Year':<8}{'Mins':<8}{'Category':<10}")
    print('-' * 75)
    for row in rows:
        if row != None:
            print(f"{row[0]:<5d}{row[1]:<36}{row[2]:<8d}{row[3]:<8d}{row[4]:<10}")

def add_movie():
    name = input("Name: ")
    year = year_get()
    while True:
        try:
            min = int(input("Minutes: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    while True:
        try:
            cat_id = int(input("Category ID: "))
            if cat_id == 1 or cat_id == 2 or cat_id == 3:
                break
            else:
                print("Please enter a valid ID")
                categories()
                print()
        except ValueError:
            print("Please enter a valid ID")
            categories()
            print()

    if cat_id == 1:
        category = 'Animation'
    elif cat_id == 2:
        category = 'Comedy'
    elif cat_id == 3:
        category = 'History'

    query3 = """INSERT INTO movies (name, year, minutes, category)
    VALUES ('{}', {}, {}, '{}')""".format(name, year, min, category)

    conn = sqlite3.connect('movies.sqlite')
    c = conn.cursor()
    c.execute(query3)
    conn.commit()
    conn.close

def year_get():
    while True:
        try:
            year = int(input("Year: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    return year

def sort_year():
    year = year_get()

    query4 = "SELECT * FROM movies where year = {}".format(year)

    conn = sqlite3.connect('movies.sqlite')
    c = conn.cursor()
    c.execute(query4)
    rows = c.fetchall()
    conn.close

def del_movie():
    query5 = "DELETE FROM movies where id = {}".format(int(input("Movie ID: ")))

    conn = sqlite3.connect('movies.sqlite')
    c = conn.cursor()
    c.execute(query5)
    conn.commit()
    print("Movie has been deleted.")
    conn.close

if __name__ == "__main__":
    main()
