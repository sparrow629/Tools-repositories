import multiprocessing
import os
import time

def output(number):
	
	print("%d Process ID: %d\n" % (number,os.getpid()))

class multiProcess(multiprocessing.Process):
	"""docstring for multiProcess"""
	def __init__(self, func, arg, worknum):
		super(multiProcess, self).__init__()
		self.func = func
		self.arg = arg	
		self.worknum = worknum

	def works(self):
		proc_record = []

		for i in range(self.worknum):
			p = multiprocessing.Process(target = self.func, args = (i,))
			p.daemon = True
			p.start()
			proc_record.append(p)
		for p in proc_record:
			p.join()
		

def main():

	procs = 4

	arg = procs
	works = multiProcess(output, arg, procs)
	works.works()
	print("The number of CPU:%d \n" % multiprocessing.cpu_count())
	print("End!")
	
if __name__ == '__main__':
	main()
