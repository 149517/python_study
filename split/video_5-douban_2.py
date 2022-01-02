import requests
import re

f = open("doubantop_2.csv",mode="w",encoding="utf-8")
for i in range(11):
    if i < 1:
        url = "https://movie.douban.com/top250"
    else:
        url = f"https://movie.douban.com/top250?start={i*25}&filter="
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    resq = requests.get(url, headers=header)
    # print(resq.text)

    # 提取电影名称，导演，时间,评分，评价
    name = re.compile(r'<div class="item">.*?<span class="title">(?P<film>.*?)</span>.*?<p class="">.*?'
                      r'导演: (?P<director>.*?)&nbsp;.*?<br>.*?(?P<year>\d+)&nbsp;.*?'
                      r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                      r'<p class="quote">.*?<span class="inq">(?P<evaluate>.*?)</span>', re.S)

    nlist = name.finditer(resq.text)
    for na in nlist:
        film = na.group("film")
        director = na.group("director")
        year = na.group("year")
        pro = na.group("score")
        evaluate = na.group("evaluate")
        f.write(f"{film},{director},{year},{pro},{evaluate}\n")

    # print(film, director, year, pro, evaluate)
f.close()
# resq.close()
print("写入完成")