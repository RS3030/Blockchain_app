import sys
sys.path.append('./')

from oop.vehicle import *

class Bus(Vehicle):
    def __init__(self, starting_top_speed=100):
        super().__init__(starting_top_speed)
        self.passengers = []

    def add_group(self, passengers):
      self.passengers.extend(passengers)


bus1 = Bus()
bus1.drive()

bus1.add_warning('bus1 New warning')
bus1.add_group(['Ryo', 'Taro', 'Poti'])
print(bus1.passengers)

bus2 = Bus(starting_top_speed=200)
bus2.drive()
print(bus2.__dict__)
bus2.__repr__()
