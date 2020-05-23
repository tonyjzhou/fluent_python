from collections import namedtuple

City = namedtuple("City", "name country population coordinates")
print(City._fields)

Coordinates = namedtuple("Coordinates", "latitude longitude")

metro_areas = [
    City("Tokyo", "JP", 36.933, Coordinates(35.689722, 139.691667)),
    City("Delhi NCR", "IN", 21.935, Coordinates(28.613889, 77.208889)),
    City("Mexico City", "MX", 20.142, Coordinates(19.433333, -99.133333)),
    City("New York-Newark", "US", 20.104, Coordinates(40.808611, -74.020386)),
    City("Sao Paulo", "BR", 19.649, Coordinates(-23.547778, -46.635833)),
]

for ma in metro_areas:
    print(ma)
    print(f"{ma.name} {ma.coordinates}")
    print(ma._asdict())
    print()
