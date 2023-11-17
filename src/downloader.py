from pytube import YouTube

def download_video(url, save_path='.'):
    """
    Downloads a YouTube video.
    
    :param url: URL of the YouTube video
    :param save_path: Path where the video will be saved, defaults to current directory
    :return: Path to the downloaded video, or None if download fails
    """
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if video_stream:
            # Download the video
            video_stream.download(save_path)
            print(f"Downloaded '{yt.title}' successfully.")
            return video_stream.default_filename
        else:
            print("No suitable video stream found.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
