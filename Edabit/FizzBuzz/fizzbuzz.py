

def fizzbuzz(number):
	try:
		number = int(number)

	except ValueError:
		print("Please enter an integer or a whole number")

	if number % 3 ==0 and number % 5 == 0:
		print("FizzBuzz")
		return "FizzBuzz"
	elif number % 3 == 0:
		print("Fizz")
		return "Fizz"
	elif number % 5 == 0:
		print("Buzz")
		return "Buzz"	
	else:
		print("{}".format(number))
		return number
