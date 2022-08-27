class Category:
  def __init__(self, name):
    self.name = name
    ledger = []

  def deposit(amount, descr=""):
    ledger.append({"amount": amount,"description": descr})

  def get_balance:
    for(transaction in ledger):
      balance += transaction["amount"]
      return balance

  def check_funds(amount):
    if(amount >= 0):
      if(amount > self.get_balance):
        return False
      else:
        return True
    else:
      if(-(amount) > self.get_balance):
        return False
      else: 
        return True

  def withdraw(amount, descr):
    if(check_funds(amount)): 
      ledger.append({"amount": amount, "description": descr})
      return True
    else:
      return False

  def transfer(amount, category):
    destination_category = Category(category)
    if(self.check_funds):
      self.withdraw(amount, "Transfer to " + category)
      destination_category.deposit(amount, "Transfer from " + category)
      return True
    else:
      return False 
      
def create_spend_chart(categories):