import datetime

def purchase():
    """
    Purchase workflow for MedStore.
    Handles customer purchasing process including:
    - input validation
    - medicine selection
    - cost calculation
    - invoice preparation

    Returns:
        list: Purchased items for invoice generation and inventory update
    """

    # list to store all purchased medicines in this session
    purchase = []

    # store current date & time for invoice records
    purchase_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    space()
    divider()
    print("👋 Welcome to MedStore! We are glad to serve you.")
    divider()

    print("💊 Get 5% discount by purchasing 2 strips or more worth of tablets!")
    space()

    name = input("👤 Please enter your name: ")

    # validate age before allowing purchase
    while True:
        try:
            age = int(input("🎂 Please enter your age: "))
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid age.")

    # restrict age range for purchase
    if age < 18 or age > 110:
        print("🚫 Sorry, you must be between 18 and 110 to purchase.")
        return []

    space()

    # main purchase loop (user can buy multiple medicines in one session)
    while True:
        medicine_name = input("💊 Enter medicine name (or type 'exit'): ")

        # exit purchase process
        if medicine_name.replace(" ", "").lower() == "exit":
            space()
            print("🚪 Exiting Purchase System...")
            space()
            divider()
            print("🙏 Thank you for visiting MedStore.")
            divider()
            break

        # read inventory file
        with open("textFiles/pharmacy.txt", "r") as file:
            lines = file.readlines()

            for i in range(1, len(lines)):
                line = lines[i].replace("\n", "")
                data = line.split(",")

                # check if medicine matches input
                if data[0].lower() == medicine_name.lower():

                    print(f"✔ Medicine found: {data[0]}")
                    space()

                    # choose purchase type
                    while True:
                        type_of_purchase = input(
                            "🧾 Do you want to purchase by tablet or strip: "
                        ).replace(" ", "").lower()

                        if type_of_purchase in ["tablet", "strip"]:
                            break
                        else:
                            print("❌ Invalid input. Please enter 'tablet' or 'strip'.")

                    # tablet purchase logic
                    if type_of_purchase == "tablet":
                        unit_type = "tablet"
                        rate_per_tablet = int(data[3])
                        tablets_per_strip = int(data[5])

                        print("💰 Rate per tablet is:", rate_per_tablet)

                        # validate tablet quantity
                        while True:
                            try:
                                quantity = int(input(
                                    "🔢 Enter the quantity of tablets you want to purchase: "
                                ))

                                if quantity <= 0 or quantity > int(data[2]):
                                    print("⚠ Invalid quantity. Please enter a valid stock range.")
                                    continue

                                break

                            except ValueError:
                                print("❌ Invalid input. Please enter a valid quantity.")

                        total_cost = quantity * rate_per_tablet
                        strips_equivalent = quantity / tablets_per_strip

                        # apply discount if eligible
                        if strips_equivalent >= 2:
                            total_cost -= total_cost * 0.05
                            discount = "5%"
                        else:
                            discount = "0%"

                    # strip purchase logic
                    elif type_of_purchase == "strip":
                        unit_type = "strip"
                        rate_per_strip = int(data[4])
                        tablets_per_strip = int(data[5])

                        print("💰 Rate per strip is:", rate_per_strip)
                        print("💊 Tablets per strip:", tablets_per_strip)

                        # validate strip quantity
                        while True:
                            try:
                                quantity = int(input(
                                    "🔢 Enter the quantity of strips you want to purchase: "
                                ))

                                total_quantity = quantity * tablets_per_strip

                                if total_quantity <= 0 or total_quantity > int(data[2]):
                                    print("⚠ Invalid quantity. Please enter a valid stock range.")
                                    continue

                                break

                            except ValueError:
                                print("❌ Invalid input. Please enter a valid quantity.")

                        total_cost = quantity * rate_per_strip

                        # apply discount if eligible
                        if quantity >= 2:
                            total_cost -= total_cost * 0.05
                            discount = "5%"
                        else:
                            discount = "0%"

                    space()
                    print(f"💵 Total cost: {total_cost}")
                    space()

                    confirmation = input(
                        "✅ Type 'yes' to confirm the purchase or 'no' to cancel: "
                    )

                    if confirmation.lower() == "no":
                        print("❌ Purchase cancelled.")
                        space()
                        break

                    print("🎉 Purchase confirmed. Thank you for shopping with us!")
                    space()

                    # check if item already exists in current purchase list
                    found = False

                    for item in purchase:
                        if item["name"] == data[0] and item["unit_type"] == unit_type:
                            item["quantity_sold"] += quantity
                            item["total_cost"] += total_cost
                            found = True
                            break

                    # add new entry if not already present
                    if not found:
                        purchase.append({
                            "name": data[0],
                            "brand": data[1],
                            "unit_type": unit_type,
                            "quantity_sold": quantity,
                            "name_of_customer": name,
                            "date_of_purchase": purchase_time,
                            "discount": discount,
                            "total_cost": total_cost
                        })

                    break

            else:
                print("❌ Medicine not found.")
                space()

    return purchase


# prints separator line for better CLI formatting
def divider():
    print("=" * 50)


# prints empty line for spacing in CLI output
def space():
    print()