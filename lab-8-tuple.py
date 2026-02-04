
coordinates = ( 10, 20, 30)
print("coordinates tupple:", coordinates)

# Attempt to change the x-coordinate
try:
    coordinates[0] = 100
except TypeError as e:
    print("Error:", e)

