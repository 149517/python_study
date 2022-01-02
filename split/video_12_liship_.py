import requests

# 拿到contId
# 拿到videoStatus返回的json
# srcURl里面的内容进行处理
# 下载视频

# 视频的上一级地址
url = "https://www.pearvideo.com/video_1746894"
# resq = requests.get(url)
# print(resq.text)
contId = url.split('_')[1]
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.4729557299719296"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Referer": url
}
res = requests.get(videoStatusUrl, headers=header)
dic = res.json()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime, f'cont-{contId}')
print(srcUrl)
with open("li.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)

print("下载完成")
