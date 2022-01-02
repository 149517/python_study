import re
import requests

f = open("dytt.csv","w",encoding="utf-8")
url = "https://www.dytt8.net/index2.htm"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
# }
resq = requests.get(url)
resq.encoding = "gbk"
# print(resq.text)
# 获取 “2021新片精品”

obj1 = re.compile(r'2021新片精品.*?<ul>(?P<html>.*?)</ul>', re.S)
html = obj1.search(resq.text)
html = html.group("html")

# print(html)

obj2 = re.compile("最新电影下载.*?<a href='(?P<url_>.*?)'>2021.*?《(?P<name>.*?)》(HD|BD)", re.S)
file_name = obj2.finditer(html)


# f_na = file_name.finditer(resq.text)

# 二级链接
def r_url(url):
    resq2 = requests.get(f"https://www.dytt8.net{url}")
    resq2.encoding = "gbk"
    # print(resq2.text)
    obj3 = re.compile(
        r'<!--Content Start--><span style="FONT-SIZE: 12px">.*?<a target="_blank" href="(?P<link1>.*?)"><strong>.*?'
        r'<font color=red>下载地址2：<a href="(?P<link2>.*?)" target="_blank"', re.S)
    result = obj3.search(resq2.text)
    result1 = result.group("link1")
    result2 = result.group("link2")
    # return {"link1":result1,"link2":result2}
    return result1

for fa in file_name:
    name = fa.group("name")
    url_ = fa.group("url_")
    url = r_url(url_)
    f.write(name,)
    f.write(f"link:{url}\n")
    # print(name,r_url())
f.close()
resq.close()
print("输入完成")