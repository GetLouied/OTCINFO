import unittest
from feedaggregater import RSSFeedParser

class RSSFeedParserTestCase(unittest.TestCase):
    def test_parse_entries(self):
        # Sample entries for testing
        entries = [
            {
                'pink_symbol': 'ABC',
                'pink_type': 'Type1',
                'pink_tier': 'Tier1',
                'published': '2023-05-20',
                'title': 'Sample Title',
                'link': 'https://example.com'
            },
            {
                'pink_symbol': 'XYZ',
                'pink_type': 'Type2',
                'pink_tier': 'Tier2',
                'published': '2023-05-21',
                'title': 'Another Title',
                'link': 'https://example.com/another'
            }
        ]

        parser = RSSFeedParser('')
        result = parser.parse_entries(entries)

        # Assert the expected values
        self.assertEqual(result, [
            {
                'symbol': 'ABC',
                'type': 'Type1',
                'tier': 'Tier1',
                'date': '2023-05-20',
                'title': 'Sample Title',
                'link': 'https://example.com'
            },
            {
                'symbol': 'XYZ',
                'type': 'Type2',
                'tier': 'Tier2',
                'date': '2023-05-21',
                'title': 'Another Title',
                'link': 'https://example.com/another'
            }
        ])

if __name__ == '__main__':
    unittest.main()