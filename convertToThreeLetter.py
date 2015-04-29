__author__ = 'M. Umut ATASEVER'

satir = 0
dictionary = {'G':'H', 'I':'H', 'B':'E', 'S':'L', 'T':'L', 'C':'L', ' ':'L'}

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

oku = open('CB513.fasta', 'r+')
yaz = open('converted.fasta', 'w')

for line in oku:
    islem = satir % 3
    if islem==2 :
        line = replace_all(line , dictionary)
    yaz.write(line)
    satir = satir + 1

oku.close()
yaz.close()



