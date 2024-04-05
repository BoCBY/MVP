import requests
from bs4 import BeautifulSoup
import re

def get_bilibili_playlist_info(url):
    # 发送请求
    response = requests.get(url)
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # 找到所有视频信息的元素
    video_elements = soup.select('.video-list .list-item')
    print(f"找到 {len(video_elements)} 个视频元素")
    # 初始化一个空列表来存储视频信息
    playlist_info = []
    # 遍历每个视频元素
    for video_element in video_elements:
        # 获取标题
        title = video_element.select_one('.title').get_text(strip=True)
        # 获取片长
        duration_text = video_element.select_one('.so-imgTag_rb').get_text(strip=True)
        # 将片长文本转换为秒数
        duration_seconds = convert_duration_text_to_seconds(duration_text)
        # 将标题和片长添加到播放列表信息中
        playlist_info.append({'title': title, 'duration_seconds': duration_seconds})
    return playlist_info

def convert_duration_text_to_seconds(duration_text):
    # 使用正则表达式提取小时、分钟和秒数
    matches = re.match(r'(\d+):(\d+):(\d+)', duration_text)
    if matches:
        hours = int(matches.group(1))
        minutes = int(matches.group(2))
        seconds = int(matches.group(3))
        # 将时间转换为总秒数
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds
    else:
        return None

# 测试
playlist_url = 'https://www.bilibili.com/video/BV1KK41167mH/?p=3&vd_source=3dd15bae5592d893117773fb400ee427'
playlist_info = get_bilibili_playlist_info(playlist_url)
for video_info in playlist_info:
    print(f"标题: {video_info['title']}, 片长: {video_info['duration_seconds']} 秒")
