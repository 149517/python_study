from lxml import etree
import requests

f = open("zhubajie_py.txt", mode="w", encoding="utf-8")
url = "https://chengdu.zbj.com/search/f/?kw=python"
resq = requests.get(url)
# print(resq.text)
et = etree.HTML(resq.text)
e_div_ = et.xpath("//div[@class='new-service-wrap']/div")
# print(e_div_)
for div in e_div_:
    company = div.xpath(".//p[@class='text-overflow']/text()")
    pp = div.xpath(".//p[@class='title']/text()")
    price = div.xpath(".//span[@class='price']/text()")
    company = "".join(company).strip()
    pp = "".join(pp)
    price = "".join(price).strip()
    # print(company, pp, price)
    f.write(f'{company},\t')
    f.write(f'{pp},')
    f.write(f'{price},\n')
f.close()
print("录入完毕")