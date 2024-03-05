# Load required libraries
library(dplyr)
library(ggplot2)

# Sample transaction data (replace with your own dataset)
transactions <- data.frame(
  customer_id = c(1, 1, 2, 3, 3, 3, 4, 4, 4, 4),
  purchase_date = as.Date(c('2021-01-01', '2021-02-15', '2021-03-20', '2021-04-10', '2021-05-05', '2021-06-20', '2021-07-15', '2021-08-01', '2021-09-10', '2021-10-05')),
  amount = c(100, 50, 200, 150, 75, 100, 120, 80, 90, 110)
)

# Calculate total revenue per customer
total_revenue <- transactions %>%
  group_by(customer_id) %>%
  summarise(total_revenue = sum(amount))

# Calculate time between first and last purchase per customer
customer_lifetime <- transactions %>%
  group_by(customer_id) %>%
  summarise(
    first_purchase_date = min(purchase_date),
    last_purchase_date = max(purchase_date)
  ) %>%
  mutate(lifetime = as.numeric(difftime(last_purchase_date, first_purchase_date, units = "days")))

# Calculate average revenue per day per customer
customer_lifetime <- left_join(customer_lifetime, total_revenue, by = "customer_id")
customer_lifetime <- mutate(customer_lifetime, avg_daily_revenue = total_revenue / lifetime)

# Calculate CLV (sum of average revenue per day for each customer)
clv <- sum(customer_lifetime$avg_daily_revenue, na.rm = TRUE)

# Print CLV
print(paste("Total Customer Lifetime Value (CLV): $", round(clv, 2)))

# Plot CLV distribution
ggplot(customer_lifetime, aes(x = avg_daily_revenue)) +
  geom_histogram(binwidth = 10, fill = "skyblue", color = "black") +
  labs(title = "Customer Lifetime Value (CLV) Distribution", x = "Average Daily Revenue", y = "Frequency")
