# coding=utf-8
import requests
# 引入config配置接口的文件
import config

# 发送请求 使用config.来调用想要的接口 调用首页接口
r = requests.get(config.url_home)
# 请求的状态码 200代表成功
status = r.status_code
# 进行接口的状态码断言，等于200则认为通过，不是200不通过
if status == 200:
    print('状态码校验过')
else:
    print('状态码校验不通过')
print(status)
# 请求的内容
j = r.json()
# 判断接口返回内容里面，有没有 裤子女夏 内容
# 裤子女夏  增加了一个1
if '裤子女夏1' in str(j):
    print('存在此数据')
else:
    print('不存在此数据')
print(j)
