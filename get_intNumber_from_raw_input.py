#coding:utf-8
#从控制台输入的带空格的无规则字符串中得到纯数字并作为int类型储存输出


def Filter_input(inputlist):
	charlist =  inputlist.split()
	numlist = []

	def is_number(char):
		try:
			int(char)
			return True
		except ValueError:
			return False

	for i in charlist:
		if is_number(i):
			num = int(i)
			numlist.append(num)
	count = len(numlist)
	return numlist


AlbumInfo = False
while not AlbumInfo:
	inputlist = raw_input("请输入你要下载的相册序号:")
	Numlist = Filter_input(inputlist)
	for i in Numlist:
		print('%d' % i)