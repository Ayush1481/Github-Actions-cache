import numpy as np

# Sample data for 'Returns' and 'Net_Sales'
returns = np.array([10, 20, 15, 25, 30, 5, 40, 50, 60, 12])
net_sales = np.array([100, 210, 160, 240, 310, 50, 420, 510, 600, 150])

# Calculate the correlation
correlation = np.corrcoef(returns, net_sales)[0, 1]

# Create the result dictionary
result = {
    'pair': 'Returns-Net_Sales',
    'correlation': float(correlation)
}

# Print the result
print(result)