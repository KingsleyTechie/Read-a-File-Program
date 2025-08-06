# Ask the user for the filename to read from
filename = input("Enter the name of the file to read: ")

try:
    # Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (for example: make everything uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("modified_" + filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"Modified content written to 'modified_{filename}'.")

except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: The file could not be read or written.")