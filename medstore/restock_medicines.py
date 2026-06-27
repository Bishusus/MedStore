import datetime

def restock_medicines():
    """
    Restock workflow for MedStore.
    Handles restocking medicines into inventory by taking user input,
    validating it, and storing restock records for invoice and updates.

    Returns:
        list: Restocked medicine details for invoice generation and inventory update.
    """

    # list to store all restock records in this session
    restock = []

    # store current date & time for restock tracking
    date_of_restock = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    space()
    divider()
    print("📦 Welcome to MedStore Restock System")
    divider()
    space()

    vendor_name = input("🏭 Please enter the name of the vendor: ")
    space()

    # main restock loop (allows multiple medicines until user exits)
    while True:
        medicine_name = input(
            "💊 Enter the name of the medicine you want to restock (or type 'exit'): "
        )

        # exit condition for restock process
        if medicine_name.replace(" ", "").lower() == "exit":
            space()
            print("🚪 Exiting restock system...")
            space()
            divider()
            print("🚪 System exited successfully.")
            divider()
            break

        # read inventory file to search for medicine
        with open("textFiles/pharmacy.txt", "r") as file:
            lines = file.readlines()

            for i in range(1, len(lines)):
                line = lines[i].replace("\n", "")
                data = line.split(",")

                # check if entered medicine exists in inventory
                if data[0].lower() == medicine_name.lower():

                    print(f"✔ Medicine found: {data[0]}")
                    space()

                    # validate unit type input (must be tablet or strip)
                    while True:
                        unit_type = input(
                            "📦 Do you want to restock by 'tablet' or 'strip'? "
                        ).replace(" ", "").lower()

                        if unit_type in ["tablet", "strip"]:
                            break
                        else:
                            print("❌ Invalid input. Please enter 'tablet' or 'strip'.")

                    # validate quantity input (must be positive integer)
                    while True:
                        try:
                            quantity = int(input("🔢 Enter the quantity you want to restock: "))

                            if quantity <= 0:
                                print("⚠ Quantity must be greater than 0.")
                                continue

                            break

                        except ValueError:
                            print("❌ Invalid input. Please enter a valid number.")

                    space()

                    # decide rate based on selected unit type
                    if unit_type == "tablet":
                        rate = int(data[3])
                    else:
                        rate = int(data[4])

                    found = False  # checks if medicine already exists in restock list

                    # update existing entry if same medicine + unit type found
                    for item in restock:
                        if item["name"] == data[0] and item["unit_type"] == unit_type:
                            item["quantity"] += quantity
                            item["total_cost"] += quantity * rate
                            found = True
                            break

                    # add new entry if not already in list
                    if not found:
                        restock.append({
                            "name": data[0],
                            "brand": data[1],
                            "quantity": quantity,
                            "unit_type": unit_type,
                            "rate": rate,
                            "vendor_name": vendor_name,
                            "date_of_restock": date_of_restock,
                            "total_cost": quantity * rate
                        })

                    break

            else:
                print("❌ Medicine not found.")
                space()

    # show success message if any restock was done
    if restock:
        space()
        print("🎉 Restock Successful!")

    return restock


# prints line separator for CLI formatting
def divider():
    print("=" * 50)


# prints blank line for spacing
def space():
    print()