import math as m


total = 0

def maclaurin(n):
    x = 0.3*m.pi
    return ((-1)**n)*((x**(2*n + 1)) / m.factorial(2*n + 1))

for i in range(0,9) :
    total = total + maclaurin(i)

print(total)
