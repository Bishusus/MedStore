# 🏥 MedStore

A command-line pharmaceutical management system built with Python that enables customers to purchase medicines and vendors to restock inventory.

## 📋 Overview

MedStore is an online pharmaceutical service that provides a seamless experience for both customers and vendors. Customers can browse available medicines, purchase them individually or in bulk with discount support, while vendors can efficiently restock medicines to maintain optimal inventory levels. All transactions are tracked through automated invoice generation.

## ✨ Features

- **🛍️ Medicine Purchase System**: Customers can purchase medicines by individual tablets or strips with real-time inventory validation
- **💰 Discount System**: Automatic 5% discount when purchasing 2 or more strips or equivalent tablets
- **📦 Vendor Restocking**: Vendors can efficiently restock medicines to replenish inventory
- **🧾 Invoice Generation**: Automatic generation of detailed invoices for both purchases and restocking transactions
- **👥 Age Verification**: Safety feature ensuring only adults (18-110 years) can purchase
- **📊 Inventory Management**: Real-time inventory updates after each transaction
- **🎯 CLI Interface**: User-friendly command-line interface with intuitive navigation

## 🔧 How It Works

### Purchase Flow
1. Customer selects the "Buy" option from the main menu
2. Customer provides name and age (must be between 18-110)
3. Customer searches for desired medicine by name
4. Customer chooses purchase unit (tablet or strip)
5. Customer enters desired quantity with validation against available stock
6. System calculates total cost and applies 5% discount if eligible
7. Customer confirms the purchase
8. System generates a personalized invoice and updates inventory

### Restock Flow
1. Vendor selects the "Restock" option from the main menu
2. Vendor provides their company/vendor name
3. Vendor searches for medicine to restock
4. Vendor selects unit type (tablet or strip)
5. Vendor enters restock quantity
6. System records the transaction
7. Vendor can restock multiple medicines in one session
8. System generates restock invoice and updates inventory

## 📁 Architecture

```
medstore/
├── main.py                          # Entry point & main orchestration
├── medstore/
│   ├── print_table.py               # Display current inventory in formatted table
│   ├── purchase_medicines.py        # Handle customer purchase transactions
│   ├── generate_purchase_invoice.py # Create purchase invoices
│   ├── restock_medicines.py         # Handle vendor restocking transactions
│   ├── generate_restock_invoice.py  # Create restock invoices
│   └── update_inventory.py          # Update inventory after transactions
└── textFiles/
    ├── pharmacy.txt                 # CSV inventory file
    ├── purchaseFolder/              # Stores customer purchase invoices
    └── restockFolder/               # Stores vendor restock invoices
```

**main.py** - Entry point that orchestrates the entire application, handles user menu selection, and coordinates all modules.

**print_table.py** - Reads pharmacy inventory file and displays medicines in a formatted CLI table with details like brand, quantity, rates.

**purchase_medicines.py** - Manages the complete purchase workflow including input validation, medicine selection, cost calculation with discounts, and purchase confirmation.

**generate_purchase_invoice.py** - Generates formatted purchase invoices as text files with customer details, purchased items, and total cost breakdown.

**restock_medicines.py** - Handles vendor restocking workflow including medicine selection, quantity input, and maintains restock records.

**generate_restock_invoice.py** - Creates restock invoices for vendors showing restocked medicines, quantities, rates, and total cost.

**update_inventory.py** - Updates the pharmacy.txt inventory file by reducing stock for purchases and increasing stock for restocking based on unit types.

## 🚀 Basic Usage

### Installation

1. Clone the repository:
```
git clone https://github.com/Bishusus/medstore.git
cd medstore
```

2. Ensure you have Python 3.x installed

3. Run the application:
```
python main.py
```

### Using the Application

#### Main Menu
```
0. Buy         - Purchase medicines
1. Restock     - Restock medicines (vendor)
2. Display     - View current inventory
```

#### Example Purchase Session
```
Type 0 to buy 1 to restock and 2 to display: 0
Please enter your name: John Doe
Please enter your age: 25
Enter medicine name (or type 'exit'): Aspirin
Do you want to purchase by tablet or strip: strip
Enter the quantity of strips you want to purchase: 3
```

#### Example Restock Session
```
Type 0 to buy 1 to restock and 2 to display: 1
Please enter the name of the vendor: PharmaCorp Inc
Enter the name of the medicine you want to restock (or type 'exit'): Aspirin
Do you want to restock by 'tablet' or 'strip'? strip
Enter the quantity you want to restock: 100
```

## 📈 Future Improvements

- **User Authentication** - Implement login system for both customers and vendors with user profiles
- **Database Integration** - Migrate from CSV files to SQL database (SQLite/PostgreSQL) for better scalability
- **Payment Gateway** - Integrate real payment systems for online transactions
- **Advanced Analytics** - Add sales reports, stock forecasting, and inventory analytics
- **Web Interface** - Develop a web-based frontend for improved user experience
- **Medicine Search Filters** - Advanced search with filtering by category, price range, manufacturer
- **Stock Alerts** - Automatic notifications when medicines reach low stock thresholds
- **Multi-location Support** - Support for multiple pharmacy branches with centralized inventory management
- **Prescription Management** - Feature to upload and manage digital prescriptions
- **Customer Loyalty Program** - Rewards points system for repeat customers
- **Expiry Date Tracking** - Track medicine expiration dates and prevent sales of expired medicines
- **Return Management** - Handle medicine returns and refunds with proper documentation
