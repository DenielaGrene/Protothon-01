import itertools
s='ProtoSem'
for j in range(0, len(s)+1):
    t=list(itertools.permutations(s,j))
    for i in range(0,len(t)):
        print (''.join(t[i]))