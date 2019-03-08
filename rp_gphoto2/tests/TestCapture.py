import unittest
from rp_gphoto2.rp_gphoto2 import init_camera, capture_to_file


class TestCapture (unittest.TestCase):
    def test_capture(self):
        c = init_camera()
        capture_to_file(c, "test.jpg")


if __name__ == '__main__':
    unittest.main()
