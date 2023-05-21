import feedparser
import requests
import time

class RSSFeedParser:
    def __init__(self, url):
        self.url = url
        self.parsed_data = []

    def fetch_feed(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'accept-language': 'en-US,en-CA;q=0.9,en;q=0.8,hi-IN;q=0.7,hi;q=0.6'}
        response = requests.get(self.url, headers=headers)
        otc_feed = feedparser.parse(response.content.decode('utf-8'))
        return otc_feed.entries

    def parse_entries(self, entries):
        data = []
        parsed_ids = set()  # Set to store unique identifiers of parsed entries
        for entry in entries:
            entry_id = entry.get('link')  # Replace 'unique_identifier' with the appropriate field
            if entry_id not in parsed_ids:
                data.append({
                    'symbol': entry.get('pink_symbol'),
                    'type': entry.get('pink_type'),
                    'tier': entry.get('pink_tier'),
                    'date': entry.get('published'),
                    'title': entry.get('title'),
                    'link': entry.get('link')
                })
                parsed_ids.add(entry_id)
        return data


    def run(self):
        while True:
            entries = self.fetch_feed()
            data = self.parse_entries(entries)
            self.parsed_data.extend(data)
            time.sleep(300)  # Reduce the sleep duration for debugging



"""
Example:
url = 'https://www.otcmarkets.com/syndicate/rss.xml'
parser = RSSFeedParser(url)
parsed_data = parser.run()
"""

