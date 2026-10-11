# IntensitySlider

Lo slider dell'intensità: 10 scatti, binario nei colori del fuoco e cursore a forma di fiamma.

## Uso

- Seconda riga del pannello. Valore "N/10": il numero ruota in verticale a ogni cambio (`dur-roll`), "/10" resta fermo.
- Parte piena del binario: sfumatura `fire-07` → `fire-13` → `fire-21` → `fire-35`; parte vuota `track`. `--pct` = (valore − 1) / 9.
- Cursore: `flame-thumb.svg` (gruppo Icone), `size-flame-w` × `size-flame-h`, alzato di 10px sul binario perché il peso della fiamma sta in basso, con `shadow-flame`. La fiamma è sempre `fg`; lo stacco di 2px in `panel` la separa dal binario.
- Lo stesso valore si cambia trascinando in verticale sul fuoco: lì è frazionario e segue il dito; al rilascio si aggancia all'intero.

## Cosa fornisce chi lo usa

- `<input type="range" class="ef-slider is-flame" min="1" max="10" step="1">` con `aria-valuetext` "N su 10" e la variabile `--pct` aggiornata.

## Da non fare

- Non colorare la fiamma con il livello: il colore del livello lo dà già il binario.
