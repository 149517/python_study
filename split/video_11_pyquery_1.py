from pyquery import PyQuery
import requests


# 读取源代码
# 找到所要的信息

def get_url(url):
    resq = requests.get(url)
    resq.encoding = "gbk"
    # print(resq.text)
    return resq.text


def parse_page_source(html):
    p = PyQuery(html)
    name = p(".name-text").items()
    car_model = p(".font-arial").items()
    place = p(".c333").items()
    dateandprice = p(".choose-dl").items()

    for na, c_m, pla, dat in zip(name, car_model, place, dateandprice):
        na = na("p a").text()
        c_m = c_m.text()
        pla = pla.text()
        dat = dat.text()

        print(na, c_m, pla, dat)


def main():
    url = "https://k.autohome.com.cn/692/###"
    html = get_url(url)
    parse_page_source(html)


if __name__ == '__main__':
    main()
