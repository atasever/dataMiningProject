__author__ = 'M. Umut ATASEVER'

import itertools
import collections
from collections import Counter

def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

counter = 0
aaGlobalDict = {}

dataFile = open('data/converted.fasta', 'r+')

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
            aaSet = list(set(aminoSegment))
            aaGlobalDict = set(list(aaGlobalDict) + list(aaSet))

    counter += 1


aaGlobalDict = sorted(aaGlobalDict)


structureDict = {}
for x in aaGlobalDict:
    structureDict[x] = '?'

print "Repeated structures dictionary : "
print structureDict


helix = open('data/helix.txt', 'r+')
beta = open('data/beta.txt', 'r+')
loop = open('data/loop.txt', 'r+')
helixArff = open('data/helix_small.arff', 'w')
betaArff = open('data/beta_small.arff', 'w')
loopArff = open('data/loop_small.arff', 'w')

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
    aaSet = (set(line))
    for aa in aaSet:
        lineDict[aa] = 'yes'
    lineDict = str(collections.OrderedDict(sorted(lineDict.items())).values())
    lineDict = lineDict[1:-1].replace("'","")
    helixArff.write( lineDict + '\n')
    TID += 1

TID=1
for line in beta:
    lineDict = structureDict.copy()
    line = line.rstrip()
    aaSet = (set(line))
    for aa in aaSet:
        lineDict[aa] = 'yes'
    lineDict = str(collections.OrderedDict(sorted(lineDict.items())).values())
    lineDict = lineDict[1:-1].replace("'","")
    betaArff.write( lineDict + '\n')
    TID += 1

TID=1
for line in loop:
    lineDict = structureDict.copy()
    line = line.rstrip()
    aaSet = (set(line))
    for aa in aaSet:
        lineDict[aa] = 'yes'
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
