import sqlite3
import time
from feedaggregater import RSSFeedParser

url = 'https://www.otcmarkets.com/syndicate/rss.xml'
parser = RSSFeedParser(url)

conn = sqlite3.connect('rss_feed.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS rss_feed (
                symbol TEXT,
                type TEXT,
                tier TEXT,
                pubdate TEXT,
                title TEXT,
                link TEXT
            )''')

conn.commit()

while True:
    parser.run()
    parsed_data = parser.parsed_data 

    if parsed_data:
        print("Parsed data:", parsed_data)  # Print the parsed data

        for item in parsed_data:
            c.execute("INSERT INTO rss_feed (symbol, type, tier, pubdate, title, link) VALUES (?, ?, ?, ?, ?, ?)", (
                item['symbol'],
                item['type'],
                item['tier'],
                item['date'],
                item['title'],
                item['link']
            ))

        conn.commit()
        print("Data inserted successfully!")
    else:
        print("No data to insert.")

    parser.parsed_data = []

    time.sleep(5)

conn.close()









