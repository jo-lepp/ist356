# write a sentinel controlled loop to input a color until quit
# add the colors to a list and print the list each time  
# don't add a color if it is already in the list
# Keep a separate list of duplicate colors and print that list at the end of the program
colors = []
duplicates = []
while True:
    color = input("Enter a color (or 'quit' to exit): ")
    if color.lower() == "quit":
        break
    if color in colors:
        duplicates.append(color)
    else:
        colors.append(color)
    print("You entered the following colors:")
    for c in colors:
        print(c)
print("Duplicate colors entered:")
for d in duplicates:
    print(d)
