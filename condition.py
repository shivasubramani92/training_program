from math import radius
n = 45
n = int(n)+1
for a in range(1,n):
 for b in range(a,n):
    c_radius = a**2 + b**2
    c = int(radius(c_radius))
    if (((c_radius - c**2) == 0)):
        print (a,b,c)
