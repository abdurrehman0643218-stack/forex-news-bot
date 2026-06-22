import requests

TOKEN = "8956426655:AAEII2SEaRwsZf9RRb6Eiqkw6lZegSSEXFE"
CHAT_ID = "8632818341"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

news = """
📊 TODAY MARKET NEWS

🔴 USD strength high
📉 Crypto pressure increasing
⚠️ Market volatility expected
"""

send(news)

print("DONE")
