from os import read
import unittest

from traffic_data_processor import total_cars_seen
from traffic_data_processor import read_traffic_data
from traffic_data_processor import cars_by_day
from traffic_data_processor import top_half_hours
from traffic_data_processor import period_data

class TestTrafficDataProcessor(unittest.TestCase):

    def test_file_reader(self):
        # testing with wrong file path
        self.assertEqual(read_traffic_data('./input.txt'), [])
        self.assertEqual(len(read_traffic_data('./data/input.txt')), 24)
    
    def test_total_cars_seen(self):
        data = read_traffic_data('./data/input.txt')
        self.assertIsInstance(total_cars_seen(data), int)
        self.assertGreater(total_cars_seen(data), 0)
        data_empty = read_traffic_data('./data/input_empty.txt')
        self.assertEqual(total_cars_seen(data_empty), 0)

    def test_car_by_day(self):
        data = read_traffic_data('./data/input.txt')
        self.assertIsInstance(cars_by_day(data), dict)
        # test input file has 4 days only, testing correct categorisation
        self.assertEqual(len(cars_by_day(data)), 4)
        # testing empty files
        data_empty = read_traffic_data('./data/input_empty.txt')
        self.assertEqual(len(cars_by_day(data_empty)), 0)

    def test_top_half_hours(self):
        data = read_traffic_data('./data/input.txt')
        self.assertIsInstance(top_half_hours(data), list)
        self.assertEqual(len(top_half_hours(data)), 3)
        self.assertEqual(len(top_half_hours(data, top=5)), 5)
        data_empty = read_traffic_data('./data/input_empty.txt')
        self.assertEqual(len(top_half_hours(data_empty)), 0)

    def test_period_data(self):
        data = read_traffic_data('./data/input.txt')
        self.assertIsInstance(period_data(data), list)
        for i in period_data(data):
            self.assertIsInstance(i[1], int)
        data_empty = read_traffic_data('./data/input_empty.txt')
        self.assertEqual(len(period_data(data_empty)), 0)



if __name__ == '__main__':
    unittest.main()