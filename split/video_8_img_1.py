import requests
from bs4 import BeautifulSoup

url = "https://www.umei.cc/katongdongman/"
resq = requests.get(url)
resq.encoding = "utf-8"
# print(resq.text)

img_pag = BeautifulSoup(resq.text, "html5lib")
img_a = img_pag.find("div", {"class": "TypeList"})
img_sr = img_a.find_all("img")
img_name = img_a.find_all("span")

# for name in img_name:
#     print(name.text)

# dict_1 = {}
# for src,name in zip(img_sr,img_name):
#     dict_1[name] = src
#
# print(dict_1)
for src, name in zip(img_sr, img_name):
    name = name.text
    src = src.get("src")
    img = requests.get(src)
    with open(f"img_2/{name}.jpg","wb") as f:
        f.write(img.content)
    print(name + " : " + src)
# for src in img_sr:
#     sr = src.get("src")
#