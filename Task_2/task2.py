import csv

# Step 1: hardcoded stock prices entered
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 130,
    "MSFT": 310
}

# Step 2: choosing stock and entering quantity
print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ', '.join(stock_prices.keys()))
print("Note: Enter stock names in any case (e.g., aapl, Tsla)")

portfolio = {}

while True:
    stock_name = input("\nEnter the stock you want to invest in (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("⚠️ Stock not found. Please choose from the available list.")
        continue

    try:
        qty = int(input(f"Enter quantity for {stock_name}: "))
        if qty < 0:
            print("⚠️ Quantity cannot be negative. Skipping.")
            continue
        portfolio[stock_name] = portfolio.get(stock_name, 0) + qty
    except ValueError:
        print("⚠️ Invalid number. Try again.")

# Step 3: Calculating total investment value
if not portfolio:
    print("\nNo stocks selected. Exiting program.")
    exit()

total_value = 0
print("\n📊 Your Stock Portfolio Summary:")
print("-" * 40)

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    print(f"{stock}: Qty={qty}, Price=${price}, Value=${value}")
    total_value += value

print("-" * 40)
print(f"💰 Total Investment Value: ${total_value}")

# Step 4: Saving summary to .csv or .txt
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    #for saving as .txt
    """with open("portfolio.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write("Stock Portfolio Summary\n")
        txt_file.write("=======================\n")
        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            txt_file.write(f"{stock}: Qty={qty}, Price=${stock_prices[stock]}, Value=${value}\n")
        txt_file.write(f"\nTotal Investment Value: ${total_value}")
    print("✅ Saved to portfolio.txt")"""

    #for save as .csv
    with open("summary.csv", "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        for stock, qty in portfolio.items():
            writer.writerow([stock, qty, stock_prices[stock], qty * stock_prices[stock]])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total_value])
    print("✅ Saved to summary.csv")
else:
    print("File save skipped.")