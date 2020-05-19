# coding=utf-8
import requests

# 请求的链接
url = 'http://suggest.taobao.com/sug?code=utf-8&q=裤子&callback=cb 用例'
# 发送get请求
r = requests.get(url)
# 请求的状态码 200代表成功
status = r.status_code
print(status)
# 请求的内容
j = r.json()
print()
print(j)