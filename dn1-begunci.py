# Naloga 1: Begunci
# Martin Dolenc, 27161078
# matematika, 3. letnik
#
# naloga: https://putka-upm.acm.si/tasks/t/begunci/

n, p = map(int, input().split())
kapacitetaCentrov = list(map(int, input().split()))
stevilkeBeguncev = list(map(int, input().split()))
rez = [0]*p

for i in range(1, n):
    kapacitetaCentrov[i] += kapacitetaCentrov[i-1]

z = 0
for j in range(p):
    k = stevilkeBeguncev[j] ^ z
    a = 0
    b = n-1
    while b-a > 1:
        if (kapacitetaCentrov[(a+b)//2] > k):
            b = (a+b)//2
        else:
            a = (a+b)//2
    else:
        if (kapacitetaCentrov[a] >= k):
            y = a
        else:
            y = b
        while kapacitetaCentrov[y] == kapacitetaCentrov[y-1] and y > 0:
            y -= 1
        else:
            rez[j] = y+1
    z = rez[j]

print(" ".join(map(str, rez)))
