# Renndagen
Funksjonen "Admin - renndagen" eller "Dashboard - under rennet" gir oversikt over funksjoner som benyttes mens rennet pågår.

### Fremdrift i rennet
![image](https://user-images.githubusercontent.com/56455987/229273802-751694fa-a1fb-418d-888e-311daee6dea3.png)
Denne oversikten gir oversikt over fremdrift i rennet. Rød merking på et heat krever handling. Ved å holde musepeker over aktuelt heat kommer mer informasjon om hva som er feil.

![image](https://user-images.githubusercontent.com/56455987/229273738-d274c6bd-435e-4830-835c-932c568f0924.png)

### DNS/DNF
DNS (did not start) eller DNF (did not finish) bør alltid registreres når løpere ikke kommer til mål. Dette sikrer at arrangøren kan holde oversikt over alle løpere gjennom konkurransen. Tidtaker kan registrere (og avregistrere) DNF ved hjelp av sjekkboks på tidtakersiden. DNS registreres ved start eller på rennkontoret (egne funksjoner). Dersom summen av DNS, DNF og målpasseringer ikke stemmer med antall påmeldte vil dette dukke opp som et avvik i renn-dashbordet.

### Registrer målpassering
Startnummer skrives inn i den rekkefølgen løpere passerer mål. Ingenting lagres før lagre-knappen trykkes. Dersom det er behov for å gjøre endringer så gjøres disse og Lagre trykkes igjen. Alle endringer blir da registrert, inkludert startlister til neste runde. Sjekkboksen “Publisere” brukes til å bekrefte at resultatene er offisielle. Dersom den ikke er sjekket vil det komme et gult varsel om at resultatene er uoffisielle.

### Resultatliste for klasser
Disse genereres automatisk så snart resultater for finale A er registrert. Dersom man i etterkant gjør endringer i heat-resultater må klasse-resultater genereres på nytt. Dette gjøres gjennom en egen funksjon på renn-admin siden.

### Live resultater på stadion
Det anbefales å sette ut skjermer med live resultater på stadion. Live siden er laget for å følge en løpsklasse og vil automatisk oppdatere seg for å fokusere på gjeldende runde. Pro tip: Det er mulig å endre refresh rate på siden ved å skru på parameter i side-url. Anbefaling er å sette 30 sekunder (default er 120). 

### Etteranmelding
Etteranmeldinger kan gjøres så lenge det er ledige plasser i heat. Startnummer må velges manuelt og løperen vil automatisk bli plassert i et av heatene med færrest løpere. Det tas ikke hensyn til seeding.
