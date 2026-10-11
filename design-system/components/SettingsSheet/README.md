# SettingsSheet

Il foglio delle impostazioni generali: sale dal basso sopra il pannello e lascia il fuoco visibile, rimpicciolito.

## Contenuto

- Titolo "Impostazioni" (`sheet-title`) e pulsante Chiudi (secondario).
- Altezza, Celle, Velocità (SettingSlider).
- "Controlli e gesti" (secondario di testo, apre la pagina Controlli sopra il foglio) e "Ripristina valori predefiniti" (primario), a tutta larghezza in quest'ordine.

## Comportamento

- Su telefono sale dal basso; da `size-desktop` in su è un pannello laterale largo `size-side-panel` che entra ed esce da destra a tutta altezza, con bordo sinistro `line`, e il fuoco non si muove.
- "Controlli e gesti" apre la pagina Controlli dentro il pannello: su desktop la pagina occupa lo stesso spazio, il contenuto delle impostazioni scivola a sinistra del 30% e si attenua, e Indietro lo riporta.
- Se il contenuto non entra (orizzontale, testo grande) il foglio scorre.

- È un `<dialog>` modale, largo al massimo `size-sheet`, angoli superiori `radius-md`, fondo `panel`, padding `space-24` (più il margine di sicurezza in basso), fondo dietro `backdrop`.
- Apertura in `dur-sheet-in` con `ease-drawer`; insieme il fuoco scende a `scale-fire-settings` ma continua a riempire tutto lo spazio sopra il foglio: prima dello zoom la griglia si allarga a spazio disponibile / 0,75, le colonne nuove ai lati ripetono quelle esistenti e le righe nuove in alto si riempiono mentre le fiamme salgono; la base si appoggia sul bordo superiore del foglio; il volume generale scende al 50%.
- Chiusura con Chiudi, tocco fuori o Esc: il foglio scende in `dur-sheet-out` con `ease-out`, partendo da dove si trova (è una transizione: chiudere a metà apertura non fa salti), il fuoco torna al 100% in `dur-fire-return` con `ease-in-out`, il volume torna al 100%.
- Con prefers-reduced-motion compare e sparisce in dissolvenza (`dur-reduced`).
