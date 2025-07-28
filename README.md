# Files-Exceptions-and-Errors-in-Python
# Task 1
# Read a File and Handle Errors 
1) Opens a File
    The program attempts to open a file named sample.txt in read mode using:
    with open(filename, 'r') as file:
    This ensures the file is automatically closed after reading, even if an error occurs.
2) Reads and Prints Content Line by Line
    If the file opens successfully, it reads the file one line at a time using a for loop:
    for line in file:
    print(line.strip())
    The strip() method is used to remove extra whitespace and newline characters, making the output cleaner.

3) Handles Errors Gracefully
    If the file does not exist, the program catches the FileNotFoundError and displays a clear error message:
    except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
    It also includes a general except block to handle any unexpected errors:
    except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Task 2
#  Write and Append Data to a File
1) Takes User Input and Writes to the File (output.txt)
    The program first prompts the user to enter some text.
    It opens the file in write mode ('w'), which creates the file if it doesn’t exist or overwrites its content if it does.
    The user's input is written into the file followed by a newline character:
    with open(filename, 'w') as file:
       file.write(user_input + '\n')
2) Appends Additional Data to the Same File
    Next, the program asks the user for more input.
    It opens the same file in append mode ('a'), which adds the new input without erasing the previous content.
    The additional input is appended to the end of the file:
    with open(filename, 'a') as file:
       file.write(additional_input + '\n')
3) Reads and Displays the Final Content
    Finally, the program opens the file in read mode ('r') and prints its content line by line.
    It uses rstrip() to remove trailing newline characters and keep the output clean:
    for line in file:
       print(line.rstrip())
