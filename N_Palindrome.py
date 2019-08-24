n = int(input())
t = n
r = 0
if n<10:
    if n==2 or n==3 or n==5 or n==7:
        print("Yes")
    else:
        print("No")
else:
    while t!=0:
        r = r*10 + t%10
        t = int(t/10)  
    if r == n:
        for i in range(2,n):  
            if (n % i) == 0:  
                flag=0   #no
                break  
            else:  
                flag=1  #yes
        if flag==0:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
