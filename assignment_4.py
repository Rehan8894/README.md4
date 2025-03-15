# ASSIGNMENT 4:
# Module 5: Files, Exceptions, and Errors in Python
#
# Task 1: Read a File and Handle Errors

#Task 1

# prompt: Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end="")  # end="" prevents extra newline
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
read_and_print_file("sample.txt")

# Task 2  (Task 2: Write and Append Data to a File)

# prompt: Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

user_input = input("Enter text to write to the file: ")

# Write user input to the file
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Append additional data to the file
with open("output.txt", "a") as file:
    file.write("This text is appended.\n")
    file.write("This is another line of appended text.\n")

# Read and display the file contents
with open("output.txt", "r") as file:
    contents = file.read()
    print("\nFile contents:\n", contents)