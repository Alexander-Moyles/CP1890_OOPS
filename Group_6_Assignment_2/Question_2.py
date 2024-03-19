"""
Assignment 2

Question 2
"""

from Classes import RandomIntList

def main():
    print("Random Integer List")
    
    while True:
        try:
            num = int(input("\nHow many random integers should the list contain?: "))
            break
        except ValueError:
            print("Invalid integer, try again.")
    
    while True:
        int_list = RandomIntList(num)
    
        print("\nRandom Integers\n================")
        print(f"{'Integers:':12}{int_list}")
        print(f"{'Count:':12}{int_list.count}")
        print(f"{'Total:':12}{int_list.total}")
        print(f"{'Average:':12}{int_list.average:.3f}")
    
        cont = contin()
        if cont == 'n':
            break
        elif cont == 'y':
            continue

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
