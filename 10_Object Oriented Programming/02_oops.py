# Exerices

class product:
  def inputdata(self):
        self.pname = input("Enter the product name::")
        self.price = int(input("Enter the price ::"))
        self.qty = int(input("Enter the amount of product ::"))
  def calculation(self):
    self.dis = (self.price*self.qty)*10/100
    self.bill = (self.price*self.qty)-self.dis
    print("Discount=",self.dis)
    print("Bill amount=",self.bill)

prod1 = product()
prod2 = product()
prod1.inputdata()
prod1.calculation()
prod2.inputdata()
prod2.calculation()