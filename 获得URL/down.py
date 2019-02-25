#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
#解析excel获取包的url并批量下载
import xlrd
import sys
import os 
import subprocess
import urllib2

file=sys.argv[1]

all_num = 0
now_num = 0
err_num = 0
errorlist=[]
data = xlrd.open_workbook(file) 
table = data.sheets()[1] 
nrows = table.nrows 
print 'nrows: %s' %(nrows) 

for i in range(nrows):
	# url = table.row_values(i)[1:3]
	 url = table.row_values(i)[2]
	 ifsql = table.row_values(i)
#	 module = table.row_values(i)[1]
#	 print i,ifsql
	 result=any(url)
		
	 if result == True and url != u"编译日期" and url != u"模块路径" and ifsql[0] != u"修改数据库脚本":
		
		all_num = all_num + 1
		print "\033[1;32m  url: %s  \033[0m"  %(url)
		cmd = 'wget %s' %(url)
		try: 
	 		urllib2.urlopen(url)
			subprocess.call(cmd,shell=True)
		except urllib2.HTTPError as e:
			print "\033[1;31;40m **************************************************",e.code,"********************************************************* \033[0m"
       			print "\033[1;31;40m ****",url,"**** \033[0m"
        		print "\033[1;31;40m ****************************************************url is invaild*************************************************\033[0m"
			err_num = err_num + 1
			errorlist.append(url)





		
print "\033[1;30;47m' + '***************************************************' + '\033[0m"
print "\033[1;32m package all : %s \033[0m" %(all_num)
print "\033[1;31;40m package field: %s 个 \033[0m" %(err_num)
print "\033[0;31m field address: %s \033[0m" %(errorlist)
