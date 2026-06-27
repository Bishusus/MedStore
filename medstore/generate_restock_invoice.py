def generate_restock_invoice(restock_list):
    """
    This function generates a restock invoice for the vendor based on
    the list of restocked medicines.

    Parameters:
        restock_list (list): List of dictionaries containing restock details.
    """

    # if no restock data exists, no invoice is generated
    if not restock_list:
        return

    overall_total_cost = 0  # stores final total of all restocked items

    # create filename using vendor name and date for uniqueness
    filename = (
        restock_list[0]["vendor_name"].replace(" ", "_") + "_" +
        restock_list[0]["date_of_restock"].replace(" ", "_").replace(":", "-")
    )

    # invoice layout settings
    width = 110
    title = "MedStore PVT. LTD."
    spacing = (width - len(title)) // 2  # used to center invoice title

    # open file to write restock invoice
    with open("textFiles/restockFolder/" + filename + ".txt", "w") as file:

        # invoice header section
        file.write("=" * width + "\n")
        file.write(f"{spacing * ' '}{title}{spacing * ' '}\n")
        file.write("=" * width + "\n\n")

        # vendor details section
        file.write(f"Vendor Name   : {restock_list[0]['vendor_name']}\n")
        file.write(f"Date          : {restock_list[0]['date_of_restock']}\n")
        file.write("-" * width + "\n\n")

        # formatted table header for restock items
        file.write(
            f"{'Medicine Name':<25} | {'Brand':<20} | {'Unit':<10} | "
            f"{'Quantity':<15} | {'Rate':<15} | {'Total Cost':<15}\n"
        )
        file.write("-" * width + "\n")

        # write each restocked item to invoice
        for item in restock_list:
            file.write(
                f"{item['name']:<25} | {item['brand']:<20} | {item['unit_type']:<10} | "
                f"{item['quantity']:<15} | {item['rate']:<15} | {item['total_cost']:<15}\n"
            )

            # calculate grand total
            overall_total_cost += item["total_cost"]

        file.write("-" * width + "\n")

        # write final total amount
        file.write(f"\nGrand Total   : {overall_total_cost}\n")
        file.write("=" * width + "\n")