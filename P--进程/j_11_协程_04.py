import gevent
import urllib.request
from gevent import monkey

monkey.patch_all()


def download(url):
    response = urllib.request.urlopen(url)
    content = response.read()
    print("获取了{}的数据，长度为{} ".format(url, len(content)))


if __name__ == '__main__':
    urls = ["https://www.baidu.com/", "https://www.csdn.net/", "https://cn.bing.com/?scope=web&FORM=HDRSC1"]
    g1 = gevent.spawn(download, urls[0])
    g2 = gevent.spawn(download, urls[1])
    g3 = gevent.spawn(download, urls[2])

    gevent.joinall((g1, g2, g3))
