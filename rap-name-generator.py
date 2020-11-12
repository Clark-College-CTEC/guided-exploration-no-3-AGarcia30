# Guided Exploration No. 3
# Austin Garcia

# importing random
import random

# Defining a list
possible_names = []

# Opening text file
outputFile = open('rap-names-output.txt', 'w')

# using with to open rap names for read access
with open('rap-names.txt', 'r') as dataFile:
    # Looping name in dataFile
    for name in dataFile:
        # strips off the invisible line-feed and pick randomly in the list.
        possible_names.append(name.rstrip())

# Asking the user how many rap names would they like to create.
count = int(input('How many rap names would you like to create? '))
# Asking the user how many parts should the name contain?
parts = int(input('How many parts should the name contain? '))

# Looping on how many rat names in count
for i in range(count):
    # Defining name_parts as a list variable
    name_parts = []
    # another loop on the number of parts
    for j in range(parts):
        # will randomly select random names from possible_names and append it to name_parts
        name_parts.append(possible_names[random.randint(0, len(possible_names)-1)])

        # writes out a generated rap name
        outputFile.write(f"{' '.join(name_parts)}\n")
    # lists and glues together rap names and spaces them out.
    print(f"{' '.join(name_parts)}")

# Closes outputFile
outputFile.close()