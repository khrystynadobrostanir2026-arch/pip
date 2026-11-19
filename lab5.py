class Furniture:

    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates

    def set_name(self, name):
        self.name = name

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def get_name(self):
        return self.name

    def get_coordinates(self):
        return self.coordinates

    def get_info(self):
        print("Name:", self.name, ", coordinates:", self.coordinates, sep=" ")

    def __del__(self):
        print("\nObject", self.name, "deleted")

class Bed(Furniture):

    def __init__(self, name, coordinates, size):
        super().__init__(name, coordinates)
        self.size = size

    def get_info(self):
        super().get_info()
        print("Size:", self.size)

class Table(Furniture):
    def __init__(self, name, coordinates, material):
        super().__init__(name, coordinates)
        self.material = material

    def get_info(self):
        super().get_info()
        print("Material:", self.material)

class Carpet(Furniture):
    def __init__(self, name, coordinates, color):
        super().__init__(name, coordinates)
        self.color = color

    def get_info(self):
        super().get_info()
        print("Color:", self.color)

class Room:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(item.get_name(), "added to the room.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.get_name() == item_name:
                self.items.remove(item)
                print(item_name, "removed from the room.")
            return
        print("Item not found.")

    def rearrangement(self, item_name, new_coordinates):
        for item in self.items:
            if item.get_name() == item_name:
                item.set_coordinates(new_coordinates)
                print("Coordinates of", item_name, "changed to", new_coordinates)
                return
        print("Item not found.")

    def show_room(self):
        print("\nRoom Items")
        if not self.items:
            print("The room is empty.")
        for item in self.items:
            item.get_info()

def main():
    bed = Bed("bed", [3, 4], "double")
    table = Table("table", [5, 5], "wood")
    carpet = Carpet("carpet", [3, 2], "blue")
    my_room = Room()

    print("Adding Items")
    my_room.add_item(bed)
    my_room.add_item(table)
    my_room.add_item(carpet)

    my_room.show_room()

    print("Rearrangement")
    my_room.rearrangement("bed", [0, 0])

    my_room.show_room()

    print("Removing Item")
    my_room.remove_item("carpet")

    my_room.show_room()

object1 = Furniture("sofa", [1,1])
object2 = Furniture("chair", [6,4])
object3 = Furniture("wardrobe", [3,5])

my_room = Room()
my_room.add_item(object1)
my_room.add_item(object2)
my_room.add_item(object3)

for item in my_room.items:
    print(item.get_name())

if __name__ == "__main__":
    main()

