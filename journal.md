# Journal for intervjuoppgave

## Timeline

### Fredag formiddag

På fredag når jeg mottok oppgaven, mens jeg var ute og trillet barnevogn, leste jeg kjapt gjennom oppgaveteksten for å få en idé om oppgavens omfang og for å la den marinere litt mens jeg gikk.

### Fredag kveld

Leste mer nøye gjennom oppgaven og gjorde meg følgende notater fra teksten: 

* Gyldig data er hvilken som helst Json
* Fra seerne på play, altså mange kunder og potensielt mye trafikk. Tjenesten må være skalerbar.
* Persistering er "veldig viktig", så tjenesten må svare at request er akkseptert først når kafka har ACKet innholdet

Planlegger å implementere i Python, siden det er kjent for meg og et effektivt språk for å få opp en POC. I følge ChatGPT er pakkene FastAPI og confluent-kafka velegnet for dette.

### Søndag, på Apparat HQ

Jeg er i pappaperm og har ikke tid til å lese meg opp på hvordan man bruker fastAPI og confluent-kafka. Siden tjenesten skal gjøre en enkel og konkret oppgave regner jeg med at ChatGPT har et godt forslag til implementasjon.

Prompt:
> I'm implementing a POC of a python service that will accept arbitrary json data and send it to a kafka topic. 
> The service should use FastAPI and confluent-kafka. 
> The service should accept POST requests to /data and respond 200 OK if the request was valid and it's content was successfully sent to the kafka topic.
> Respond 400 bad request in the case of invalid json.
> Any other errors should be propagated so that they result in a http 500 error response. Keep this minimal and clean

Etter litt finpuss av ChatGPTs forslag har jeg en veldig minimal implementasjon, som kan være tilstrekkelig for en POC som beskrevet i oppgaveteksten

Ber også ChatGpt om en Dockerfile og å få startet den i docker-compose.yml

## Forbedringer og tiltak

### I koden
* Tjenesten kaller producer.flush() for hvert kall til apiet for å garantere mottak i kafka. Dette kallet blokkerer håndteringen av andre requests og burde endres til å være callback basert. Jeg har vurdert det som utenfor scope for denne oppgaven. Kall av flush for hver request hindrer også fordeler man får av kafka sin interne buffering mekanisme, så det bør vurderes hvilke garantier tjenesten skal gi for data som sendes inn
* Tjenesten aksepterer alt kan tolkes som json. Dette betyr at "foo" og null også er gyldig data, men jeg ser for meg at dette ikke er hva brukerne og videre konsumenter av kafka topic forventer. Ville sjekket med disse hvilket behov de egentlig har
* Det settes ikke key på kafka meldinger, som hindrer god utnyttelse av partisjoneringen i kafka. Siden dette er data fra brukerne ser jeg for meg at vi ville hatt tilgjengelig en  bruker-id eller lignende å bruke som key
* Der er ingen tester. Siden det ikke er noen business logikk her er det ikke behov for masser av unit-tester, men det burde settes opp en enkel integrasjonstest som verifiseres at gyldige requests går gjennom

### Klargjøring for produksjon
* Siden dette er data fra play-brukere som jeg antar stort sett oppholder seg i Norge er det antagelig mer trafikk rundt noen tidspunkter og hendelser, og andre roligere perioder. Tjenesten bør kjøre i kubernetes eller på andre måter som lar oss skalere opp antall instanser ved behov. Dette hindrer også nedetid ved oppgradering
* Vi må ha autentisering. Dette ville jeg implementert ihht behovet og hva som brukes ellers i organisasjonen
* Det bør sørges for at feilsituasjoner logges og at disse loggene sendes til elastic eller tilsvarende for feilsøking
* Vi bør samle inn metrikker på ting som antall forskjellige http respons koder og latency
