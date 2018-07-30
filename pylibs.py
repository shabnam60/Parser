import re
from datetime import datetime

global invalid_counter
invalid_counter = 0

global value_2_dict
value_2_dict = {}

#validate date
def validate_date(date_str):
	try:
		datetime.strptime(date_str, '%Y-%m-%d-%H:%M:%S')
		return True
	except ValueError:
		return False

def validate_stuff(input):

	global invalid_counter

	ID_split = input.strip().split(" ", 1)
	#print(ID_split)
	ID = int(ID_split[0].strip())
	if ID <= 0:
		invalid_counter += 1
		return

	#validate date
	date_split = ID_split[1].strip().split(" ", 1)
	if validate_date(date_split[0].strip()) is False:
		invalid_counter += 1
		return

	#validate arguments
	rest = date_split[1].strip()
	#print(rest)
	rest1 = re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+',rest)
	value=rest1[1]
	if len(rest1) != 3 :
		invalid_counter +=1
		return
	else :
		#print (value_2_dict)
		if ID in value_2_dict:
			value_2_dict[ID].append(value)
		else:
			value_2_dict[ID] = [value]

#To open to text
test_file = open("test.txt","r")

#testing portion
lines = [line.rstrip('\n') for line in (test_file)]
for line in lines:
    validate_stuff(line)


print("Total no. of invalid lines: " + str(invalid_counter))

requests = input("Please enter the IDs each separated by a comma: ")
requestsList = requests.split(",")
intRequestList = []

#inputchecker
for request in requestsList:
	try:
		intRequestList.append(int(request.strip()))
	except ValueError:
		print("\"" + request.strip() + "\" is not a valid input :(")

for ID in intRequestList:
	try:
		for value in value_2_dict[ID]:
			print(str(ID) + ' ' + value)
	except KeyError:
		print("ID: " + str(ID) + " not found in database")
