class Vehicle:
  def __init__(self, starting_top_speed=100):
      self.top_speed = starting_top_speed
      self.__warnings = []

  def __repr__(self):
    print('Printing...')
    return 'Top speed: {}, Warnings: {}'.format(self.top_speed, self.__warnings)

  def add_warning(self, warning_text):
    self.__warnings.append(warning_text)

  def get_warnings(self):
    return self.__warnings

  def drive(self):
    print('I am driving but certainly not faster than {}'.format(self.top_speed))
