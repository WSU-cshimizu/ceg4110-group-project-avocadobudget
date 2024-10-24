from flask import *
import sqlite3
import sys
import ast
from pathlib import Path
from dbOperations import *


printTest()

print(sys.path)

app = Flask(__name__)

# Handle insert page if post get items from form and save insert to DB
# Otherwise just display insert page 
@app.route('/', methods=['POST', 'GET'])
def home():
    print("inside home")
    error = None
    if request.method == 'POST':
        db = dbOperations
        con = db.getConnection()
        print("handled post")
        expense_cat = request.form.get('expcat')
        expense_desc = request.form.get('expdesc')
        expense_amount = request.form.get('expamt')
        expense_date = request.form.get('expdate')
        expense_payment_method = request.form.get('exppay')

        pkID = db.maxExpenseID(con)

        print(pkID)
        print(expense_date)
        insertExp = Expense(pkID, expense_cat, expense_desc, expense_amount, expense_date, expense_payment_method)

        fields =""
        print("Expense item" + str(insertExp))

        # insertTuple = insertExp.returnExpense()

        # print(insertTuple)
        # print("Truth Check: " + str(insertExp.validExpense()))
        if(insertExp.validExpense() == True):
            fields = insertExp.returnExpense()
            db.insertExpense(fields,con)
            print(fields)
            con.close()
            print("expense desc: " + expense_desc + " expense amount: $" + str(expense_amount))
            return redirect(url_for('table', code = 302))

        '''
        fields = [
                (pkID,expense_cat, expense_desc, expense_amount, expense_date, expense_payment_method)
            ]
        '''

        db = dbOperations
        con = db.getConnection()
       
        listItems = db.getExpenseTable(con)

        print(listItems)

        con.close()
        print("handled get table")
        return render_template('expensetable.html', listItems = listItems)
        
    elif request.method == 'GET':
        
        print("handled get")
        return render_template('index.html')
    else:
        return "<p>Other Call</p>"


@app.route('/success', methods=['POST', 'GET'])
def success():
    print("inside home")
    error = None
    if request.method == 'POST':
        print("pass in post")
        return render_template('success.html')
    elif request.method == 'GET':
        
        #return render_template('success.html')
        print("Got to success get")
        fields = request.args['fields']
        listItems = list(ast.literal_eval(fields))
        print(listItems)
        return render_template('success.html', listItems = listItems)
    print("neither")
    return render_template('success.html')

# handle display expense table, right now just show all items in table
@app.route('/expensetable', methods=['GET'])
def table():
    print("inside table")
    error = None
    if request.method == 'GET':
        db = dbOperations
        con = db.getConnection()
       
        listItems = db.getExpenseTable(con)

        print(listItems)

        con.close()
        print("handled get table")
        return render_template('expensetable.html', listItems = listItems)

@app.route('/modifyexpense', methods=['POST'])
def expenseButton():
    if request.method == 'POST':
        methodRequested = request.form['button']
        print("String button passed: " + str(methodRequested))
        #check for delete button 
        if (methodRequested == "DELETE"):
            db = dbOperations
            con = db.getConnection()
        
            deleteID = request.args['listItems']

            print("There are the arugments: " + str(deleteID))

            db.deleteIDExpense(con, deleteID)

            listItems = db.getExpenseTable(con)

            print(listItems)

            con.close()
            return render_template('expensetable.html', listItems = listItems)
        elif (methodRequested == "UPDATE"):
            print("UPDATE button clicked")
           
            updateItem = request.args['listItems']
            print(updateItem)
            db = dbOperations
            con = db.getConnection()


            
            listItems = db.selectIDExpense(con,updateItem)
            print("List Items")
            print(listItems)
            
            #return redirect(url_for('update', listItems = listItems))
            return render_template('updateExpense.html', listItems = listItems)
        else:
            return render_template('index.html')
@app.route('/updateExpense', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        print("update button clicked")

        expense_id = request.form.get('expid')
        expense_cat = request.form.get('expcat')
        expense_desc = request.form.get('expdesc')
        expense_amount = request.form.get('expamt')
        expense_date = request.form.get('expdate')
        expense_payment_method = request.form.get('exppay')

        db = dbOperations
        con = db.getConnection()

        print("expense_id: " + str(expense_id))
        
        #expense
        expenseObj = Expense(expense_id,expense_cat,expense_desc, expense_amount, expense_date, expense_payment_method)

        # need array to pass to update expense (this are the items to insert)
        expenseArray = expenseObj.returnExpense()

        print("Expense Array: " + str(expenseArray))

        #call update expense using array above
        db.updateIDExpense(con, expenseObj)

        listItems = db.getExpenseTable(con)

        return render_template('expensetable.html', listItems = listItems)
    elif request.method == 'GET':
        
        db = dbOperations
        con = db.getConnection()

        updateID = request.args['listItems']
      
        print('get method')
        
        listItems = db.selectIDExpense(con,updateID)
        print("List Items GET")
        print(listItems)

        return render_template('updateExpense.html', listItems = listItems)

if __name__ == '__main__':
   app.run(debug=True, port=5000)
   
 