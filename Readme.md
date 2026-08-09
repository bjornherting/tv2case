# Intervjuoppgave: Backend API + Kafka

## Problemstilling

Reklameteknologi trenger å raskt få opp en tjeneste som kan motta arbitrær json-data
fra seerne på play. Det er veldig viktig at dataen blir persistert for videre prossesering.

Oppgaven din blir å utvikle en Proof-of-Concept av en slik løsning ved å benytte

* HTTP Backend API (Go, Java, Python, C#)
* Kafka
* cURL / Bash / Python for enkel verifisering av endepunktet lokalt

Flyt: Klient -> Backend API -> Kafka -> 200 OK

Ettersom dette bare er en Proof-of-Concept kan man hoppe over normalt sett viktige deler av produksjons-kode, men vi forventer en liste over forbedringer og andre tiltak som bør implementeres for å ta prosjektet videre.

Når du starter oppgaven før en liten journal over tankene dine og valgene du tar underveis.

Oppgaven besvares ved å levere 
* git repository / .zip fil av all koden
* Listen over forbedringer og nødvendige tiltak for videreutvikling
* Journal

# Infrastruktur
For å hjelpe deg litt i gang har vi allerede definert en docker-compose.yml fil som kan brukes til å enkelt sette opp kafka lokalt på maskinen.
Dette krever at du har installert Docker på maskinen din.
Denne konfigurasjonen eksponerer kafka på localhost:9094 (host-maskin), eller på kafka:9092 inni docker-nettverket.

# Hjelpemidler
Alle hjelpemidler er i utgangspunktet lov, hvis du skulle stå fast på noe, så kan du velge
å bruke mer av din tid på andre deler av oppgaven. Eventuelt løse problemet på en annen måte.

# Tidsbruk
2-4t 
Det viktigste er at vi har en felles problemstilling å snakke rundt
