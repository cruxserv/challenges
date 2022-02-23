import csv

output = []
count = 0
with open('data.csv') as file:
    reader = csv.reader(file)
    for line in reader:
        output.append(line)

    # next(file)
    # namedict = {}
    # for i, column in enumerate(reader, 1):
        # namedict[i] = column[1]
        count += 1

        if count > 5:
            break
# print(namedict)

search = input("Enter something to search for: ")

col = [x[1] for x in output]

if search in col:
    for x in range(0, len(output)):
        if search == output[x][1]:
            print(output[x])
else:
    print("data not found")
