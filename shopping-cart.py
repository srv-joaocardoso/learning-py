class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = float(price)

class ShoppingCart:
  def __init__(self):
    self.itens = list()

  def __len__(self):
    return len(self.itens)

  def add(self, item, qtt=1):
    if isinstance(qtt, (int, float)):
      self.itens.append({"qtt": qtt, "item": item})

  def show(self):
    return self.itens

  def remove(self, index):
    self.itens.pop(index)

  def total(self):
    total = 0
    for element in self.itens:
      total+= element["item"].price * element["qtt"]
    return total
    
class User:
  def __init__(self, first_name, second_name):
    self.first_name = first_name
    self.second_name = second_name
