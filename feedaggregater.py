import feedparser
import requests
import time

class RSSFeedParser:
    def __init__(self, url):
        self.url = url
        self.parsed_data = []


 # Need accept-language header to pass otc bot recognition for rss feed
    def fetch_feed(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'accept-language': 'en-US,en-CA;q=0.9,en;q=0.8,hi-IN;q=0.7,hi;q=0.6'}
        response = requests.get(self.url, headers=headers)
        return response.text  

    def parse_entries(self, raw_xml):
        data = []
        parsed_ids = set()
        otc_feed = feedparser.parse(raw_xml)
        entries = otc_feed.entries
        for entry in entries:
            entry_id = entry.get('link')
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
            raw_xml = self.fetch_feed()
            data = self.parse_entries(raw_xml)
            self.parsed_data.extend(data)
            return data 
            time.sleep(300)


