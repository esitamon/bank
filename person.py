

class Person:
  #counter class Attribute
  counter = 0
  def __init__(self, name, origin, address):
    self.name = name 
    self.origin = origin
    self.address = address 

  @classmethod
  def counter(counter):
    counter+=1
    return counter

  @property
  def name(self):
    return self.name 
  @property
  def origin(self):
    return self.origin
  @property
  def address(self):
    return self.addres

  @name.setter
  def set_name(self, name):
    self.name = name 
  @origin.setter
  def set_origin(self,origin):
    self.origin = origin
  @address.setter
  def set_address(self, address):
    self.address = address

