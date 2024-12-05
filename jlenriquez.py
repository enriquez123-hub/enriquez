# Get the number of rows from the user
num_rows = int(input("Enter the number of rows: "))

# Initialize a variable to start counting from
number = 1

# Loop through each row
for i in range(1, num_rows + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()  # Move to the next line after each row
