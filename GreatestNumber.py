def findthegreatest(number):
    result=0
    n=len(number)

    for i in range(n):
        if number[i]>result:
            result=number[i]

    return result

number=[12,88,66,77,100,55,3,22,33,77]
result=findthegreatest(number)
print("Greatest number in the List is:",result)
