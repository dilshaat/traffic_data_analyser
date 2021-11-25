from traffic_data_processor import read_traffic_data
from traffic_data_processor import total_cars_seen
from traffic_data_processor import cars_by_day
from traffic_data_processor import top_half_hours
from traffic_data_processor import period_data

def run(traffic_data):
	print("Please choose:")
	print("1)", "Get total number of cars")
	print("2)", "Cars by date")
	print("3)", "Top 3 half hours recorded most cars")
	print("4)", "Show 3 continuous half hours recorded least cars")
	print("your choice: ", end="")
	user_input = input()
	print()

	if user_input == "1":
		print('*' * 50)
		print(f"Total cars recorded: {total_cars_seen(traffic_data)}")

	if user_input == "2":
		day_car = cars_by_day(traffic_data)
		print('*' * 50)
		for k, v in day_car.items():
			print(k, v)

	if user_input == "3":
		top_values = top_half_hours(traffic_data)
		print('*' * 50)
		print("Top half hours:")
		for i in top_values:
			print(i[0], i[1])

	if user_input == "4":
		period, num_of_cars = period_data(traffic_data)[0]
		print('*' * 50)
		print(f'In period {period} only {num_of_cars} recorded')

if __name__ == '__main__':
	data = read_traffic_data('./data/input.txt')
	print("Please use Ctrl+C to exit the program:")
	while True:
		try:
			run(data)
			print('*' * 50)
		except KeyboardInterrupt:
			print()
			print("Bye!")
			exit()