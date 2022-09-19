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
  output = "Percentage spent by category\n"
  
  width = (len(categories)*3)+1
  
  total = 0
  category_totals = {}
  category_name_length = []
  
  
  for i in range(0,len(categories)):
    category_total = 0 
    for transaction in categories[i].ledger:
      if str(transaction["amount"]).find("-") != -1:
        category_total += -transaction["amount"]
    category_totals[i] = round(category_total,2)
    category_name_length.append(len(categories[i].name))
    total += round(category_total,2) 

  print(total)
  print(category_totals)

  for i in range(100,-10,-10):
    output += (str(i) + "| ").rjust(5)
    for j in range(0,len(categories)):
      if int(round((category_totals[j]/total)*100,-1)) >= i:
        if j == 0:
          output += "o".rjust(j)
        else:  
          output += "o".rjust(3)
      else:
        if j == 0:
          output += " ".rjust(j)
        else:  
          output += " ".rjust(3)
    output += "  \n"

  line = "-"*width
  output += line.rjust(width+4)+"\n"

  category_name_length.sort(reverse = True)
  max_length = category_name_length[0]
  
  for i in range(0,max_length):
    for j in range(0,len(categories)):
      if i > len(categories[j].name)-1:
        if j == 0:
          output += " ".rjust(6)
        else:
          output += " ".rjust(3)
      else:
        if j == 0:
          output += categories[j].name[i].rjust(6)
        else:
          output += categories[j].name[i].rjust(3)
    if i == max_length-1:
      output += "  "
    else:
      output += "  \n"
      
  return output