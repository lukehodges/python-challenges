def triangle(n):
  '''
  outputs the triangled number of the input
  triangle(1) ➞ 1
  triangle(6) ➞ 21
  '''
	count = 0
	for i in range(n+1):
		count += i
	return count
