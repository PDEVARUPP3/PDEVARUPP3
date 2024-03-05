-- Query to identify potentially fraudulent transactions

-- Create a temporary table to store transaction details with aggregated information
CREATE TEMPORARY TABLE TempTransactionDetails AS
SELECT
    transaction_id,
    account_id,
    transaction_amount,
    transaction_date,
    -- Calculate rolling average transaction amount for each account
    AVG(transaction_amount) OVER (PARTITION BY account_id ORDER BY transaction_date ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING) AS rolling_avg_amount,
    -- Calculate standard deviation of transaction amount for each account
    STDDEV(transaction_amount) OVER (PARTITION BY account_id ORDER BY transaction_date ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING) AS std_dev_amount
FROM
    transactions;

-- Query to identify potentially fraudulent transactions
SELECT
    transaction_id,
    account_id,
    transaction_amount,
    transaction_date
FROM
    TempTransactionDetails
WHERE
    transaction_amount > (rolling_avg_amount + 2 * std_dev_amount)
    OR transaction_amount < (rolling_avg_amount - 2 * std_dev_amount);
