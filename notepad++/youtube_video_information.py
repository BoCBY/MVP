import requests
from bs4 import BeautifulSoup

def get_video_info(youtube_url):
    response = requests.get(youtube_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Video title
    title = soup.find('title').get_text()
    title = title.split('-')[0].strip()
    
    

youtube_url = "https://www.youtube.com/watch?v=1EqCRWJzBgk"

print("Title:", title)
