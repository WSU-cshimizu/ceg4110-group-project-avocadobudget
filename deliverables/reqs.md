# Project Requirements

## System Requirements
- The application shall run on the latest version of Chrome (V. 129.0.6668.58/59).
- The application shall run on the latest version of Edge (V. 128.0.2739.79)
- The application shall run on the latest version of Safari (V. 18)
- The application shall run on the latest version of Firefox (V. 130.0.1)
- User logged expenses shall be stored in the database to be removed at the users discretion

## User Requirements

### The user shall be able to manage their expenses for retrieval and change.
  1. The user will be able to store the following content for each new expense on a nice form.
     - Expense description
     - Expense Category
     - Expense Amount
     - Expense Date
     - Expense Payment Method (Card, Cash, Venmo, etc)
  2. The user will be able to insert, update or delete their expenses. 
  3. The user will have a form that displays a table of expenses that allows them to select a button to delete or update the desired transaction, for user ease it will be searchable by several different filter options.
  4. The user will have validation to help collect accurate data. For example, no negative number or zero value numbers and of course float values only in the amount box

### The user shall be able to access a general built-in budget template if they choose to have the app help them
  1. The user will have default categories defined
  2. The user will have default percentages defined for these category
  3. The user will enter their net monthly income income and based off the percentages it will determine their budget
  4. The user will have an easy interface to click a button for default options to be pulled into their permanent category comparison. This will be done based on user net monthly income.
  5. The user will be able to define their default income driven selection to drive the default template
  6. The user will have validation to help reduce their chance of error when selecting their income
  7. The form will display the budget template in an easy to understand and change format
  8. Later if the user desires, they can click a button to clear their personalized budget and replace with default template based on their income
  
### The user shall be able to proovide personalized numbers to their budget
  1. The user will not be able to change categories given time constraints.
  2. The user will be able to set and change target amounts for each category if desired.
  3. The user will have an interface where they can pull up their current categories and amounts selected. They will to be able to update the amounts only as part of a time constraint.
  4. The user will be able to clear their budget settings and return to default template if desired. This will be based on net monthly income provided when reseting.
  5. The user will have some validation to avoid entering negative numbers, missing boxes, etc

### The user may be able to access an intuitive reporting system that displays their monthly results.
  1. The user wants a form that it is easy to navigate and click buttons to display results by month
  2. The user wants easy to digest information. The representation will be graph form and display expense total by category, by month against the budget targets

### The user may be able to load credit card reports directly into their expenses for efficiency.
  1. The user would like some functionality where they could load a file in the app to automatically pull in expenses based on a predifined format
  2. The user would appreciate using this feature so they can also shift over any excel sheet they use for their own budgeting purposes
  3. ***This functionality was a extra feature that did not get added due to time constraints*** On the flip side we did add an export to excel feature. This is why we said "may" be able to. 

### The user shall be able to access the application without internet access.
  1. The user will have their app run locally as well as store locally. This avoids sending sensitive data over the web

### The user shall be able to access all features with minimal amount of local storage.
  1. The user will have a simple database structure that does not require storage
  
## GUI Requirements - derived from user stories
  1. One form to display all expenses by month - options to update / delete each expense
  2. Another form to display to insert a new expense or update selected expense from the form in bullet 1
  3. Another form to handle budget selection. Income entry can be used to drive a percentage driven default budget, or personalize however you see fit.
  4. Another form for to handle data analysis and graphs.
  5. A nav bar to easily switch between different parts of the app.

## Testing

### Adding Expenses:
Ensure users can add a new expense by entering valid values for description, category, amount, date, and payment method. Verify that invalid data (e.g., negative/zero amounts or missing fields) is rejected with appropriate error messages.

### Updating Expenses:
Test the functionality for editing an expense from the expense table. Ensure changes (e.g., adjusting amount or category) are saved correctly. Validate that invalid updates, like negative amounts, are prevented.

### Deleting Expenses:
Confirm that users can delete an expense from the table. Check that the expense is removed from both the table display and the local database.

### Searching/Filtering:
Validate that users can search and filter expenses by different criteria (e.g., date range, category, or description). Ensure the filtered results update dynamically and accurately.

### Default Template Loading:
Test that clicking the "Calculate Budget" button applies default categories and percentages based on the user’s monthly income.

### Setting Custom Budgets:
Verify users can set and save personalized target amounts for budget categories. Ensure these changes persist and can be updated.

### Validation for Inputs:
Test that all forms prevent invalid inputs such as negative amounts, non-numeric data, or empty fields, ensuring robust validation.

### Displaying Monthly Reports:
Validate that the monthly expense report shows a breakdown of expenses by category in graphical form. Ensure the data aligns with budget targets.

### Navigation:
Ensure smooth navigation between the expense form, budget form, and reporting system. Check that buttons and links are clearly labeled and functional.

### Offline Functionality:
Test the app’s functionality in offline mode. Ensure all features, like adding expenses or generating reports, work seamlessly without internet access.

### Local Data Storage:
Verify that all user data is stored locally, securely, and efficiently, ensuring sensitive data remains private.

### Graph Representation:
Ensure budget and expense data are represented clearly in graphs. Validate visual consistency and alignment with the inputted data.

### Expense Table Management:
Test that users can view all their expenses in a table format, with options to update or delete specific entries.

### Budget Validation:
Validate the app correctly calculates budget percentages and targets based on user-provided income.

### Search and Filter UI:
Verify the search and filter interface is user-friendly, with responsive and accurate filtering for expenses.

### Default Validation:
Test validation for income input when generating a default budget. Prevent zero, negative, or invalid income entries.

### Efficiency Testing:
Ensure the app efficiently processes large numbers of expenses or file imports without noticeable delays.

### Reporting Interface Usability:
Validate that the reporting interface is intuitive, with buttons to generate reports.

### Data Integrity:
Confirm that all displayed and stored data accurately reflects the user’s inputs and calculations.

