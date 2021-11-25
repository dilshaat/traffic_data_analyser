traffic_data = []

with open('./data/input.txt', 'r') as input_file:
	lines =input_file.readlines()
	for line in lines:
		timestamp_, number_of_cars = line.split()
		traffic_data.append((timestamp_, int(number_of_cars)))
	
cars_by_day = {}
for i in traffic_data:
	day = i[0].split('T')[0]
	if day in cars_by_day:
		cars_by_day[day] += i[1]
	else:
		cars_by_day[day] = i[1]
print(cars_by_day)
# group_by_30min = []
# for index in range(len(traffic_data)):
# 	group_by_three = dict(traffic_data[index:index+3])
# 	if (len(group_by_three) == 3):
# 		group_by_30min.append(group_by_three)

# for i in group_by_30min:
# 	print(i)
# 	print(tuple(i.keys()), sum(i.values()))
# least_cars_by_15 = []
# for i in group_by_30min:
# 	cars = []
# 	period = []
# 	for j in i:
# 		period.append(j[0])
# 		cars.append(j[1])
# 	least_cars_by_15.append((tuple(period), sum(cars)))
# for i in least_cars_by_15:
# 	print(i)
	

# for index in range(len(traffic_data)):
# 	if index == len(traffic_data) - 2:
# 		break
# 	group_by_30min.append((traffic_data[index], traffic_data[index+1], traffic_data[index+2]))


# for i in group_by_30min:
# 	print(i)
# print(traffic_data)

# total_cars_seen = [i[1] for i in traffic_data]
# print(sum(total_cars_seen))

# sorted_traffic_data = sorted(traffic_data, key=lambda item: item[1], reverse=True)

# print(list(sorted_traffic_data)[:3])