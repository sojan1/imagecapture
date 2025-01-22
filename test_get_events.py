import unittest
from bs4 import BeautifulSoup
from event_logs import get_events, Config  


class TestGetEvents(unittest.TestCase):

    def test_get_events_success(self):
        #get events
        response = get_events()
        html_content = response.body.decode()

        #parse html
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            valid_html = True
        except Exception as e:
            valid_html = False

        print(f"Response body: {response.body.decode()}")
        #assertions
        self.assertTrue(valid_html, "The HTML content is not valid")


if __name__ == '__main__':
    unittest.main(verbosity=2)
