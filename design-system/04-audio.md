# Audio

L'audio parte spento: il browser lo consente solo dopo un tocco. Si attiva con il pulsante in alto a destra o con M.

## Fuoco

- Due registrazioni in loop, incorporate nella pagina (AAC 128 kbps): fuoco basso e fuoco alto, mixate in dissolvenza secondo l'intensità.

| Intensità | Fuoco basso | Fuoco alto |
|---|---|---|
| 1 | 95% | 5% |
| 7 | 60% | 40% |
| 10 | 25% | 75% |

- Tra questi punti il mix è lineare, anche sui valori frazionari del trascinamento; il passaggio ha una costante di tempo di 150ms.
- Volume generale al 70% del livello dei file. Si spegne con il fuoco (costante 0,8s) e torna con lui (0,3s).
- Con il foglio impostazioni aperto il volume generale scende al 50%; torna al 100% alla chiusura.
- Si sospende quando la pagina va in secondo piano. Esci spegne l'audio.
- Su iPhone un audio muto in loop parte al tocco: tiene la sessione in riproduzione, così il fuoco si sente anche con il tasto silenzioso, come un video.

## Feedback

Due suoni sintetizzati dal vivo, rumore filtrato senza note: timbro di aria e fuoco.

| Suono | Forma | Durata |
|---|---|---|
| Accensione | click secco passa-alto a 3,2 kHz (40ms, come un fiammifero) + soffio passa-banda che sale da 300 a 2400 Hz | circa 450ms |
| Spegnimento | soffio passa-banda che scende da 1800 a 250 Hz, coda più lunga | circa 600ms |

- Verso l'alto = si attiva, verso il basso = si chiude.
- Suonano solo con l'audio attivo, con un guadagno di circa metà di quello del fuoco, e rispettano l'abbassamento delle impostazioni.
- Al massimo uno ogni 150ms. Sono sempre accompagnati da un riscontro visivo (pulsante e HUD).
