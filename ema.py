import yfinance as yf
from datetime import datetime

def get_crossover_time(symbol):
    # Fetch historical data
    stock_data = yf.download(symbol, start="2023-01-01", end="2023-08-24", interval="1h")  # Use 1-hour interval

    # Calculate 5 EMA and 20 EMA
    stock_data['EMA5'] = stock_data['Close'].rolling(window=5).mean()
    stock_data['EMA20'] = stock_data['Close'].rolling(window=20).mean()

    crossover_times = []
    for i in range(1, len(stock_data)):
        if stock_data['EMA5'][i] > stock_data['EMA20'][i] and stock_data['EMA5'][i - 1] <= stock_data['EMA20'][i - 1]:
            crossover_time = stock_data.index[i].strftime('%Y-%m-%d %H:%M:%S')
            crossover_times.append(crossover_time)

    return crossover_times

nifty50_symbols = ["RELIANCE.NS", "TATASTEEL.NS", "HDFCBANK.NS",  # Add all Nifty 50 symbols here
                   "WIPRO.NS", "INFY.NS", "ICICIBANK.NS",  # ...and so on
                   # Add the rest of the symbols
                  ]

for symbol in nifty50_symbols:
    crossover_times = get_crossover_time(symbol)
    if crossover_times:
        stock_name = yf.Ticker(symbol).info['longName']
        for time in crossover_times:
            print(f"{stock_name}: {time}")
