# Function to calculate percentage value
# x: base value, y: percentage to calculate

def c(x, y):
    # Multiply x by y and divide by 100 to get the percentage
    return x * y / 100

# Example values
a = 200  # Base value
b = 15   # Percentage to calculate

# Calculate 15% of 200 and print the result
result = c(a, b)
print("15% of 200 is:", result)  # Output: 30.0

# Descriptive Analysis:
# The function c(x, y) computes y percent of x.
# For a = 200 and b = 15, it calculates 200 * 15 / 100 = 30.0.
# This is useful for finding percentage values in various scenarios, such as discounts, interest, or statistics.
