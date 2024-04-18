print("starting line")
a=[11,12,13]
try:
    print(y)
except  ZeroDivisionError:
    print("Exceptoin raised due to zero division error")
except IndexError:
    print("Exception raised due to index error")
except NameError:
    print("Exception rasied due to undefined variable")
except:
    print("Some exception raised")
else:
    print("NO exception raised ,everything worked perfectly")
finally:
    print("this is a final block")
print("outside the try block")        
