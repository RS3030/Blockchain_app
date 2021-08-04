import sys
sys.path.append('./')

from oop.vehicle import *

class Car(Vehicle):
  def brag(self):
    print('How how cool my car is!')

car1 = Car()
car1.drive()

car1.add_warning('car1 New warning')
print(car1.__dict__)

car2 = Car(starting_top_speed=200)
car2.drive()
print(car2.__dict__)
car2.__repr__()