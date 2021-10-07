# Naloga 2: Beli
# Martin Dolenc, 27161078
# matematika, 3. letnik
#
# naloga: https://putka-upm.acm.si/tasks/t/beli/

from bisect import bisect_left

def does_sorted_list_contain(a, b):     # iskanje z pomočjo bisekcije
    if len(a) != 0:
        x = bisect_left(a, b)
        return x != len(a) and a[x] == b
    else:
        return False

w, h, k = map(int, input().split())
crnaPolja = [list(map(int, input().split())) for i in range(k)]

#######################################################################

steviloBelihBlokov = w+h

if w == 1 or h == 1:
    steviloBelihBlokov = 1

trenutniStolpec = 1
if k != 0:
    trenutniStolpec = crnaPolja[0][0]

visinaPrejsnjegaPolja = 0
prejsnjaEnaKratEnaPolja = []
enaKratEnaPolja = []

if h == 1 and trenutniStolpec == 2:     # edge case
    prejsnjaEnaKratEnaPolja = [1]

zadnjiPojavVvrstici = [0]*h
crnaPolja.sort()

#######################################################################

for i in range(0, k):
    if crnaPolja[i][0] != trenutniStolpec:  # nov stolpec
        if h != 1:
            if h - visinaPrejsnjegaPolja == 0:  # gledamo konec prejšnega stolpca (oziroma razlika gor)
                steviloBelihBlokov -= 1
            elif h - visinaPrejsnjegaPolja == 1:
                steviloBelihBlokov -= 1
                enaKratEnaPolja.append(visinaPrejsnjegaPolja + 1)

        if crnaPolja[i][0] - trenutniStolpec == 1:
            prejsnjaEnaKratEnaPolja = enaKratEnaPolja.copy()
        else:
            prejsnjaEnaKratEnaPolja.clear()

        enaKratEnaPolja.clear()
        trenutniStolpec = crnaPolja[i][0]
        visinaPrejsnjegaPolja = 0               # resetiramo višino

    # tu teče za vsako polje

    razlikaDol = crnaPolja[i][1] - visinaPrejsnjegaPolja
    razlikaLevo = crnaPolja[i][0] - zadnjiPojavVvrstici[crnaPolja[i][1]-1]

    if razlikaDol == 2:
        enaKratEnaPolja.append(crnaPolja[i][1] - 1)
    elif razlikaDol != 1:
        steviloBelihBlokov += 1

    if razlikaLevo == 2:
        if does_sorted_list_contain(prejsnjaEnaKratEnaPolja, crnaPolja[i][1]):
            steviloBelihBlokov += 1
    elif razlikaLevo != 1:
        steviloBelihBlokov += 1

    zadnjiPojavVvrstici[crnaPolja[i][1]-1] = crnaPolja[i][0]
    visinaPrejsnjegaPolja = crnaPolja[i][1]

if h != 1:
    if h - visinaPrejsnjegaPolja == 0:      # gledamo konec zadnjega stolpca
        steviloBelihBlokov -= 1
    elif h - visinaPrejsnjegaPolja == 1:
        steviloBelihBlokov -= 1
        enaKratEnaPolja.append(visinaPrejsnjegaPolja + 1)

if w != 1:                                  # gledamo konce vrstic
    for i in range(0, h):
        if w - zadnjiPojavVvrstici[i] < 2:
            steviloBelihBlokov -= 1

counter = 0                                 # counter za ugotoviti koliko enaKratEnaPolji je fake (oziroma razlika desno)
for i in range(0, len(enaKratEnaPolja)):
    if w - zadnjiPojavVvrstici[enaKratEnaPolja[i]-1] != 1:
        counter += 1

steviloBelihBlokov += len(enaKratEnaPolja) - counter
print(steviloBelihBlokov)
