# Create or open a file to write the numbers
with open('input.txt', 'w') as f:
    # Loop through numbers from 1 to 50,000 and write each on a new line
    for i in range(1, 500001):
        f.write(f"{i}\n")
