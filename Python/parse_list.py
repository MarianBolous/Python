fname = input ("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From"):
        continue
    if line.startswith ("From"):
        line = line.split()
        line=line[1]
        count = count +1
        print (line)
print("The number of line that start with From are : ",count)
