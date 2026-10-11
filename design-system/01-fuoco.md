# Il fuoco

Il fuoco è una griglia di celle che vale da 0 a 36. Ogni valore ha un colore della palette `fire-00` … `fire-36`.

## Algoritmo

- La riga in fondo vale la temperatura di base, che segue l'intensità: base = 36 × intensità / 10. A fuoco spento la base è 0 e le fiamme si esauriscono da sole.
- A ogni passo ogni cella prende il valore della cella sotto e sottrae un numero r (0, 1 o 2, estratto a caso). Lo stesso r sposta la cella di r colonne nel verso del vento: a sinistra, a destra, o nessuno spostamento se il vento è fermo. Le colonne si richiudono ai bordi.
- La base non salta: insegue il valore richiesto con una costante di tempo di 120ms, così ogni cambio di intensità è morbido.
- L'altezza controlla la probabilità di r: fiamme alte = r piccolo in media. Se la griglia è troppo bassa per arrivarci con 0-2, si aggiunge un'estrazione (r fino a 3 o 4).
- Al primo disegno e quando l'area cresce, le righe e colonne nuove si riempiono subito simulando i passi mancanti.

## Parametri

| Parametro | Valori | Predefinito | Dove |
|---|---|---|---|
| Intensità | 1-10 (frazionaria durante il trascinamento) | 7 | pannello, trascinamento verticale |
| Vento | sinistra, fermo, destra | sinistra | pannello, trascinamento orizzontale |
| Altezza | 10-100%, passi di 5 | 100% | foglio impostazioni |
| Celle | 4, 8, 16, 24, 32, 48 px | 8 px | foglio impostazioni |
| Velocità | 20-60 fps, passi di 5 | 20 fps | foglio impostazioni |

- Intensità e vento tornano ai predefiniti a ogni riaccensione (pulsante, Spazio, tocco al centro, ripartenza dalla splash).
- Il trascinamento verso l'alto a fuoco spento riaccende partendo da intensità 1.
- Altezza, celle e velocità sono impostazioni generali: non cambiano con l'accensione e tornano ai predefiniti solo con "Ripristina valori predefiniti".
- Le impostazioni restano salvate nel browser.

## Disegno

- Ogni cella è un pixel di un canvas grande quanto la griglia, ingrandito a `cell` px con `image-rendering: pixelated`.
- Il canvas è ancorato in basso a sinistra dell'area del fuoco, con origine delle trasformazioni in basso al centro: lo zoom tiene la base appoggiata.
