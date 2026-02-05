# python -m pip install schedule

import requests as r, json, schedule, time

with open("binance-symbols.json") as file:
  json_data = json.loads(file.read())

def get_binance_data(symbol="BTCBRL", interval="1d", limit=1000):
  url = f"https://api2.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
  return r.get(url).json()

def run():
  symbols = []

  for symbol in json_data:
    klines = get_binance_data(symbol = symbol, limit = 360)
    symbols.append({
      "symbol": symbol,
      "last": float(klines[len(klines) - 1][4]),
      "lower": float(min([float(k[4]) for k in klines])),
      "upper": float(max([float(k[4]) for k in klines])),
    })

  with open("lowers.json", "w+") as lowers_file:
    lowers_file.write(json.dumps([s["symbol"] for s in symbols if s["last"] == s["lower"]]))

  with open("uppers.json", "w+") as uppers_file:
    uppers_file.write(json.dumps([s["symbol"] for s in symbols if s["last"] == s["upper"]]))

# schedule.every().hours.do(run)
schedule.every().minutes.do(run)

while True:
  schedule.run_pending()
  time.sleep(1)
