__author__ = 'ml'

counter = 0
protein = ""
fasta = open('data/chemical.fasta', 'r+')

for line in fasta:
    printed = False
    lineType = counter % 3
    if lineType == 0 :
        protein = line
    if lineType==1 :

        if line.find('B')>=0:
            print "b",protein,line
            printed = True
        if line.find('X')>=0:
            if not printed:
                print "x",protein,line
                printed = True
        if line.find('Z')>=0:
            if not printed:
                print "z",protein,line
                printed = True

    counter = counter + 1
