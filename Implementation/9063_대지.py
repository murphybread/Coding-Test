N=int(input())


if N <=1:
    print(0)a
    X,Y = map(int,input().split())
    
    mx=X
    Mx =X
    my=Y
    My=Y
    
    for _ in range(N-1):
        X,Y = map(int,input().split())
        if X < mx :
            mx = X
        if X > Mx:
            Mx =X
        if Y < my :
            my = Y
        if Y > My:
            My = Y
    print(( Mx-mx) * (My-my))
        
            