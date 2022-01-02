import requests

query = input("输入检索内容：")
url = f"https://www.sogou.com/web?query={query}"

# 访问被拦截
# 用户您好，我们的系统检测到您网络中存在异常访问请求。<br>此验证码用于确认这些请求是您的正常行为而不是自动程序发出的，需要您协助验证。？

# 获取请求头信息
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

resp = requests.get(url)
print("默认的请求头信息：")
print(resp.request.headers)

resp = requests.get(url,headers=header)

print(resp.request.headers)
