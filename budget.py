class Category:
  
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0.00

  def __str__(self):
    output = ""
    adjustment = int(((30 - len(self.name))/2) + len(self.name))
    output +=  self.name.ljust(adjustment,'*').rjust(30,'*') + '\n'

    for transaction in self.ledger:
      output += transaction["description"][:23].ljust(23,' ') + "{:.2f}".format(transaction["amount"]).rjust(7,' ')  + '\n'

    output += 'Total: ' + str(self.balance)
    
    return output

  def deposit(self, amount, descr=""):
    self.ledger.append({"amount": amount,"description": descr})
    self.balance += amount

  def get_balance(self):
    return self.balance

  def check_funds(self, amount):
    if(amount > self.get_balance()):
      return False
    else:
      return True

  def withdraw(self, amount, descr=""):
    if(self.check_funds(amount)): 
      self.ledger.append({"amount": -amount, "description": descr})
      self.balance -= amount
      return True
    else:
      return False

  def transfer(self, amount, category):
    if(self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  
  
def create_spend_chart(categories):
  return 'poop'