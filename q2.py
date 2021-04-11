for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    if sum(a)>=100:
        print("Yes")
    else:
        print("No")
