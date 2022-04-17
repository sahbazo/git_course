import math as m

def bisection(x):
    return m.log(x) - m.cos(x) - m.exp(-x)

a = 1
b = 2
c = 0


f = bisection(2)

if not (f > 0.0005 or f < - 0.0005):
    print(b)
else: 
    while f > 0.0005 or f < - 0.0005 :
        c = (a + b) / 2
        f = bisection(c)
        if f > 0 :
            b = c
        elif f < 0 :
            a = c
        else:
            print(c)
            break
        
        print('f=', f, 'c=', c)


    
