#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#name=input('enter file:')
fhand=open('mbox-short.txt')
counts=dict()
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        #print(line)
        email=line.split()
        word=email[1]
        #print(x)
        counts[word]=counts.get(word,0)+1
#print(counts)
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word
print(bigword,bigcount)




