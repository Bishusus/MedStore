def generate_purchase_invoice(purchased_medicines):
    """
    This function generates a purchase invoice for the customer based on
    the list of purchased medicines.

    Parameters:
        purchased_medicines (list): List of dictionaries containing medicine details.
    """

    # if no medicines were purchased, no invoice is created
    if not purchased_medicines:
        return

    overall_total_cost = 0  # stores final total of all items

    # create filename using customer name and date for uniqueness
    filename = (
        purchased_medicines[0]["name_of_customer"].replace(" ", "_") + "_" +
        purchased_medicines[0]["date_of_purchase"].replace(" ", "_").replace(":", "-")
    )

    # invoice layout settings
    width = 110
    title = "MedStore PVT. LTD."
    spacing = (width - len(title)) // 2  # used to center the title

    # create and write invoice file
    with open("textFiles/purchaseFolder/" + filename + ".txt", "w") as file:

        # invoice header
        file.write("=" * width + "\n")
        file.write(f"{spacing * ' '}{title}{spacing * ' '}\n")
        file.write("=" * width + "\n\n")

        # customer details
        file.write(f"Customer Name : {purchased_medicines[0]['name_of_customer']}\n")
        file.write(f"Date          : {purchased_medicines[0]['date_of_purchase']}\n")
        file.write("-" * width + "\n\n")

        # formatted table header for invoice items
        file.write(
            f"{'Medicine Name':<25} | {'Brand':<20} | {'Unit':<10} | "
            f"{'Quantity':<15} | {'Discount':<15} | {'Total Cost':<15}\n"
        )
        file.write("-" * width + "\n")

        # write each purchased item to invoice
        for item in purchased_medicines:
            file.write(
                f"{item['name']:<25} | {item['brand']:<20} | {item['unit_type']:<10} | "
                f"{item['quantity_sold']:<15} | {item['discount']:<15} | {item['total_cost']:<15}\n"
            )

            # calculate grand total
            overall_total_cost += item["total_cost"]

        file.write("-" * width + "\n")

        # write final total amount
        file.write(f"\nGrand Total   : {overall_total_cost}\n")
        file.write("=" * width + "\n")