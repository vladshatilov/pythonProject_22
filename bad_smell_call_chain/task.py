class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self):
        self.planet = Planet()
        self.population = 100500
        self.room_capacity = 42


    def get_person_room(self):
        return self.room_capacity

    def get_city_population(self):
        return self.population
