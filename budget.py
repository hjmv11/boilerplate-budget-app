class Category:

  #set class object properties when created 
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0.00

  #set result when class object printed
  def __str__(self):
    output = ""
    adjustment = int(((30 - len(self.name))/2) + len(self.name))
    output +=  self.name.ljust(adjustment,'*').rjust(30,'*') + '\n'

    for transaction in self.ledger:
      output += transaction["description"][:23].ljust(23,' ') + "{:.2f}".format(transaction["amount"]).rjust(7,' ')  + '\n'

    output += 'Total: ' + str(self.balance)
    
    return output

  #amount provided added to balance
  def deposit(self, amount, descr=""):
    self.ledger.append({"amount": amount,"description": descr})
    self.balance += amount

  #balance
  def get_balance(self):
    return self.balance

  #check if amount provide is greater than balance
  def check_funds(self, amount):
    if(amount > self.get_balance()):
      return False
    else:
      return True

  #balance subtracted by negative amount provided 
  def withdraw(self, amount, descr=""):
    if(self.check_funds(amount)): 
      self.ledger.append({"amount": -amount, "description": descr})
      self.balance -= amount
      return True
    else:
      return False

  #withdraw amount provided and deposit to category provided, if funds sufficient funds available
  def transfer(self, amount, category):
    if(self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  

def create_spend_chart(categories):
  #create output string
  output = "Percentage spent by category\n"

  #width after the pipe 
  width = (len(categories)*3)+1

  #spending total, total spent by category, category name length variables 
  total = 0
  category_totals = {}
  category_name_length = []
  
  #loop through categories provided to populated variables 
  for i in range(0,len(categories)):
    category_total = 0 
    for transaction in categories[i].ledger:
      if str(transaction["amount"]).find("-") != -1:
        category_total += -transaction["amount"]
    category_totals[i] = round(category_total,2)
    category_name_length.append(len(categories[i].name))
    total += round(category_total,2) 

  #loop through numbers and percentage spent by category
  for i in range(100,-10,-10):
    #adds number, pipe and space
    output += (str(i) + "| ").rjust(5)
    for j in range(0,len(categories)):
      #if percentage times 100 is greather or equal to the current number add 'o' for the current category, if not add blanks 
      if int(round((category_totals[j]/total)*100,-1)) >= i:
        #if the first category no spaces, if not 2 spaces behind the o 
        if j == 0:
          output += "o".rjust(j)
        else:  
          output += "o".rjust(3)
      else:
        if j == 0:
          output += " ".rjust(j)
        else:  
          output += " ".rjust(3)
    #add two spaces and end of line character
    output += "  \n"

  #add dashed line
  line = "-"*width
  output += line.rjust(width+4)+"\n"

  #get the longest category name's length 
  category_name_length.sort(reverse = True)
  max_length = category_name_length[0]

  #loop through each letter for each category name provided
  for i in range(0,max_length):
    for j in range(0,len(categories)):
      #if the current category name is smaller than the longest category name add blanks, if not add the character 
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
    #if the last character of the longest category name exclude end of line character, ifnot include 
    if i == max_length-1:
      output += "  "
    else:
      output += "  \n"
      
  return output