m=input()
alp=dict()
alp['c=']=0
alp['c-']=0
alp['dz=']=0
alp['d-']=0
alp['lj']=0
alp['nj']=0
alp['s=']=0
alp['z=']=0
xnt=0

for i in alp:
  alp[i]=m.count(i)
  xnt+=m.count(i)

print(len(m)-xnt)