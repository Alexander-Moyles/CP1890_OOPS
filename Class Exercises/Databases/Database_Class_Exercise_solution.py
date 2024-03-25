import sqlite3
from Database_Class_Exercise_Objects import Category, Movie


def connect_to_db():
    db_file = "movies.sqlite"
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

def close(conn):
    if conn:
        conn.close()

def make_category(row):
    return Category(row['categoryID'], row['categoryName'])

def make_movie(row):
    return Movie(row['movieID'], row['name'], row['year'], row['minutes'], make_category(row))

def get_categories(conn):
    try:
        query = '''SELECT categoryID, categoryName FROM Category'''
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()

        categories = []
        for row in results:
            categories.append(make_category(row))
        return categories
    except:
        return(Category(1, "Animation"), Category(2, "Comedy"), Category(3, "History"))

def get_category(conn, category_id):
    try:
        query = '''SELECT categoryID, name as categoryName from Category WHERE categoryID = ?'''
        cur = conn.cursor()
        cur.execute(query, (category_id,))
        row = cur.fetchone()
        if row:
            return make_category(row)
        else:
            return None
    except:
        pass


def make_movie_list(list_movies):
    movies = []
    for row in list_movies:
        movies.append(make_movie(row))
    return movies

def get_movies_by_category(conn, category_id):
    query = '''SELECT movieID,Movie.name, year, minutes,Movie.categoryID, Category.name as categoryName FROM Movie JOIN Category ON Movie.categoryID = Category.categoryID WHERE Movie.categoryID = ?'''
    cur = conn.cursor()
    cur.execute(query, (category_id,))
    results = cur.fetchall()

    return make_movie_list(results)

def insert_movie(conn, movie):
    query = '''INSERT INTO Movie (categoryID, name, year, minutes) VALUES (?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(query, (movie.category.id, movie.name, movie.year, movie.minutes))
    conn.commit()

def display_welcome():
    print("The Movie List program")
    print()
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("cat - ")
    print("year - ")
    print("add - ")
    print("del = ")
    print("exit - ")
    print()

def display_categories(conn):
    print("CATEGORIES")
    categories = get_categories(conn)
    for category in categories:
        print(f"{category.id}.  {category.name}")
    print()

def add_movie(conn):
    name = input("Name: ")
    year = int(input("Year: "))
    minutes = int(input("Minutes: "))
    category_id = int(input("Category ID: "))

    movie = Movie(name, year, minutes, category_id)
    insert_movie(conn, movie)
    print(f"{name} was added to the database. \n")

def main():
    conn = connect_to_db()
    display_welcome()
    display_categories(conn)
    while True:
        command = input("Command: ").lower()
        if command == "add":
            add_movie(conn)
        elif command == "cat":
            pass
        elif command == "exit":
            break
        else:
            print("Not a valid command. Try again. \n")
            display_menu()
    close(conn)
    print("Bye!")


if __name__ == "__main__":
    main()
