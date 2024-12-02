from collections import Counter
a,b = [],[]
# Open file and iterate to feed lists with values
with open('distancias.txt','r') as f:
    for line in f.readlines():
        x,y = (int(z) for z in line.split())
        a.append(x)
        b.append(y)

# Sort lists, and get length for future loops
a.sort()
b.sort()
n=len(a)

# First answer, with the absolute values of the diferences between list rows.
print('Primer reto')
print (sum(abs(a[i]-b[i]) for i in range(n)))
print('\n')

# Second answer, getting the counter of second list to iterate with values from first list.
c=Counter(b)
resp=0
for i in range(n):
    resp += a[i]*c[a[i]]
print('Segundo reto')
print(resp)
