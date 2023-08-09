N= int(input())


def s (n):
    if n !=N:
        print(n)
        return s(n+1)
    else:
        print(N)

s(1)