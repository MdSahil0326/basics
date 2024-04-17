g=[10,20,30,20,20,66]
def EvenNumber(g):
    n=len(g)
    result=0
    for i in range(n):
      if g[i]%2==0:
          result=result+1
    return result      
result=EvenNumber(g)
print("Even numbers present in list:",result)


e=[10,20,33,44,55,66,44]
r=EvenNumber(e)
print("Even numbers present in list:",r)
