a=int(input())
lt=[]
ct=0
while(a!=-1):
  lt=[]
  ct=0
  for i in range(1,a):
    if(a%i==0):
      lt.append(i)

  if(a==sum(lt)):
    print(a,'=',end=' ')
    for i in range(len(lt)-1):
      print(lt[i], '+',end=' ')
    print(lt[len(lt)-1])
  else:
    print(a , "is NOT perfect.")
  a=int(input())