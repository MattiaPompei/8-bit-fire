8-bit fire è un fuoco in pixel da tenere acceso sul telefono: si accende, si scalda, si piega al vento con un dito. L'interfaccia è un pannello scuro e quieto sotto un fuoco rumoroso. Il fuoco è il protagonista, i controlli si fanno da parte.

## Principi

- **Il fuoco prima di tutto.** Tieni l'area del fuoco ad almeno 3/4 dello schermo. Il pannello resta in basso, ad altezza fissa, e ospita solo vento, intensità e accensione; altezza, celle e velocità stanno nel foglio impostazioni.
- **Un gesto, una grandezza.** Trascinare in verticale cambia l'intensità, in orizzontale il vento, un tocco al centro accende o spegne. Il primo movimento oltre 10px decide il gesto, che resta quello fino al rilascio.
- **Ogni cambio si vede.** Ogni valore che cambia si muove (rotazione dei numeri, scorrimento delle parole del vento) e la HUD lo ripete sul fuoco.
- **Pixel solo dove serve.** Il carattere 8-bit sta nel fuoco, nel titolo della splash e nel cursore a fiamma. Il resto dell'interfaccia è monospaziato, piatto e sobrio.

## Testi

- Scrivi in italiano, frasi brevi, seconda persona implicita. Le azioni sono verbi all'infinito: "Accendi il fuoco", "Spegni il fuoco", "Ripristina valori predefiniti".
- Le chiavi sono nomi singoli con l'iniziale maiuscola: "Vento", "Intensità", "Altezza", "Celle", "Velocità".
- I valori sono brevi e concreti: "Sinistra", "Fermo", "Destra", "Nessuno" (vento a fuoco spento), "7/10", "100%", "8 px", "20 fps", "Acceso", "Spento".
- Niente emoji, niente punti esclamativi, niente trattini lunghi.
- Il nome del prodotto si scrive `8-bit fire`, con lo spazio. Nel titolo della splash va in maiuscolo.

## Colore

- Tema unico scuro, voluto: il fuoco ha bisogno del nero. Non esiste un tema chiaro.
- Superfici, dal più scuro: `stage` per l'area del fuoco, `bg` per la pagina, `panel` per pannello e foglio, `raise` per i pulsanti di testo neutri, `btn` per i pulsanti secondari, `power` per il primario a fuoco acceso.
- Testo: `fg` per valori e testo principale, `label` per le chiavi, `muted` per il secondario. Su `accent` il testo è sempre `ink`, mai bianco.
- `accent` è il solo colore d'accento: pulsanti primari, parte piena degli slider, barra di selezione. Non usarlo per decorare.
- Il fuoco usa solo la palette `fire-00` … `fire-36`, dal nero (`fire-00` = `stage`) al bianco. La palette appartiene al fuoco: l'interfaccia ne prende in prestito solo la sfumatura del binario dell'intensità (`fire-07`, `fire-13`, `fire-21`, `fire-35`).
- La HUD sopra il fuoco usa `hud` (88%). Sopra il fuoco e sopra la splash i controlli (audio, schermo intero, Esci, Controlli) usano `glass` con 8px di sfocatura; con riduzione della trasparenza tornano a `btn`.

## Tipografia

- Un'unica famiglia per l'interfaccia: `ui` (IBM Plex Mono), da Google Fonts, pesi 400, 500 e 600.
- `pixel` (Silkscreen 700) serve solo al titolo della splash, stile `title-pixel`.
- Le coppie chiave/valore usano `key` (12px, `label`) sopra `value` (16px, `fg`): rapporto 4:3. Le cifre sono sempre tabellari.
- Pulsanti primari in `primary-label`, titolo del foglio in `sheet-title`.

## Spazi, forme e layout

- Griglia di 8px: ogni spazio, padding e misura dei controlli è un multiplo di 8 (`space-8`, `space-16`, `space-24`, `space-32`; `size-tap` 48, `size-primary` 56, `size-key-col` 96).
- Margine esterno uniforme `space-24`, uguale ai lati e in basso nella splash e nella pagina: padding di pannello e foglio, distanza del pulsante primario dal fondo (più il margine di sicurezza), distanza dei pulsanti in alto dai bordi.
- Tra elementi e tra tap area diverse `space-16`. Contenuto del pannello e pulsante primario della splash larghi al massimo `size-panel`.
- Ogni tap area misura almeno `size-tap` (48px).
- Righe del pannello e del foglio: colonna chiave/valore da `size-key-col` (96px), poi il controllo.
- Un solo raggio, `radius-md` (8px), per pulsanti, HUD e angoli superiori del foglio. I binari degli slider usano `radius-track`; il cursore tondo e il cursore a fiamma fanno eccezione per forma.
- Niente ombre decorative. Le sole ombre sono stati: `shadow-selected`, `shadow-hover`, `shadow-selected-hover` e `shadow-flame`.
- Da `size-desktop` (768px) in su il foglio impostazioni diventa un pannello laterale da `size-side-panel` che entra ed esce da destra a tutta altezza; il fuoco resta com'è. La pagina Controlli entra sempre da destra.
- Layout verticale a tutta viewport: fuoco sopra (flessibile), pannello sotto (alto quanto il contenuto). Pagina senza scroll; usa `height: 100%`, mai `100vh`.

## Iconografia

- Icone a linea, 24px su viewBox 24, tratto 2px, estremità e giunzioni tonde (`size-icon`). Nel prodotto sono SVG inline con `currentColor`; i file del gruppo Icone sono a inchiostro `fg`.
- Il vento ha tre frecce che leggono come la direzione delle fiamme: sinistra, dritto in su (fermo), destra. Non usare il simbolo di pausa: si confonde con l'accensione.
- L'unica icona piena è la fiamma del cursore dell'intensità, bianca (`fg`) con uno stacco di 2px in `panel` che la separa dal binario.

## Stati dei controlli

| Stato | Pulsanti secondari | Pulsanti primari |
|---|---|---|
| Riposo | `btn`, nessun bordo | `accent` con testo `ink`, alti `size-primary`; a fuoco acceso l'accensione usa `power` con testo `fg` |
| Hover (solo dispositivi con puntatore) | `btn-hover` + `shadow-hover` | `accent-hover` |
| Premuto | `btn-press`, scala `scale-press`, icona giù di 1px (`dur-press`) | scala `scale-press` (`dur-press`) |
| Selezionato | `shadow-selected` (barra di 6px), senza transizione | — |
| Disattivato | `opacity-disabled`, nessuna selezione | — |
| Focus da tastiera | anello 2px `focus` a 2px di distanza | uguale |

## Accessibilità

- Testo `fg` 16.6:1, `label` 9.9:1, `muted` 7:1 su `panel`; `ink` su `accent` 5.1:1; `fg` su `power` 11:1. La barra `accent` su `btn` è 3.9:1. La HUD su `hud` resta sopra 4.5:1 anche sulla base bianca del fuoco.
- Ogni controllo ha un nome accessibile; il vento è un radiogroup. L'accensione è un pulsante la cui etichetta dice cosa farà, senza `aria-pressed`; audio e schermo intero hanno etichetta fissa e `aria-pressed`.
- La HUD è solo visiva (`aria-hidden`): i lettori di schermo ricevono il valore finale di ogni gesto da una regione `aria-live` nascosta.
- Il canvas ha `role="img"` e descrive i gesti; il gioco sta in `<main>` ed è `inert` finché è visibile la splash.
- Dopo "Accendi il fuoco" il focus passa al pulsante di accensione.
- Le scorciatoie a un tasto sono sempre attive (scelta di prodotto) e non agiscono con un foglio aperto. Non si possono spegnere: WCAG 2.1.4 resta aperto.
- Con prefers-reduced-motion niente movimenti: i valori cambiano senza animazione, foglio e splash compaiono e spariscono subito.
- Tastiera: Spazio accende e spegne, H nasconde l'interfaccia, F schermo intero, M audio, + e − intensità, frecce sinistra/giù/destra per il vento.
