# Binance USDT-M Futures Trading Bot (CLI-Based)

A command-line trading bot for **Binance USDT-M Futures**, supporting both core and advanced order types with structured logging, input validation, and modular code design.

---

## Features

- Market Orders
- Limit Orders
- Stop-Limit Orders
- OCO Orders (Take-Profit + Stop-Loss simulation)
- TWAP (Time-Weighted Average Price)
- Grid Trading (Buy low, sell high strategy)
- Input Validation
- Structured Logging (`bot.log`)

---


## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourname/binance-futures-bot.git
cd binance-futures-bot

```

---

### 2 How to Run

python src/main.py

### 3. Order Types Demo

   #### Market Order
   Choice: 1  
   Symbol: BTCUSDT  
   Side: BUY  
   Quantity: 0.01

   #### Limit Order

   Choice: 2  
   Symbol: ETHUSDT  
   Side: SELL  
   Quantity: 0.02  
   Price: 3100

   ####  Stop-Limit Order

   Choice: 3  
   Symbol: BTCUSDT  
   Side: SELL  
   Stop Price: 62000  
   Limit Price: 61900

   #### OCO Order (Simulated)

   Symbol: BTCUSDT  
   Side: BUY  
   TP Price: 63500  
   SL Price: 61000


### Contact

Author: Kumar Gosala
LinkedIn: [Link Text](https://www.linkedin.com/in/sowjanya-kumar-gosala/)
Email: kumargosala2024@gmail.com






