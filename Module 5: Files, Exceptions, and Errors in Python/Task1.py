# Task 1: Read a File and Handle Errors 


# filename = "sample.txt"

# try:
#     with open(filename, 'r') as f:
#         print("Reading file content:")
#         lines = f.readlines()
#         print(lines)
#         n = len(lines)
#         print(n)
#         for i in range(1,n+1):
#             print(f"Line {i}: {lines[i].strip()}")
#         f.close()
# except FileNotFoundError:
#     print(f"Error: The file '{filename}' was not found.")



# Python Program to read a file and handle errors (using range)

filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        print("Reading file content:")
        lines = file.readlines()
        for i in range(len(lines)):
            print(f"Line {i + 1}: {lines[i].strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
