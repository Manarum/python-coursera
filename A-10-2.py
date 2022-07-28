#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# Note that the autograder does not have support for the sorted() function.
# addded extra comment
fhandle=open('mbox-short.txt')
d=dict()
l=list()
for line in fhandle:
    line=line.rstrip()
    if line.startswith('From '):
        #print(line)
        ls=line.split()
        t=ls[5]
        #print(t)
        hs=t.split(':')
        #print(hs)
        h=hs[0]
        #print(h)
        l.append(h)
#print(l)
for w in l:
    d[w]=d.get(w,0)+1
#print(d)
for k,v in sorted(d.items()):
    print(k,v)

