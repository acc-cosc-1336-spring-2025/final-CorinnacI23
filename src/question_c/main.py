class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


def create_stock_file():
    default_data = """AAPL Apple Inc
CAT Caterpillar
EK Eastman Kodak
GOOG Google
MSFT Microsoft
"""
    with open("stock_file.dat", "w") as file:
        file.write(default_data)
    print("stock_file.dat created with default data.")



def get_stock_list():
    stock_list = []
    try:
        with open("stock_file.dat", "r") as file:
            for line in file:
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    symbol, company_name = parts
                    stock = Stock(symbol, company_name)
                    stock_list.append(stock)
    except Exception as e:
        print("Error reading stock file:", e)
    return stock_list



def display_stock_report(stock_list):
    print("\nStock Report")
    print(f"{'Company':<20} {'Symbol'}")
    print("-" * 30)
    for stock in stock_list:
        print(f"{stock.get_company_name():<20} {stock.get_symbol()}")



def main():
    create_stock_file()  # Always overwrite with default stock data

    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            stock_list = get_stock_list()
            if stock_list:
                display_stock_report(stock_list)
            else:
                print("No stock data found.")
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")



if __name__ == "__main__":
    main()

