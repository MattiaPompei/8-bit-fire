# ControlsPage

La pagina Controlli: rende visibili i gesti sul fuoco e spiega ogni controllo, con piccole dimostrazioni animate.

## Dove si apre

- Dal pulsante "i" in alto a destra nella splash e da "Controlli e gesti" nel foglio impostazioni.
- Entra ed esce sempre da destra. Su telefono a tutto schermo; da `size-desktop` in su pannello laterale da `size-side-panel` con bordo sinistro `line`.
- Aperta dalle impostazioni è annidata: fondo dietro trasparente, su desktop occupa lo stesso pannello delle impostazioni (che scivolano a sinistra del 30% e si attenuano), e la testata mostra Indietro (freccia a sinistra, "Torna alle impostazioni") al posto di Chiudi.
- Si chiude con Chiudi o con Esc; il focus torna al pulsante che l'ha aperta.

## Struttura

- Foglio a tutta altezza, fondo `panel`, fondo dietro al 60% (trasparente se annidata).
- Testata fissa: titolo "Controlli" (`sheet-title`) e Chiudi (secondario a icona), padding `space-24`, bordo inferiore `line`.
- Corpo che scorre, padding `space-24`, gruppi a 32px:
  1. Introduzione in `label`, 14px.
  2. **Sul fuoco**: tocca al centro, trascina in su o in giù, trascina ai lati, a fuoco spento trascina in su. Ogni voce ha una dimostrazione `size-demo`: un dito (`fg`) su un fuoco in miniatura nella palette del fuoco, con griglia di pixel da 8px.
  3. **Pannello**, **In alto**: riquadro `size-demo` su `btn` con le icone del sistema, poi titolo (`value`) e descrizione (14px `label`).
  4. **Impostazioni**: termine in `fg` e descrizione, in colonna `size-key-col`.
  5. **Tastiera**: tasti come `kbd` (32px, `btn`, raggio `radius-md`) e azione.

## Movimento

- Entra da destra in `dur-sheet-in` con `ease-drawer` ed esce a destra in `dur-sheet-out` con `ease-out`; transizioni interrompibili.
- I gruppi entrano salendo di 16px (`dur-reveal`, 40ms l'uno dall'altro).
- Dimostrazioni in loop (`dur-demo`, `ease-in-out`; il tocco 1800ms `ease-out`), solo a pagina aperta; ferme con movimento ridotto.

## Accessibilità

- `dialog` con `aria-labelledby`; ogni gruppo è una `section` con titolo `h3`; le dimostrazioni e le icone sono `aria-hidden`, il testo dice tutto.
