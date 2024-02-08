import sqlite3
import time
from feedaggregater import RSSFeedParser

url = 'https://www.otcmarkets.com/syndicate/rss.xml'
parser = RSSFeedParser(url)

conn = sqlite3.connect('rss_feed.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS rss_feed (
                symbol TEXT,
                type TEXT,
                tier TEXT,
                date TEXT,
                title TEXT,
                link TEXT
            )''')

conn.commit()

while True:
    parser.run()
    parsed_data = parser.parsed_data 

    if parsed_data:

        for item in parsed_data:
            print(item)
            c.execute("INSERT INTO rss_feed (symbol, type, tier, date, title, link) VALUES (?, ?, ?, ?, ?, ?)", (
                item['symbol'],
                item['type'],
                item['tier'],
                item['date'],
                item['title'],
                item['link']
            ))

        conn.commit()
    else:
        print("No data to insert.")

    parser.parsed_data = []

    time.sleep(5)

conn.close()






