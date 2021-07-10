from person import Person

class customer(Person):
  def __init__(self, name, origin, address,bank,transaction):
    self.bank = bank
    self.transaction = transaction
    super().__init__( name, origin, address)

  @property
  def bank(self):
    return self.bank 

  @property
  def transaction(self):
    return self.transaction