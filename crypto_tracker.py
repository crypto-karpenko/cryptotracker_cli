import json
import requests
import os

DATA_FILE = 'data/coins.json'
API_URL = 'https://api.coingecko.com/api/v3/simple/price'

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

def load_coins():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump(["bitcoin", "ethereum"], f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_coins(coins):
    with open(DATA_FILE, 'w') as f:
        json.dump(coins, f, indent=4)

def fetch_prices(coins):
    ids = ','.join(coins)
    params = {
        'ids': ids,
        'vs_currencies': 'usd'
    }
    try:
        response = requests.get(API_URL, params=params)
        data = response.json()
        for coin in coins:
            price = data.get(coin, {}).get('usd')
            if price:
                print(f"{coin.capitalize()}: ${price}")
            else:
                print(f"{coin.capitalize()}: Price not found.")
    except Exception as e:
        print("Error fetching prices:", e)

def add_coin():
    coin = input("Enter the coin ID to add (e.g., bitcoin): ").lower()
    coins = load_coins()
    if coin not in coins:
        coins.append(coin)
        save_coins(coins)
        print(f"{coin} added to the watchlist.")
    else:
        print(f"{coin} is already in the list.")

def remove_coin():
    coin = input("Enter the coin ID to remove: ").lower()
    coins = load_coins()
    if coin in coins:
        coins.remove(coin)
        save_coins(coins)
        print(f"{coin} removed.")
    else:
        print(f"{coin} not found.")

def show_menu():
    while True:
        print("\n=== CryptoTracker CLI ===")
        print("1. View prices")
        print("2. Add coin")
        print("3. Remove coin")
        print("4. View watchlist")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            fetch_prices(load_coins())
        elif choice == '2':
            add_coin()
        elif choice == '3':
            remove_coin()
        elif choice == '4':
            print("Watchlist:", ", ".join(load_coins()))
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    show_menu()
