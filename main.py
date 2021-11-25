from traffic_data_processor import read_traffic_data
from traffic_data_processor import total_cars_seen
from traffic_data_processor import half_hour_data
from traffic_data_processor import periodic_least_data



if __name__ == '__main__':
	data = read_traffic_data('./data/input.txt')
	print(read_traffic_data.__doc__)
	print(data)