class Category:
  
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0.00

  def deposit(self, amount, descr=" "):
    if descr:
      self.ledger.append({"amount": amount,"description": descr})
    else:
      self.ledger.append({"amount": amount,"description": " "})

  def get_balance(self):
    for transaction in self.ledger:
      self.balance += transaction["amount"]
      return self.balance

  def check_funds(self, amount):
    if(amount >= 0):
      if(amount > self.balance):
        return False
      else:
        return True
    else:
      if(-(amount) > self.balance):
        return False
      else: 
        return True

  def withdraw(self, amount, descr=" "):
    if(self.check_funds(amount)): 
      self.ledger.append({"amount": amount, "description": descr})
      return True
    else:
      return False

  def transfer(self, amount, category):
    destination_category = Category(category)
    if(self.check_funds):
      self.withdraw(amount, "Transfer to " + category.name)
      destination_category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False 
      
def create_spend_chart(categories):
    return "poop"