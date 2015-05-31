__author__ = 'M. Umut ATASEVER'

counter = 0
dictionary = {'D':'1', 'E':'1', 'A':'2', 'G':'2', 'I':'2', 'L':'2', 'V':'2', 'N':'3', 'Q':'3', 'F':'4', 'W':'4', 'Y':'4', 'R':'5', 'H':'5', 'K':'5', 'S':'6', 'T':'6', 'P':'7', 'C':'8', 'M':'8'}

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

reader = open('data/converted.fasta', 'r+')
writer = open('data/chemical.fasta', 'w')

for line in reader:
    lineType = counter % 3
    if lineType==1 :
        line = replace_all(line , dictionary)
    writer.write(line)
    counter = counter + 1

reader.close()
writer.close()



