import Question_1_Classes as Q1

def menu():
    """
    Prints title and menu options for programs.
    """
    print("Product Manager\n")

    print("Categories\nGuitars | Basses | Drums\n")

    print("COMMAND MENU")
    print(f"{'view'} - View products by category")
    print(f"{'update'} - Update product price")
    print(f"{'exit'} - Exit program")


def view():
    pass


def update():
    pass


def main():
    while True:
        command = input("Enter command: ").lower()
        if command == "view":
            view()
            print("")
        elif command == "update":
            update()
            print("")
        elif command == "exit":
            break
        else:
            print("Invalid command, try again.")
            print("")


if __name__ == "__main__":
    main()
