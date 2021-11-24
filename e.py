import csv

datafile = "Shape.csv"
data = list(csv.reader(open(datafile)))
lines= len(list(data))
line = lines - 1
i = 1

for i in range(1, line):
    shapeId = data[i][1]
    if data[i+1][1] == '':
        data[i+1][1] = shapeId
        i += 1
    else:
        i += 1

i = 1

for i in range(1, line):
    shapeId = data[i][0]
    if data[i+1][0] == '':
        data[i+1][0] = shapeId
        i += 1
    else:
        i += 1


writer = csv.writer(open('output.csv', 'a'))
writer.writerows(data)

with open('output.csv') as reader, open('output.csv', 'r+') as writer:
    for line in reader:
      if line.strip():
        writer.write(line)
    writer.truncate()

bad_words = ['Shape 1']

with open('output.csv') as oldfile, open('output_1.csv', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
