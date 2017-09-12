#!/bin/python
#coding=utf-8
#记录log创建或者直接打开并在文件末尾追加

import datetime

def log(string):
	txtName = "log.txt"
	f=file(txtName, "a")
	timestamp = datetime.datetime.now()
	try:
		new_context = "%s\n%s" % (timestamp,string) + '\n'
		f.write(new_context)
		print("%s\nlog succeed！" % timestamp)
	except:
		print('log file.')
	finally:
		f.close()

if __name__ == '__main__':
	string = 'success!'
	log(string)