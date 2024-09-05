### Members:
- Daniel Cronauer
- Owen Hill
- Abhik Ashwinkumar Patel
- Devkumar Prakashbhai Patel

### Project Overview Proposal for Avocado Budget App

### Pitch:

As a college student in this time of high inflation it is important to watch your dollars so you can purchase more avocado toast. The proposed project is a Budget app that focuses on customization to make a budget that works for you. The project will allow users to track income and expenses against their plan monthly. The app will be flexible to track on the categories that matter and make sense to you. It will also provide visualization of transactions over time and some additional bonus features as time allows. This project will help you understand where your money is coming from and where it is going. As for how much avocado toast to purchase, that is up to you.

### Components:

The project will be divided into several major components amongst the team members. The project will focus on a local solution for the budget app  (no web component as the project aims to be local to the users device).

- **UI / UX**: Abhik will handle the graphics and visual design the project. He will focus on ensuring that the budget app look pleasing, easy to navigate and understand. This will include the look for the various forms to collect transaction data for purchases, for income, and for categories to track income and expenses by.
- **Front End**: Devkumar will handle the HTML, CSS and any needed JS to provide a skeleton on which to hang the UI design provided by Abhik. He will work on providing the HTML pages for these various types of transactions to process transactions, read data, display data, etc.
- **Database Design**: Owen will focus on database schema design, some business logic and other gaps as needed. He will focus on getting the data design correct, because this will drive all the other parts of the project. Tables will include a transaction table, expense category table, income category table, budget category table, user table, etc. 
- **Database crud**: Daniel will focus on the glue and crud operations from HTML pages to the back-end database. He will also work on the business logic code and help where needed. Will need to take get / post requests from various forms / pages and route to the proper handler. Will need to take request object and manipulate to pull the data needed for recoding transactions, user category setup, user account set up, etc. 
- **Reports / queries**: this will be a group effort to ensure that the required outputs are displayed or accessed in a pleasant and easy to understand format.
- **Testing and Validation**: – Abhik and Devkuymar will focus on this portion of the project as they are the graduate students in the group.

### Architecture:

- **UI / UX design**: Figma will be used to create a visual and graphic design for the project.
- **RDMS**: – will use a relational database and software system to help organize and visualize the design of this database. This will be crucial to organize, store, and change data. A requirement will be the ability to interact with HTML / CSS webpages on a local host basis to start. Future design potential would be to move from local device use to a web access component.
- **Front End**: HTML, CSS, and JS will be utilized to provide a pleasing interface for users to experience and interact with the budget app. 
- **Crud Glue**: use software library to enable the front end to send GET, PUT, DELETE and other HTTP requests that will be handled by the crud software to interact with the local RDMS.
- **Testing tools**: we have not decided on a testing tool set to use yet but will explore options (maybe internal testing) as this project progresses. 
### Tech Stack:
- **DB Browser** will be the RDMS used for our database needs. This is an open-source database software management system that works well with managing SQLite databases. It is easy to install, open source, well documented and reliable.
- **Database SQLite** Plan is to use SQLite database. This is a lightweight near universal software available on almost all devices. It is highly reliable and the most common database software in the world. It is open source and free to use for any purpose. 
- **Front End** Plan is to use HTML, CSS, and JS for website pages on local host. This is a proven method to display forms for collection of data. Once again this is free to use software.
- **Crud glue** Flask is a Python library that will be used to capture HTML requests and perform crud operations on the DB as requested by front end prompts from the user.  It is open source, easy to use and quick to start local testing on.
- **Python** will be the main coding language for glue, business logic and other back-end tasks. There are robust libraries available to interact with front end in Flask and back end in SQlite3. 
- **Testing** – blurb from graduates here
- **Tech stack validation** given that this stack open source and widely supported; it will be cheap to start development on. Given the local file method for SQLite much of the complexity from web applications will be reduced by provided local only solutions. This will also simplify security concerns as the communication between the app and the back-end database will be handled locally. 

### Justification:

HTML,CSS, and JS will be used for an interactive front end that can adapt to changing needs. Python is an easy to read and develop language with many libraries to tie the front end with the SQLite back-end. These tools are open-source, free licesning and very reliable. This will enable a project that is fast to code, test and implement.

### Software Development Life Cycle Methodology:

Feature Driven Agile

### Meeting Expectations:

1x per week 20-minute scrum meeting at minimum. During the scrum, every group member will answer the following three questions: What am I working on? What am I going to work on? Is there anything blocking me from doing said work?
Further communication and collaboration will be done over discord; here we can schedule additional meetings as needed.

### Git Branching Strategies:

We will be using a feature branching strategy where each feature will get its own branch. These branches will vary whether they are worked on by an individual group member or multiple group members.

