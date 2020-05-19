# coding=utf-8
import requests

# 请求的链接
url = 'http://suggest.taobao.com/sug?code=utf-8&q=裤子&callback=cb 用例'
# 发送请求
r = requests.post(url)

# 请求的状态码 200代表成功
status = r.status_code

# 进行接口的状态码断言，等于200则认为通过，不是200不通过
if status == 200:
    print('用例测试通过')
else:
    print('测试不通过')
print(status)
# 请求的内容
j = r.json()
print(j)