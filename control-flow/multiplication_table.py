# multiplication_table.py

# Prompt user to input a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table using a for loop
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
