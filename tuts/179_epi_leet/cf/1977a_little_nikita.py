
for s in[*open(0)][1:]:
    n,m=map(int,s.split())
    print('YNeos'[n-m&1or n<m::2])


