# FireCanvas

Il fuoco: una griglia di celle da 0 a 36 disegnata con la palette `fire-00` … `fire-36` e ingrandita a pixel.

## Uso

- Occupa l'area del fuoco, ancorato in basso a sinistra, una cella = un pixel del canvas ingrandito a `cell` px con `image-rendering: pixelated`.
- Algoritmo, parametri e predefiniti: sezione "Il fuoco". Disegno a passo fisso (20-60 fps), indipendente dal refresh dello schermo.
- Griglia centrata orizzontalmente sull'area. Trasformazioni con origine in basso al centro: `scale-fire-settings` con le impostazioni aperte, `scale-fire-prestart` dietro la splash.
- Con le impostazioni aperte la griglia si allarga a spazio disponibile / 0,75 prima dello zoom, così il fuoco rimpicciolito riempie ancora tutta l'altezza e la larghezza sopra il foglio; torna alle misure dell'area a ritorno finito, senza salti.
- Riceve i gesti (tocco al centro, trascinamento verticale e orizzontale): sezione "Interazioni".

## Accessibilità

- `role="img"` con un'etichetta che descrive i gesti; sta dentro `<main>`.

## Cosa fornisce chi lo usa

- Un `<canvas>` dentro un contenitore `overflow: hidden` con fondo `stage`, e lo stato: intensità, vento, altezza, celle, velocità, acceso/spento.
