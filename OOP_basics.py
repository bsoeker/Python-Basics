class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("You can only add points to other points")
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Drawing a point!")


point = Point(1, 2)
point.draw()
Point.zero().draw()

point2 = Point(1, 2)
print(point == 1)
print(point + point2)


# User defined container
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag: str):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag: str):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, value):
        self.__tags[tag] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
print(cloud["pythonsdf"])
print(cloud.__dict__)
