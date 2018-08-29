dict = {}

dict['one'] = "say one"
dict['two'] = "say two"
dict[20] = " twenty"
dict[45] = "fourty five"

tinydict = {'name' :'siva','code': 0005,'dept': 'training' }
 
print dict ['one']
print dict [20]
print tinydict.keys()
print tinydict.values()
print tinydict
print tinydict * 2
print tinydict + dict['one'] + dict[20]

