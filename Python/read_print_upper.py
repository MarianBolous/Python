file = input('enter file name:')
fname = 'words.txt'
try:
 fhandle = open(fname)
except:
 print('Cannot open the file ',fname ,'please try again')
 quit()

for line in fhandle:
 line = line.upper()
 line = line.rstrip()
 print(line)
