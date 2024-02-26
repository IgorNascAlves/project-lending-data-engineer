# Lending Operation Analysis

## The dataset

The clients and loans tables translate the Lending operation of a Brazilian bank. All the loans have 90 days duration and no installments payments. The clients must pay at the pace that they see fit. The cost (interest) of the loan is fixed. The due amount of the loan is clearly stated for the client when the contract is issued. For this example, let’s suppose that it doesn't matter how fast the loan is repaid, the amount charged will remain unchanged despite the interest rate.

Consider the current date to be Jan 25 of 2024

## Case Resolution

### Database

1. Set up a PostgreSQL database with the provided tables.
2. Explain the relationship between the tables.

> Use this database to answer the questions in the next section.

### SQL and Data Viz

1. Identify the best month in terms of loan issuance. What was the quantity and amount lent in each month?
2. Which batch had the best overall adherence?
3. Do different interest rates lead to different loan outcomes in terms of default rate?
4. Rank the best 10 and 10 worst clients. Explain your methodology for constructing this ranking.
5. What is the default rate by month and batch?
6. Assess the profitability of this operation. Provide an analysis of the operation's timeline.

> adherence: clients that got loans\
> season: loan issuing month\
> default rate: defaulted/issued loans

### Python and Infra

1. Develop functions to add and alter users in the clients table in a safe way.
2. Propose processes that should run daily, weekly, or monthly to maintain a healthy operation.
3. Develop an automated email service to remind users with ongoing loans about payments. Select the frequency and content as you see fit.
4. Create an automated weekly email summarizing operation activities. Define the layout and information included.
Submission

## Presentation

The presentation will be purely technical, focused on the case resolution.

- Part I: Provide a comprehensive overview of the database tables and the nature of the data you will be handling.
- Part II: Present your answers to the SQL and Data Viz session. Make a closing statement regarding the current status of this Lending operation.
- Part III: Q&A

Good luck!
