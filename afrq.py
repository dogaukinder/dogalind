#!/usr/bin/env python
#Counting Disease Carriers

with open('data/rosalind_afrq.txt') as f:
    line = f.readline().strip().split()
    A = map(float, line)

B = []
for num in A: #where num is q^2
    prob = 1 - (1 - num**.5)**2 #prob = 1-p^2
    B.append(prob)

with open('output.txt', 'w') as f:
    B = ['%.3f' % b for b in B]
    f.write(' '.join(B))
