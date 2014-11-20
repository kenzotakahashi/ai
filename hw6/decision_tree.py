from math import log
from sys import argv

def myLog(x, base):
	"""support log 0"""
	return log(x, base) if x != 0 else 0

def entropy(pList):
	"""Compute entropy"""
	collection = sum(pList)
	return sum(-(p / collection) * myLog(p / collection, 2) for p in pList)

# print (entropy([9,5]))

def gain(pList, attributes):
	"""Compute information gain. Greater the gain is, the better the attribute is."""
	collection = sum(pList)
	return entropy(pList) - sum([sum(a) / collection * entropy(a) for a in attributes])

def main():
	# print (gain([9,5], [[6,2],[3,3]])) # wind
	# print (gain([9,5], [[3,4],[6,1]])) # humidity
	# print (gain([9,5], [[2,3],[4,0],[3,2]])) # outlook
	# print (gain([9,5], [[2,2],[4,2],[3,1]])) # temperature

	if len(argv) == 1:
		# print (gain([29,35],[[21,5],[8,30]]))
		# print (gain([9,5],[[4,3],[6,1]]))
		# print (gain([9,5],[[2,3],[4,0],[3,2]]))
		print (gain([7,4],[[4,1],[1,1],[2,2]]))
		print (gain([7,4],[[4,1],[3,0],[1,3],[1,0]]))
	else:
		if argv[1] == 'e':
			print (entropy([int(i) for i in argv[2:]]))
		if argv[1] == 'l':
			# Log 2
			if len(argv) == 3:
				print (myLog(int(argv[-1]), 2))
			# Log 2 wih division
			else:
				print (myLog(int(argv[-2]) / int(argv[-1]), 2))

if __name__ == '__main__':
	main()