# coding=utf-8
import urllib
import urllib2
import cookielib
#cookie文件的保存路径 
filename = 'cookie'
#声明对象实例保存cookie ，然后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#从文件中读取cookie内容
#cookie.load('cookie',ignore_discard=True , ignore_expires=True)
#声明Cookiejar对象事例保存cookie
#cookie = cookielib.CookieJar()
# 创建处理器 用urllib2库的HTTPCookieProcessor
handler = urllib2.HTTPCookieProcessor(cookie)

#通过handler构建opener;urllib2的urlopen 是opener的一个特例
opener = urllib2.build_opener(handler)


#定义url 也可以直接在open函数中写URL
#url = 'http://passport.csdn.net/account/login'
url2 = 'http://www.baidu.com'

#定义Agent 和 data部分，request函数有三个参数：url , data ,timeout
#user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
#values = {'username':'1601874413@qq.com','password':'g151U16o151642'}
#headers = {'User-Agent': user_agent}
#data = urllib.urlencode(values)
#geturl = url +'?'+data
#print geturl
#请求服务器
request = urllib2.Request(url2)
#request = urllib2.Request(url2,data,headers)

#处理error部分
#try:
#获取服务器上的数据
 # urllib2.urlopen(request)
#except urllib2.HTTPError,e:
 # print e.code
  #print e.reason
#except urllib2.URLError,e:
#  print e.reason
#else:
#  print"ok"
respone = opener.open(request)
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)
#打印cookie数据
#for item in cookie:
#  print 'name ='+ item.name
#  print 'Value = '+ item.value
#read才可以显示出具体的数据，不然显示的是这些数据的描述
page = respone.read()
print page

