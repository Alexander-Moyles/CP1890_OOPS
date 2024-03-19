"""
Assignment 2

Question 1
"""

from Classes import Customer, Employee


def main():
    """
    Main code for program, calls data_entry function.
    """
    print("Customer/Employee Data Entry")
    cont = 'y'
    
    while cont == 'y':
        while True:
            pers_type = input("\nCustomer or employee? (c/e): ").lower()
            if pers_type == 'e' or pers_type == 'c':
                break
            else:
                print("\nInvalid input, try again.")
        
        entry = data_entry(pers_type)
        
        if isinstance(entry, Customer):
            print("\nCUSTOMER")
            print(f"{'Name:':<12}{entry.fullname}")
            print(f"{'Email:':<12}{entry.email}")
            print(f"{'Number:':<12}{entry.number}")
        elif isinstance(entry, Employee):
            print("\nEMPLOYEE")
            print(f"{'Name:':<12}{entry.fullname}")
            print(f"{'Email:':<12}{entry.email}")
            print(f"{'SSN:':<12}{entry.ssn}")
            
        cont = contin()
    
    print("\nBye!")


def data_entry(pers_type):
    """
    Takes user input to create class object

    Parameters
    ----------
    pers_type : str
        Lowercase c or e to determine type of object (Customer or Employee).

    Returns
    -------
    person : Customer / Employee
        Class object created from user input.

    """
    print("\nDATA ENTRY")
    name1 = input("First name: ").capitalize()
    name2 = input("Last name: ").capitalize()
    mail = input("Email: ").lower()
    if pers_type == 'c':
        num = input("Number: ")
        person = Customer(name1, name2, mail, num)
    elif pers_type == 'e':
        snum = input("SSN: ")
        person = Employee(name1, name2, mail, snum)
    return person

def contin():
    while True:
        cont = input("\nContinue? (y/n): ").lower()
        if cont == 'n' or cont == 'y':
            break
        else:
            print("\nInvalid input, try again.")
    return cont

if __name__ == "__main__":
    main()
