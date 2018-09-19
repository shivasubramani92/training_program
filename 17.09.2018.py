city = ["trichy","chennai","madurai"]
city1 = ["namakkal","salem","bangalore"]
cities = city + city1
print(cities)
city.append(city1)
print(city)
city.extend(city1)
print (city)
city.insert(2,"kovai")
city1.insert(0,"theni")
print(city)
city.remove("madurai")
city1.remove("namakkal")
print(city)
