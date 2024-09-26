# Project Requirements

## System Requirements
- The application shall run on the latest version of Chrome (V. 129.0.6668.58/59).
- The application shall run on the latest version of Edge (V. 128.0.2739.79)
- The application shall run on the latest version of Safari (V. 18)
- The application shall run on the latest version of Firefox (V. 130.0.1)
- User logged expenses shall be stored in the database to be removed at the users discretion

## User Requirements

### The user shall be able to submit their expenses for later retrieval.
  1. The user will be able to store the following content for each new expense on a nice form
     - Expense description
     - Expense Category
     - Expense Amount
     - Expense Date
     - Expense Payment Method (Card, Cash, Venmo, etc)
  2. The user will be able to insert or update theirs expenses 
  3. The user will have a form that displays a table of expenses that allows them to select a button to delete or update the desired transaction, for user ease it will be searchable by month
  4. The user will have validation to help collect accurate data. For example, no negative number or zero value numbers and of course float values only in the amount box

### The user shall be able to access a general built-in budget template if they choose to have the app help them
  1. The user will have default categories defined
  2. The user will have default percentages defined for these category
  3. The user will enter their income and based off the percentages it will determine their budget
  4. The user will have an easy interface to click a button for default options to be pulled into their permanent category comparison
  5. The user will be able to load their default income driven selection to be stored for later tracking 
  6. The user will have validation to help reduce their chance of error when selecting their income
  7. The form will display the budget template in an easy to understand and change format
  8. Later if the user desires, they can click a button to clear their personalized budget and replace with default template based on their income
  
### The user shall be able to proovide personalized numbers to their budget
  1. The user will be able to personalize the categories if desired
  2. The user will be able to set target amounts for each category if desired
  3. The user will have an interface where they can pull up their current categories and amounts selected. They will to be able to add, update, remove items as needed
  4. The user will be able to clear their budget settings and return to default template if desired
  5. The user will have some validation to avoid entering negative numbers, missing boxes, etc

### The user may be able to access an intuitive reporting system that displays their monthly results.
  1. The user wants a form that it is easy to navigate and click buttons to display results by month

### The user may be able to compare their currently monthly report to older monthly reports.
  1. The user will be able to navigate to a form that provides an intuitive interface to compare their expenses against budget over time
  2. The user wants easy to digest information. The representation will be graph form and display expense total by category, by month against the budget targets

### The user may be able to load credit card reports directly into their expenses for efficiency.
  1. The user would like some functionality where they could load a file in the app to automatically pull in expenses based on a predifined format
  2. The user would appreciate using this feature so they can also shift over any excel sheet they use for their own budgeting purposes

### The user shall be able to access the application without internet access.
  1. The user will have their app run locally as well as store locally. This avoids sending sensitive data over the web

### The user shall be able to access all features with minimal amount of local storage.
  1. The user will have a simple database structure that does not require storage
  

