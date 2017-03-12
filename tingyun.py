#!/usr/bin/env python
# -*- coding:utf-8 -*-  
import sys,os
import re
import time
import subprocess
import commands
import random
import json
import requests
from headers import USER_AGENTS,ALL_COOKIES
import MySQLdb
conn = MySQLdb.connect('127.0.0.1','root','liaohong','big_v',charset='utf8')
cur = conn.cursor()

#读取V号的数据库big_v并插入数据，这个后续自己添加.	使用mysql，接受一个json串
#表的字段有：v_name , v_id , v_url , v_fans , v_search_count , v_focus
def insert_V(v_info):
	cur.execute('insert INTO weibo_stars(v_name,v_id,v_url,v_fans,v_search_count,v_focus) VALUES ("%s","%s","%s","%s","%s","%s")'%(v_info['v_name'],v_info['v_id'],v_info['v_url'],v_info['v_fans'],v_info['v_search_count'],v_info['v_focus']))

def get_info(keywork):
	pass


#请求url(带上cookies和headers)
def Request(url):
	header = random.choice(USER_AGENTS)
	cookie = random.choice(ALL_COOKIES)
	res = requests.get(url,headers={"USER_AGENT":header}).content
	return res

	"""
	good_code = [100000,0]
	if int(res["code"]) in good_code:
			return res
	else:
			#raise ValueError("访问失败，请检查cookies是否失效!")
			print "访问失败，请检查cookies是否失效!"
			return False
	"""
#从内容部获取关键词keyword(list)，使用微博搜索去访问，得到的count结果大于n，就将其保存到big_v库中，包含的信息有表的各个字段
def get_big_v(keyword,n):
	#这个key要查到准确的人(明星之类的)，一般输入英文全拼
	weibo_search = "http://s.weibo.com/ajax/suggestion?where=gs_weibo&type=gs_weibo&key={key}"
	#返回的结果，一堆dict的list
	res_list = []
	for key in keyword:
			url = weibo_search.format(key=key)
			map(lambda x:res_list.append(x) if (int(x['count']) > n) else "", Request(url)['data'])
	return res_list
#使用上面的得到的关键词（dict数据），拿到满足条件的key即可.
#我们这里拿到的结果是dict型的，如下：
#{fans_name : 
#		{
#			content:[value_list前十条内容],
#			type:a or b{关注微博并“差评的”，删除}
#		}		
#	}
def get_fans_type(keylist):
	bigv_name = "http://weibo.com/{name}?refer_flag=1001030101_&is_all=1"
	for key in keylist:
		res = Request(url)
	




if __name__ == '__main__':
	artist_name = ["xuezhiqian","jinsha","baijingting"]
	#res = get_big_v(artist_name , 1000000)
	print Request("http://s.weibo.com/ajax/suggestion?where=gs_weibo&type=gs_weibo&key=jinsha")

	
		


		
		

