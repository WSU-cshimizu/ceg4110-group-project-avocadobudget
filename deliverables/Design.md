# Design Specification

## Requirement 1: The user shall be able to submit their expenses
1. ***Crud***The local web server will collect user entered expenses and store them in a SQLite database.
    - Flask will be used for front-end to back-end integration.
    - When the user enters an expense it will run as an HTTP post request then sends the user entered expenses to python code that will store it in our database.
    - will create db class to handle connections, db crud methods by page, etc (this section will build out as the db class is written and expands)

2. ***Database Design***The default expense table will contain the following:
    - ***expense id (primary key)***
    - ***expense category (foreign key category table)***
    - ***expense description***
    - ***expense amount***
    - ***expense date***
    - ***expense payment method***
3. ***UI/UX***Dedicated html page for inserting an expense

## Requirement 2: The user shall be able to access a general built-in monthly budget template if they choose to have the app help them
1. The built in budget template will produce a general expense template table with recommended expense allocation based on the user's monthly

2. The default category table will contain the following fields in SQLite:
   1. ***category*** - will be text describing the category that the expenses will take (also the primary key) The categories will be defind for the program and they are below.
    - rent
    - groceries
    - entertainment
    - miscellaneous
    - bills/subscriptions 
    - Retirement
    2. ***category amount*** to define the monthly budget for each category

3. There will be validation to ensure that negative values are not allowed, also only allow valid floats.



## Requirement 3: The user shall be able to provide personalized numbers to their budget
1. This means that the user can bypass our recommended budget allocation algorithm that is based on user income and use their one budget allocation.
    - There is a button to change the amount allocated, when a new amount is saved, a new percentage will be calculated with back-end code.

## Requirement 4: The user may be able to access an intuitive reporting system that displays their monthly results
1. When the user wants to retrieve their expenses, a get request will be sent to flask and this will query the expense records from the database.
    - The user can retrieve expenses by sending a [date range I think] that will send a query to the database and display it back to the user's html page.

## Requirement 5: The user may be able to compare their current monthly expense report to older monthly reports
1. The back-end will send a range of dates to the database and query the expense results for those date ranges.
    - Will be displayed in form of a bar chart.

## Requirement 6: The user shall be able to access the application without internet access.
1. Set to run on a local system which doesn't require internet access.

## Requirement 7: The user shall be able to access all features with minimal amount of local storage
1. The program is extremely small (< 1GB) and stores less than 1GB.



## WIREFRAME
1. Homepage.....

2. MyBudget displays ......
    - How it will work

3. Contains a Expenses page that .......
    - How the different components work

4. 

