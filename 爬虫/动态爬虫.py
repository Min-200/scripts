#动态页面爬虫，先使用selenium模拟，在使用无界面浏览器phantomJS浏览，在用beautfuSoup对格式进行处理
from selenium import webdriver
import sys
from bs4 import BeautifulSoup
from urllib import error
from urllib import request

url=sys.argv[1]
url_list = []
driver = webdriver.PhantomJS(executable_path='/usr/sbin/phantomjs')
driver.get(url)
html=driver.page_source

all_num=0
succ_num=0
field_num=0
field_list=[]



soup = BeautifulSoup(html, 'html.parser')


for k in soup.find_all('a'):
    url = k.get('href')
    c= str(url)
    MM = c.startswith(('http://192.168.1.1','http://192.168.1.2'))
    if MM:
        url_list.append(url)

url_list = list(set(url_list))


for line in url_list:
#       line=line.strip('\n')
        all_num  = all_num  + 1
        try:
                req = request.Request(line)
                response = request.urlopen(req)
		
        except error.URLError as e:

                field_num = field_num + 1
                field_list.append(line)

        else:
                succ_num = succ_num + 1

print ("一共要传输的数量 : %s"  %(all_num))
print ("传输成功的数量: %s"  %(succ_num))
print ("传输失败的数量: %s"  %(field_num))


if field_num != 0:
	print ("以下目标地址没有成功传输")
	for i in field_list:
                print (i)
	sys.exit(2)
else:
	print ("所有包上传成功")

