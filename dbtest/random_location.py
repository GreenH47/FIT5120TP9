import csv
from random import uniform

# Set the range of Melbourne coordinates
latitude_range = (-38.1, -37.5)
longitude_range = (144.6, 145.5)

# Generate random coordinates in Melbourne
locations = [{"latitude": uniform(*latitude_range), "longitude": uniform(*longitude_range)} for _ in range(100)]

# Define the CSV file path and name
csv_file = 'melbourne_coordinates.csv'

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['latitude', 'longitude'])
    writer.writeheader()
    writer.writerows(locations)

print(f"CSV file '{csv_file}' has been generated successfully.")
