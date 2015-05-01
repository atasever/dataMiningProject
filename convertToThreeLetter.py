__author__ = 'M. Umut ATASEVER'

counter = 0
dictionary = {'G':'H', 'I':'H', 'B':'E', 'S':'L', 'T':'L', 'C':'L', ' ':'L'}

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

reader = open('data/CB513.fasta', 'r+')
writer = open('data/converted.fasta', 'w')

for line in reader:
    lineType = counter % 3
    if lineType==2 :
        line = replace_all(line , dictionary)
    writer.write(line)
    counter = counter + 1

reader.close()
writer.close()



