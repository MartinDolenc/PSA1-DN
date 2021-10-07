# Naloga 4: Lov na zaklad
# Martin Dolenc, 27161078
# matematika, 3. letnik
#
# naloga: https://putka-upm.acm.si/tasks/t/zakladi/

import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
graf = [[] for _ in range(n)]
for i in range(m):
    l = list(map(int, input().split()))
    graf[l[0]-1].append((l[1]-1, l[2]))

def dodaj_v_sort_graf(krizisce):        # narejeno po psevdo kodi
    global stevec

    steviloKorakov[krizisce] = stevec
    najmanjseSteviloKorakov[krizisce] = stevec
    zbiralnik.append(krizisce)
    aliSmoZeObdelaliKrizisce[krizisce] = True
    stevec += 1

    for x, y in graf[krizisce]:
        if steviloKorakov[x] == -1:                  # izračunaj za povezavo če še ni bila
            dodaj_v_sort_graf(x)
            najmanjseSteviloKorakov[krizisce] = min(najmanjseSteviloKorakov[krizisce], najmanjseSteviloKorakov[x])
        elif aliSmoZeObdelaliKrizisce[x]:
            najmanjseSteviloKorakov[krizisce] = min(najmanjseSteviloKorakov[krizisce], steviloKorakov[x])

    if najmanjseSteviloKorakov[krizisce] == steviloKorakov[krizisce]:
        acc = []
        while True:
            w = zbiralnik.pop()
            aliSmoZeObdelaliKrizisce[w] = False
            acc.append(w)
            if w == krizisce:
                break
        sortiranGraf.append(acc)


stevec = 0
zbiralnik = []
aliSmoZeObdelaliKrizisce = [False]*n
najmanjseSteviloKorakov = [n+1]*n
steviloKorakov = [-1]*n
sortiranGraf = []     # topološko bomo sortirali graf vzvratno

for i in range(n):
    if steviloKorakov[i] == -1:
        dodaj_v_sort_graf(i)

indexPojavitve = [-1]*n
for i in range(len(sortiranGraf)):
    for j in sortiranGraf[i]:
        indexPojavitve[j] = i

# Izračunamo krožišča in povezave na pojavitvah

vrednostiKrozisc = [0]*len(sortiranGraf)
povezaveKriziscaPojavitve = [[] for _ in range(len(sortiranGraf))]
for x in range(n):
    for y, z in graf[x]:
        if indexPojavitve[x] == indexPojavitve[y]:            # sta skupaj v krožišču
            vrednostiKrozisc[indexPojavitve[x]] += z
        else:
            povezaveKriziscaPojavitve[indexPojavitve[x]].append((indexPojavitve[y], z))

maximumiKrizisc = [0]*len(sortiranGraf)
for x in range(len(sortiranGraf)):
    for y, z in povezaveKriziscaPojavitve[x]:
        maximumiKrizisc[x] = max(maximumiKrizisc[x], maximumiKrizisc[y] + z)
    maximumiKrizisc[x] += vrednostiKrozisc[x]

for i in range(n):
    print(maximumiKrizisc[indexPojavitve[i]])
