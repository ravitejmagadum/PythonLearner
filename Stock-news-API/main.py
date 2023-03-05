import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

api_key = "I99TZ1CFBSNRQX68"
# param = {
#     "function" = "TIME_SERIES_DAILY_ADJUSTED",
#     "symbol"=STOCK,
#     "apikey"=api_key,
# }
response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey={api_key}")
response.raise_for_status()
data = response.json()
price_change = data["Time Series (Daily)"]

ohlc = [price for date,price in price_change.items()]
dates = [date for date,price in price_change.items()]

try:
    for i in range(len(ohlc)):
        pct_chg = (float(ohlc[i + 1]['1. open']) - float(ohlc[i]["4. close"]))/float(ohlc[i]["4. close"]) * 100
        if  pct_chg <= -5:

            print(f"decreased between {pct_chg} {dates[i]} and {dates[i+1]}")

        elif pct_chg > 5:

            print(f"increased between {pct_chg} {dates[i]} and {dates[i+1]}")

        else:
            pass
except IndexError:
    pass


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


def get_news():
    news_api = "757c2f8a52cd4a96860d3c309fc29d41"
    param = {"apiKey": news_api, "q": COMPANY_NAME}

    response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=757c2f8a52cd4a96860d3c309fc29d41")  #"https://newsapi.org/v2/everything", params=param)#?q=Tesla Inc&apiKey=757c2f8a52cd4a96860d3c309fc29d41")
    response.raise_for_status()
    data = response.json()
    list = data["articles"][:3]
    articles = []

    for i in list:
        articles.append(i["title"])
    return articles

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_message():
    account_sid = "AC48c5779130cd09c5d9aa2d876f639d97"
    auth_token = "89f9640e9a4018e9ce267ac9c6953997"

    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body=get_news(),
                         from_='+12708179976',
                         to='+918867908584'
                     )

    print(message.status)

send_message()


