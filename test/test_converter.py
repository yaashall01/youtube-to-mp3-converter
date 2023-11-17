import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from converter import convert_to_mp3

class TestConverter(unittest.TestCase):

    def test_convert_to_mp3(self):
        test_video = 'sample_video.mp4'
        expected_output = 'sample_video.mp3'

        convert_to_mp3(test_video)

        self.assertTrue(os.path.exists(expected_output))

        if os.path.exists(expected_output):
            os.remove(expected_output)

if __name__ == '__main__':
    unittest.main()
