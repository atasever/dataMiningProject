import math

allHelix = open('results/helix_apriori_small_set_permutations.txt', 'r+')
allLoop = open('results/loop_apriori_small_set_permutations.txt', 'r+')
allBeta = open('results/beta_apriori_small_set_permutations.txt', 'r+')

total = 0

for line in allHelix:
    line = line.rstrip()
    atoms = line.split(' ')
    #print atoms[0],atoms[1]
    total = total + int(atoms[1])

allHelix = open('results/helix_apriori_small_set_permutations.txt', 'r+')

entropy = 0.0

for line in allHelix:
    line = line.rstrip()
    atoms = line.split(' ')
    norm = float(int(atoms[1])) / total
    #print atoms[0],atoms[1],norm
    entropy = entropy + norm * math.log(norm)

print "Helix Entropy: ",entropy * -1.0







total = 0

for line in allBeta:
    line = line.rstrip()
    atoms = line.split(' ')
    #print atoms[0],atoms[1]
    total = total + int(atoms[1])

allBeta = open('results/beta_apriori_small_set_permutations.txt', 'r+')

entropy = 0.0

for line in allBeta:
    line = line.rstrip()
    atoms = line.split(' ')
    norm = float(int(atoms[1])) / total
    #print atoms[0],atoms[1],norm
    entropy = entropy + norm * math.log(norm)

print "Beta Entropy: ",entropy * -1.0




total = 0

for line in allLoop:
    line = line.rstrip()
    atoms = line.split(' ')
    #print atoms[0],atoms[1]
    total = total + int(atoms[1])

allLoop = open('results/loop_apriori_small_set_permutations.txt', 'r+')

entropy = 0.0

for line in allLoop:
    line = line.rstrip()
    atoms = line.split(' ')
    norm = float(int(atoms[1])) / total
    #print atoms[0],atoms[1],norm
    entropy = entropy + norm * math.log(norm)

print "Loop Entropy: ",entropy * -1.0















allHelix = open('results/helix_chemical_apriori_small_set_permutations.txt', 'r+')
allLoop = open('results/loop_chemical_apriori_small_set_permutations.txt', 'r+')
allBeta = open('results/beta_chemical_apriori_small_set_permutations.txt', 'r+')

total = 0

for line in allHelix:
    line = line.rstrip()
    atoms = line.split(' ')
    #print atoms[0],atoms[1]
    total = total + int(atoms[1])

allHelix = open('results/helix_chemical_apriori_small_set_permutations.txt', 'r+')

entropy = 0.0

for line in allHelix:
    line = line.rstrip()
    atoms = line.split(' ')
    norm = float(int(atoms[1])) / total
    #print atoms[0],atoms[1],norm
    entropy = entropy + norm * math.log(norm)

print "Helix Chemical Class Entropy: ",entropy * -1.0







total = 0

for line in allBeta:
    line = line.rstrip()
    atoms = line.split(' ')
    #print atoms[0],atoms[1]
    total = total + int(atoms[1])

allBeta = open('results/beta_chemical_apriori_small_set_permutations.txt', 'r+')

entropy = 0.0

for line in allBeta:
    line = line.rstrip()
    atoms = line.split(' ')
    norm = float(int(atoms[1])) / total
    #print atoms[0],atoms[1],norm
    entropy = entropy + norm * math.log(norm)

print "Beta Chemical Class Entropy: ",entropy * -1.0




total = 0

for line in allLoop:
    line = line.rstrip()
    atoms = line.split(' ')
    #print atoms[0],atoms[1]
    total = total + int(atoms[1])

allLoop = open('results/loop_chemical_apriori_small_set_permutations.txt', 'r+')

entropy = 0.0

for line in allLoop:
    line = line.rstrip()
    atoms = line.split(' ')
    norm = float(int(atoms[1])) / total
    #print atoms[0],atoms[1],norm
    entropy = entropy + norm * math.log(norm)

print "Loop Chemical Class Entropy: ",entropy * -1.0
