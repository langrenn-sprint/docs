# Part 2 Administrasjon - før rennet

Dette avsnittet beskriver nødvendige forberedelser for å gjøre klart til renn! For å få tilgang til funskjonene må du være innlogget som event-administrator. Rennforberedelsene er delt opp i 9 steg.

Før du starter er det viktig å kontollere at "Globale innstillinger" er riktige. ![link](settings/index.md)

# Steg 1 - Nytt arrangement
Start på hovedsiden og velg knappen "Nytt arrangement". Fyll deretter inn nøkkelinformasjon om rennet.

![image](https://user-images.githubusercontent.com/56455987/151457997-f0b2641c-9e2a-41bf-8351-76ee4122901d.png)

Når arrangementet er opprettet vises oversikten for rennforberedelser.

![image](https://user-images.githubusercontent.com/56455987/151458061-78937b50-b6b4-4763-9c3f-750d497d2a9d.png)

# Steg 2 - Deltakere
Påmelding skjer normalt via Min Idrett og deltakerlisten hentes ut gjennom Sportsadmin. Last ned deltakerlisten i format NSF XLS (excel). Bruk excel til å sjekke at alle data er riktige (normalt vil Sportsadmin markere med rødt de feltene som kan være feil, for eksempel påmelding i feil aldersklasse). Når data er korrigert lagres deltakerlista som en kommaseparert fil (csv).
Trykk "Last inn deltakere" fra oversikten for å komme til siden for innlasting av deltakere.

![image](https://user-images.githubusercontent.com/56455987/151652549-baa4cecd-6ed4-43e2-875f-5fcdec1b4d12.png)

Velg riktig fil og trykk last opp.
![image](https://user-images.githubusercontent.com/56455987/151458498-8877f4a1-7448-4082-9ae8-630a8e2e7057.png)

Etter innlasting av deltakere vises resultatet. Her ble 112 deltakere lastet inn. Dersom du får melding om feil eller duplikater bør dette verifiseres i kildefilen.

![image](https://user-images.githubusercontent.com/56455987/151458725-9a91ad0e-3837-4c4b-8bbc-0d58ff127c5b.png)

# Steg 3 - Klasser
Det genereres automatisk løpsklasse for hver aldersklasse i påmeldingslisten. Utføres ved å trykke på 'Generer klasser'.

![image](https://user-images.githubusercontent.com/56455987/151652608-a8efabf7-798b-4f8c-91a8-e0c61b095f22.png)

I dette eksemplet opprettes 4 klasser. Det er mulig å lage felles løpsklasse for flere årsklasser - dette gjøres med funskjonen 'Slå sammen klasser'.

![image](https://user-images.githubusercontent.com/56455987/151652646-8b16c72a-6a65-4c09-8f03-76e65effb795.png)

# Steg 4 - Startrekkefølge
Funksjonen 'Rediger startrekkefølge' er neste steg. Her settes startgruppe - alle løpsklasser i samme startgruppe går samtidig og startrekkefølge bestemmer innbyrdes startrekkefølge. Alle heat og runder i en startgruppe gjøres ferdig før klassene i neste startgruppe starter. 

![image](https://user-images.githubusercontent.com/56455987/151652673-e71e7d92-ae13-45c2-a422-259969b5d409.png)

I dette eksemplet starter jentene først og en og en årgang går om gangen.

![image](https://user-images.githubusercontent.com/56455987/151458888-1dc76611-5f26-4ce6-ad53-2277bc883017.png)

# Steg 5 - Startnummer
Det er nå klart for å tildele startnummer. 
![image](https://user-images.githubusercontent.com/56455987/151652702-4f9baffa-69cd-4e4a-8d83-6f7285c37d30.png)

Startnummer tildeles i henhold til startrekkefølgen i forrige steg. Samtidig gjøre det en sortering av brukerne slik at det tildeles startnummer i tilfeldig rekkefølge innenfor hver klasse.

![image](https://user-images.githubusercontent.com/56455987/151459034-4d209d57-32e7-451d-bb76-eb8b11effe9a.png)

Når startnummer er tildelt blir funksjonene for å skrive ut deltakerlister - pr klubb og pr klasse - tilgjengelig.

Merk: Det er også mulig å tildele startnummer manuelt. Dette kan enten gjøres ved at startnummer legges inn i deltakerfilen (steg 2) eller gjennom detaljsiden for deltakere.

# Steg 6 - Kjøreplan
Funksjonen 'Generer kjøreplan' setter opp alle heat (kvartfinaler, semifinaler, finaler) i henhold til et pre-definert oppsett. Starttider settes basert på eventens start-tidspunkt og de globale innstillingene.

![image](https://user-images.githubusercontent.com/56455987/151459080-46fd576c-601d-413a-8cc7-ee8c8eea99f3.png)

Når kjøreplanen er generert (kode 201 betyr at alt gikk OK) kommer funksjonen 'Skriv ut' til syne.

# Steg 7 - Tilpass tidskjema
Denne funksjonen benyttes for å optimalisere tidskjema. Det bør sjekkes manuelt at hviletider for løperne er passe lange. Helst mellom 15 og 30 minutter. Gjerne ned mot 15 i de yngre klassene og opp mot 30 for de eldste.

![image](https://user-images.githubusercontent.com/56455987/151459148-959052b1-b7bf-479f-bae6-f0a23cfaf1c0.png)

Merk: Utgangspunkt for oppsett av tid er basert på Globale innstillinger.

# Steg 8 - Startliste
Med denne funksjonen plasseres alle løpere i sine kvartfinale-heat. Funksjonen 'Skriv ut' dukker opp når operasjonen er fullført. Verifiser at alle deltakere blir plassert i et heat ved å sammenligne antall starter og antall deltakere.

![image](https://user-images.githubusercontent.com/56455987/151459226-3e93d6ad-4b2c-4197-a676-b12dddf42959.png)

# Steg 9 - "Videre til"
Siste steg er å opprette oppsett for kvalifisering til semifinaler og finaler. Merk at det i oppsettet tas høyde for maks 10 (konfigurerbart) løpere i hvert heat.

![image](https://user-images.githubusercontent.com/56455987/151459313-9569ad91-d55d-41cf-9718-3b4578cd955e.png)

Gratulerer - vi er nå klare til å kjøre renn!

