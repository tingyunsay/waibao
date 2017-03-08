#!/usr/bin/env python
# -*- coding:utf-8 -*-  
import sys,os
import re
import time
import subprocess
import commands
import random
import json
from headers import USER_AGENTS

conn = MySQLdb.connect('127.0.0.1','root','liaohong','liaohong_test',charset='utf8')
cur = conn.cursor()

#默认读取当前目录下的mycookies.json文件,发挥cookies的list，供后续请求头部附加
def get_cookies():
	with open('./mycookies.json') as f:
		cookies_count = []
		data = f.read()
		res = re.findall('{.+?}',data)
		for i in res:
			cookies_count.append(json.loads(i))
		f.close()
	return cookies_count

#读取V号的数据库big_v并插入数据，这个后续自己添加.	使用mysql，接受一个json串
#表的字段有：v_name , v_id , v_url , v_fans , v_search_count , v_focus
def insert_V(v_info):
	cur.execute('insert INTO weibo_stars(v_name,v_id,v_url,v_fans,v_search_count,v_focus) VALUES ("%s","%s","%s","%s","%s","%s")'%(v_info['v_name'],v_info['v_id'],v_info['v_url'],v_info['v_fans'],v_info['v_search_count'],v_info['v_focus']))

def get_info(keywork):
	pass


#从内容部获取关键词keyword，使用微博搜索去访问，得到的count结果大于n，就将其保存到big_v库中，包含的信息有表的各个字段
def get_big_v(keyword,n):
	





if __name__ == '__main__':
		all_cookies = get_cookies()


		


		
		

