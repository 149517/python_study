import requests

url = "https://fanyi.baidu.com/sug"

data = {
    "kw":input("输入一个单词")
}

resp = requests.post(url,data)
print(resp.text)    #返回的数据类型是json，resp.text返回的是字符串
print(resp.json())