# Naloga 5: Konjske dirke
# Martin Dolenc, 27161078
# matematika, 3. letnik
#
# naloga: https://putka-upm.acm.si/tasks/t/konjske_dirke/

n = int(input())
poljaFigur = []
zacetnoPoljeKonja = ()
for i in range(n):
    vrstica = input()
    for j in range(n):
        if vrstica[j] == "#":
            poljaFigur.append((i+1, j+1))
        elif vrstica[j] == "*":
            zacetnoPoljeKonja = (i+1, j+1)

steviloPoljKiJihMoramoDoseci = int(input())
koordinatePolj = [tuple(map(int, input().split())) for i in range(steviloPoljKiJihMoramoDoseci)]
slovarKoordinat = {i:-1 for i in koordinatePolj}

mozniSkoki = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]   # vse možne poteze

nedostopnaPolja = []
novaPolja = [zacetnoPoljeKonja]
stevecKorakov = 0
while len(novaPolja) != 0:
    stevecKorakov += 1
    accNovihPolj = []
    for koordinate in novaPolja:
        for skok in mozniSkoki:
            polje = (koordinate[0] + skok[0], koordinate[1] + skok[1])
            if 0 < polje[0] < n + 1 and 0 < polje[1] < n + 1:                   # poglej če smo v polju
                if polje not in poljaFigur and polje not in nedostopnaPolja:     # poglej če je polje zasedenu
                    if polje in slovarKoordinat:
                        slovarKoordinat[polje] = stevecKorakov
                    accNovihPolj.append(polje)
                    nedostopnaPolja.append(polje)
    novaPolja = accNovihPolj.copy()
    accNovihPolj.clear()

for i in koordinatePolj:
    print(slovarKoordinat[i])
