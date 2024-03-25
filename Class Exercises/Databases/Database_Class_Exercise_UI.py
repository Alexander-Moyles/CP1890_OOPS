from Database_Class_Exercise_Objects import Category, Movie
import Database_Class_Exercise_dbfunctions as db


def display_welcome():
    print("The Movie List program")
    print()
    display_menu()


def display_menu():
    print("COMMAND MENU")
    print("cat - View movies by category ")
    print("year - View movies by year")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()


def display_categories(connection):
    print("Categories")
    categories = db.get_categories(connection)
    for category in categories:
        print(f"{category['id']}. {category['name']}")
    print()


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number")


def display_movies(movies, title_term):
    print(f"MOVIES - {title_term}")
    print(f"{'ID':4}{'Name':38}{'Year':6}{'Mins':6}{'Category':10}")
    print('-'*63)
    for movie in movies:
        print(f"{movie.id:<4d}{movie.name:38}{movie.year:<6d}{movie.minutes:<6d}{movie.category.name:10}")
    print()


def display_movies_by_category(connection):
    category_id = get_int("Category ID: ")
    category = db.get_category_name(connection, category_id)
    if category is None:
        print("Invalid category specified")
    else:
        movies = db.get_movies_by_category(connection, category_id)
        display_movies(movies, category.upper())


def add_movie(connection):
    name = input("Name: ")
    year = int(input("Year: "))
    minutes = int(input("Minutes: "))
    category_id = int(input("Category ID: "))

    category = db.get_category_name(connection, category_id)
    if category is None:
        print("Invalid category specified. Movie NOT added\n")
    else:
        movie = Movie(name=name, year=year, minutes=minutes, category=Category(category_id, category))
        db.add_movie(connection, movie)
        print(f"Added movie {name} to the database")


def main():
    conn = db.connect()
    display_welcome()
    display_categories(conn)
    while True:
        command = input("Command: ").lower()
        if command == 'cat':
            display_movies_by_category(conn)
        elif command == 'year':
            pass
        elif command == 'add':
            add_movie(conn)
        elif command == 'del':
            pass
        elif command == 'exit':
            break
        else:
            print("Invalid command. Please try again.\n")
            display_menu()

    db.close(conn)
    print("Bye!")


if __name__ == "__main__":
    main()
