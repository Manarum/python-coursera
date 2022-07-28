#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#        X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when
#you are testing below enter mbox-short.txt as the file name.
#Desired output: Average spam confidence: 0.7507185185185187

fname = input('Enter file name:')
fh = open(fname)
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        # print(line)
        # print(float(line[20:]))
        number = float(line[20:])
        total = total + number
# print(count)
# print(total)
print('Average spam confidence:', float(total / count))
#file name is mbox-short.txt
