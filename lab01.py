def main():
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

    # Part 3: Investment calculation
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    for _ in range(5):
        investment += investment * interest_rate
    print(f'After 5 years, your investment will be worth {investment} dollars.')

if __name__ == "__main__":
    main()