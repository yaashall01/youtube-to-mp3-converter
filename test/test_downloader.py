import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from downloader import download_video

class TestDownloader(unittest.TestCase):
    
    @patch('downloader.YouTube')
    def test_download_video(self, mock_youtube):
        mock_youtube.return_value.streams.filter.return_value.order_by.return_value.desc.return_value.first.return_value.download.return_value = 'video_path'

        response = download_video('http://youtube.com/video')

        self.assertEqual(response, 'video_path')

if __name__ == '__main__':
    unittest.main()
