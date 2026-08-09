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

Jeg har ikke tid til å lese meg opp på hvordan man bruker fastAPI og confluent-kafka, og siden tjenesten skal gjøre en enkel og konkret oppgave regner jeg med at ChatGPT har et godt forslag til implementasjon.

Prompt:
> I'm implementing a POC of a python service that will accept arbitrary json data and send it to a kafka topic. 
> The service should use FastAPI and confluent-kafka. 
> The service should accept POST requests to /data and respond 200 OK if the request was valid and it's content was successfully sent to the kafka topic.
> Respond 400 bad request in the case of invalid json.
> Any other errors should be propagated so that they result in a http 500 error response. Keep this minimal and clean

Etter litt finpuss av ChatGPTs forslag har jeg en veldig minimal og enkel POC som jeg mener er god nok for denne programmeringsoppgaven. Kommer tilbake til forbedringspotensiale.