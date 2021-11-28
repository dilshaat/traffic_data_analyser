# Traffic Data Analyzer

## Introduction

This project analyzes a data file produced by a machine which records number of cars passed every 30 minutes in a particular street. The machine writes the data in:
```
'datetime' int
```
format where the `dattime` is the every 30 minutes timestamp starting from midnight and `int` is the number of cars passed in that half hour. 
This project is to perform certain statistical analysis:
- Total number of cars recorded in the file
- Total number of cars by day
- Most cars seen `half-hour`s
- Least cars seen `half-hour` periods
    - three `half-hour` period : 1.5 hours

## Assumptions
The code assumed the data provided in the file is correct format, (`datetime` `int`), and second column is numeric only. Also, the code assumes that there is no missing fields in the file, hence, the code (read file) does not perform any sanity checks against the data found in the file. 

## Project Structure
This project is structured in the following format:
```
│--- .gitignore
│--- main.py
│--- README.md
|--- test_traffic_data_processor.py
│---  traffic_data_processor.py
└───data
        input.txt
        input_empty.txt
```

### main.py
This file is the entry point of the project it provides basic (terminal) user interface.

### traffic_data_processor.py
This file contains five main functions of this project:
1. `read_traffic_data`
2. `total_cars_seen`
3. `cars_by_day`
4. `top_half_hours`
5. `period_data`

#### `read_traffic_data`
This function takes one parameter, `file_path`, and reads the lines of the file and splits the line into `timpestamp` and `number_of_car` and forms a `tuple` from these two data and appends the newly formed `tuple` to a local `list`, `traffice_data`. If the file is empty or wrong path is provided to the function, an empty `list` is returned.

#### `total_cars_seen`
This functions takes a `list` as its argument and assumes the items in the list is a `tuple` : `('timestamp`, `int`). It simply reads the `int` part of the `list` and returns its `sum`.

#### `cars_by_day`
This functions takes a `list` as its argument and assumes the items in the list is a `tuple` : ('timestamp', `int`). It creates local `dict`, `day_car`. The functions traverses the `list` argument and takes the data part of the timestamp as key and `int` part will be added to the key. 

#### `top_half_hours`
This functions takes a `list` as its argument and assumes the items in the list is a `tuple` : ('timestamp', `int`). The `list` is reverse sorted by second part of each item, then by default, first three are returned as a `list`.

#### `period_data`
This functions takes a `list` as its argument and assumes the items in the list is a `tuple` : ('timestamp', `int`). The function traverses the list by its index and adds the next three items to a local list as a dictionary, e.g. :
```python
{'2016-12-01T05:00:00': 5, '2016-12-01T05:30:00': 12, '2016-12-01T06:00:00': 14}
```
Second step, create new list, and travers first list by create a tuple:
```python
(('2016-12-01T05:00:00', '2016-12-01T05:30:00', '2016-12-01T06:00:00'), 31)
```
where the first one is the grouping of timestamps, and second item is the sum of the number for each grouped timestamp. 
Finally, sort the list and return the first.

## Tests
A simple `unittest` is used to test the functions. The test file is `test_traffic_data_processor.py` and to run the test:

```python
python test_traffic_data_processor.py
```
