

def fizzbuzz(number):

	fizz = "Fizz"
	buzz = "Buzz"
	fizzbuzz = fizz + buzz

	try:
		number = int(number)

	except ValueError:
		print("Please enter an integer or a whole number")

	if number % 3 ==0 and number % 5 == 0:
		print(fizzbuzz)
		return fizzbuzz
	elif number % 3 == 0:
		print(fizz)
		return fizz
	elif number % 5 == 0:
		print(buzz)
		return buzz	
	else:
		print("{}".format(number))
		return number
