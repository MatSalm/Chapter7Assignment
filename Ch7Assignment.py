# Use the file name mbox-short.txt as the file name



fname = input("Enter file name: ")
fh = open(fname)
newnum = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    line = line[20:]
    newnum = float(newnum)
    line = float(line)
    newnum = newnum + line



print("Average spam confidence:", newnum/count)
