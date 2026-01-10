class Item:
  def __init__(self, name, price, weight):
    self.name = name
    self.price = float(price)
    self.weight = weight

class ShoppingCart:
  def __init__(self):
    self.items = list()

  def __len__(self):
    return len(self.items)

  def add(self, item, qtt=1):
    if isinstance(qtt, (int, float)):
      self.items.append({"qtt": qtt, "item": item})

  def show(self):
    return self.items

  def remove(self, index):
    self.items.pop(index)

  def total_price(self):
    total = 0
    for element in self.items:
      total+= element["item"].price * element["qtt"]
    return total
    
  def total_weight(self):
    total = 0
    for element in self.items:
      total+= element["item"].weight * element["qtt"]
    return total
    
class User:
  def __init__(self, first_name, second_name):
    self.first_name = first_name
    self.second_name = second_name
    self.tabs = list()

  def open_tab(self, shopping_cart):
    self.tabs.append(shopping_cart)

  def close_tab(self, index):
    self.tabs.pop(index)

  def sum_tabs(self):
    total = 0
    for tab in self.tabs:
      total += tab.total_price()
    return total
