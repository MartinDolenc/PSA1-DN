# Naloga 3: Jame
# Martin Dolenc, 27161078
# matematika, 3. letnik
#
# naloga: https://putka-upm.acm.si/tasks/t/jame/

n, m = map(int, input().split())
povezave = [list(map(int, input().split())) for i in range(n)]

indexTrenutneJame = -1
trenutniKorak = 0
zeObiskaneJame = [0]

for i in range(0, m):
    indexTrenutneJame = -1
    if zeObiskaneJame[indexTrenutneJame] == m:      # prišli smo v jamo z zakladom
        break
    else:
        x = 0
        y = povezave[zeObiskaneJame[indexTrenutneJame]].index(1)
        while zeObiskaneJame.__contains__(y):
            x = y
            try:
                y = povezave[zeObiskaneJame[indexTrenutneJame]].index(1, x+1)    # throw exception vrnemo se nazaj
            except ValueError:
                indexTrenutneJame -= 1
                y = povezave[zeObiskaneJame[indexTrenutneJame]].index(1)
        else:
            zeObiskaneJame.append(y)
            trenutniKorak += 1

if zeObiskaneJame[-1] != m:
    print("Lipko")
elif trenutniKorak < m:
    print("Jamko")
else:
    print("Nihce")