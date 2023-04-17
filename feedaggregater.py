import feedparser
import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'accept-language': 'en-US,en-CA;q=0.9,en;q=0.8,hi-IN;q=0.7,hi;q=0.6'}
response = requests.get(
    'https://www.otcmarkets.com/syndicate/rss.xml', headers=headers)

otc_feed = feedparser.parse(response.content.decode('utf-8'))

data = []
for entry in otc_feed.entries:
    data.append({
        'title': entry.title,
        'link': entry.link,
        'symbol': entry.pink_symbol,
        'type': entry.pink_type,
    })

df = pd.DataFrame(data)
print(df.head(15))
