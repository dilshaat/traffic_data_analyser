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
	# second item of each [traffic_data] item is the number of car
	cars = [item[1] for item in traffic_data]
	return sum(cars)

def cars_by_day(traffic_data):
	"""Returns dictionary, Key: day, Value: number of cars"""
	day_car = {}
	for data in traffic_data:
		# day part is before 'T'
		day = data[0].split('T')[0]
		cars = data[1]
		if day in day_car:
			day_car[day] += cars
		else:
			day_car[day] = cars
	return day_car


def top_half_hours(traffic_data, top=3):
	"""sorts [traffic_data] reversed, returns top value, top defaults to 3"""
	sorted_traffic_data = sorted(traffic_data, key=lambda item: item[1], reverse=True)
	return sorted_traffic_data[:top]


def period_data(traffic_data, period=3):
	""""""
	# list to hold the period data: dictionary
	group_by_period= []
	for index in range(len(traffic_data)):
		# every loop gets the slice of next 3(period) items
		group_by_three = dict(traffic_data[index:index+period])
		# only take if the slice fit in the period set
		if (len(group_by_three) == period):
			group_by_period.append(group_by_three)
	group_by_summed = []
	for i in group_by_period:
		group_by_summed.append((tuple(i.keys()), sum(i.values())))
	return sorted(group_by_summed, key=lambda item: item[1])