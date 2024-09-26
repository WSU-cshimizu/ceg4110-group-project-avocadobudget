# Project Requirements

## System Requirements
- The application shall run on the latest version of Chrome (V. 129.0.6668.58/59).
- The application shall run on the latest version of Edge (V. 128.0.2739.79)
- The application shall run on the latest version of Safari (V. 18)
- The application shall run on the latest version of Firefox (130.0.1)
- User logged expenses shall be stored in the database for no longer than five years.

## User Requirements

### The user shall be able to submit their expenses for later retrieval.
  1. The user will be able to store the following content for each new expense on a nice form
     - Expense description
     - Expense Category
     - Expense Amount
     - Expense Date
     - Expense Payment Method (Card, Cash, Venmo, etc)
  2. The user will be able to store the information from the expense entry form on a database for persistence beyond the session.
  3. The user will have a form to update/delete/read past transactions entered, for user ease it will be searchable by month and changes will persist in the database.
  4. The user will have validation to help the user provide accurate data. For example, no negative number or zero value numbers and of course float values only in the amount box.

### The user shall be able to access a general built-in budget template.
  1. The user will have default categories provided
  2. The user will have default amounts for each category provided
  3. The user will have these settings saved for later use, comparison and display
  4. The user will have an easy interface to click a button for default options to be pulled into their permanent category comparison
  5. The user will have the option in the interface (form) listed above that allows them to pick default budget or personalized budget. By default, the user has a personalized template, however, it defaults to a specific template the first time they load the form. 
  6. The user will have validation to help reduce their chance of error.
  7. The form will display rows of data with the following columns
    - Budget Category
    - Budget Catgory Amount
    - Button to Update
    - Button to Delete
  8. Later if the user desires, they can click a button to clear their personalized budget and replace with default template.  
  
### The user shall be able to access a personalized monthly budget template to fit their exact needs.
  1. The user will be able to personalize the categories if desired. This could include, add, remove, or update categories. The user would like this form to be the same as the built-in budget template to avoid confusion.
  2. The user will be able to set target amounts for each category
  3. The user will have their personalized settings saved for later comparison against their tracked expenses
  4. The user will have an interface where they can pull up their current categories and amounts selected. They will to be able to add, update, remove items as needed.
  5. The user will be able to clear their budget settings and return to default template if desired.
  6. The user will have some validation to avoid entering negative numbers, missing boxes, etc

### The user shall be able to access an intuitive reporting system that displays the their monthly results.
  1. The user wants a form what it is easy to navigate and click buttons to display results by month or maybe by other ranges of time. 

### The user shall be able to compare their currently monthly report to older monthly reports.
  1. The user will be able to navigate to a form that provides an intuitive interface to compare their expenses against budget over time.
  2. The user wants easy to digest information. The representation will be graph form and display expense total by category, by month against the budget targets.

### The user may be able to load credit card reports directly into their expenses for efficiency.
  1. The user would like some functionality where they could load a file in the app to automatically pull in expenses based on a predifined format.
  2. The user would appreciate using this feature so they can also shift over any excel sheet they use for their own budgeting purposes.

### The user shall be able to access the application with or without internet access.
  1. The user will have their app run locally as well as store locally. This avoids sending sensitive data over the web.

### The user shall be able to access all features with minimal amount of local storage.
  1. The user will have a simple database structure that does not require storage.

# Sub-System Requirements

### GUI Requirements

### Database Requirements

### Back-end Requirements

### Error-Handling Requirements
