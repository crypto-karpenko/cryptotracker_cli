# CryptoTracker CLI 🪙

CryptoTracker CLI is a simple command-line tool that allows you to track cryptocurrency prices in real time using data from the CoinGecko API.

## 💡 Features

- View current USD prices for selected cryptocurrencies
- Add new coins to your watchlist
- Remove coins from your list
- View your current watchlist

## 🛠 Tech Stack

- Python 3
- Requests library
- CoinGecko API

## 📦 Project Structure

crypto_tracker_cli/

├── crypto_tracker.py # Main script

├── data/

│   └── coins.json # Stored watchlist

└── README.md

            
## 🚀 Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/crypto-karpenko/cryptotracker_cli.git
cd crypto_tracker_cli
```
2. (Optional) Create a virtual environment
  ``` 
  python3 -m venv venv

  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
3. Install dependencies'
  ```
  pip install requests
  ```

4. Run the app
  ```
  python crypto_tracker.py
  ```
