cities = {
    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Nashik": "Maharashtra",
    "Delhi": "Delhi",
    "Bengaluru": "Karnataka"
}

city = input("Enter city name: ")

if city in cities:
    print(city, "is in", cities[city])
else:
    print("City not found")