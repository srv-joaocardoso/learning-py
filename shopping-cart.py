class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = float(price)

class ShoppingCart:
  def __init__(self):
    self.itens = list()

  def __len__(self):
    return len(self.itens)

  def add(self, item):
    self.itens.append(item)

  def show(self):
    return self.itens

  def total(self):
    sum = 0
    for item in self.itens:
      sum+= item.price

    return sum
