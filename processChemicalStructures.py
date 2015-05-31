__author__ = 'M. Umut ATASEVER'

import itertools
import collections
from collections import Counter

def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

counter = 0
aaGlobalDict = []

dataFile = open('data/chemical.fasta', 'r+')

helix = open('data/helixChemical.txt', 'w')
beta = open('data/betaChemical.txt', 'w')
loop = open('data/loopChemical.txt', 'w')

for line in dataFile:
    lineType = counter % 3
    if lineType == 1 :
        protein = line.rstrip('\r\n')
    if lineType == 2 :
        secondary = line.rstrip('\r\n')
        groups = [''.join(value) for key, value in itertools.groupby(secondary)]
        start = 0
        for index in range(len(groups)):
            segment = groups[index]
            end = start + len(segment)
            aminoSegment = protein[start:end]
            start = start + len(segment)
            #print segment + "-" + aminoSegment
            if segment[0]=='H' :
                helix.write( aminoSegment + '\n' )
            elif segment[0]=='E' :
                beta.write( aminoSegment + '\n' )
            elif segment[0]=='L' :
                loop.write( aminoSegment + '\n' )
            else :
                print "unexpected secondary structure : " + segment[0]
                quit()
            segmentCounter = Counter(aminoSegment)
            aaDict = dict(segmentCounter)
            for aa,count in aaDict.iteritems():
                item = aa + str(count).zfill(2)
                if item not in aaGlobalDict:
                    aaGlobalDict.append(item)

    counter += 1

aaGlobalDict = sorted(aaGlobalDict)

print "Repeated structures dictionary : "
print aaGlobalDict

structureDict = {}
for x in aaGlobalDict:
    structureDict[x] = '?'

helix.close()
beta.close()
loop.close()
helix = open('data/helixChemical.txt', 'r+')
beta = open('data/betaChemical.txt', 'r+')
loop = open('data/loopChemical.txt', 'r+')
helixArff = open('data/helixChemical.arff', 'w')
betaArff = open('data/betaChemical.arff', 'w')
loopArff = open('data/loopChemical.arff', 'w')

helixArff.write("@RELATION helix\n\n")
betaArff.write("@RELATION beta\n\n")
loopArff.write("@RELATION loop\n\n")


#helixArff.write("@ATTRIBUTE TID numeric\n")
#betaArff.write("@ATTRIBUTE TID numeric\n")
#loopArff.write("@ATTRIBUTE TID numeric\n")

for x in aaGlobalDict:
    helixArff.write("@ATTRIBUTE "+ x +" {yes}\n")
    betaArff.write("@ATTRIBUTE "+ x +" {yes}\n")
    loopArff.write("@ATTRIBUTE "+ x +" {yes}\n")

helixArff.write("\n@Data\n")
betaArff.write("\n@Data\n")
loopArff.write("\n@Data\n")


TID=1
for line in helix:
    lineDict = structureDict.copy()
    line = line.rstrip()
    segmentCounter = Counter(line)
    aaDict = dict(segmentCounter)
    for aa,count in aaDict.iteritems():
        item = aa + str(count).zfill(2)
        lineDict[item] = 'yes'
    lineDict = str(collections.OrderedDict(sorted(lineDict.items())).values())
    lineDict = lineDict[1:-1].replace("'","")
    helixArff.write( lineDict + '\n')
    TID += 1

TID=1
for line in beta:
    lineDict = structureDict.copy()
    line = line.rstrip()
    segmentCounter = Counter(line)
    aaDict = dict(segmentCounter)
    for aa,count in aaDict.iteritems():
        item = aa + str(count).zfill(2)
        lineDict[item] = 'yes'
    lineDict = str(collections.OrderedDict(sorted(lineDict.items())).values())
    lineDict = lineDict[1:-1].replace("'","")
    betaArff.write( lineDict + '\n')
    TID += 1

TID=1
for line in loop:
    lineDict = structureDict.copy()
    line = line.rstrip()
    segmentCounter = Counter(line)
    aaDict = dict(segmentCounter)
    for aa,count in aaDict.iteritems():
        item = aa + str(count).zfill(2)
        lineDict[item] = 'yes'
    lineDict = str(collections.OrderedDict(sorted(lineDict.items())).values())
    lineDict = lineDict[1:-1].replace("'","")
    loopArff.write( lineDict + '\n')
    TID += 1

dataFile.close()
helix.close()
beta.close()
loop.close()
helixArff.close()
betaArff.close()
loopArff.close()
