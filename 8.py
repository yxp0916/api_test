# coding=utf-8
import requests
# 引入config配置接口的文件
import config


# 测试注册接口的函数
def test_register():
    # 发送post请求，通过config文件获取接口url 和接口的参数 ，如果参数更改了，咱们就修改config文件就可以了
    r = requests.post(config.url_register['注册接口'], config.url_register['parmras'])
    # 请求的状态码 200代表成功
    status = r.status_code
    # 进行接口的状态码断言，等于200则认为通过，不是200不通过
    if status == 200:
        print('状态码校验过')
    else:
        print('状态码校验不通过')
    # 输出状态码
    print(status)
    # 因为展示测试的接口没有json，所以只能输出content啦~
    print(r.content)


# 测试登录接口的函数
def test_login():
    # 因为发送的get请求，参数是跟在接口的后面的，所以不用通过字典的形式获取
    r = requests.post(config.url_login)
    # 请求的状态码 200代表成功
    status = r.status_code
    # 进行接口的状态码断言，等于200则认为通过，不是200不通过
    if status == 200:
        print('状态码校验过')
    else:
        print('状态码校验不通过')
    # 输出状态码
    print(status)
    # 因为展示测试的接口没有json，所以只能输出content啦~
    print(r.json())
    # 预期结果 在接口返回结果后，查看接口里面有没有此值，也就是传说的断言了
    expected = '裤子男夏季'
    # 将接口返回的信息转为字符串类型，in 是判断接口的返回值里面 存不存在 预期结果的值，存在就通过 不存在就不通过
    if expected in str(r.json()):
        print('断言通过')
    else:
        print('断言不通过')


# 调用执行测试接口
test_register()
print('执行了 测试注册接口的函数')
# 调用执行登录接口
test_login()
print('执行了 测试登录接口的函数')
