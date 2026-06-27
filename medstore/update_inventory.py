def update_inventory(purchased_medicines, restock_list):
    """
    This function updates the inventory in the pharmacy.txt file based on
    purchased medicines and restocked medicines.

    Parameters:
        purchased_medicines (list): List of dictionaries for purchased items.
        restock_list (list): List of dictionaries for restocked items.
    """

    # store current inventory data from file
    inventory = []

    # read inventory file
    with open("textFiles/pharmacy.txt", "r") as file:
        lines = file.readlines()

        for i in range(len(lines)):
            line = lines[i].replace("\n", "")
            data = line.split(",")  # split CSV format into list
            inventory.append(data)

    # update inventory after purchases (reduce stock)
    for item in purchased_medicines:
        # loop through inventory items (skip header)
        for i in range(1, len(inventory)):

            # match medicine name
            if inventory[i][0] == item["name"]:

                # update stock based on unit type
                if item["unit_type"] == "strip":
                    inventory[i][2] = str(
                        int(inventory[i][2]) -
                        item["quantity_sold"] * int(inventory[i][5])
                    )
                else:
                    inventory[i][2] = str(
                        int(inventory[i][2]) - item["quantity_sold"]
                    )

    # update inventory after restock (increase stock)
    for item in restock_list:
        # loop through inventory items (skip header)
        for i in range(1, len(inventory)):

            # match medicine name
            if inventory[i][0] == item["name"]:

                # update stock based on unit type
                if item["unit_type"] == "strip":
                    inventory[i][2] = str(
                        int(inventory[i][2]) +
                        item["quantity"] * int(inventory[i][5])
                    )
                else:
                    inventory[i][2] = str(
                        int(inventory[i][2]) + item["quantity"]
                    )

    # write updated inventory back to file
    with open("textFiles/pharmacy.txt", "w") as file:
        for item in inventory:
            file.write(",".join(item) + "\n")