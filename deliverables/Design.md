# Design Specification

## Requirement 1: The user shall be able to submit their expenses
1. The local web server will collect user entered expenses and store them in a SQLite database.
    - Flask will be used for front-end to back-end integration.
    - When the user enters an expense it will run as a post request then sends the user entered expenses to python code that will store it in our database.

## Requirement 2: The user shall be able to access a general built-in budget template if they choose to have the app help them
1. The built in budget template will produce a general expense template table with recommended expense allocation based on the user's monthly or yearly income.

2. The default expense fields will contain the following:
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
    - water [optional]
    - gas [optional]
    - electric [optional]
    - Retirement [optional]


## Requirement 3: The user shall be able to provide personalized numbers to their budget
1. This means that the user can bypass our recommended budget allocation algorithm that is based on user income and use their one budget allocation.


## Requirement 4: The user may be able to access an intuitive reporting system that displays their monthly results
1. When the user wants to retrieve their expenses, a get request will be sent to flask and this will query the expense records from the database.
    - The user can retrieve expenses by sending a [date range I think] that will send a query to the database and display it back to the user's html page.

## Requirement 5: The user may be able to compare their current monthly expense report to older monthly reports


## Requirement 6: The user may be able to load credit card reports directly into their expenses for effeciency

## Requirement 7: The user shall be able to access the application without internet access.

## Requirement 8: The user shall be able to access all features with minimal amount of local storage
