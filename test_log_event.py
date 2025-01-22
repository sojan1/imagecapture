import unittest
from event_logs import log_event
from config import Config
import json
from general import print_test_comment_started, print_test_comment_completed

class test_log_event(unittest.TestCase):
    
    def test_log_event_success(self):
        print_test_comment_started(f"test_log_event_started")
        timestamp = "2025-01-01_12-00-00"
        event_type = "IMAGE_CAPTURED"
        image_filename = "2025-01-01_12-00-00_image.jpg"
        log_event(timestamp, event_type, image_filename)

        #read events
        with open(Config.EVENTLOG_PATH, 'r') as f:
            logged_events = json.load(f)


        #validate last event
        latest_event = logged_events[-1]
        print(f"Timestamp: {latest_event["timestamp"]}")
        print(f"Event Type: {latest_event["event_type"]}")
        print(f"File Name: {latest_event["image_filename"]}")

        
        self.assertEqual(latest_event["timestamp"], timestamp)
        self.assertEqual(latest_event["event_type"], event_type)
        self.assertEqual(latest_event["image_filename"], image_filename)
        
        print_test_comment_completed(f"test_log_event_completed")

#run
if __name__ == '__main__':
    unittest.main(verbosity=2)
