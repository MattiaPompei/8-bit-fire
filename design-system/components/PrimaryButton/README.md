# PrimaryButton

Il pulsante primario: "Accendi il fuoco" nella splash, l'accensione nel pannello, "Ripristina valori predefiniti" nel foglio impostazioni. Pieno `accent`, testo `ink`, a tutta larghezza.

## Misure

- Alto `size-primary` (56px), raggio `radius-md`, padding orizzontale `space-24`, etichetta `primary-label`.
- Splash: largo fino a `size-panel`, a `space-24` dai lati e dal fondo (più il margine di sicurezza).
- Pannello: ultima riga, a tutta larghezza con accanto il pulsante impostazioni (secondario, `size-primary` di lato) a `space-16`. Il pannello ha padding `space-24`: i due pulsanti primari cadono nello stesso punto dello schermo.

## Stati

- Riposo `accent`, hover `accent-hover`, premuto `scale-press` in `dur-press` con `ease-out`, focus anello `focus`.
- Variante neutra (`is-on`): a fuoco acceso l'accensione dice "Spegni il fuoco" su fondo `power` con bordo `track` e testo `fg`; forma e misure restano quelle del primario. L'accento invita solo ad accendere.
- L'etichetta dice l'azione; nessun `aria-pressed`.

## Cosa fornisce chi lo usa

- `<button class="ef-btn ef-primary">` con l'etichetta; nella splash aggiungi `is-start` per la larghezza massima; nel pannello mettilo dentro `.ef-actions`.

- Foglio impostazioni: "Ripristina valori predefiniti" è il primario, sotto il secondario "Controlli e gesti".

## Da non fare

- Un solo primario per schermata. Niente icone accanto al testo.
