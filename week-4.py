# File Read & Write 
# Open the original file for reading
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify content (uppercase in this case)
modified_content = content.upper()

# Write to a new file
with open("output.txt", "w") as outfile:
    outfile.write("Modified Content:\n")
    outfile.write(modified_content)

print(f" output.txt created successfully with modified text!")
