# Naloga 6: Glasovanje
# Martin Dolenc, 27161078
# matematika, 3. letnik
#
# naloga: https://putka-upm.acm.si/tasks/t/glasovanje/

n, m = map(int, input().split())

stevilo_poslancev = list(map(int, input().split()))
stalisce = list(map(int, input().split()))
pogodbe = list(range(n))
vseh = sum(stevilo_poslancev)


def Najdi_Ali_Vstavi(x):
    if pogodbe[x] == x:
        return x
    pogodbe[x] = Najdi_Ali_Vstavi(pogodbe[x])
    return pogodbe[x]

for i in range(m):
    l = list(map(Najdi_Ali_Vstavi, [int(x) - 1 for x in input().split()]))

    if len(l) == 2:
        if l[0] != l[-1]:
            pogodbe[l[-1]] = l[0]
            stevilo_poslancev[l[0]] += stevilo_poslancev[l[-1]]
    else:
        if stalisce[l[-1]] - stalisce[l[-2]] == 0:      # spremeni vse na [-2]
            novo_stalisce = stalisce[l[-2]]
        else:                                           # spremeni vse na [0]
            novo_stalisce = stalisce[l[0]]

        for stranka in l:
            stalisce[stranka] = novo_stalisce

za = 0
for i in range(n):
    if pogodbe[i] == i:
        za += stalisce[pogodbe[i]]*stevilo_poslancev[i]

print(za, vseh - za)
