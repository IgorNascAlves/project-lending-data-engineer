-- Count the number of rows in the Clients table
SELECT COUNT(*) AS num_clients FROM Clients;

-- Count the number of rows in the Loans table
SELECT COUNT(*) AS num_loans FROM Loans;

-- Retrieve the first 10 rows from the Clients table
SELECT * FROM Clients LIMIT 10;

-- Retrieve the first 10 rows from the Loans table
SELECT * FROM Loans LIMIT 10;

-- Retrieve the total loan amount for each user
SELECT user_id, SUM(loan_amount) AS total_loan_amount
FROM Loans
GROUP BY user_id
ORDER BY total_loan_amount DESC;

-- Retrieve the total amount paid for each loan status
SELECT status, SUM(amount_paid) AS total_amount_paid
FROM Loans
GROUP BY status;

-- Retrieve the number of users by status from the Clients table
SELECT status, COUNT(*) AS num_users
FROM Clients
GROUP BY status;

-- Retrieve the number of loans by status from the Loans table
SELECT status, COUNT(*) AS num_loans
FROM Loans
GROUP BY status;
