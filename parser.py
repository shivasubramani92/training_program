import json
from pprint import pprint

json_data = []

with open('training.json') as json_data:
    d = json.load(json_data)
for line in d:
    a = line
    pprint(a) 
    tr  =  open('a.txt',"a")
    json.dump(a,tr)
               
