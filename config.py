# coding=utf-8

# baseurl 一般接口都是分测试接口和正式接口的，只需要修改ip即可
baseurl = 'http://suggest.taobao.com'
# 假装是登录接口 baseurl=于楼上
url_login = baseurl + '/sug?code=utf-8&q=裤子&callback=cb 用例'

# 假装是注冊接口 假装是post请求 拼接成字典格式，通过吗，通过key value的形式获取
# 注册接口是key  链接是value
url_register = {'注册接口':baseurl+'/sug','parmras': {'code': 'utf-8', 'q': '裤子', 'callback': 'cb 用例'}}

# 假装是首页接口
url_home = baseurl + '/sug?code=utf-8&q=裤子&callback=cb 用例'
