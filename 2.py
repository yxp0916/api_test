import requests
url = 'http://suggest.taobao.com/sug'

# post请求以字典格式传入
data = {'code': 'utf-8', 'q': '裤子', 'callback': 'cb 用例'}

# 发送post请求
r = requests.post(url, data)

# 请求的状态码 200代表成功
status = r.status_code
print(status)

# 请求的内容
print(r.content)