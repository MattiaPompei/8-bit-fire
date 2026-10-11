# SettingSlider

Lo slider delle impostazioni generali: binario sottile `track` con parte piena `accent` e cursore tondo `fg`.

## Uso

- Solo nel foglio impostazioni, una riga per grandezza: Altezza (10-100%, passi di 5, predefinito 100%), Celle (4, 8, 16, 24, 32, 48 px su 6 scatti, predefinito 8 px), Velocità (20-60 fps, passi di 5, predefinito 20 fps).
- Il numero del valore ruota in verticale a ogni cambio; l'unità resta ferma.
- Tutta la riga da `size-tap` risponde al tocco; il cursore misura `size-thumb`.

## Cosa fornisce chi lo usa

- `<input type="range" class="ef-slider">` con `--pct` aggiornata e, per le celle, `aria-valuetext` "N pixel".
