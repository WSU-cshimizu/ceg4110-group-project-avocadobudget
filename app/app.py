from flask import *
import sqlite3
import sys
import ast
from pathlib import Path
from dbOperations import *
from datetime import *


def buildExpenseString(desc, cat, sDate, eDate, parameterArray):
    #default branch in case no filters have a match
    filterSQLString = "SELECT * FROM expense WHERE 1=1"

    # build string based on if variables exists or not
    # this allows a dynamic select query to be run as a filter
    # from the My expense page
    if desc != "":
        filterSQLString += " AND expense_Description = ?"
        parameterArray.append(desc)

    if cat != "":
        filterSQLString += " AND expense_Category = ?"
        parameterArray.append(cat)

    if sDate != "":
        filterSQLString += " AND expense_Date >= ?"
        parameterArray.append(sDate) 

    if eDate != "":
        filterSQLString += " AND expense_Date <= ?"
        parameterArray.append(eDate)

    return filterSQLString

def storeExpenseSession(desc, cat, sDate, eDate):
    session['desc'] = desc
    session['cat'] = cat
    session['sDate'] = sDate
    session['eDate'] = eDate

def getExpenseSessionArray():
    return [session.get('desc',""), session.get('cat',""), session.get('sDate', ""), session.get('eDate',"")]

app = Flask(__name__)
app.secret_key = 'Avocado_toast'

# This handle default launch page - 
# GET request causes insert expense page to come up
# Post request to / pulls information from insert expense html page and inserts it to the DB
@app.route('/insertexpense', methods=['POST', 'GET'])
def home():
    print("inside home")
    error = None
    
    # handle POST request on insert expense html page
    if request.method == 'POST':
        
        # create dbOperations object and create connection object to the SQlite db
        db = dbOperations
        con = db.getConnection()
        print("handled post")

        # pull data from different html input boxes for expense category, expense description, expense amount, 
        # expense date, expense payment method etc
        expense_cat = request.form.get('expcat')
        expense_desc = request.form.get('expdesc')
        expense_amount = request.form.get('expamt')
        expense_date = request.form.get('expdate')
        expense_payment_method = request.form.get('exppay')

        # take database object, call maxExpenseID - this gets max id in expense table then adds one to 
        # store new id we want to insert to
        pkID = db.maxExpenseID(con)

        #debug
        print(pkID)
        
        # now that we have the data desired, we pass items to Expense contructor
        insertExp = Expense(pkID, expense_cat, expense_desc, expense_amount, expense_date, expense_payment_method)

        # create empty fields var
        fields =""
        # use built in __str__ function for expense class to see what we got from the HTML form 
        print("Expense item" + str(insertExp))

        # test if expense object is valid object to insert to SQlite Expense table
        if(insertExp.validExpense() == True):
            
            # get array of tuple to insert single record to DB
            fields = insertExp.returnExpense()
            # pass connection object and fields above to insert to SQLite expense table
            db.insertExpense(fields,con)
            print(fields)
            # remember to close the connection
            con.close()
            print("expense desc: " + expense_desc + " expense amount: $" + str(expense_amount))
            # redirect to table() function in order to avoid resubmit post errors, redirect to GET to 
            # expense table allows us to see updated expense table on susseful insert
            return redirect(url_for('table', code = 200))

        # this handles the cause of error not valid - we are just loading the expense table again
        # new expense we wanted to insert will not work. At some point we want a message box to pop up
        # that will tell us that variables were incorrect in the expense object
        db = dbOperations
        con = db.getConnection()

        arraySession = getExpenseSessionArray()

        print("Array session" + str(arraySession))

        # Get the current date
        #today = datetime.now().date()
        today = arraySession[3]

        # Get the first day of the current month
        # first_day = today.replace(day=1)
        firstDay = arraySession[2]

        print("today: " + str(today) + "first day: " + str(firstDay))

        desc = arraySession[0]
        cat = arraySession[1]

        #parameters
        parameterArray = []

        #string
        filterSQLString = buildExpenseString(desc, cat, str(firstDay), str(today), parameterArray)

    
        # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
        # page
        print("String for query is: " + str(filterSQLString))

        listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

        print(listItems)

        con.close()
        print("handled get table")
        return render_template('expensetable.html', listItems = listItems)

    # if we have GET request after calling this we just want to display the insert page, which is the insert page        
    elif request.method == 'GET':
        
        print("handled get")
        return render_template('insertExpense.html')
    else:
        # handle method we were not expecting
        return "<p>Other Call</p>"

# handle display expense table, right now just show all items in table, should only handle get request
@app.route('/', methods=['GET'])
def table():
    print("inside table")
    error = None
    # display expense table with current items in the expense table
    if request.method == 'GET':
        # create database operations object, use that to create connection to the database
        db = dbOperations
        con = db.getConnection()
       
        # Get the current date
        today = datetime.now().date()

        # Get the first day of the current month
        first_day = today.replace(day=1)

        print("today: " + str(today) + "first day: " + str(first_day))

        desc = ""
        cat = ""

        #parameters
        parameterArray = []

        #string
        filterSQLString = buildExpenseString(desc, cat, str(first_day), str(today), parameterArray)

      
        # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
        # page
        print("String for query is: " + str(filterSQLString))

        listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

        print(listItems)
        #close conneciton
        con.close()
        print("handled get table")
        #have flaskk render the new html page with the items collected
        return render_template('index.html', listItems = listItems)

@app.route('/returnIndex', methods=['GET'])
def returnIndex():
    print("inside table")
    error = None
    # display expense table with current items in the expense table
   
    # create database operations object, use that to create connection to the database
    db = dbOperations
    con = db.getConnection()
    
    arraySession = getExpenseSessionArray()

    # Get the current date
    today = arraySession[3]

    # Get the first day of the current month
    first_day = arraySession[2]

    print("today: " + str(today) + "first day: " + str(first_day))

    desc = arraySession[0]
    cat = arraySession[1]

    #parameters
    parameterArray = []

    #string
    filterSQLString = buildExpenseString(desc, cat, str(first_day), str(today), parameterArray)

    
    # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
    # page
    print("String for query is: " + str(filterSQLString))

    listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

    print(listItems)
    #close conneciton
    con.close()
    print("handled get table")
    #have flaskk render the new html page with the items collected
    return render_template('index.html', listItems = listItems)


# handle display expense table, right now just show all items in table, should only handle get request
@app.route('/applyExpense', methods=['GET'])
def filtertable():
    print("inside apply expense")
    error = None
    # display expense table with current items in the expense table
    if request.method == 'GET':
        # create database operations object, use that to create connection to the database
        db = dbOperations
        con = db.getConnection()
        
        desc = request.args['search-description']
        cat = request.args['expcat']
        sDate = request.args['sDate']
        eDate = request.args['eDate']

        print("description: " + str(desc) + " category " + str(cat) + " start date " + str(sDate))
        
        storeExpenseSession(desc, cat, sDate, eDate)

        print("apply test session array: " + str(getExpenseSessionArray()))


        #parameters
        parameterArray = []

        filterSQLString = buildExpenseString(desc, cat, sDate, eDate, parameterArray)

      
        # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
        # page
        print("String for query is: " + str(filterSQLString))

        listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

        print(listItems)
        #close conneciton
        con.close()
        print("handled get table")
        #have flaskk render the new html page with the items collected
        return render_template('index.html', listItems = listItems)


# routing to this only accepts POST request
@app.route('/modifyexpense', methods=['POST'])
def expenseButton():
    
    if request.method == 'POST':
        # this is the button requested could be update or delete
        methodRequested = request.form['button']
        print("String button passed: " + str(methodRequested))
        
        #check for delete button if so delete based on ID tied to form that delete button was in
        if (methodRequested == "DELETE"):
            # create db object and connection
            db = dbOperations
            con = db.getConnection()
            # get ID to delete
            deleteID = request.args['listItems']

            print("There are the arugments: " + str(deleteID))
            # call delete using the connection object and deleteID defined
            db.deleteIDExpense(con, str(deleteID))
            
            arraySession = getExpenseSessionArray()

            print("Array session" + str(arraySession))

            # Get the current date
            #today = datetime.now().date()
            today = arraySession[3]

            # Get the first day of the current month
            # first_day = today.replace(day=1)
            firstDay = arraySession[2]

            print("today: " + str(today) + "first day: " + str(firstDay))

            desc = arraySession[0]
            cat = arraySession[1]

            #parameters
            parameterArray = []

            #string
            filterSQLString = buildExpenseString(desc, cat, str(firstDay), str(today), parameterArray)

        
            # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
            # page
            print("String for query is: " + str(filterSQLString))

            listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

            print(listItems)
            # close connection
            con.close()
            # render template based on new set of records
            return render_template('index.html', listItems = listItems)
        # handle case for update
        elif (methodRequested == "UPDATE"):
            print("UPDATE button clicked")
            # this is the item we want to update
            updateItem = request.args['listItems']
            print(updateItem)
            # create connection to desired database
            db = dbOperations
            con = db.getConnection()

            # this gets the array for the current expense in the expense object
            listItems = db.selectIDExpense(con,updateItem)
            print("List Items")
            print(listItems)

            
            

            
            #return redirect(url_for('update', listItems = listItems)) this will prefill the updateExpense.html page
            return render_template('updateExpense.html', listItems = listItems)
        else:
            return render_template('index.html')

# this will load the page of the desired updateID passed in listItems array
# or handle post request from this page
@app.route('/updateExpense', methods=['POST', 'GET'])
def update():
    # handle post request, which is triggered by clicking update button in updateExpense.html
    if request.method == 'POST':
        print("update button clicked")
        
        # get values for items we want to update
        expense_id = request.form.get('expid')
        expense_cat = request.form.get('expcat')
        expense_desc = request.form.get('expdesc')
        expense_amount = request.form.get('expamt')
        expense_date = request.form.get('expdate')
        expense_payment_method = request.form.get('exppay')

        # create db object and connection to the database 
        db = dbOperations
        con = db.getConnection()

        print("expense_id: " + str(expense_id))
        
        #expense object created based on variables collected from HTML page
        expenseObj = Expense(expense_id,expense_cat,expense_desc, expense_amount, expense_date, expense_payment_method)

        # need array to pass to update expense (these are the items to insert)
        expenseArray = expenseObj.returnExpense()

        print("Expense Array: " + str(expenseArray))

        #call update expense using array above
        db.updateIDExpense(con, expenseObj)

        #call up session variables
        arraySession = getExpenseSessionArray()
        # Get the current date
        #today = datetime.now().date()
        today = arraySession[3]

        # Get the first day of the current month
        #first_day = today.replace(day=1)
        first_day = arraySession[2]
       

        print("today: " + str(today) + "first day: " + str(first_day))

        desc = arraySession[0]
        cat = arraySession[1]

        print("Update array session: " + str(arraySession))

        #parameters
        parameterArray = []

        #string
        filterSQLString = buildExpenseString(desc, cat, str(first_day), str(today), parameterArray)

    
        # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
        # page
        print("String for query in update is: " + str(filterSQLString))

        listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

        # render expensetable.html

        return render_template('index.html', listItems = listItems)
    # otherwise if GET, just want to display current ID given ID passed to get request
    elif request.method == 'GET':
        # create DB and connection object
        db = dbOperations
        con = db.getConnection()
        #get ID to display
        updateID = request.args['listItems']
      
        print('get method')
        # get record for ID desired
        listItems = db.selectIDExpense(con,updateID)
        print("List Items GET")
        print(listItems)
        # create template with the one id passed for display
        return render_template('updateExpense.html', listItems = listItems)
    


# this will load the mybudget page and handle based on get or post
@app.route('/mybudget', methods=['POST', 'GET'])
def budget():
    # handle post request, which is triggered by clicking update button in updateExpense.html
    if request.method == 'POST':

        db = dbOperations
        con = db.getConnection()       
        expense_amt = request.form.get('catamt')
        expense_cat = request.form.get('cat')
        catList = [expense_cat, expense_amt]
        cat = request.args['item']
        print(catList)
        print("got inside budget post")

        #amt = request.args
        listItems = db.selectSingleCategory(con, cat)
        print(listItems)
        # print("item: " + str(item))
        # print("listitems: " + str(item))
        return render_template('updateCategory.html', listItems = listItems)

        # print("Inside post update category")
        # db = dbOperations
        # con = db.getConnection()
        # #catToChange = request.form.get('cat')
        # print(str(request.forms))
        # #print(str(catToChange))
        # listItems = ["testinggggg"]
        # methodRequested = request.form['button']
        # return render_template('myBudget.html', listItems = listItems)

    # otherwise if GET, just want to display current ID given ID passed to get request
    elif request.method == 'GET':
        # create DB and connection object
        db = dbOperations
        con = db.getConnection()

        #get ID to display
        #updateID = request.args['listItems']
      
        print('get method mybudget')
        
        # get record for ID desired
        #listItems = db.selectIDExpense(con,updateID)

        listItems = db.getCategoryTable(con)

        #print("List Items GET")
        #print(listItems)
        # create template with the one id passed for display
        return render_template('myBudget.html', listItems = listItems)
    else:
        return render_template('mybudget.html')

    
@app.route('/updateCategory', methods=['POST'])
def updateCategory():
    if request.method == 'POST':
        db = dbOperations
        con = db.getConnection() 
        expense_amt = request.form.get('catamt')
        expense_cat = request.form.get('cat')
        catList = [str(expense_amt), str(expense_cat)]
        listItems = db.updateCategoryAmount(con, catList)
        return render_template('myBudget.html', listItems = listItems)


# this will load the my reports page and handle based on get or post
@app.route('/myreport', methods=['GET' ,'POST'])
def report():
    # handle post request, which is triggered by clicking update button in updateExpense.html
    if request.method == 'POST':
        listItems = ["test"]
        return render_template('char.html', listItems = listItems)
    # otherwise if GET, just want to display current ID given ID passed to get request
    elif request.method == 'GET':
        # create DB and connection object
        db = dbOperations
        con = db.getConnection()
        #get ID to display
        #updateID = request.args['listItems']
      
        print('get method mybudget')
        
        # get record for ID desired
        #listItems = db.selectIDExpense(con,updateID)
        listItems = ["test"]
        #print("List Items GET")
        #print(listItems)
        # create template with the one id passed for display
        return render_template('char.html', listItems = listItems)


## if this file is run directly, then it is main and runs the flask app object to start listening on localhost 
# port 5000 for requests
if __name__ == '__main__':
   app.run(debug=True, port=5000)
   
 