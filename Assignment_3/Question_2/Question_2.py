"""
Assignment 3

Question 2 - Main User Interface.
"""
import Question_2_Functions as Func


def title_menu():
    """
    Prints out title and command menu.
    """
    print("Player Manager")
    print(f"\nCOMMAND MENU\n{'view':>6} - View players")
    print(f"{'add':>6} - Add a player\n{'del':>6} - Delete a player")
    print(f"{'update':>6} - Update a player's stats\n{'exit':>6} - Exit program\n")


def main():
    """
    Main function/UI, calls other functions/classes from 2nd file.
    """
    title_menu()
    while True:
        command = input("Command: ").lower()
        if command == "view":
            Func.player_list.view_players()
            print("")
        elif command == "add":
            name = input("Name: ")
            wins, losses, ties = Func.get_int()
            Func.player_list.add_player(name, wins, losses, ties)
            print("")
        elif command == "del":
            Func.player_list.del_player(input("Name: "))
            print("")
        elif command == "update":
            name = input("Name: ")
            wins, losses, ties = Func.get_int()
            Func.player_list.update_player(name, wins, losses, ties)
            print("")
        elif command == "exit":
            break
        else:
            print("\nInvalid command, try again.")
    print("Bye!")


if __name__ == "__main__":
    main()
