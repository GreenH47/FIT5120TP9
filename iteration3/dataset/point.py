import json
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon


def find_point():
    # Load the JSON data from a file
    with open('kingston.json', 'r') as json_file:
        data = json.load(json_file)

    # Access the JSON properties
    print("Type:", data["type"])
    print("Name:", data["name"])

    # Access the features
    features = data["features"]

    coordinates = []
    print("there are %d collection date in this council" % len(features))
    # Extract the coordinates
    for i in range(len(features)):
        coordinate = data["features"][i]["geometry"]["coordinates"][
            0]  # Assuming you want the first feature's coordinates
        coordinates.append(coordinate)

    # Split the coordinates into latitude and longitude
    # print test template
    latitudes, longitudes = zip(*coordinates[0])




    # Plot the polygon
    plt.plot(longitudes, latitudes)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Polygon from JSON Data')
    plt.gca().invert_yaxis()  # Invert the Y-axis to match a typical map
    plt.grid(True)
    plt.show()


def enter_point():
    longitudes = input("Enter longitudes: ")
    latitudes = input("Enter latitudes: ")

    find_point(point)


if __name__ == '__main__':
    enter_point()

