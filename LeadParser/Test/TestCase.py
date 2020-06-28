import json
import os

with open('Correct.json') as f:
	correct_data = json.load(f)

test_data_path = (os.path.dirname(os.getcwd()) + '\\Output')

with open(test_data_path + "\\" + "output.json") as f2:
	test_data = json.load(f2)

if(correct_data == test_data):
	print("Test passed")
else:
	print("Test Failed")