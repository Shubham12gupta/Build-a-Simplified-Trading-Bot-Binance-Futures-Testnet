# Build-a-Simplified-Trading-Bot-Binance-Futures-Testnet
# Binance Futures Testnet Trading Bot
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/da23ae7b-29ee-4463-b79c-9440b1e29715" />


## 🚀 Features

* Place MARKET and LIMIT orders on Binance Futures Testnet (USDT-M)
* Supports BUY and SELL sides
* CLI-based input using Click
* Streamlit UI for trading interface (bonus)
* Input validation and error handling
* Logging of API requests and responses

---

## ⚙️ Setup

```bash
git clone <your_repo_url>
cd trading_bot
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create `.env` file:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

## ▶️ Run CLI

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 70000
```

---

## 🖥️ Run UI (Bonus)

```bash
streamlit run ui.py
```

---

## 📊 Output

The application prints:

* Order request summary
* Order response:

  * orderId
  * status
  * executedQty
  * avgPrice
* Success / Failure message

---

## 📝 Logs

Logs are stored in:

```
bot.log
```

Includes:

* API request payload
* API response
* Errors

---

## ⚠️ Assumptions

* Binance Futures Testnet API keys are used
* Internet connectivity available
* Due to Binance geo-restrictions, cloud deployments (e.g., Render) may not execute trades; local execution is recommended

---

## 📦 Dependencies

See `requirements.txt`
