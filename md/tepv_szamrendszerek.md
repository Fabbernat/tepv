# Tehetségkutató Egyetemi Programozási Verseny 3. forduló – 2024/25
## Számrendszerek
Bob baba a bölcsődében a számrendszerekről tanult. A kedvenc számjegye a `9`, ezért például a `10`-es
számrendszerben felírt `203433` szám eddig nem érdekelte különösebben, mert nem tartalmaz `9`-es
számjegyet. Azonban most már tudja, hogy ha `16`-os számrendszerben írja fel ugyanezt a számot, akkor
`31AA9` adódik (ahol A jelöli a `10`-es számjegyet), ami már tartalmaz `9`-est. Sőt, ha `12`-es számrendszerben írja fel, akkor már `99889` érték adódik, ami három darab `9`-es számjegyet tartalmaz.

Bob babát így most az érdekli általánosan, hogy ha adott egy `10`-es számrendszerben felírt `N` szám,
és egy (számrendszertől független) D kedvenc számjegy, akkor a számrendszer megfelelő megválasztásával legfeljebb hány darab `D`-s számjegyet tartalmazhat az N átírt alakja. Például belátható, hogy
`N = 203433` és `D = 9` esetén a három előfordulás maximális is.

Írj programot, ami `N` és `D` ismeretében kiszámítja a választ Bob baba kérdésére
## Bemenet
A standard bemenet első és egyetlen sorában `N` és `D` pozitív egészek találhatóak.



## Kimenet
Astandard kimenetre egy sort kell írni egyetlen számmal, a D előfordulásainak maximális számát az N egy megfelelő számrendszerben felírt alakjában.
Csak a 2 vagy annál nagyobb alapú számrendszereket kell figyelembe venni!


### Példa

#### Bemenet1
203433 9
#### Kimenet1
3

#### Bemenet2
48899 4
####  Kimenet2
2

### Korlátok
1 ≤ N, D ≤ 1018.


**Időlimit**: 2.0 s
**Memórialimit**:  256 MB
### Pontozás
A megoldásodat sok különböző tesztesetre lefuttatjuk. A tesztesetek részfeladatokba vannak csoportosítva. Egy-egy részfeladatot akkor tekintünk megoldottnak, ha volt legalább egy olyan beadásod, amely
az adott részfeladat minden tesztesetére helyes megoldást adott. A feladat összpontszámát a megoldott
részfeladatokra kapott pontszámok összege adja.

```table
Részfeladat Korlátok Pontszám
0 a minta 0
1 1 ≤ N, D ≤ 106 40
2 1 ≤ N, D ≤ 1012 30
3 nincsenek további megkötések 30
```
