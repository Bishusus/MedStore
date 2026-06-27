def print_to_cli():
    """
    This function prints the current inventory of medicines in a formatted table to the command line interface.
    """

    print("Welcome to MedStore Pvt. Ltd.")
    print("Available medicines:")

    #Print the formatted table header
    print(f"{'Name':^20} | {'Brand':^15} | {'Quantity':^10} | {'Rate/Tablet':^15} | {'Rate/Strip':^15} | {'Tablets/Strip':^15}")
    print("-" * 110)

    # Read the pharmacy inventory file and print each medicine's details in a formatted manner
    with open("textFiles/pharmacy.txt", "r") as file:
        lines = file.readlines()

        # Exclude the header line and print the details of each medicine in a formatted table
        for i in range(1, len(lines)):
             # Remove newline characters from the end of each line
            line = lines[i].replace("\n", "")

            # Split the line into components based on commas since the inventory file is comma-separated
            data = line.split(",") 

            print(f"{data[0]:<20} | {data[1]:<15} | {data[2]:<10} | {data[3]:<15} | {data[4]:<15} | {data[5]:<15}")

    print()