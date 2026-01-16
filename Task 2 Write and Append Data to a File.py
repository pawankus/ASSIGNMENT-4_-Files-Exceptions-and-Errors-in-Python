# Task 2: Write and Append Data to a File

filename = "output.txt"

# Step 1: Take user input and write to file
text_to_write = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

# Step 2: Take additional input and append to file
text_to_append = input("\nEnter additional text to append: ")
with open(filename, "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open(filename, "r") as file:
    print(file.read(), end="")

