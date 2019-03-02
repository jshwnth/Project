def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y)
    return x//y

a,b=int(input().split())

print('1.add/n 2.sub/n 3.mul/n 4.div /n')
c=int(input())

if c==1:
    print(add(a,b))
elif c==2:
    print(sub(a,b))
elif c == 3:
    print(mul(a, b))
elif c==4:
    print(div(a,b))
