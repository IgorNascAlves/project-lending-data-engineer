# Lending Operation Analysis

## Database

The PostgreSQL database was set up with the scripts [create_db.py](scripts/create_db.py), [create_tables.py](scripts/create_tables.py), and [load_data.py](scripts/load_data.py).

The relationship between the `Clients` and `Loans` tables allows for the association of loans with the respective clients who obtained them. Each client in the `Clients` table can have multiple loans associated with them, as indicated by the one-to-many relationship established through the `user_id` column.

This conclusion provides a clear understanding of the structure and relationship between the database tables, facilitating efficient data management and analysis.

## SQL and Data Viz Results

### 1. Loan Issuance Analysis

Identify the best month in terms of loan issuance. What was the quantity and amount lent in each month?

| Month       | Total Quantity | Total Amount    |
|-------------|----------------|-----------------|
| December 2023 | 17,351         | $442,464,966.00|

The analysis indicates that December 2023 had the highest loan issuance, with a total of 17,351 loans issued and a total amount lent of $442,464,966.00. This information provides insights into the peak activity of loan issuance, which can be further analyzed to understand potential factors contributing to the increased demand for loans during that month.

### 2. Overall Adherence by Batch

Which batch had the best overall adherence?

| Batch ID | Total Loans | Paid Loans | Adherence |
|----------|-------------|------------|-----------|
| 2        | 37,415      | 22,558     | 60.29%    |

The result indicates that batch number 2 had the highest proportion of clients who successfully repaid their loans compared to the other batches, with an adherence rate of approximately 60.29%.

### 3. Loan Outcomes by Interest Rate

Do different interest rates lead to different loan outcomes in terms of default rate?

| Interest Rate | Total Clients | Paid Loans | Rate of Paid Loans |
|---------------|---------------|------------|--------------------|
| 30            | 42,214        | 22,271     | 52.76%             |
| 90            | 42,793        | 22,579     | 52.76%             |
| 70            | 41,963        | 22,103     | 52.67%             |
| 20            | 42,779        | 22,642     | 52.93%             |

Overall, it seems that regardless of the interest rate, the rate of paid loans is quite similar, hovering around 52-53%.

### 4. Ranking Clients based on Payment Rate

Rank the best 10 and 10 worst clients. Explain your methodology for constructing this ranking.


| User ID | Paid Loans | Total Loans | Payment Rate | Ranking |
|---------|------------|-------------|--------------|---------|
| 84878   | 5          | 5           | 100.0%       | 1       |
| 45007   | 5          | 5           | 100.0%       | 2       |
| 55496   | 6          | 6           | 100.0%       | 3       |
| 77401   | 5          | 5           | 100.0%       | 4       |
| 49381   | 6          | 6           | 100.0%       | 5       |
| 64827   | 5          | 5           | 100.0%       | 6       |
| 65125   | 5          | 5           | 100.0%       | 7       |
| 73264   | 5          | 5           | 100.0%       | 8       |
| 50001   | 5          | 5           | 100.0%       | 9       |
| 78645   | 5          | 5           | 100.0%       | 10      |
| ...     | ...        | ...         | ...          | ...     |
| 19499   | 4          | 5           | 80.0%        | 2321    |
| 38637   | 4          | 5           | 80.0%        | 2322    |
| 49405   | 4          | 5           | 80.0%        | 2323    |
| 11998   | 4          | 5           | 80.0%        | 2324    |
| 40702   | 4          | 5           | 80.0%        | 2325    |
| 23856   | 4          | 5           | 80.0%        | 2326    |
| 73871   | 4          | 5           | 80.0%        | 2327    |
| 45583   | 4          | 5           | 80.0%        | 2328    |
| 81486   | 4          | 5           | 80.0%        | 2329    |
| 36328   | 4          | 5           | 80.0%        | 2330    |


The top 10 clients listed have demonstrated the highest payment rates, indicating a strong track record of loan repayment. Conversely, the bottom 10 clients listed have lower payment rates, indicating a lower rate of loan repayment compared to others.

### 5. Default Rate Analysis by Month and Batch

What is the default rate by month and batch?

| Batch | Loan Month | Total Loans | Defaulted Loans | Default Rate |
|-------|------------|-------------|-----------------|--------------|
| 4     | 12.0       | 925         | 21              | 2.27%        |
| 4     | 1.0        | 837         | 20              | 2.39%        |
| 3     | 11.0       | 1061        | 28              | 2.64%        |
| 1     | 12.0       | 14,819      | 394             | 2.66%        |
| 4     | 11.0       | 773         | 22              | 2.85%        |
| 1     | 1.0        | 14,424      | 426             | 2.95%        |
| 3     | 12.0       | 1,357       | 40              | 2.95%        |
| 3     | 1.0        | 1,284       | 41              | 3.19%        |
| 1     | 11.0       | 11,729      | 375             | 3.20%        |
| 2     | 12.0       | 5,453       | 176             | 3.23%        |
| 2     | 1.0        | 5,221       | 178             | 3.41%        |

Batches and months with lower default rates are generally more favorable because they indicate a lower likelihood of loan defaults.

You can check the full analysis in the [Jupyter Notebook](notebooks/exploring.ipynb) or on the HTML page [here](results/exploring.html).

## Python and Infra Solution

### First was developed a Python script with a function to add and alter users in the clients table in a safe way

Both functions utilize parameterized queries, ensuring protection against SQL injection attacks by separating SQL code from data. Connection management is handled adeptly within try...finally blocks, guaranteeing closure of connections regardless of potential errors, thus preventing resource leaks. Error handling is comprehensive, effectively catching and logging any database interaction errors for troubleshooting. Sensible use of environment variables via os.getenv() and .env files maintains security by keeping sensitive database connection details out of the source code. Structured with clear control flow, the functions maintain readability and maintainability, bolstering overall code reliability.

[client_management](python_infra/client_management.py)

### automated email service

* remind users with ongoing loans about payments
* weekly email summarizing operation activities

To this part, I use Airflow DAGs to schedule the email sending. The DAGs are in the [dags](python_infra/airflow/DAGS) folder.

Certainly! Here's a revised explanation with the inclusion of links to the Python files for each DAG:

### Client Interaction DAG:

This DAG is responsible for managing communication with clients who have ongoing loans and need reminders about upcoming payments.

#### Tasks:

1. **Client Check Task:** This task checks for all clients with ongoing loans whose payment due date falls within a certain timeframe from the current date. It identifies these clients and extracts their user IDs, then searches for their corresponding email addresses and saves them into a CSV file.

2. **Email Sending Task:** Once the CSV file is generated, this task reads the file and sends reminder emails to the identified clients based on a predefined email template.

**Python File:** [clients_email.py](python_infra/airflow/DAGS/clients_email.py)

### Weekly Operational Summary DAG:

This DAG focuses on sending a weekly email summarizing operational activities.

#### Tasks:

1. **Data Retrieval Task:** This task gathers relevant information from the database, such as the profit generated in the current month, loans issued in the current month, and the total amount of loans issued in the current month. It then saves this information into a CSV file.

2. **Email Composition and Sending Task:** After the CSV file is created, this task reads its contents, compiles the information into an email template suitable for a weekly operational summary, and sends it out.

**Python File:** [operational_email.py](python_infra/airflow/DAGS/operational_email.py)

In both DAGs, the tasks are orchestrated to ensure seamless execution of the workflow. This approach streamlines the process of communicating with clients regarding payments and provides stakeholders with regular updates on operational performance.