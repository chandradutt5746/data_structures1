import json
from pprint import pprint

# Opening JSON file
#f = open('C:\\Users\\chandradutt patel\\Desktop\\Practice\\data structures\\smartserv\\assignment.json', encoding='utf-8')

with open('C:\\Users\\chandradutt patel\\Desktop\\Practice\\data structures\\smartserv\\assignment.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))
 
    # Print the data of dictionary
    print("\products:", data['products'])

# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['products']:
    print(i)
 
# Closing file
f.close()