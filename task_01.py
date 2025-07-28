def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File content:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
read_file("sample.txt")        
