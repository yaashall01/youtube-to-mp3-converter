from moviepy.editor import VideoFileClip
import os

def convert_to_mp3(video_path, output_path=None):
    """
    Converts a video file to an MP3 file.

    :param video_path: Path to the video file.
    :param output_path: Path to save the MP3 file. If not provided, saves in the same directory as the video.
    :return: Path to the converted MP3 file, or None if conversion fails
    """
    if not output_path:
        output_path = os.path.splitext(video_path)[0] + '.mp3'

    try:
        # Load the video file
        video_clip = VideoFileClip(video_path)

        # Extract audio from the video
        audio_clip = video_clip.audio

        # Write the audio to a file
        audio_clip.write_audiofile(output_path)

        # Close the clips
        audio_clip.close()
        video_clip.close()

        print(f"Converted '{video_path}' to MP3 successfully.")
        return output_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
