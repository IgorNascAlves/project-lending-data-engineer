# Lending Operation Analysis

## Results

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