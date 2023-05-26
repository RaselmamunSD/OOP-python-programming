def max_split(s):
    count = 0  # Count of balanced strings
    result = []  # List to store the balanced strings
    temp = ''  # Temporary string to track the current balanced string

    for char in s:
        temp += char  # Add the current character to the temporary string

        if temp.count('L') == temp.count('R'):  # Check if the temporary string is balanced
            count += 1
            result.append(temp)
            temp = ''  # Reset the temporary string

    print(count)
    for string in result:
        print(string)

# Read the input string
s = input()

# Call the max_split function
max_split(s)
