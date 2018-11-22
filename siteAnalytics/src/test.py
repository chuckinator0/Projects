import unittest
import process_log
import datetime

class TestLogProcessor(unittest.TestCase):
    def test_format_date(self):
        d = datetime.datetime(2005, 7, 14, 12, 30)
        self.assertEqual(process_log.convertHours(d), "14/Jul/2005:12:30:00")

    def test_parse_date(self):
        self.assertEqual(process_log.parseDateTime("[01/Jul/1995:00:00:59"), datetime.datetime(1995, 7, 1, 0, 0, 59))

    def test_round_time(self):
        d = datetime.datetime(2005, 7, 14, 12, 30, 3)
        self.assertEqual(process_log.roundDown(d), d.replace(minute=0, second=0))

    def test_parse_line(self):
        entry = process_log.LogEntry('128.159.122.119 - - [01/Jul/1995:00:00:41 -0000] "GET /icons/image.xbm HTTP/1.0" 200 509')

        self.assertEqual(entry.host, '128.159.122.119')
        self.assertEqual(entry.timestamp, datetime.datetime(1995, 7, 1, 0, 0, 41, tzinfo=datetime.timezone.utc))
        self.assertEqual(entry.statusCode, 200)
        self.assertEqual(entry.contentLength, 509)
        self.assertEqual(entry.verb, 'GET')
        self.assertEqual(entry.resource, '/icons/image.xbm')



if __name__ == '__main__':
    unittest.main()

