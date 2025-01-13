import pickle

vehicle = {
    'brand': 'BMW',
    'model': '530i',
    'year': 2015,
    'color': 'Black Sapphire'
}

my_file = open('./Exercise01_4/vehicledetail.bin', 'wb')
# Calling the pickle.dump() method
# while passing 'vehicle' as the dictionary,
# and 'my_file' as the file object.
pickle.dump(vehicle, my_file)
my_file.close()

with open('./Exercise01_4/vehicledetail.bin', 'rb') as my_file:
    vehicle = pickle.load(my_file)

print("Vehicle details - ")
print("Name:  " + vehicle['brand'] + " " + vehicle['model'])
print("Year:  " + str(vehicle['year']))
print("Color: " + vehicle['color'])
