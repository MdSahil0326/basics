    def totaloccurence(g,target):
    n=len(g)
    result=0
    for i in range(n):
      if g[i]==target:
          result=result+1
    return result      
g=[10,20,30,20,20,66]
target=20
result=totaloccurence(g,target)
print("count",result)

e=[10,20,33,44,55,66,44]
t=44
r=totaloccurence(e,t)
print("count",r)
