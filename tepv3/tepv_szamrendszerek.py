def f(n,b,d):
    c=0
    while n>0:
        if n%b==d:
            c+=1
        n//=b
    return c

def main():
    n,d=map(int,input().split())
    m=0
    for b in range(max(2,d+1),min(n+1,10**6)+1):
        if d>=b:
            continue
        m=max(m,f(n,b,d))
    print(m)

if __name__=="__main__":
    main()