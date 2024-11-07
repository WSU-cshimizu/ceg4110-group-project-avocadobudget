'''
DB Method:
inputs:
processing:
outputs:
'''

import sqlite3
from datetime import *
#import expense

def printTest():
    print("this is a test")

### DB wide methods ###
''' 
DB Method: getConnection
inputs: None
outputs: Provides object that provides connection to project database
'''
def getConnection():
    # take in string, create connection, return connection object
    con = sqlite3.connect("AvocadoToast_Database_CEG4110.db")
    return con


### EXPENSE TABLE METHODS ###
'''
DB Method: insertExpense
inputs: tuple with expense items, connection object
processing: Take in connection, create SQlite3 cursor object, then use prepared statement to pass insertTuple
to the execute many method. This will take those valus and insert into the database. Then commit it. We will provide
validation checks in back end before passing tuple, so no need to error handle
outputs: No return 
'''
def insertExpense(insertTuple, con):
    # take in array tuple and insert based on parameters
    cur = con.cursor()
    cur.executemany('INSERT INTO Expense VALUES (?,?,?,?,?,?)', insertTuple)
    con.commit()

'''
DB Method: maxExpenseID
inputs: connection object to SQlite database
processing: take con object, make cursor, then execute string to get max ID in expense table.
If one exists add one to maxID, if none exists then default with 1 as the value.
outputs: return the maxID derived to use for insert in Expense table
'''    
def maxExpenseID(con):
    # get max id from table add one return the value, otherwise if no records return 1
    cur = con.cursor()
    selectString = "SELECT Max(Expense_ID) FROM Expense"
    result = cur.execute(selectString).fetchone()
    
    maxID = None
    
    if result[0] != None:
        maxID = int(result[0]) + 1
    else:
        maxID = 1

    return maxID

'''
DB Method: getExpenseTable
inputs: connection object to database
processing: Take in connection object, create cursor, read all record from Expense.
Provide this to execute method and fetchall() to get all records in result variable then return
to calling object
outputs: result variable with all the records collected from the expense table
'''
def getExpenseTable(con):
    
    # get all records in expense table
    cur = con.cursor()
    # select all records from expense table
    selectString = "SELECT * FROM Expense"
    # return array or arrays for result of string above
    result = cur.execute(selectString).fetchall()
    
    return result
'''
DB Method: deleteIDExpense
inputs: connection object to database and ID to delete from the expense table
processing: Take in connection object create a curspr and take the id and delete it from the eepsne table. 
Will check that Id exists before calling this function so no need to provide testing if id exists. 
outputs: nothing, but provided ID will be delete from the expense table now
'''    
def deleteIDExpense(con, ID):
    cur = con.cursor()

    # create parameterized string
    deleteString = "DELETE FROM Expense WHERE Expense_ID = " + str(ID)
    print("delete ID pressed: " + ID)
    print("DElete String: " + deleteString)
    #pass string and ID to delete send delete command to database
    cur.execute(deleteString)
    # commit the change    
    con.commit()  
'''
DB Method: updateIDExpense
inputs: take in connection object and expense object you want to update
processing: create cursor object from connection passed, use that to first
insert object based on array passed to function. Want to change ID to current maxID + 1 in table
then we want after successful instertion to delete the record at desired update record, then update
current record at top of table to have PK value of the record we just deleted
outputs: No output to return, just updated values in table.
'''         
def updateIDExpense(con, expenseObject):
    cur = con.cursor()
    print("Got inside updateIDExpense!!")

    #store desired update id
    updateID = expenseObject.getID()

    print("Update ID: " + str(updateID))
    
    #get new id to insert to
    newID = maxExpenseID(con)

    #set id of object to new id - we are going to insert copy of object to top of table
    expenseObject.setID(newID)

    # get array tuple of expense object
    updateArray = expenseObject.returnExpense()

    print("Update array:" + str(updateArray))

    print("newID: " + str(newID))
    print("updateID: " + str(updateID))

    #set bool to false as signal if insert was successful
    insertSucess = False

    # create tuple with old ID to replace and newID to create temporarily
    updateIDs = (updateID,newID)
        
    #now attempt insert with new array - newID
    try:
        insertExpense(updateArray, con)
        insertSucess = True
    except:
        print("error inserting record no need to delete or update!!")
    # if valid insert, now we want to delete current record at ID of target update
    if insertSucess == True:
        # delete record current update ID
        deleteIDExpense(con,updateID)
        # string to update table on ID onlys
        updateString = "UPDATE Expense SET Expense_ID = (?) WHERE Expense_ID = ?"
        # change record we inserted at top of table and set ID to the ID of the record we wanted to update
        cur.execute(updateString, updateIDs)
        print("Sucessful Update")
        con.commit()
'''
DB Method: selectIDExpense
inputs: pass connection object and id of expense record we want from DB
processing: take in ID passed to function, search expense table for that ID
outputs: return records that match the query, in this case should only be one record
since we are searching on PK
'''         
def selectIDExpense(con, ID):
    cur = con.cursor()
    # Get record from expense table that matches the ID passed to this function
    selectString = "SELECT * FROM Expense WHERE Expense_ID = ?"
    result = cur.execute(selectString, [ID]).fetchone()
    
    print ("Result: " + str(result))
    
    return result

'''
DB Method: selectParamExpense
inputs: pass connection object parameters for select statement
processing: take in more than one parameter and pass to prep query
outputs: return records that match the query
'''         
def selectParamsExpense(con, parameterQueryString, parameterArray):
    cur = con.cursor()
    
    #pass string, array and execute
    result = cur.execute(parameterQueryString, parameterArray).fetchall()
    
    print ("Result: " + str(result))
    
    return result
'''
DB Method: 
inputs: 
outputs: 
''' 
def sumExpenseByCategory(con,categoryArray, startDate, endDate):
    cur = con.cursor()

    sumDict = {}

    # loop through each item add sum() for each 
    for item in categoryArray:
        if item != None:
            stringUpdate = "SELECT sum(expense_Amount) FROM Expense Where expense_Category = '" + str(item) + "'" " AND expense_Date >= '" + str(startDate) \
            + "' AND expense_Date < '" + str(endDate) + "'" 
            print("String select: " + stringUpdate)
            result = cur.execute(stringUpdate).fetchone()
            print("result: " + str (result[0]))
            sumDict[item] = result[0]
    
    
    print("Result: " + str(sumDict))
    return sumDict

######### CATEGORY CRUD ##########
def getCategoryTable(con):
    cur = con.cursor()
    selectString = "SELECT * FROM Category"
    
    result = cur.execute(selectString).fetchall()

    return result

'''
DB Method: selectSingleCategory
inputs: pass connection object and text for category
processing: take in category and return record with matching value
outputs: return record that matches
'''         
def selectSingleCategory(con, cat):
    cur = con.cursor()
    # Get record from expense table that matches the ID passed to this function
    selectString = "SELECT * FROM Category WHERE category_ID = ?"
    result = cur.execute(selectString, [cat]).fetchone()
    
    print ("Result: " + str(result))
    
    return result

def updateCategoryAmount(con, catList):
    cur = con.cursor()
    print("Cat list Update: " + str(catList))
    insertCatAmount = "UPDATE Category SET category_Budget = ? WHERE category_ID = ?"
    result = cur.execute(insertCatAmount, catList)
    con.commit()
    selectString = "SELECT * FROM Category"
    result = cur.execute(selectString).fetchall()

    return result
    
    
