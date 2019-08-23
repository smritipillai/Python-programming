try:
    t = int(input())
    while t!=0:
        n = int(input())
        sum = 1
        if n==0:
                print("1")
                break
        else:
            for i in range(1,n+1):
                sum = sum * i
                t = t-1
        print(sum)
except EOFError as e : pass

