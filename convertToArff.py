__author__ = 'M. Umut ATASEVER'

import itertools

def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

TIDenabled = True

satir = 0

oku = open('converted.fasta', 'r+')

helix = open('helix.arff', 'w')
helix.write("@RELATION helix\n\n")
if TIDenabled :
    helix.write("@ATTRIBUTE TID numeric\n")
helix.write("@ATTRIBUTE aminoAcidSequence string\n\n@DATA\n")

beta = open('beta.arff', 'w')
beta.write("@RELATION beta\n\n")
if TIDenabled :
    beta.write("@ATTRIBUTE TID numeric\n")
beta.write("@ATTRIBUTE aminoAcidSequence string\n\n@DATA\n")

loop = open('loop.arff', 'w')
loop.write("@RELATION loop\n\n")
if TIDenabled :
    loop.write("@ATTRIBUTE TID numeric\n")
loop.write("@ATTRIBUTE aminoAcidSequence string\n\n@DATA\n")

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
                if TIDenabled:
                    helix.write( str(helixTID) + ',' )
                helix.write( aminoSegment + '\n' )
            elif segment[0]=='E' :
                betaTID = betaTID + 1
                if TIDenabled:
                    beta.write( str(betaTID) + ',' )
                beta.write( aminoSegment + '\n' )
            elif segment[0]=='L' :
                loopTID = loopTID + 1
                if TIDenabled:
                    loop.write( str(loopTID) + ',' )
                loop.write( aminoSegment + '\n' )
            else :
                print "unexpected secondary structure : " + segment[0]
                quit()

    satir = satir + 1

oku.close()
helix.close()
beta.close()
loop.close()



