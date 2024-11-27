from datetime import *

# Expense class
class Expense:
    # CONSTRUCTOR - checks if expense is valid - starts true, and if any object is invalid change state to false
    def __init__(self,id, cat, desc, amt, date, payment):
        print("Check for expense init")
        #bool keep track of valid instance set default state to true, might need to change later
        self.valid = True
        #check id for int if so set id to that value
        if(isinstance(int(id), int)):
           self.id = id
        else:
            # otherwise have invalid expense object set it to invalid by coding as False 
            # and set ID to empty
            self.valid = False
            self.id = ""
        
        #check cat is string if so safe to store in category
        if(type(cat) == str):
            self.category = cat
        else:
            # if not a string we want to code expense object as invalid and set category to ""
            self.valid = False
            self.category = ""
        
        # same concept as above
        if(type(desc) == str):
            self.description = desc
        else:
            self.valid = False
            self.description = ""
        
        #check amt is float
        amt = float(amt)
        # confirm that we have float instance and amount > 0
        if(isinstance(amt, float) and amt > 0):
            # if float round to decimal spots so goes in DB as calid currency
            self.amount = round(amt,2)
        else:
            #otherwise invalid expense object change state to false and make amount "" to let us know
            self.valid = False
            self.amount = ""
        
        #check if date is valid according to this format
        dateFormat = '%Y-%m-%d'
        # create date object from string date passed based on format in dateFormat
        dateObj = datetime.strptime(date,dateFormat)
        # check if dateObj is valid datetime object, if so, the string used to create
        # this date is safe to store in the sqlite3 database
        if(isinstance(dateObj, datetime)):
            self.date = date
        else:
            # otherwise invalid date passed, keep date null so we know and code expense object as invalid
            self.valid = False
            self.date = ""

        #check if payment is string
        # if so define payment based on string, otherwise invalid data type set object to invalid
        # do not enter value in payment
        if(type(payment) == str):
            self.payment = payment
        else:
            # otherwise expense object is invalid so change state to false and leave payment as empty so we know
            self.valid = False
            self.payment = ""
    
    # default string return for printing object
    def __str__(self):
        return f"Variables, {self.id}, {self.category}, {self.description}, {self.amount}, {self.date}, {self.payment} "
    
    # return state of expense true for valid or false for invalid
    def validExpense(self):
        print("Valid expense check: " + str(self.validExpense))
        return self.valid
    
    # return array of single tuple for expense object, this format is built for queries used by SQlite3
    def returnExpense(self):
        return [
                (self.id,self.category, self.description, self.amount, self.date, self.payment)
            ]
    
    # change ID of object if needed
    def setID(self, newID):
        self.id = newID
    
    # get ID of object if needed
    def getID(self):
        return str(self.id)
    
    # this function will look at each variable and built a string to let us know the variables that were invalid
    def dislayInvalidVariables(self):
        # default error string to empty
        
        errorString = ""

        # start building string of error variables by checking the current state of each one
        if self.valid == False:
            #check each item for errors if empty there was an error and we want to add to error string
            if self.id == "":
                # we add to errorString that variable was invalid
                errorString += "ID value passed was invalid \n"
            
            #same process for expense category
            if self.category == "":
                # we add to errorString that variable was invalid
                errorString += "Category value passed was invalid \n"

            #same process for expense description
            if self.description == "":
                # we add to errorString that variable was invalid
                errorString += "Desciption value passed was invalid \n"

            #same process for expense amount
            if self.amount == "":
                # we add to errorString that variable was invalid
                errorString += "Amount value passed was invalid \n"

            #same process for expense date
            if self.date == "":
                # we add to errorString that variable was invalid
                errorString += "Date value passed was invalid \n"

            #same process for expense payment method
            if self.payment == "":
                # we add to errorString that variable was invalid
                errorString += "Payment method value passed was invalid \n"

        return errorString
        
        