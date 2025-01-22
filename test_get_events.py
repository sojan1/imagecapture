import unittest
from bs4 import BeautifulSoup
from event_logs import get_events, Config  
from general import print_test_comment_started, print_test_comment_completed

class test_get_events(unittest.TestCase):
    
    def test_get_events_success(self):
        print_test_comment_started(f"test_get_events_started")
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
        print_test_comment_completed(f"test_get_events_success_completed")

if __name__ == '__main__':
    unittest.main(verbosity=2)
