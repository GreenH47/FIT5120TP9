import json
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon


def is_point_inside_shape(point, polygon):
    if polygon.contains(Point(point)):
        return True
    else:
        return False


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
    print("There are %d collection dates in this council" % len(features))
    # Extract the coordinates
    for i in range(len(features)):
        coordinate = data["features"][i]["geometry"]["coordinates"][
            0]  # Assuming you want the first feature's coordinates
        coordinates.append(coordinate)

    # Split the coordinates into latitude and longitude
    latitudes, longitudes = zip(*coordinates[3])

    # # Iterate over the coordinates list
    # for coordinate in coordinates:
    #     # Create a Polygon object
    #     polygon = Polygon(coordinate)
    #
    #     # Check if the point is inside the shape
    #     if is_point_inside_shape(point, polygon):
    #         print("The point is inside the shape")
    #     else:
    #         print("The point is outside the shape")

    # Plot the polygon
    plt.plot(longitudes, latitudes)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Polygon from JSON Data')
    plt.gca().invert_yaxis()  # Invert the Y-axis to match a typical map
    plt.grid(True)
    plt.show()


def enter_point():
    latitudes = float(input("Enter latitudes: "))
    longitudes = float(input("Enter longitudes: "))
    point = [latitudes, longitudes]
    find_point(point)


if __name__ == '__main__':
    # enter_point()
    find_point()
