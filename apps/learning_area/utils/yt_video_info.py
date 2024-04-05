import requests
from bs4 import BeautifulSoup

def get_seconds_from_duration(duration):
    # Parse the duration string (e.g., "PT1H2M3S") into hours, minutes, and seconds
    hours = 0
    minutes = 0
    seconds = 0

    if 'H' in duration:
        hours = int(duration.split('H')[0][2:])
        duration = duration.split('H')[1]
        if 'M' in duration:
            minutes = int(duration.split('M')[0][0:])
            duration = duration.split('M')[1]
        if 'S' in duration:
            seconds = int(duration.split('S')[0][0:])
    if 'M' in duration:
        minutes = int(duration.split('M')[0][2:])
        duration = duration.split('M')[1]
    if 'S' in duration:
        seconds = int(duration.split('S')[0][0:])

    # Calculate the total seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def title_and_duration(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('title').get_text()
    title = title.split('-')[0].strip()

    # Get video duration
    duration_tag = soup.find('meta', itemprop='duration')
    duration = duration_tag['content'] if duration_tag else None
    duration_seconds = get_seconds_from_duration(duration)

    return title, duration_seconds
    '''{
        'title': title,
        'duration': duration,
        'duration_seconds': duration_seconds
    }'''

'''url = "https://www.youtube.com/watch?v=T9i7o0RTCYY"
title, duration_seconds = title_and_duration(url)
print(title)
print(duration_seconds)'''