import unittest
from rp_gphoto2.rp_gphoto2 import capture_to_file


class TestCapture (unittest.TestCase):
    def test_capture(self):
        capture_to_file("test.jpg")


if __name__ == '__main__':
    unittest.main()

