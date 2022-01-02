import requests

url = "https://movie.douban.com/j/chart/top_list"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}
data = {
    "type": "5",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}
resq = requests.get(url,params=data,headers=header)
print(resq.request.url)
print(resq.json())
