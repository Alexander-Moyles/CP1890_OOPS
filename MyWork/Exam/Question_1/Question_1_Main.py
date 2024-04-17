import Question_1_Classes as Q1
import Question_1_SQL as SQL


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
    """
    Prints all products of chosen category.
    """
    cat_id = 0
    categories = Q1.CategoryList()
    categories.create()
    prod_list = Q1.ProductList()

    category = input("Category Name: ").title()

    for cat in categories.catList:
        if category == cat.name:
            cat_id = int(cat.catID)

    if cat_id == 0:
        print("Category Not Found")
    else:
        prod_list.create(cat_id)
        print(f"{'Code':<12}{'Name':<40}{'Price'}")
        print('-' * 60)
        for product in prod_list.products:
            print(f"{product}")


def update():
    """
    Updates the price of chosen product.
    """
    prod_codes = SQL.product_codes()
    code = str(input("Product code: "))
    check = 0

    for prod_code in prod_codes:
        if code == prod_code[0]:
            check = 1

    if check == 1:
        while True:
            try:
                price = float(input("New product price: "))
                break
            except ValueError:
                print("Invalid decimal, try again.")

        SQL.update(code, price)
        print("Product updated.")
    else:
        print("Product code not found.")


def main():
    """
    Main function, takes user inputs for commands and calls functions for those commands.
    """
    menu()
    while True:
        command = input("\nEnter command: ").lower()
        if command == "view":
            view()
        elif command == "update":
            update()
        elif command == "exit":
            break
        else:
            print("Invalid command, try again.")
    print("Bye!")


if __name__ == "__main__":
    main()
