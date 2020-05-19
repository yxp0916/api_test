import requests
import config

r=requests.post(config.url_register['注册接口'],config.url_register['parmras'])
status=r.status_code
print(status)
if status==200:
    print('状态码校验通过')
else:
    print('状态码校验不通过')
print(status)
print(r.content)