# Design Specification

## Requirement 1: The user shall be able to submit their expenses
1. The local web server will collect user entered expenses and store them in a SQLite database.
    - Flask will be used for front-end to back-end integration.
    - When the user enters an expense it will run as a post request then sends the user entered expenses to python code that will store it in our database.

## Requirement 2: The user shall be able to access a general built-in budget template if they choose to have the app help them
1. The built in budget template will produce a general expense template table with recommended expense allocation based on the user's monthly or yearly income.

2. The default expense table will contain the following:
    - primary key
    - expense category
    - expense description
    - expense amount
    - expense date
    - expense payment method

3. The default category table will contain the following records in SQLite:
   
    - rent
    - groceries
    - entertainment
    - miscellaneous
    - bills/subscriptions [optional]
    - Retirement [optional]

- Each record will be a unique key for the expense records.

4. There will be a category class in the back-end code.
    - This helps to determine if a optional category is active
    - Helps with determining if a category already exists so you can't add the same category to the budget twice.

5. There may be an expense class that will be inherited by the category class.
    - Improves code readibility
    - Simplifies the functions in the category class.

## Requirement 3: The user shall be able to provide personalized numbers to their budget
1. This means that the user can bypass our recommended budget allocation algorithm that is based on user income and use their one budget allocation.
    - There is a button to change the amount allocated, when a new amount is saved, a new percentage will be calculated with back-end code.

## Requirement 4: The user may be able to access an intuitive reporting system that displays their monthly results
1. When the user wants to retrieve their expenses, a get request will be sent to flask and this will query the expense records from the database.
    - The user can retrieve expenses by sending a [date range I think] that will send a query to the database and display it back to the user's html page.

## Requirement 5: The user may be able to compare their current monthly expense report to older monthly reports
1. The back-end will send a range of dates to the database and query the expense results for those date ranges.
    - Will be displayed in form of a bar chart.

## Requirement 6: The user may be able to load credit card reports directly into their expenses for effeciency

## Requirement 7: The user shall be able to access the application without internet access.
1. Set to run on a local system which doesn't require internet access.

## Requirement 8: The user shall be able to access all features with minimal amount of local storage
1. The program is extremely small (< 1GB) and stores less than 1GB.



## WIREFRAME
1. Homepage.....

2. MyBudget displays ......
    - How it will work

3. Contains a Expenses page that .......
    - How the different components work

4. 

