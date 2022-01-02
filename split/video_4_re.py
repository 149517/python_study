import re

div = """
    <div class="name"><span id="10010">中国电信</span>
    <div class="name"><span id="10086">中国移动</span>
"""
res = re.compile(r'<span id="(?P<id>\d+)">(?P<name>.*?)</span>')
result = res.finditer(div)
print(result)

for item in result:
    id = item.group("id")
    print(id)
    name = item.group("name")
    print(name)