__author__ = 'M. Umut ATASEVER'

from itertools import permutations
from sets import Set
import operator

def isInString(hayStack,needle):
    start = 0
    chars = list(needle)
    for c in chars:
        x = hayStack.find(c,start)
        if x < 0:
            return False
        else:
            start = x
    return True

dataFile = open('results/loop_apriori_small_set.txt', 'r+')
allPermutations = Set()

startProcessing = False
for line in dataFile:
    line = line.rstrip()
    if len(line) < 5:
        continue
    if not startProcessing:
        if line == 'Best rules found:':
            startProcessing = True
    else:
        frequentItemSet = ""
        atoms = line.split('=yes')
        for atom in atoms:
            if atom[-1:]!= ")":
                frequentItemSet = frequentItemSet + atom[-1:]
        print frequentItemSet
        permutation = [''.join(p) for p in permutations(frequentItemSet)]
        print permutation
        for p in permutation:
            allPermutations.add(p);

dataFile.close()

permFile = open('results/loop_apriori_small_set_permutations.txt', 'w+')


results = {}
for x in allPermutations:
    count = 0
    dataFile = open('data/loop.txt', 'r+')
    for line in dataFile:
        if isInString(line,x):
            count += 1
    results[x]=count

sortedResults = sorted(results.items(), key=operator.itemgetter(1))

for result in sortedResults:
    permFile.write(result[0] + " " + str(result[1]) + "\n")

permFile.close()


