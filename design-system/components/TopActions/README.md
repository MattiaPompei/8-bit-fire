# TopActions

I pulsanti in alto sopra il fuoco: Esci a sinistra, audio e schermo intero a destra.

## Uso

- Esci a `space-24` dal bordo superiore e sinistro; audio e schermo intero a `space-24` dal bordo superiore e destro, distanziati di `space-16`. A schermo intero si aggiungono i margini di sicurezza. Esci sta da solo per non essere premuto per sbaglio insieme agli altri.
- Pulsanti secondari variante vetro (`glass`). Audio e schermo intero sono toggle a icona con `aria-pressed`: attivi, l'icona dell'audio diventa `accent-fg` e quella dello schermo intero passa a "riduci". Esci è l'unico secondario di testo.
- Esci torna alla splash: chiude foglio e schermo intero, spegne l'audio, ferma il fuoco dietro alla splash.
- Alla partenza compaiono per ultimi (`dur-detail`, ritardo 400ms). Con H spariscono insieme al pannello.

## Da non fare

- Non aggiungere altri pulsanti qui: lo spazio sopra il fuoco resta libero.
