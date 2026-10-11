# Interazioni

## Gesti sull'area del fuoco

Valgono con il pannello visibile e a schermo intero. I pulsanti sopra il fuoco (audio, schermo intero, Esci) non avviano gesti.

| Gesto | Effetto | Regole |
|---|---|---|
| Tocco al centro | a fuoco spento riaccende; a fuoco acceso servono due tocchi entro 450ms per spegnere (al primo la HUD dice "Tocca ancora per spegnere") | zona centrale con il 75% dell'area (circa 6,7% di margine per lato), movimento sotto 10px, rilascio entro 400ms |
| Trascinamento verticale | intensità, su = più intensa | mezza altezza dell'area copre 1-10; il valore segue il dito anche tra un livello e l'altro, al rilascio si aggancia all'intero più vicino |
| Trascinamento verticale a fuoco spento | verso l'alto riaccende da intensità 1 | verso il basso non fa nulla |
| Trascinamento orizzontale | vento a passi: sinistra, fermo, destra | un passo ogni 72px o 18% della larghezza; cambia mentre trascini; disattivato a fuoco spento |

- Il gesto si decide al primo movimento oltre 10px, sulla direzione prevalente, e resta quello fino al rilascio: verticale e orizzontale non si mescolano mai.
- Durante un gesto la HUD mostra la grandezza e il suo valore, e sparisce 700ms dopo il rilascio (900ms dopo un tocco). Il valore finale viene anche annunciato ai lettori di schermo.
- Alla prima partenza, dopo 1,4 secondi, la HUD mostra "Gesti · Trascina il fuoco" per 3,5 secondi; poi non ricompare più.

## Pannello

- Vento: tre pulsanti in un radiogroup. A fuoco spento sono disattivati e nessuno è selezionato; il valore diventa "Nessuno".
- Intensità: slider a 10 scatti con cursore a fiamma.
- Accensione: pulsante primario a tutta larghezza, stessa forma del primario della splash; l'etichetta dice cosa farà ("Spegni il fuoco" / "Accendi il fuoco"). A fuoco acceso il fondo è neutro (`power`), a fuoco spento `accent`. Accanto, il pulsante impostazioni (`size-primary` di lato).

## Foglio impostazioni

- Apertura: il foglio sale dal basso, il fuoco scende al 75% (`scale-fire-settings`) e la sua base si appoggia sul bordo superiore del foglio, ma continua a occupare tutta l'altezza e la larghezza sopra il foglio: la griglia si allarga prima dello zoom; il volume generale scende al 50%.
- Chiusura con la X, toccando fuori o con Esc: il foglio scende, poi il dialog si chiude; fuoco e volume tornano al 100%.
- Contiene Altezza, Celle, Velocità, "Controlli e gesti" (secondario) e "Ripristina valori predefiniti" (primario).
- Da `size-desktop` in su è un pannello laterale che entra ed esce da destra a tutta altezza; il fuoco non si rimpicciolisce e non sale.
- Se non entra nello schermo (orizzontale, testo grande) scorre.

## Schermo intero

- Nasconde il pannello e porta il fuoco fino al fondo dello schermo, ignorando i margini di sicurezza. Dove il browser lo consente (Android, desktop) chiede anche lo schermo intero vero; su iPhone resta la sola modalità a pagina piena.
- La HUD scende a 32px dal fondo dello schermo; i pulsanti in alto rispettano i margini di sicurezza.
- Uscire dallo schermo intero del browser (Esc, gesto indietro) riporta anche il pannello.

## Pulsanti in alto

- Esci in alto a sinistra; audio e schermo intero in alto a destra, distanziati di `space-16`. Tutti a `space-24` dai bordi.
- Esci torna alla splash: chiude foglio e schermo intero, spegne l'audio, ferma il fuoco dietro alla splash e rimette il focus su "Accendi il fuoco". Ripartire riaccende il fuoco con intensità e vento predefiniti.

## Pagina Controlli

- Si apre dal pulsante "i" in alto a destra nella splash e da "Controlli e gesti" nelle impostazioni. Entra sempre da destra: su telefono a tutto schermo, su desktop come pannello laterale da `size-side-panel`.
- Aperta dalle impostazioni è "annidata": su desktop occupa lo stesso pannello (le impostazioni scivolano a sinistra e si attenuano), la testata ha Indietro al posto di Chiudi e torna alle impostazioni.
- Foglio a tutta altezza, largo al massimo 512px: testata fissa con il titolo e Chiudi, corpo che scorre.
- Gruppi: Sul fuoco (i quattro gesti con dimostrazione animata), Pannello, In alto, Impostazioni, Tastiera.
- Si chiude con Chiudi (o Indietro) o con Esc; il focus torna al pulsante che l'ha aperta.

## Splash

- Titolo a 1/3 dell'altezza; in alto a destra il pulsante "i" (Controlli); in fondo "Accendi il fuoco".
- Il fuoco reale aspetta fermo e `inert` dietro alla splash. "Accendi il fuoco" fa partire l'interfaccia con il fuoco acceso, intensità e vento predefiniti.
- Sulla splash le scorciatoie da tastiera sono spente; Invio e Spazio attivano la CTA, che ha il focus.

## Tastiera

Le scorciatoie sono sempre attive fuori dai fogli; con un foglio aperto i tasti fanno il loro lavoro normale.

| Tasto | Azione |
|---|---|
| Spazio | accende o spegne (con un foglio aperto preme il pulsante a fuoco) |
| H | nasconde o mostra tutta l'interfaccia |
| F | schermo intero |
| M | audio |
| + / − | intensità |
| ← / ↓ / → | vento sinistra, fermo, destra (solo a fuoco acceso) |
| Esc | chiude impostazioni e Controlli |
