def matrix(x, y, z):
	lst = []
	item = ""
	for i in range(x):
			item = []
			for a in range(y):
				item.append(z)
			print(item)
			lst.append(item)
	return lst
 '''
 example
 > matrix(3,2'hello')
 [['hello','hello'],['hello,'hello'],['hello','hello']]
 '''
