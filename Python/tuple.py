fname = input("Enter file: ")
if len(fname)<1:
 name = "mbox-short.txt"
hand = open (fname)
d=dict()
lst = list()
for line in hand:
    if not line.startswith("From:"): continue
else:
    line = line.split()
    print (line)
    time = None
    stime = time.split(":")
    hours = stime[0]
    l = list(stime[0:1])
    for dl in l:
     d[dl]=d.get(dl,0)+1

for count,value in sorted(d.items()):
    ntupl = (int(count),value)
    lst.append (ntupl)
    print (count,value)
