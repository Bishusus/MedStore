# importing all the functions from the respective files
from medstore.print_table import print_to_cli
from medstore.purchase_medicines import purchase, divider
from medstore.generate_purchase_invoice import generate_purchase_invoice
from medstore.restock_medicines import restock_medicines
from medstore.generate_restock_invoice import generate_restock_invoice
from medstore.update_inventory import update_inventory

def main():
    """
    The main entry point of the program. 
    It handles user interactions, calls the necessary functions based on user input 
    and updates the inventory accordingly.
    """

    # Display current inventory to the user
    print_to_cli()
    purchased_medicines = []
    restock_list = []

    divider()

    # Prompt user to select an option: Buy, Restock, or Display
    print("Please select an option:")
    print("0. Buy")
    print("1. Restock")
    print("2. Display")

    name = input("Type 0 to buy 1 to restock and 2 to display: ")
    
    # validate user input and call the corresponding functions
    try:
        name = int(name)
    except ValueError:
        print("Please enter the valid number choice")
        return

    match name:
        case 0:
            purchased_medicines = purchase()
            generate_purchase_invoice(purchased_medicines)
        case 1:
            restock_list = restock_medicines()
            generate_restock_invoice(restock_list)
        case 2:
            print_to_cli()
        case _:
            print("Please enter a valid number")

    update_inventory(purchased_medicines, restock_list)


main()