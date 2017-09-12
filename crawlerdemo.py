#coding:utf-8
from __future__ import print_function
from bs4 import BeautifulSoup
import urllib
import re
import os

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html	

class GetAlbum(object):
	"""docstring for GetAlbum"""
	
	def __init__(self, url):
		super(GetAlbum, self).__init__()
		self.url = url
		page = urllib.urlopen(self.url)
		self.html = page.read()
		
	def getAlbum(self):
		Soup = BeautifulSoup(self.html, 'lxml')
		# print Soup
		imagetags = Soup.select('#content > div.grid-16-8.clearfix > div.article > div.wr > div > div > div.pl2 > a')
		picnumbertags = Soup.select('#content > div.grid-16-8.clearfix > div.article > div.wr > div > div > span')

		for albumhref, albumname, picnumber in zip(imagetags,imagetags,picnumbertags):
			data = {
				'albumhref':albumhref.get('href'),
				'albumname':albumname.get_text(),
				'picnumber':picnumber.get_text()
			}
			print(data['albumhref'],data['albumname'],data['picnumber'],sep='\n')
		# filename = imagetag.get('alt')
		# imgurl = imagetag.get('src')

		# path = 'imgdownload/'
		# if not os.path.exists(path):
		# 	os.makedirs(path)
		# target = path + '%s.jpg' % filename
		# urllib.urlretrieve(imgurl, target)

	


if __name__ == '__main__':
	url = ""
	html = getHtml(url)

	getAlbum1 = GetAlbum(url)
	getAlbum1.getAlbum()



