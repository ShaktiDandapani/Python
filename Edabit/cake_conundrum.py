def get_total_cost(number_of_cakes):
	"""
	Return the cost of the cakes with
	the fees for each cake to buy them.

	Args:
	-----

	Return:
	-------

	"""
	try:
		number_of_cakes = int(number_of_cakes)
	except	ValueError:
		try:
			val = float(number_of_cakes)
			print("Input is a float, can only buy cakes in \
				full pieces, not fractions.")
		except ValueError:
			print("You put in a word for number of cakes :P")

	cost_per_cake = 1 # dollar $
	fees = 2
	total_cost = number_of_cakes * cost_per_cake * fees

	return total_cost


