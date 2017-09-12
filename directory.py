#coding:utf-8
#查找并新建路径存储网络URL的图片

import os, time, random, urllib
 
path = '/Volumes/G/Test/'
src = 'http://img.aitaotu.cc:8088/Pics/2016/0222/03/09.jpg'
if not os.path.exists(path):
	os.makedirs(path)

target = path + 'test.jpg' 
urllib.urlretrieve(src, target)