import os
import requests
import re

# Specify the path where you want to save the videos
save_path = "D:/TEST 2/Data/Pixel/Footage"
os.makedirs(save_path, exist_ok=True)

# List of video URLs
video_urls = [
    "https://www.pexels.com/video/a-young-man-writing-on-a-notebook-4874295/",
    "https://www.pexels.com/video/woman-working-on-laptop-at-home-4492643/",
    "https://www.pexels.com/video/a-mother-helping-her-son-with-his-book-4769635/",
    "https://www.pexels.com/video/a-young-girl-attending-her-online-classes-at-home-4498849/",
    "https://www.pexels.com/video/a-person-holding-a-book-in-front-of-a-shelf-4860894/",
    "https://www.pexels.com/video/a-person-typing-on-a-laptop-keyboard-4496268/"
]

def extract_video_name_and_id(url):
    # Extract video name and ID from URL
    match = re.match(r"https://www\.pexels\.com/video/([a-zA-Z0-9\-]+)-(\d+)/", url)
    if match:
        video_name = match.group(1)
        video_id = match.group(2)
        return video_name, video_id
    return None, None

def download_video(video_id, video_name):
    download_url = f"https://www.pexels.com/download/video/{video_id}/"
    file_name = os.path.join(save_path, f"{video_name}.mp4")

    # Get the video from the download URL
    response = requests.get(download_url, stream=True)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded video '{video_name}' to {file_name}")
    else:
        print(f"Failed to download video {video_id}. Status code: {response.status_code}")

# Process videos
for url in video_urls:
    video_name, video_id = extract_video_name_and_id(url)
    if video_name and video_id:
        print(f"Video name: {video_name}")
        print(f"ID: {video_id}")
        download_video(video_id, video_name)
    else:
        print(f"Failed to extract information from URL: {url}")



