__author__ = 'M. Umut ATASEVER'

import itertools

def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

satir = 0

oku = open('converted.fasta', 'r+')

helix = open('helix.arff', 'w')
helix.write("@RELATION helix\n\n@ATTRIBUTE TID numeric\n@ATTRIBUTE aminoAcidSequence string\n\n@DATA\n")

beta = open('beta.arff', 'w')
beta.write("@RELATION beta\n\n@ATTRIBUTE TID numeric\n@ATTRIBUTE aminoAcidSequence string\n\n@DATA\n")

loop = open('loop.arff', 'w')
loop.write("@RELATION loop\n\n@ATTRIBUTE TID numeric\n@ATTRIBUTE aminoAcidSequence string\n\n@DATA\n")

loopTID = 0
betaTID = 0
helixTID = 0

for line in oku:
    islem = satir % 3
    if islem == 1 :
        protein = line.rstrip('\r\n')
    if islem == 2 :
        secondary = line.rstrip('\r\n')
        groups = [''.join(value) for key, value in itertools.groupby(secondary)]
        start = 0
        for index in range(len(groups)):
            segment = groups[index]
            end = start + len(segment)
            aminoSegment = protein[start:end]
            start = start + len(segment)
            print segment + "-" + aminoSegment
            if segment[0]=='H' :
                helixTID = helixTID + 1
                helix.write(str(helixTID) + ',' + aminoSegment + '\n')
            elif segment[0]=='E' :
                betaTID = betaTID + 1
                beta.write(str(betaTID) + ',' + aminoSegment + '\n')
            elif segment[0]=='L' :
                loopTID = loopTID + 1
                loop.write(str(loopTID) + ',' + aminoSegment + '\n')
            else :
                print "hatali ikincil yapi!!"
                quit()

    satir = satir + 1

oku.close()
helix.close()
beta.close()
loop.close()



