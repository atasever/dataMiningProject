__author__ = 'M. Umut ATASEVER'

from sets import Set

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


helix = []
loop = []
beta = []

allHelixPatterns = []
allLoopPatterns = []
allBetaPatterns = []

allHelixPatternReader = open('data/helix.txt', 'r+')
allLoopPatternReader = open('data/loop.txt', 'r+')
allBetaPatternReader = open('data/beta.txt', 'r+')

for line in allHelixPatternReader:
    line = line.rstrip()
    allHelixPatterns.append(line)

for line in allLoopPatternReader:
    line = line.rstrip()
    allLoopPatterns.append(line)

for line in allBetaPatternReader:
    line = line.rstrip()
    allBetaPatterns.append(line)



helixReader = open('results/helix_apriori_small_set_permutations.txt', 'r+')
loopReader = open('results/loop_apriori_small_set_permutations.txt', 'r+')
betaReader = open('results/beta_apriori_small_set_permutations.txt', 'r+')

for line in helixReader:
    line = line.rstrip()
    atoms = line.split(' ')
    helix.append(atoms[0])

for line in loopReader:
    line = line.rstrip()
    atoms = line.split(' ')
    loop.append(atoms[0])

for line in betaReader:
    line = line.rstrip()
    atoms = line.split(' ')
    beta.append(atoms[0])

onlyHelix = (Set(helix)-Set(loop)) - Set(beta)
onlyLoop = (Set(loop)-Set(helix)) - Set(beta)
onlyBeta = (Set(beta)-Set(loop)) - Set(helix)

helixAndBeta = (Set(helix) & Set(beta))
loopAndBeta = (Set(loop) & Set(beta))
loopAndHelix = (Set(helix) & Set(loop))

commonPatterns = (Set(helix) & Set(beta) & Set(loop))

onlyHelixSubstracted = Set([])
onlyLoopSubstracted = Set([])
onlyBetaSubstracted = Set([])

for pattern in onlyHelix:
    for p in allLoopPatterns:
        if isInString(p,pattern):
            onlyHelixSubstracted.add(pattern)
    for p in allBetaPatterns:
        if isInString(p,pattern):
            onlyHelixSubstracted.add(pattern)

print "only Helix : " ,len(onlyHelix),len(onlyHelixSubstracted)

for pattern in onlyLoop:
    for p in allHelixPatterns:
        if isInString(p,pattern):
            onlyLoopSubstracted.add(pattern)
    for p in allBetaPatterns:
        if isInString(p,pattern):
            onlyLoopSubstracted.add(pattern)

print "only Loop : " ,len(onlyLoop),len(onlyLoopSubstracted)

for pattern in onlyBeta:
    for p in allLoopPatterns:
        if isInString(p,pattern):
            onlyBetaSubstracted.add(pattern)
    for p in allHelixPatterns:
        if isInString(p,pattern):
            onlyBetaSubstracted.add(pattern)

print "only Beta : " ,len(onlyBeta),len(onlyBetaSubstracted)

print "Patterns common in beta and helix structures : ", len(helixAndBeta)
print "Patterns common in beta and loop structures : ", len(loopAndBeta)
print "Patterns common in loop and helix structures : ", len(loopAndHelix)

print "Patterns common in loop, beta and helix structures : ", len(commonPatterns)
