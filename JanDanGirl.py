# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import re
import string
import HTMLParser
import uuid
from bs4 import BeautifulSoup

jandan_url = "http://jandan.net/ooxx/page-"
#img_basic_path = r'G:/Ex/PythonEx/PyImage/JanDanImages/'
img_basic_path = r'G:/Images/JanDan/'


def processData(beginPage,endPage):
	for i in range(beginPage,endPage):
		#获取数据
		url = jandan_url + str(i)
		print url
		data = load_data(url)
		#解析
		soup = BeautifulSoup(data,"html.parser")
		listContent = soup("a",class_="view_img_link")
		for item in listContent:
			imgHref = str(item['href'])
			if ".jpg" in imgHref:
				strImg = str(uuid.uuid1()) + ".jpg"
				down_load_img(item['href'],strImg)
			# if ".gif" in imgHref:
			# 	strImg = str(uuid.uuid1()) + ".gif"
			# 	down_load_img(item['href'],strImg)

			


def load_data(url):
	#user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
	user_agent="Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10"
	headers = {"User-Agent": user_agent}

	req = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(req)
	html = response.read()

	return html

def down_load_img(url,imgName):
	path = img_basic_path + imgName
	data = urllib.urlretrieve(url,path)



def main():
	processData(200,210)

if __name__ == "__main__":
	main()
