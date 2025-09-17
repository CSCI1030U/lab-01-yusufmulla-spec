def main():
    cost_per_item = 19.99
    quantity = 5 

    # YOUR CODE FOR PART 1 GOES HERE  

#Given Variable
cost_per_item = 19.99
quantity = 5

# Calculate the total cost (subtotal + 13% tax) in a single step
total_cost = (cost_per_item * quantity) * 1.13

# You can still print the final result
print(f"total cost: ${total_cost:.2f}")

    # YOUR CODE FOR PART 2 GOES HERE

# Given variables
cost_per_item = 19.99
quantity = 5

# Calculate and store costs
subtotal_cost = cost_per_item * quantity
tax = subtotal_cost * 0.13
total_cost = subtotal_cost + tax

# Print all variables in the specified format
print(f'cost_per_item = ${cost_per_item:0.2f}')
print(f'quantity = {quantity}')
print(f'subtotal_cost = ${subtotal_cost:0.2f}')
print(f'tax = ${tax:0.2f}')
print(f'total_cost = ${total_cost:0.2f}')

    # THIS IS THE CODE FOR PART 3
    # initial_investment = 1000
    # interest_rate = 0.035
    # investment = initial_investment
    # investment += investment * interest_rate
    # investment += investment * interest_rate
    # investment += investment * interest_rate
    # investment += investment * interest_rate
    # investment += investment * interest_rate
    # print('After 5 years, your investment will be worth ' + investment + ' dollars.')
    # expected output: After 5 years, your investment will be worth 1187.6863056468749 dollars.


initial_investment = 1000
interest_rate = 0.035
investment = initial_investment

investment += investment * interest_rate
investment += investment * interest_rate
investment += investment * interest_rate
investment += investment * interest_rate
investment += investment * interest_rate

print('After 5 years, your investment will be worth ' + str(investment) + ' dollars.')
if __name__ == "__main__":
    main()