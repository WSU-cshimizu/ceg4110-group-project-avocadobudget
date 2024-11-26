from flask import *
import sqlite3
# import sys
# import ast
import os
from kaleido import *
from pathlib import Path
from dbOperations import *
from datetime import *
import plotly.graph_objects as plotGraph
import pandas as pd



graphPath = os.path.join(os.path.dirname(__file__), 'static', 'budgetBar.png')



'''
inputs: desc = description for expense string, cat = categroy for expense string, sDate = start date
eDate = end date, parameterArray = object for array to be built 
processing: If the variables are not empty, then we add to string and also add item to paramter array
outputs: return properly build string and array we passed will now have the proper paramters entered in the correct order.
'''
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

'''
inputs: desc = description for expense string, cat = categroy for expense string, sDate = start date
eDate = end date
processing: Set values for session variables
outputs: no return value, but session variables are now updated with new values
'''
def storeExpenseSession(desc, cat, sDate, eDate):
    session['desc'] = desc
    session['cat'] = cat
    session['sDate'] = sDate
    session['eDate'] = eDate


'''
inputs: no inputs
eDate = end date
processing: take the session variables and add them inside an array for later pulling
outputs: return array with session variables inside
'''
def getExpenseSessionArray():
    return [session.get('desc',""), session.get('cat',""), session.get('sDate', ""), session.get('eDate',"")]


## This section builds a flask object, and secret key for sessions.
app = Flask(__name__)
app.secret_key = 'Avocado_toast'

# This handles when insert expense is desired
# GET request causes insertExpense.html page to come up
# Post request pulls information from insertExpense.html page and inserts it to the DB
@app.route('/insertexpense', methods=['POST', 'GET'])
def home():
    print("inside home")
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

        #debug new PK
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
        # that will tell us that variables were incorrect in the expense object, however, ran out of time to implement
        db = dbOperations
        con = db.getConnection()

        # get session array to load expense page after insert is done
        arraySession = getExpenseSessionArray()

        print("Array session" + str(arraySession))

        # Get the current date
        #today = datetime.now().date()
        today = arraySession[3]

        # Get the first day of the current month
        # firstDay = today.replace(day=1)
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

        # this builds the records up for the matching filter to display after insertion
        listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

        print(listItems)

        # close connection object
        con.close()
        print("handled get table")

        #render template with listItems being the records to pass from result of select statement
        return render_template('expensetable.html', listItems = listItems)

    # if we have GET request after calling this we just want to display the insert page, which is the insert page        
    elif request.method == 'GET':
        print("handled get")
        return render_template('insertExpense.html')
    else:
        # handle method we were not expecting should not get here
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
        firstDay = today.replace(day=1)

        print("today: " + str(today) + "first day: " + str(firstDay))

        #want next month
        nextMonth = firstDay + timedelta(days = 32) 

        #first day next month
        lastDay = nextMonth.replace(day=1)

        desc = ""
        cat = ""

        # get array session
        arraySession = getExpenseSessionArray()

        boolNotEmpty = False

        for item in arraySession:
            if item:
                boolNotEmpty = True

        #check if array is filled with empty
        if boolNotEmpty == False:
            # if this triggers it means we had an empty session variable array, so want to pull current month by default
            storeExpenseSession(desc, cat, str(firstDay), str(lastDay) )

        #parameter array to store non empty variables for select statement
        parameterArray = []

        #string for dynamic return variable from session variables
        filterSQLString = buildExpenseString(desc, cat, str(firstDay), str(lastDay), parameterArray)
      
        # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
        # page
        print("String for query is: " + str(filterSQLString))

        # pass SQL string based on dynamic filters, also array that we filled above to hold the values to pass to parameter query
        listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

        print(listItems)
        #close conneciton
        con.close()
        print("handled get table")
        #have flaskk render the new html page with the items collected
        return render_template('index.html', listItems = listItems)

# This route handles when cancel is clicked in update or insert expense page
@app.route('/returnIndex', methods=['GET'])
def returnIndex():
    print("inside table")
   
    # create database operations object, use that to create connection to the database
    db = dbOperations
    con = db.getConnection()
    
    # get session variables
    arraySession = getExpenseSessionArray()

    #set to flase by default
    boolNotEmpty = False

    #loop and determine if array is empty if so set to true
    for item in arraySession:
        if item:
            boolNotEmpty = True
    
    print('Array sessions' + str(arraySession) )

    # Get the date from the arraySession if it exists
    endDate = arraySession[3]

    # Get the next day if it exists
    startDate = arraySession[2]

    print("today: " + str(startDate) + "first day: " + str(endDate))

    # same thing this will be none if session variables are still empty
    desc = arraySession[0]
    cat = arraySession[1]

    #parameters
    parameterArray = []

    # if bool not empty is false it means we need to define start date as first day of current month
    if boolNotEmpty == False:
        today = datetime.now().date()
        startDate = today.replace(day=1)
        
    #parameters
    parameterArray = []

    #string built for dynamic array
    filterSQLString = buildExpenseString(desc, cat, str(startDate), str(endDate), parameterArray)

    
    # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
    # page
    print("String for query is: " + str(filterSQLString))

    # build up string and pass items to display on expense table page
    listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

    print(listItems)
    #close conneciton
    con.close()
    print("handled get table")
    #have flaskk render the new html page with the items collected
    return render_template('index.html', listItems = listItems)


# handle display expense table based on filter options selected uses dynamic select statement to apply filter
@app.route('/applyExpense', methods=['GET'])
def filtertable():
    print("inside apply expense")
    
    # display expense table with current items in the expense table
    if request.method == 'GET':
        # create database operations object, use that to create connection to the database
        db = dbOperations
        con = db.getConnection()
        
        # get items from html elements that define items to filter on
        desc = request.args['search-description']
        cat = request.args['expcat']
        sDate = request.args['sDate']
        eDate = request.args['eDate']

        print("description: " + str(desc) + " category " + str(cat) + " start date " + str(sDate))
        
        # store variables as session objects based on what was collected
        storeExpenseSession(desc, cat, sDate, eDate)

        print("apply test session array: " + str(getExpenseSessionArray()))

        # get array session for later review 
        arraySession = getExpenseSessionArray()

        boolNotEmpty = False

        # let us know if no filter items were passed
        for item in arraySession:
            if item:
                boolNotEmpty = True

        #check if array is filled with empty
        if boolNotEmpty == False:
            # Get the current date for providing default filter of current month
            today = datetime.now().date()

            # Get the first day of the current month
            sDate = today.replace(day=1)

            #want next month
            nextMonth = sDate + timedelta(days = 32) 

            #first day next month
            eDate = nextMonth.replace(day=1)

            desc = ""
            cat = ""
            storeExpenseSession(desc, cat, str(sDate), str(eDate) )


        #parameters
        parameterArray = []

        # build expense string based on variables above
        filterSQLString = buildExpenseString(desc, cat, sDate, eDate, parameterArray)

      
        # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
        # page
        print("String for query is: " + str(filterSQLString))

        # pass result table to index.html template
        listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

        print(listItems)
        #close conneciton
        con.close()
        print("handled get table")
        #have flaskk render the new html page with the items collected
        return render_template('index.html', listItems = listItems)


# routing to this only accepts POST request when trying to update an expense or delete one
@app.route('/modifyexpense', methods=['POST'])
def expenseButton():
    if request.method == 'POST':
        # this is the button requested could be update or delete
        methodRequested = request.form['button']
        
        print("String button passed: " + str(methodRequested))
        
        #check for delete button if so delete based on ID tied to form that delete button was in
        # each table record on expense page is a form
        if (methodRequested == "DELETE"):
            # create db object and connection
            db = dbOperations
            con = db.getConnection()
            # get ID to delete
            deleteID = request.args['listItems']

            print("There are the arugments: " + str(deleteID))
            # call delete using the connection object and deleteID defined
            db.deleteIDExpense(con, str(deleteID))
            
            # build up sesion variables in array
            arraySession = getExpenseSessionArray()

            print("Array session" + str(arraySession))

            # Get the current date
            #today = datetime.now().date()
            today = arraySession[3]

            # Get the first day of the current month
            # firstDay = today.replace(day=1)
            firstDay = arraySession[2]

            print("today: " + str(today) + "first day: " + str(firstDay))

            desc = arraySession[0]
            cat = arraySession[1]

            #parameters
            parameterArray = []

            #string built for returning back to expense table with update based on what was deleted
            filterSQLString = buildExpenseString(desc, cat, str(firstDay), str(today), parameterArray)

        
            # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
            # page
            print("String for query is: " + str(filterSQLString))

            # this object is passed to template for building up table in html page when rendering
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

            # based on ID passed pass that id's properties to updateExpense.html page so it comes preloaded with current values
            return render_template('updateExpense.html', listItems = listItems)
        else:
            return render_template('index.html')

# this will load the page of the desired updateID passed in listItems array if get request
# or handle post request from this page to update object 
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
       
        #today = datetime.now().date()
        today = arraySession[3]

        # Get the first day of the current month
        #firstDay = today.replace(day=1)
        firstDay = arraySession[2]

        print("today: " + str(today) + "first day: " + str(firstDay))

        desc = arraySession[0]
        cat = arraySession[1]

        print("Update array session: " + str(arraySession))

        #parameters
        parameterArray = []

        #string
        filterSQLString = buildExpenseString(desc, cat, str(firstDay), str(today), parameterArray)

    
        # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
        # page
        print("String for query in update is: " + str(filterSQLString))

        listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

        # render expensetable.html with updated record and keeping old filter 
        return render_template('index.html', listItems = listItems)
    # otherwise if GET, just want to display current ID given ID passed to get request
    elif request.method == 'GET':
        # create DB and connection object
        db = dbOperations
        con = db.getConnection()
        #get ID to display
        updateID = request.args['listItems']
      
        print('get method')
        # get record for ID desired this will pull up page with html elements filled out
        listItems = db.selectIDExpense(con,updateID)
        print("List Items GET")
        print(listItems)
        # create template with the one id passed for display
        return render_template('updateExpense.html', listItems = listItems)
    

# this will load the mybudget page and handle based on get or post
@app.route('/mybudget', methods=['POST', 'GET'])
def budget():
    # handle post request, which is triggered by clicking update button in mybudget.html
    if request.method == 'POST':

        # create db object, connection, and get the selected category and amount
        db = dbOperations
        con = db.getConnection()       
        expense_amt = request.form.get('catamt')
        expense_cat = request.form.get('cat')
        catList = [expense_cat, expense_amt]
        cat = request.args['item']
        print("CHECK THIS" + str(catList))
        print("CHECK THIS too" + str(cat))
        print(request.args)

        print("got inside budget post")

        #amt = request.args
        listItems = db.selectSingleCategory(con, cat)
        
        print(listItems)
        
        # print("item: " + str(item))
        # print("listitems: " + str(item))
        return render_template('updateCategory.html', listItems = listItems)

    # otherwise if GET, just want to display current ID given ID passed to get request
    elif request.method == 'GET':
        # create DB and connection object
        db = dbOperations
        con = db.getConnection()


        listItems = db.getCategoryTable(con)
        amountArray = []
        for item in listItems:
            catAmount = item[1]
            print("Category Amount: " + str(catAmount))
            amountArray.append(float(catAmount))
            
        totalBudget = sum(amountArray)
        print("The total budget: " + str(totalBudget))


        percArray = []
        for item in amountArray:
            if item != None and item != 0 and item != "":
                percArray.append(round(float(item / totalBudget) * 100, 2))
            else:
                percArray.append(round(0, 2))


        
      
        print('get method mybudget')
        
        # get record for ID desired
        #listItems = db.selectIDExpense(con,updateID)

        listItems = db.getCategoryTable(con)

        #print("List Items GET")
        #print(listItems)
        # create template with the one id passed for display

        return render_template('myBudget.html', listItems = listItems, percArray = percArray)
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

        listItems = db.getCategoryTable(con)
        amountArray = []
        for item in listItems:
            catAmount = item[1]
            print("Category Amount: " + str(catAmount))
            amountArray.append(float(catAmount))
            
        totalBudget = sum(amountArray)
        print("The total budget: " + str(totalBudget))


        percArray = []
        for item in amountArray:
            percArray.append(round(float(item / totalBudget) * 100, 2))

        return render_template('myBudget.html', listItems = listItems , percArray = percArray)


# this will load the char.html page if a get or update and rerender if post
@app.route('/myreport', methods=['GET' ,'POST'])
def report():
    # handle post request, which is triggered by clicking update button in updateExpense.html
    if request.method == 'POST':
        
        # create db object and get connectional to SQL database
        db = dbOperations
        con = db.getConnection()

        # define year from form
        year = request.form.get('year')

        #get month from form
        month = request.form.get('month')
        
        #dictionary for building date string based on month
        monthDict = {'January': '-01-01', 'February': '-02-01', 'March': '-03-01', 'April': '-04-01',
                     'May': '-05-01', 'June': '-06-01', 'July': '-07-01', 'August': '-08-01', 'September': '-09-01',
                     'October': '-10-01', 'November': '-11-01', 'December': '-12-01'
                     }

        print("month: " + str(month))

        print("request object" + str(request))

        # get string for month based on match
        currentMonth = monthDict.get(month)

        # append year and month string for proper filter on date
        dateString = year + currentMonth

        print("Date string: " + str(dateString))

        # use date format 
        dateFormat = '%Y-%m-%d'

        # create date with string passed and format passed
        startDate = datetime.strptime(dateString, dateFormat)

        #build string for month and year to place in the title
        dateTitle = startDate.strftime("%B %Y")

        print("Date Text for graph: " + str(dateTitle))

        #want next month
        nextMonth = startDate + timedelta(days = 32) 

        # gives us first day next month
        lastDay = nextMonth.replace(day=1)

        #dont forget to convert date objects to string
        startDate = startDate.strftime(dateFormat)
        lastDay = lastDay.strftime(dateFormat)
        
        categoryArray = db.getCategoryTable(con)
        arrayChart = []
        amountChart = []

        #create array for categories, category budget amounts, and total budget
        totalBudget = 0
        for category in categoryArray:
            arrayChart.append(category[0])
            amountChart.append(category[1])
            totalBudget += float(category[1])
        
        #now want line to compare total spent too
        amountChart.append(totalBudget)

        print("category array: " + str(categoryArray))
        print("arrayChart array: " + str(arrayChart))
        print("amount array: " + str(amountChart) + "total budget: " + str(totalBudget))

        #now get result for sums
        sumResult = db.sumExpenseByCategory(con,arrayChart, startDate, lastDay)
        
        #categories and values
        categories = list(sumResult.keys())
        values = list(sumResult.values())

        #get total spend using values array
        expenseTotal = 0
        for value in values:
            if value != None:
                expenseTotal += float(value)
        
        #add total to figure
        values.append(expenseTotal)
        categories.append("Total")

        print("categories: " + str(categories))
        print("values: " + str(values))

        # build up graph using plotly 
        graph = plotGraph.Figure(data=[plotGraph.Bar(x=categories, y=values, name="Amount by Category")])
        
        graph.add_trace(plotGraph.Scatter(x=categories, y=amountChart, name='Budget by Category', mode='lines+markers'))

        graph.update_layout(
            title = 'Category Spent ' + str(dateTitle),
            xaxis_title = 'Expense Categories',
            yaxis_title = 'Amount Spent ($)'
        )

        graph.write_image(graphPath)

        # get char.html to display again with new graph as selected 
        return render_template('char.html', listItems = sumResult)
    # otherwise if GET, just want to display current month in graph form as this is our first time opening the page
    elif request.method == 'GET':
        # create DB and connection object
        db = dbOperations
        con = db.getConnection()
        #get ID to display
        #updateID = request.args['listItems']
      
        print('get method mybudget')
        
        #next couple of lines gets categories in category table
        # Then we append to an array all the categories, this is then sent 
        # to sumExpenseByCategory, where we get the sum of all categories
        # which then returns back as a dictionary
        categoryArray = db.getCategoryTable(con)
        arrayChart = []
        amountChart = []

        #create array for categories, category budget amounts, and total budget
        totalBudget = 0
        for category in categoryArray:
            arrayChart.append(category[0])
            amountChart.append(category[1])
            totalBudget += float(category[1])
        
        #now want line to compare total spent too
        amountChart.append(totalBudget)

        print("category array: " + str(categoryArray))
        print("arrayChart array: " + str(arrayChart))
        print("amount array: " + str(amountChart) + "total budget: " + str(totalBudget))

        # Get the current date
        today = datetime.now().date()

        # Get the first day of the current month
        firstDay = today.replace(day=1)

        #build string for month and year to place in the title
        dateTitle = firstDay.strftime("%B %Y")

        print("Date Text for graph: " + str(dateTitle))

        #want next month
        nextMonth = firstDay + timedelta(days = 32) 

        lastDay = nextMonth.replace(day=1)

        print("firstDay: " + str(firstDay) + "first day: " + str(lastDay))
        
        #now get result for sums
        sumResult = db.sumExpenseByCategory(con,arrayChart, firstDay, lastDay)
        
        #categories and values
        categories = list(sumResult.keys())
        values = list(sumResult.values())

        #get total spend using values array
        expenseTotal = 0
        for value in values:
            if value != None:
                expenseTotal += float(value)
        
        #add total to figure
        values.append(expenseTotal)
        categories.append("Total")

        print("categories: " + str(categories))
        print("values: " + str(values))

        graph = plotGraph.Figure(data=[plotGraph.Bar(x=categories, y=values, name="Amount by Category")])
        
        graph.add_trace(plotGraph.Scatter(x=categories, y=amountChart, name='Budget by Category', mode='lines+markers'))

        graph.update_layout(
            title = 'Category Spent ' + str(dateTitle),
            xaxis_title = 'Expense Categories',
            yaxis_title = 'Amount Spent ($)'
        )

        print("Graph Path: " + str(graphPath))

        graph.write_image(graphPath)

        print("wrote to graph")
        #return render_template('char.html', listItems = sumResult, firstDay = firstDay, lastDay = lastDay )
        return render_template('char.html')

# send currently filtered set of records to excel file for easier manipulation 
@app.route('/sendexcel', methods=['GET'])
def expenseExcel():
   
    # create database operations object, use that to create connection to the database
    db = dbOperations
    con = db.getConnection()
    
    # get session variables
    arraySession = getExpenseSessionArray()


    boolNotEmpty = False

    # check if empty to avoid none issues
    for item in arraySession:
        if item:
            boolNotEmpty = True
    
    
        

    print('Array sessions' + str(arraySession) )

    # Get the date from the arraySession if it exists
    endDate = arraySession[3]

    # Get the next day if it exists
    startDate = arraySession[2]

    print("today: " + str(startDate) + "first day: " + str(endDate))

    desc = arraySession[0]
    cat = arraySession[1]

    #parameters
    parameterArray = []

    # other wise want to define first date of current month to avoid null values
    if boolNotEmpty == False:
        today = datetime.now().date()
        startDate = today.replace(day=1)

    #string
    filterSQLString = buildExpenseString(desc, cat, str(startDate), str(endDate), parameterArray)

    # this provides an array or expense records that we will use to load the expense rccords to the expensetable.html
    # page
    print("String for query is: " + str(filterSQLString))

    listItems = db.selectParamsExpense(con, filterSQLString, parameterArray)

    #create pandas object
    expenseData = pd.DataFrame(listItems, columns=['id','desc', 'cat', 'amount', 'date', 'payment'])

    # writing to Excel
    excelObject = pd.ExcelWriter('expenses.xlsx')

    # write DataFrame to excel 
    expenseData.to_excel(excelObject)

    # close excel object
    excelObject.close()

    print(listItems)
    #close conneciton
    con.close()
    print("handled get table")
    #have flaskk render the new html page with the items collected
    return render_template('index.html', listItems = listItems)



###Calcuate percentage logic
@app.route('/calculateBudget', methods=['GET'])
def calculate():
    print("Hello")
    db = dbOperations
    con = db.getConnection()
    
    # test = request.form.get('income')
    if request.args['income'] != None and request.args['income']  != 0 and request.args['income'] != "":
        income = float(request.args['income'])
    else:
        income = 1000

    print("request args: " + str(request.args['income']))
    rentPercent = .25
    groceryPercent = .20
    entertainmentPercent = .15
    miscPercent = .15
    billsPercent = .15
    savingsPercent = .10
    #nuild percentsgre array and pass to myArry
    # 
    # print((rentPercent * float(income)))
    myArray = [rentPercent * float(income), groceryPercent * float(income), entertainmentPercent * float(income), miscPercent * float(income), billsPercent * float(income), savingsPercent * float(income)]
    listItems = db.getCategoryTable(con)
    i = 0
    for item in listItems:
        catUpdateArray = [myArray[i], item[0]]
        db.updateCategoryAmount(con, catUpdateArray)
        print("current category: " + str(catUpdateArray))
        i += 1
    
    listItems = db.getCategoryTable(con)

    percArray = []
    for item in myArray:
        if item != None and item != 0 and item != "":
            percArray.append(round(float(item / income) * 100, 2))
        else:
            percArray.append(round(0, 2))

    print(myArray)
    # print(income)

    return render_template('myBudget.html', listItems = listItems, percArray = percArray)

## if this file is run directly, then it is main and runs the flask app object to start listening on localhost 
# port 5003 for requests
if __name__ == '__main__':
   app.run(debug=True, port=5000)
   
 