# User documentation for langrenn sprint

## Overview
This is a fronded application for langrenn sprint - containing user interface for operations during a race: View lists and results for users and edit for admins.

The remaining part of the documentation is currenly only in Norwegian.

- Del 1: Brukermanual for deltakere, denne siden
- Del 2: Brukermanual for [Event administrasjon - før rennet](before_race/)
- Del 3: Brukermanual for [Tidtaker administrasjon - under rennet](during_race.md)
- Del 4: [Oppsett for sprint](race_config.md) - beskrivelse av standard sprint oppsett med kvartfinaler, semifinaler og finaler.

## Part 1 - Front-end for guests / Brukergrensesnitt for åpen informasjon.
Åpen informasjon inkluderer oversikt over deltakere, startlister, kjøreplan, live resultater og sluttresultater. Ingen innlogging er nødvendig. Link til sidene finner du vanligvis via arrangementets hjemmesider eller QR koder på arenaen.

![video](https://youtu.be/jpPf93RlRG0)

### Menyen
![image](https://user-images.githubusercontent.com/56455987/150684640-9da7d4a8-9f81-426f-9e03-52798e0dd6a6.png)

Menyen, fra venstre inneholder: 
- ... Snarvei til innhold (startliste, kjøreplan, resultater)
- Navn på gjeldende side (i dette tilfellet Deltakere).
- Ytterligere valg for å filtrere (velg klasse, velg løper eller velg heat).

### Deltakere
![image](https://user-images.githubusercontent.com/56455987/150684546-641d61c8-b9da-4784-b93a-e697b9fc67d2.png)

Denne siden viser påmeldte deltakere og startnummer. Det er mulig å velge en klasse eller alle klasser.

### Kjøreplan
![image](https://user-images.githubusercontent.com/56455987/150684789-f4958605-64ed-441c-8df0-7797fece0ed2.png)

Kjøreplanen lister alle heat med starttidspunkt og runde (kvartfinale/semifinale/finale).

### Starlister
![image](https://user-images.githubusercontent.com/56455987/150684902-befe3983-48a7-4645-b9c7-6696db1025a8.png)

Startlisten viser kjøreplanen med løperne som skal starte i hvert heat. Klasse må velges før startlisten vises.
"Starter nå" er en egen visning der de neste 10 heatene vises, uavhengig av klasse.

### Live
![image](https://user-images.githubusercontent.com/56455987/150685113-82426387-f0d3-4a9a-aa87-bf4b2459f4be.png)

Live viser resultater fra heat som er ferdige og startlister for kommende heat. Siden inneholder også informasjon om løpers neste heat. Eksempel: Neste "SA1" betyr at løperen skal videre til Semifinale A1.

### Resultater

Viser resultatliste for rennet. Løpere i finaler blir rangert mens alle som slås ut i semifinaler eller kvartfinaler får samme plass. 

