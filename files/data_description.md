# Tables Structure

## Clients Table ([csv](clients.csv))

| Column Name    | Data Type      | Description                                                                                          |
|----------------|----------------|------------------------------------------------------------------------------------------------------|
| user_id        | int64          | Unique identifier for each user                                                                      |
| created_at     | datetime64[ns] | Date and time when the user was created                                                             |
| status         | string         | The status of the user (approved, denied). If denied, the user cannot take new loans.               |
| batch          | int64          | The batch to which the user belongs                                                                  |
| credit_limit   | int64          | The credit limit assigned to the user. The maximum amount the user can borrow.                      |
| interest_rate  | int64          | The annual interest rate assigned to the user. The rate at which the user will be charged for borrowing money. |
| denied_reason  | string         | The reason for denial of the user. If the user is approved, this field is empty.                     |
| denied_at      | datetime64[ns] | The date and time when the user was denied. If the user is approved, this field is empty.            |

## Loans Table ([csv](loans.csv))

| Column Name  | Data Type      | Description                                                                                               |
|--------------|----------------|-----------------------------------------------------------------------------------------------------------|
| user_id      | int64          | Unique identifier for each user                                                                           |
| loan_id      | int64          | Unique identifier for each loan                                                                           |
| created_at   | datetime64[ns] | Date and time when the loan was created                                                                   |
| due_at       | datetime64[ns] | Date and time when the loan is due                                                                        |
| paid_at      | datetime64[ns] | Date and time when the loan was paid. If the loan is not paid, this field is empty.                       |
| status       | string         | The status of the loan (paid, default, ongoing). If the loan is ongoing, it means there is an open loan. The user cannot have two open loans at the same time. If the loan is defaulted, the user cannot take new loans. |
| loan_amount  | float64        | The amount of the loan.                                                                                   |
| tax          | float64        | The tax on the loan (3.8% of the principal amount + 0.0082% of the principal amount per day for 90 days)  |
| due_amount   | float64        | The total amount due on the loan (loan_amount + tax + 90 days interest)                                   |
| amount_paid  | float64        | The amount paid on the loan, until the current moment.                                                    |
