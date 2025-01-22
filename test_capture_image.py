# test_image_capture.py
import unittest
from capture_image import capture_image  # Import the function to test
from general import print_test_comment_started, print_test_comment_completed

import unittest

class test_capture_mage(unittest.TestCase):
    
    def test_capture_image_success(self):
        print_test_comment_started(f"test_capture_image_started")
        #returns values from real function
        file_name, timestamp, result = capture_image()
        
        #print values
        print(f"Captured timestamp: {timestamp}")
        print(f"Captured file name: {file_name}")
        print(f"Result: {result}")

        #all assertions
        self.assertTrue(file_name.startswith("2025"))
        self.assertTrue(file_name.endswith("_image.jpg"))
        self.assertEqual(len(timestamp), 15)
        self.assertTrue(result)
        print_test_comment_completed(f"test_capture_image_completed")

#run
if __name__ == '__main__':
    unittest.main(verbosity=2)
