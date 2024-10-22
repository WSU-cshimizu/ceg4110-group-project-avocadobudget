from datetime import *

class Expense:
    # CONSTRUCTOR - checks if expense is valid
    def __init__(self,id, cat, desc, amt, date, payment):
        print("Check for expense init")
        #bool keep track of valid instance
        self.valid = True
        #check id for digit
        if(isinstance(int(id), int)):
           self.id = id
        else:
            self.valid = False
            self.id = -1
        
        #check cat is string 
        if(type(cat) == str):
            self.category = cat
        else:
            self.valid = False
            self.category = ""
        
        #check desc is string
        if(type(desc) == str):
            self.description = desc
        else:
            self.valid = False
            self.description = ""
        
        #check amt is float

        amt = float(amt)
        if(isinstance(amt, float) and float(amt) > 0):
            # if float round to decimal spots so goes in DB as calid currency
            self.amount = round(amt,2)
        else:
            self.valid = False
            self.amount = -1.0
        
        #check if date is valid
        dateFormat = '%Y-%m-%d'

        dateObj = datetime.strptime(date,dateFormat)

        if(isinstance(dateObj, datetime)):
            self.date = date
        else:
            self.valid = False
            self.date = ""

        
        #check if payment is string
        #check desc is string
        if(type(payment) == str):
            self.payment = payment
        else:
            self.valid = False
            self.payment = ""
    def __str__(self):
        return f"Variables, {self.id}, {self.category}, {self.description}, {self.amount}, {self.date}, {self.payment} "
    
    def validExpense(self):
        print("Valid expense check: " + str(self.validExpense))
        return self.valid
    
    def returnExpense(self):
        return [
                (self.id,self.category, self.description, self.amount, self.date, self.payment)
            ]

    def setID(self, newID):
        self.id = newID

    def getID(self):
        return self.id
        
        