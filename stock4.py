"""
Project: Stock Exchange Data
Date: 10/26/2019
Description: Intake .csv file containing stock data from Jan 2, 2009 to Dec 31, 2018 of IBM, Microsoft, and Apple and output their
respective max stock closing price and date, min closing price and date, average, and standard deviation. Lastly, take the stocks as a
whole and out put the stock with the highest closing date, with its symbol, date, and amount, and then the same with the overall lowest
closing date.
"""
import csv
import statistics


#Definitions for average(mean), standard deviation, max and min price of an individual stock and max and min of all stocks.
def average(symbol):
    nums = list(symbol)
    floats = [float(i) for i in nums]
    return statistics.mean(floats)

def stdev(symbol):
    nums = list(symbol)
    floats = [float(i) for i in nums]
    return statistics.stdev(floats)

def max_dict(symbol):
    price = max(symbol, key=float)
    for key in symbol:
        if key == price:
            return ("{} {}".format(key,symbol[key]))
        
def max_price(stockdata):
    price = max(stockdata, key=lambda sublist: float(sublist[2]))
    return ' '.join(price)
    
def min_price(stockdata):
    price = min(stockdata, key=lambda sublist: float(sublist[2]))
    return ' '.join(price)
        
def min_dict(symbol):
    price = min(symbol, key=float)
    for key in symbol:
        if key == price:
            s = ""
            return ("{} {}".format(key,symbol[key]))

#To load data from stocks_data.csv. Also checks if file is in directory.
def load_data():
    try:
        file_in = open("stocks_data.csv", 'r')
        reader = csv.reader(file_in)
        data = list(reader)
        return data
    except FileNotFoundError:
        print("File not found in directory.\nPlease place stock_data.csv in directory.", end = "")

#Given stock symbol and data, uses above functions formatted to print list.
def stock_data(symbol, data):
    return f"{symbol}\n----\nMax: {max_dict(data)}\nMin: {min_dict(data)}\nAve: {average(data)}\nDev: {stdev(data)}\n"

#Main creates dictionaries of each stock and total stocks, then runs them through stock_data above to obtain results.
def main():
    msft_dic = {}
    aapl_dic = {}
    ibm_dic = {}
    allstocks = {}
    data = load_data()
    rawdata = list(load_data())
    rawdata.pop(0)
    for sublist in data:
        if sublist[0] == "MSFT":
            date = sublist[1]
            adj_close = sublist[2]
            msft_dic.update({adj_close : date})
        elif sublist[0] == "AAPL":
            date = sublist[1]
            adj_close = sublist[2]
            aapl_dic.update({adj_close : date})
        elif sublist[0] == "IBM":
            date = sublist[1]
            adj_close = sublist[2]
            ibm_dic.update({adj_close : date})
        allstocks.update(msft_dic)
        allstocks.update(aapl_dic)
        allstocks.update(ibm_dic)
    foutput = open('stock_summary.txt', 'w')
    symbol = "AAPL"
    print(stock_data(symbol, aapl_dic))
    print(stock_data(symbol, aapl_dic), file = foutput)
    symbol = "IBM"
    print(stock_data(symbol, ibm_dic)),
    print(stock_data(symbol, ibm_dic), file = foutput)
    symbol = "MSFT"
    print(stock_data(symbol, msft_dic)),
    print(stock_data(symbol, msft_dic), file = foutput)
    print(f"Highest: {max_price(rawdata)},\nLowest: {min_price(rawdata)}")
    print(f"Highest: {max_price(rawdata)},\nLowest: {min_price(rawdata)}", file = foutput)
    foutput.close

if __name__ == "__main__":
    main()

