# Attractive Stock Portfolio Tracker
from colorama import Fore, Style, init
from tabulate import tabulate
import csv

init(autoreset=True)  # For Windows color support

# 1️⃣ Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 330,
    "GOOG": 140
}

portfolio = {}  # user’s entered stocks

print(Fore.CYAN + Style.BRIGHT + "\n=== 🌟 Stock Portfolio Tracker 🌟 ===\n")
print(Fore.YELLOW + "Available stocks and their prices:")
print("-" * 45)
for stock, price in stock_prices.items():
    print(Fore.GREEN + f"{stock:<6} {Fore.WHITE}-> ${price}")
print("-" * 45)

# 2️⃣ User Input
while True:
    stock_name = input(Fore.CYAN + "\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == 'DONE':
        break
    if stock_name not in stock_prices:
        print(Fore.RED + "❌ Stock not available. Please choose from listed stocks.")
        continue

    try:
        quantity = int(input(Fore.YELLOW + f"Enter quantity for {stock_name}: "))
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.")
        continue

    # Add to portfolio
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# 3️⃣ Calculate total investment
total_investment = 0
table_data = []
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    table_data.append([stock, qty, f"${price}", f"${value}"])

print(Fore.CYAN + "\n=== 📊 Your Portfolio ===")
print(tabulate(table_data, headers=["Stock", "Quantity", "Price per Share", "Total Value"], tablefmt="fancy_grid"))
print(Fore.GREEN + Style.BRIGHT + f"\n💰 Total Investment Value: ${total_investment}")

# 4️⃣ Save real portfolio to file
if portfolio:
    save = input(Fore.CYAN + "\nDo you want to save your portfolio to a file? (y/n): ").lower()
    if save == 'y':
        file_type = input(Fore.YELLOW + "Enter file type (txt/csv): ").lower()

        if file_type == 'txt':
            with open("portfolio.txt", "w") as f:
                f.write("Your Portfolio:\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock} - {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
                f.write(f"Total Investment Value: ${total_investment}\n")
            print(Fore.GREEN + "✅ Real portfolio saved to portfolio.txt")

        elif file_type == 'csv':
            with open("portfolio.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
                for stock, qty in portfolio.items():
                    writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock]*qty])
                writer.writerow(["Total Investment", "", "", total_investment])
            print(Fore.GREEN + "✅ Real portfolio saved to portfolio.csv")

        else:
            print(Fore.RED + "❌ Unknown file type. Skipping save.")
else:
    print(Fore.YELLOW + "No portfolio entered. Nothing to save.")

print(Fore.CYAN + Style.BRIGHT + "\n=== 🎉 Thank you for using the Stock Portfolio Tracker 🎉 ===\n")
