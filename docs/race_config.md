# Sprint oppsett - kjøreplan og seeding
Denne siden beskriver regelsett for sprint-oppsettet. Alle løpere starter direkte i en kvartfinale og går så videre til neste runde i henhold til oppsettet nedenfor.

Eksempel fra rad 3: Dette gjelder for maks 32 og minimum 25 løpere - 4 kvartfinaler hvor de 4 beste går til semi A og øvrige går til semi C. Det er 2 semi A hvor de 4 beste går til finale A og 4 neste til finale B. Det er 2 semi C hvor de 4 beste går til finale C, resten er ute. Det er 3 finaleheat (A, B og C)

Normalt ønsker vi 8 løpere pr heat, men i noen tilfeller kan det bli 9. Dette kan unngås ved å bruke alternativt oppsett (markert med alt) - det alternative oppsettet har noen flere heat og dermed også flere heat med under 6 deltakere. 

* 64 løpere er anbefalt maksimum antall løpere.

### Oppsett - antall heat styres av antall påmeldte i løpsklassen
<table border=1>
  <tr>
    <td>Max racers</td><td>Q count</td><td>Q rule</td><td>SA count</td><td>SA rule</td><td>SC count</td><td>SC rule</td><td>F count</td>
  </tr>
  <tr>
    <td>7</td><td>1</td><td>All to FA</td><td>0</td><td></td><td>0</td><td></td><td>1</td>
  </tr>
  <tr>
    <td>16</td><td>2</td><td>4 FA, 4 FB, rest out</td><td>0</td><td></td><td>0</td><td></td><td>2</td>
  </tr>
  <tr>
    <td>24</td><td>3</td><td>5 to SA, rest to FC</td><td>2</td><td>4 FA, 4 FB, rest out</td><td>0</td><td></td><td>3</td>
  </tr>
  <tr>
    <td>32</td><td>4</td><td>4 to SA, rest to SC</td><td>2</td><td>4 FA, 4 FB, rest out</td><td>2</td><td>4 FC, rest out</td><td>3</td>
  </tr>
  <tr>
    <td>40</td><td>6</td><td>4 to SA, rest to SC</td><td>4</td><td>2 FA, 2 FB, rest out</td><td>2</td><td>4 FC, rest out</td><td>3</td>
  </tr>
  <tr>
    <td>48</td><td>6</td><td>4 to SA, rest to SC</td><td>4</td><td>2 FA, 2 FB, rest out</td><td>4</td><td>2 FC, rest out</td><td>3</td>
  </tr>
  <tr>
    <td>56</td><td>7</td><td>4 to SA, rest to SC</td><td>4</td><td>2 FA, 2 FB, rest out</td><td>4</td><td>2 FC, rest out</td><td>3</td>
  </tr>
  <tr>
    <td>64</td><td>8</td><td>4 to SA, rest to SC</td><td>4</td><td>2 FA, 2 FB, rest out</td><td>4</td><td>2 FC, rest out</td><td>3</td>
  </tr>
</table>

### Seeding av løpere
Seeding utføres etter følgende prinsipp:
1. Kvalifisering / kvartfinaler: Ingen automatisk seeding i systemet - manuell seeding kan gjøres. Bruk funksjonen "Utfør seeding" på Arrangement-siden.
2. Semifinaler: Løperne rangeres basert på resultater i kvalifisering. Vinner av heat 1 får rank 1, vinner av heat 2 får rank 2 osv. Deretter fordeles løperne etter følgende nøkkel: rank 1 får posisjon 1 i semifinale 1, rank 2 får posisjon 1 i semifinale 2, rank 3 får posisjon 1 i semifinale 3 osv.

Merknader:
- I klasser der seeding gjennomføres basert på cup-stilling i lokale/regionale cup-er forbeholder arrangøren seg retten til innplassere "utenbys" løpere i heat etter avtale med TD.
- Fremtidig løsning for seeding til kvalifisering (ikke implementert ennå):
Først fordeles gruppen av høyest seeded løpere likt antallet heat, randomly ut på heatene; så neste gruppe randomly, osv. til alle seedede løpere er fordelt. Så fordeles alle useedede randomly ut på alle heat tilsvarende hvordan prosessen er for løp uten seeding. 
