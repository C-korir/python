names = input("Enter a list of names separated by commas: ").split(',')
names = list(set(names))  # remove duplicates
names.sort()  # sort in alphabetical order
print("Sorted list of names: ", names)
print("Total number of names: ", len(names))