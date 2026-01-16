# Task 1: Read a File and Handle Errors (with file creation)

filename = "sample.txt"

try:
    # Create and write to the file (only if it doesn't exist)
    with open(filename, "x") as file:
        file.write("This is a sample text file.\n")
        file.write("It contains multiple lines.\n")
except FileExistsError:
    pass  # File already exists, no need to recreate

try:
    # Read the file
    with open(filename, "r") as file:
        print("Reading file content:")
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


