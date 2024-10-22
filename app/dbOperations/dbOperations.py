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
    cur = con.cursor()
    
    selectString = "SELECT * FROM Expense"
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

    
    deleteString = "DELETE FROM Expense WHERE Expense_ID = (?)"

    cur.executemany(deleteString, (ID,) )
        
    con.commit()  
'''
DB Method: updateIDExpense
inputs: take in connection object and ID of expense you want to update
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

    #set id
    expenseObject.setID(newID)

    updateArray = expenseObject.returnExpense()

    print("Update array:" + str(updateArray))

    print("newID: " + str(newID))
    print("updateID: " + str(updateID))

    #set bool to false as signal if insert was successful
    insertSucess = False

    updateIDs = (updateID,newID)
        
    #now attempt insert with new array
    try:
        insertExpense(updateArray, con)
        insertSucess = True
    except:
        print("error inserting record no need to delete or update!!")

    if insertSucess == True:
        deleteIDExpense(con,updateID)
        # string to update table on ID onlys
        updateString = "UPDATE Expense SET Expense_ID = (?) WHERE Expense_ID = ?"
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

    selectString = "SELECT * FROM Expense WHERE Expense_ID = ?"
    result = cur.execute(selectString, [ID]).fetchone()
    
    print ("Result: " + str(result))
    
    return result
    
######### CATEGORY EXPENSE ##########

    
    
