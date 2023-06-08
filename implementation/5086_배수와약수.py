A,B = map(int,input().split())

while A!=0 and B!=0:
    
    if int(B%A) == 0 :
        print("factor")
    elif int(A%B) == 0  :
        print("multiple")
    else:
        print("neither")
    A,B = map(int,input().split())
        