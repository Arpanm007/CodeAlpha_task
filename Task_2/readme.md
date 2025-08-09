Here’s your **README.md** in Markdown format for the **Stock Portfolio Tracker** code:

````markdown
# 📈 Stock Portfolio Tracker (Python)

A simple Python script that helps you **track and calculate your stock portfolio value** based on hardcoded stock prices. You can choose stocks, enter quantities, and optionally save your portfolio summary to a `.csv` file.

---

## 📌 Features
- Preloaded stock prices for **AAPL, TSLA, GOOGL, AMZN, MSFT**.
- Accepts stock names in **any case** (e.g., `aapl`, `Tsla`).
- Allows adding multiple stocks with quantities.
- Calculates **total investment value**.
- Option to **export portfolio summary** to a CSV file.
- Handles invalid inputs gracefully.

---

## 🛠️ Requirements
- Python 3.x  
*(No external libraries required — only uses Python’s built-in `csv` module.)*

---

## 🚀 How to Run
1. **Clone this repository**  
   ```bash
   git clone https://github.com/your-username/stock-portfolio-tracker.git
   cd stock-portfolio-tracker
````

2. **Run the script**

   ```bash
   python portfolio_tracker.py
   ```

---

## 🎯 How to Use

1. The script will show a list of available stocks.
2. Enter a stock name (case-insensitive) and the quantity you want to buy.
3. Repeat until you type `done` to finish selection.
4. The program will display your **portfolio summary** with:

   * Stock name
   * Quantity
   * Price per share
   * Total value
5. You can **choose to save** this summary as a `.csv` file.

---

## 📝 Example Usage

```
📈 Welcome to the Stock Portfolio Tracker!
Available stocks: AAPL, TSLA, GOOGL, AMZN, MSFT
Note: Enter stock names in any case (e.g., aapl, Tsla)

Enter the stock you want to invest in (or type 'done' to finish): aapl
Enter quantity for AAPL: 10

Enter the stock you want to invest in (or type 'done' to finish): tsla
Enter quantity for TSLA: 5

Enter the stock you want to invest in (or type 'done' to finish): done

📊 Your Stock Portfolio Summary:
----------------------------------------
AAPL: Qty=10, Price=$180, Value=$1800
TSLA: Qty=5, Price=$250, Value=$1250
----------------------------------------
💰 Total Investment Value: $3050

Do you want to save the result to a file? (yes/no): yes
✅ Saved to summary.csv
```

---

## 📂 File Structure

```
stock-portfolio-tracker/
│
├── portfolio_tracker.py   # Main script
└── README.md              # Project documentation
```

---

## 📜 License

This project is licensed under the **MIT License** — you can use, modify, and distribute it.

```