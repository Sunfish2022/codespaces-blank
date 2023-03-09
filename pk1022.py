# Get user input
input_string = input("Enter a string: ")

# Check if string is long enough to swap characters
if len(input_string) >= 22:
    # Convert string to list of characters
    chars = list(input_string)

    # Swap characters
    chars[9], chars[21] = chars[21], chars[9]

    # Convert list back to string
    output_string = "".join(chars)

    # Print output
    print("Swapped string:", output_string)
else:
    print("String is not long enough to swap characters.")
