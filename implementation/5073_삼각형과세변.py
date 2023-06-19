A,B,C = map(int , input().split())
M = max(A,B,C)
rest = A+B+C-M

while A!=0 and B!=0 and C!=0:
    if M >=rest:
        print("invalid")
    elif A==B==C:
        print("Equilateral")
    elif A==B or B==C or A==C:
        print("Isosceles")
    elif A!=B!=C:
        print("Scalene")
    A,B,C = map(int , input().split())
    M =max(A,B,C)
    rest = A+B+C-M