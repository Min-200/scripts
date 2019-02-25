#!/usr/bin/python
#!coding=utf-8
import urllib2
import sys
from bs4 import BeautifulSoup
#python2 静态爬虫jenkins


url=sys.argv[1]

url_list=[]

all_num=0
succ_num=0
field_num=0
field_list=[]

html_doc = url
webpage = urllib2.urlopen(html_doc)
html = webpage.read()


soup = BeautifulSoup(html, 'html.parser')

for k in soup.find_all('a'):
    url = k.get('href')
    c= str(url)
    MM = c.startswith(('http://192.168.1.1','http://192.168.1.2'))
    if MM:
        url_list.append(url)

url_list = list(set(url_list))




#f=open(file,'r')
#lines=f.readlines() 
for line in url_list:
	print "lalalala %s" %(url_list)
#	line=line.strip('\n')
	all_num  = all_num  + 1
	try:
		urllib2.urlopen(line)
	except urllib2.HTTPError as e:

		field_num = field_num + 1
		field_list.append(line)
		
	else:
		succ_num = succ_num + 1

print "一共要传输的数量 : %s"  %(all_num)   
print "传输成功的数量: %s"  %(succ_num)
print "传输失败的数量: %s"  %(field_num)
	
if field_num != 0:
	print "以下目标地址没有成功传输"
        print field_list
        sys.exit(2)
else:
        print "所有包传输成功"

