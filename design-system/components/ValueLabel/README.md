# ValueLabel

La coppia chiave/valore di pannello, foglio e HUD, con il valore che si muove quando cambia.

## Uso

- Chiave in `key` (`label`, 12px), valore in `value` (`fg`, 16px, cifre tabellari): rapporto 4:3. Chiave sopra, valore sotto, `space-8` tra i due; colonna `size-key-col`.
- Numeri (intensità, altezza, celle, velocità): rotazione verticale ritagliata sulla riga. Valore che sale: il vecchio esce in alto e il nuovo entra dal basso; che scende: il contrario. L'unità ("/10", "%", " px", " fps") resta ferma fuori dalla rotazione.
- Parole del vento: scorrimento laterale nel verso del vento, sfumando, senza ritaglio.
- `dur-roll` con `ease-drawer`. Un nuovo valore durante un'animazione sostituisce quella in corso. Niente animazione durante il trascinamento sul fuoco e da tastiera. Senza movimento con prefers-reduced-motion.

## Cosa fornisce chi lo usa

- `.ef-meta` > `.ef-key` + `output.ef-value`; la parte che si anima dentro `.ef-roll` (`.v` per la rotazione verticale), con il testo corrente in uno `span`.
