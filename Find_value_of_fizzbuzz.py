def fizz_buzz(num):# num represent the number to test
	s = ''#       fizz_buzz(3) -> Fizz
	if num%3 == 0: s += 'Fizz'# if remainder is 0 add fizz to answer
	if num%5 == 0: s += 'Buzz'# if remainder is 0 add buzz to answer * this means if divisible by 3 and 5 will return fizzbuzz
	return s if s else str(num)# outputs s if s has a value otherwise print out the number
