import requests
import re
#from urllib.parse import urlparse, parse_qs

def title_and_duration(url):
    # 提取影片的 BV 号和集數 ID
    bv_match = re.search(r'BV[a-zA-Z0-9]{10}', url)
    if not bv_match:
        print("無法從 URL 中提取 BV 号。")
        return None, None

    bv = bv_match.group()

    # 提取集數 ID
    episode_match = re.search(r'p=(\d+)', url)
    if episode_match:
        episode_id = episode_match.group(1)
        #print('播放清單集數: '+episode_id)
    else:
        episode_id = None
        #print('並非來自播放清單')

    api_url = f'https://api.bilibili.com/x/web-interface/view?bvid={bv}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        if data['code'] != 0:
            print("無法獲取影片資訊。")
            return None, None
        
        if episode_id:
            #print(data['data']['pages'][int(episode_id)-1]['page'])
            title = data['data']['pages'][int(episode_id)-1]['part']
            duration = data['data']['pages'][int(episode_id)-1]['duration']
            #duration_str = f"{duration // 60}分{duration % 60}秒"
            return title, duration

        title = data['data']['title']
        duration = data['data']['duration']
        #duration_str = f"{duration // 60}分{duration % 60}秒"
        return title, duration

    except requests.exceptions.RequestException as e:
        print("發生錯誤：", e)
        return None, None

#測試
'''url = 'https://www.bilibili.com/video/BV1BC411h7xH?p=5&vd_source=3dd15bae5592d893117773fb400ee427'
title, duration = title_and_duration(url)
if title and duration:
   print(f"影片標題：{title}")
   print(f"影片片長：{duration}")'''