def fizz_buzz(num):# num represent the number to test
	s = ''#       fizz_buzz(3) -> Fizz
	if num%3 == 0: s += 'Fizz'
	if num%5 == 0: s += 'Buzz'
	return s if s else str(num)
