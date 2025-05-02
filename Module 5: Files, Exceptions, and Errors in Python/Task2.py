t = input("Enter text to write to the file: ")

with open('output.txt','w') as f:
    f.write(t + '\n')
    f.close()
print("Data successfully written to output.txt.\n")

t1 = input("Enter additional text to append to the file: ")


with open('output.txt','a') as f:
    f.write(t1 + '\n')
    f.close()

print("Data successfully appended.\n")

print("Final content of output.txt:")
with open('output.txt','r') as f:
    r = f.read()
    print(r)
    f.close()


# output:
# Enter text to write to the file: Hello, Python!
# Data successfully written to output.txt.

# Enter additional text to append to the file: Learning file handling in Python.
# Data successfully appended.

# Final content of output.txt:
# Hello, Python!
# Learning file handling in Python.