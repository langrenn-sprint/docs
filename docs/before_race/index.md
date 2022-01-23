# Part 2 Administrasjon - før rennet

Dette avsnittet beskriver nødvendige forberedelser for å gjøre klart til renn! For å få tilgang til funskjonene må du være innlogget som event-administrator. Rennforberedelsene er delt opp i 9 steg.

# Steg 1 - Nytt arrangement
Start på hovedsiden og velg knappen "Nytt arrangement". Fyll deretter inn nøkkelinformasjon om rennet.

![image](https://user-images.githubusercontent.com/56455987/150696887-4ca6576f-2e46-4eb8-bbe0-5bf06bd93f41.png)

Når arrangementet er opprettet vises oversikten for rennforberedelser.

![image](https://user-images.githubusercontent.com/56455987/150698041-37286316-4f73-41fb-9522-6fbe435518e3.png)

# Steg 2 - Deltakere
Påmelding skjer normalt via Min Idrett og deltakerlisten hentes ut gjennom Sportsadmin. Last ned deltakerlisten i format NSF XLS (excel). Bruk excel til å sjekke at alle data er riktige (normalt vil Sportsadmin markere med rødt de feltene som kan være feil, for eksempel påmelding i feil aldersklasse). Når data er korrigert lagres deltakerlista som en kommaseparert fil (csv).
Trykk "Last inn deltakere" fra oversikten for å komme til siden for innlasting av deltakere.

![image](https://user-images.githubusercontent.com/56455987/150698166-6668caa2-1f46-458c-b0a4-2e887a89b058.png)

Etter innlasting av deltakere vises resultatet. Her ble 317 deltakere lastet inn. 1 duplikat ble funnet i inn-filen (en deltaker var påmeldt 2 ganger).

![image](https://user-images.githubusercontent.com/56455987/150698249-47fb9703-9c78-4dfe-8e85-c1f3305e1536.png)

# Steg 3 - Klasser
Det genereres automatisk løpsklasse for hver aldersklasse i påmeldingslisten. Utføres ved å trykke på 'Generer klasser.

![image](https://user-images.githubusercontent.com/56455987/150698405-22909b96-db5d-4d3a-bde8-0b31ad6bfcbb.png)

I dette eksemplet opprettes 11 klasser. Det er mulig å lage felles løpsklasse for flere årsklasser - dette gjøres med funskjonen 'Slå sammen klasser'.

# Steg 4 - Startrekkefølge
Funksjonen 'Rediger startrekkefølge' er neste steg. Her settes startgruppe - alle løpsklasser i samme startgruppe går samtidig og startrekkefølge bestemmer innbyrdes startrekkefølge. Alle heat og runder i en startgruppe gjøres ferdig før klassene i neste startgruppe starter. I dette eksemplet starter jentene først og en og en årgang går om gangen - bortsett fra 15 og 16 åringene som går samtidig.

![image](https://user-images.githubusercontent.com/56455987/150698646-ef2a7887-6a24-42ea-a0e2-00e2de8e79bf.png)

# Steg 5 - Startnummer
Det er nå klart for 'Tildel startnummer'. Startnummer tildeles i henhold til startrekkefølgen i forrige steg. Samtidig gjøre det en sortering av brukerne slik at det tildeles startnummer i tilfeldig rekkefølge innenfor hver klasse.

![image](https://user-images.githubusercontent.com/56455987/150698701-cb9f64ab-4f01-4ed4-a5cc-eb987cdbe20c.png)

Når startnummer er tildelt blir funksjonene for å skrive ut deltakerlister - pr klubb og pr klasse - tilgjengelig.

# Steg 6 - Kjøreplan
Funksjonen 'Generer kjøreplan' setter opp alle heat (kvartfinaler, semifinaler, finaler) i henhold til et pre-definert oppsett. Starttider settes basert på eventens start-tidspunkt og de globale innstillingene.

![image](https://user-images.githubusercontent.com/56455987/150700200-9273bab8-f42b-4cf1-b696-4296735a4389.png)

Når kjøreplanen er generert (kode 201 betyr at alt gikk OK) kommer funksjonen 'Skriv ut' til syne.

# Steg 7 - Tilpass tidskjema
Denne funksjonen benyttes for å optimalisere tidskjema. Det bør sjekkes manuelt at hviletider for løperne er passe lange. Helst mellom 15 og 30 minutter. Gjerne ned mot 15 i de yngre klassene og opp mot 30 for de eldste.

![image](https://user-images.githubusercontent.com/56455987/150700382-0cf7e87b-af28-451e-b46f-3516fb23768f.png)

Merk: Utgangspunkt for oppsett av tid er basert på Globale innstillinger.

# Steg 8 - Startliste
Med denne funksjonen plasseres alle løpere i sine kvartfinale-heat. Funksjonen 'Skriv ut' dukker opp når operasjonen er fullført. Verifiser at alle deltakere blir plassert i et heat ved å sammenligne antall starter og antall deltakere.

![image](https://user-images.githubusercontent.com/56455987/150700451-1290db33-b2e3-4ad4-a786-f47293c94f3b.png)

# Steg 9 - "Videre til"
Siste steg er å opprette oppsett for kvalifisering til semifinaler og finaler. Merk at det i oppsettet tas høyde for maks 10 (konfigurerbart) løpere i hvert heat.

![image](https://user-images.githubusercontent.com/56455987/150700553-74e476c9-1aeb-4598-a6b0-7d4ab7ce2e46.png)

Gratulerer - vi er nå klare til å kjøre renn!

