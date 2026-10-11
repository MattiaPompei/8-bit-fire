# SecondaryButton

Il pulsante secondario dell'interfaccia: vento, impostazioni, chiudi, audio, schermo intero ed Esci condividono gli stessi stati.

## Stati

| Stato | Aspetto |
|---|---|
| Riposo | fondo `btn`, nessun bordo, icona `fg` |
| Hover (solo puntatore) | fondo `btn-hover` + `shadow-hover`: l'unico stato con un contorno |
| Premuto | fondo `btn-press`, scala `scale-press`, icona giù di 1px |
| Selezionato | `shadow-selected`, barra di `size-selected` in `accent` sul fondo |
| Selezionato + hover | `shadow-selected-hover` |
| Disattivato | `opacity-disabled`, nessuna selezione |

Fondo e scala in `dur-press` con `ease-out`; opacità del disattivato in `dur-state`. La barra di selezione e il contorno di hover cambiano senza transizione (sono `box-shadow`). Hover solo con puntatore fine.

## Varianti

- Vetro (`.ef-glass`): sopra il fuoco, fondo `glass` con 8px di sfocatura; stati premuto e hover uguali. Un toggle attivo colora l'icona di `accent-fg`.
- Nel pannello accanto all'accensione è quadrato da `size-primary`; altrove almeno `size-tap`.
- Testo (`.ef-txt`): Esci in alto a sinistra (vetro) e "Controlli e gesti" a tutta larghezza nel foglio impostazioni; padding orizzontale `space-16`, testo 14px.
- Il focus dei pulsanti in vetro ha un alone `bg` di 6px intorno all'anello `focus`, visibile anche sopra la base chiara del fuoco.

## Cosa fornisce chi lo usa

- `<button class="ef-btn ef-btn-2">` con un SVG inline 24px a `currentColor` e un `aria-label`. Per una scelta esclusiva `role="radio"` e `aria-checked`; per un toggle `aria-pressed`.

## Da non fare

- Niente bordo a riposo, niente testo dentro: per un'azione testuale usa il pulsante neutro (`.ef-btn`).
