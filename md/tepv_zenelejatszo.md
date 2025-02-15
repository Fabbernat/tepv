# Tehetségkutató Egyetemi Programozási Verseny 3. forduló – 2024/25
## Zenelejátszó
Viktor nem igazán rendszerezi a zenéit kedvenc lejátszó programjában. Egyetlen lejátszási listája van,
mely kezdetben üres. Ha új számot ad hozzá a listához, azt mindig a lista legelejére teszi. Ha megunt egy
zeneszámot és törli azt a listáról, akkor a számok sorrendje nem változik meg, csak kikerül a zeneszám
a listából. Ugyanazt a számot később ismét felveheti a listára, ekkor ismét a lista legelejére kerül fel az
adott szám.

Ha zenét szeretne hallgatni, akkor mindig a lista legelső számától kezdi a lejátszást, majd valahány percig
megszakítás nélkül hallgatja a zenét. Ha sokáig hallgat zenét és már minden szám befejeződött a listáról,
a lejátszó visszamegy a lista elejére, és onnan folytatja a lejátszást.

A feladatod, hogy nyilvántartsd Viktor lejátszási listáját és időnként válaszolj egy kérdésére, ami arra
vonatkozik, hogy egy adott zeneszámot eddig hányszor hallgatott meg összesen. Egy zeneszámot akkor
tekintünk meghallgatottnak, ha az elejétől a végéig meghallgatta megszakítás nélkül.
## Bemenet
A `standard bemenet` első sorában egy `Q` pozitív egész található, a műveletek darabszáma. Ezt `Q`
művelet leírása követi.

Minden további sor egy művelet leírását tartalmazza, mely az alábbi három típus valamelyike:

• Ha a sor első karaktere P, akkor lejátszás művelet következik. A sor egy további pozitív egészet
tartalmaz, a lejátszás időtartamát (percben).

• Ha a sor első karaktere L, akkor ezt egy zeneszám címét megadó karakterlánc és a zeneszám
hosszát (percben) megadó pozitív egész érték követi. Ha a zeneszám jelenleg nincs a listában,
akkor felkerül a lista elejére, ha rajta van a listán, akkor törlésre kerül.

• Ha a sor első karaktere Q, akkor ezt egy zeneszám címét megadó karakterlánc követi. A művelet
egy lekérdezés, amire válaszul azt kell megadni, hogy eddig összesen hány alkalommal került
meghallgatásra az adott zeneszám.

## Kimenet
A standard kimenetre egy sort kell írni minden olyan művelethez, aminek azonosítója Q.
Minden sor a megadott zeneszám meghallgatásainak darabszámát tartalmazza a művelet hívásakor.
### Példa
#### Bemenet1
3
L roundabout 509
P 7200
Q roundabout
#### Kimenet1
14
#### Bemenet2
8
L uufo 239
L ghoul 271
L ghost 349
P 858
P 619
P 9139
L mystery_circles_ultra 239
Q ghoul
####  Kimenet2
11
#### Bemenet3
13
Q nymphis_fae
L spider_dance 106
L crab_rave 256
P 824
L alchemy 300
L crab_rave 256
P 1000
Q crab_rave
L infestation 274
L sea_shanty_two 128
L crab_rave 256
P 1577
Q crab_rave
#### Kimenet3
0
2
4
### Korlátok
1 ≤ Q ≤ 500 000.

A zeneszámok címei csak az angol ábécé kisbetűiből és aláhúzás karakterből (_) állnak.

A zeneszámok címeinek összhossza az inputban legfeljebb 2 000 000 karakter.

Minden zeneszámot egyértelműen azonosít a címe.

A zeneszámok hossza 1 és 109 közti egész szám.

Minden P műveletnél a lista legalább egy zeneszámot tartalmaz.

Minden P műveletnél a lejátszás időtartama 1 és 109 közti egész szám.

**Időlimit**: 5.0 s
**Memórialimit**: 1024 MB
### Pontozás
A megoldásodat sok különböző tesztesetre lefuttatjuk. A tesztesetek részfeladatokba vannak csoportosítva. Egy-egy részfeladatot akkor tekintünk megoldottnak, ha volt legalább egy olyan beadásod, amely
az adott részfeladat minden tesztesetére helyes megoldást adott. A feladat összpontszámát a megoldott
részfeladatokra kapott pontszámok összege adja.
```table
Részfeladat Korlátok Pontszám
0 a minta 0
1 Q ≤ 1000, nincs törlés művelet, minden zene hossza 1 perc 20
2 Q ≤ 1000, nincs törlés művelet 20
3 nincs törlés művelet 30
4 nincsenek további megkötések 30
```
