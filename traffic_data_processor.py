
def read_traffic_data(file_path):
	"""Returns List of Tuples. Tuples are (date, number) pairs
	"""
	traffic_data = []
	try:
		with open(file_path, 'r') as input_file:
			lines =input_file.readlines()
			for line in lines:
				# each line assumed to have only two items separeted by space
				timestamp_, number_of_cars = line.split()
				# number_of_cars are assumed to be numbers
				traffic_data.append((timestamp_, int(number_of_cars)))
	except FileNotFoundError:
		print(f"The file '{file_path}' does not exist.")
	# returns empty list if 
	## - Error on read file
	## - file is empty file
	return traffic_data

def total_cars_seen(traffic_data):
	"""Returns the sum of all cars from [traffic_data]"""
	# traffic_data is assumed to be list of tuples, each tuple with 2 items
	# second item of each [traffic_data] item is the number of car
	cars = [item[1] for item in traffic_data]
	return sum(cars)

def half_hour_data(traffic_data, top=3):
	"""sorts [traffic_data] reversed, returns top value, top defaults to 3"""
	# traffic_data is assumed to be list of tuples, each tuple with 2 items
	sorted_traffic_data = sorted(traffic_data, key=lambda item: item[1], reverse=True)
	return sorted_traffic_data[:top]

def periodic_least_data(traffic_data, period=3):
	""""""
	# list to hold the period data: dictionary
	group_by_period= []
	# traffic_data is assumed to be list of tuples, each tuple with 2 items
	# loop through by index
	for index in range(len(traffic_data)):
		# every loop gets the slice of next 3(period) items
		# convert the slice to dictionary
		group_by_three = dict(traffic_data[index:index+period])
		# only take if the slice fit in the period set
		if (len(group_by_three) == period):
			group_by_period.append(group_by_three)

	for i in group_by_period:
		print(tuple(i.keys()), sum(i.values()))