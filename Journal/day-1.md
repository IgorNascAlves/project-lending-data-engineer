# Task 1: Database

## Task Description

To complete this task, we need to perform the following steps:

1. Create a script to create the database and tables (`scripts/create_db.py` and `scripts/create_tables.py`).
2. Create a script to insert data into the tables (`scripts/load_data.py`).

## Conclusion about Relationship Between Clients and Loans Tables

### Clients Table
- **user_id**: Primary key that uniquely identifies each client.
- **created_at**: Date and time when the client was created.
- **status**: Status of the client (e.g., approved, denied).
- **batch**: Identifier for the batch to which the client belongs.
- **credit_limit**: The credit limit assigned to the client.
- **interest_rate**: The annual interest rate assigned to the client.
- **denied_reason**: Reason for denial of the client (if applicable).
- **denied_at**: Date and time when the client was denied (if applicable).

### Loans Table
- **user_id**: Foreign key referencing the `user_id` column in the `Clients` table, establishing a link between clients and their loans.
- **loan_id**: Primary key that uniquely identifies each loan.
- **created_at**: Date and time when the loan was created.
- **due_at**: Date and time when the loan is due.
- **paid_at**: Date and time when the loan was paid (if applicable).
- **status**: Status of the loan (e.g., paid, default, ongoing).
- **loan_amount**: The amount of the loan.
- **tax**: The tax on the loan.
- **due_amount**: The total amount due on the loan.
- **amount_paid**: The amount paid on the loan.

The relationship between the `Clients` and `Loans` tables allows for the association of loans with the respective clients who obtained them. Each client in the `Clients` table can have multiple loans associated with them, as indicated by the one-to-many relationship established through the `user_id` column.

This conclusion provides a clear understanding of the structure and relationship between the database tables, facilitating efficient data management and analysis.