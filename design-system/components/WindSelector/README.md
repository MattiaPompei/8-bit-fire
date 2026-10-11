# WindSelector

La riga del vento: chiave/valore a sinistra e tre pulsanti secondari in un radiogroup, che leggono come la direzione delle fiamme.

## Uso

- Prima riga del pannello. Valori "Sinistra", "Fermo", "Destra"; a fuoco spento "Nessuno".
- Icone: freccia a sinistra, freccia in su (fiamme dritte, vento fermo), freccia a destra. Mai il simbolo di pausa.
- Il valore cambia con lo scorrimento laterale nel verso del vento (`dur-roll`).

## Stati

- Fuoco acceso: un pulsante selezionato con la barra `shadow-selected`.
- Fuoco spento: tutti e tre disattivati e nessuno selezionato. Alla riaccensione torna "Sinistra".
- Lo stesso valore si cambia trascinando in orizzontale sul fuoco (un passo ogni 72px) o con le frecce della tastiera.

## Cosa fornisce chi lo usa

- `.ef-row` con `.ef-meta` (chiave `.ef-key`, valore `.ef-value`) e `.ef-wind` con tre `button.ef-btn.ef-btn-2[role=radio]`.
