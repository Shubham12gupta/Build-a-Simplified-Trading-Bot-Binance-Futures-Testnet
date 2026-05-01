import streamlit as st
from bot.client import BinanceFuturesClient
from bot.orders import place_order

st.set_page_config(page_title="Trading Bot UI", layout="centered")

st.title("📈 Binance Futures Testnet UI")

# Sidebar
st.sidebar.header("⚙️ Order Settings")

symbol = st.sidebar.text_input("Symbol", "BTCUSDT")
side = st.sidebar.selectbox("Side", ["BUY", "SELL"])
order_type = st.sidebar.selectbox("Order Type", ["MARKET", "LIMIT"])
quantity = st.sidebar.number_input("Quantity", min_value=0.0, value=0.001)

price = None
if order_type == "LIMIT":
    price = st.sidebar.number_input("Price", min_value=0.0, value=70000.0)

st.divider()

# Buttons like Binance
col1, col2 = st.columns(2)

buy_clicked = col1.button("🟢 BUY", use_container_width=True)
sell_clicked = col2.button("🔴 SELL", use_container_width=True)

client = BinanceFuturesClient()

def execute_trade(selected_side):
    try:
        st.subheader("📦 Order Request")
        st.write({
            "symbol": symbol,
            "side": selected_side,
            "type": order_type,
            "quantity": quantity,
            "price": price
        })

        response = place_order(
            client,
            symbol,
            selected_side,
            order_type,
            quantity,
            price
        )

        st.subheader("✅ Order Response")
        st.success("Order placed successfully!")

        st.json({
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A")
        })

    except Exception as e:
        st.error(f"❌ Order failed: {str(e)}")


if buy_clicked:
    execute_trade("BUY")

if sell_clicked:
    execute_trade("SELL")