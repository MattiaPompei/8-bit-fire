# Animazioni

Ogni movimento comunica un cambio di stato. Tre curve: `ease-out` per entrate, uscite e pressioni, `ease-drawer` per il foglio e i valori, `ease-in-out` per il fuoco che torna al suo posto. Mai ease-in. Anima solo transform e opacity; le animazioni che possono essere interrotte (foglio) sono transizioni, non keyframes, così ripartono da dove si trovano.

## Interfaccia

| Momento | Cosa si muove | Durata | Curva |
|---|---|---|---|
| Pressione di un pulsante | scala `scale-press`; nei secondari fondo `btn-press` e icona giù di 1px | `dur-press` | `ease-out` |
| Selezione del vento | la barra `shadow-selected` compare senza transizione | istantaneo | — |
| Cambio numero (intensità, altezza, celle, velocità) | il vecchio esce in alto e il nuovo entra dal basso se il valore sale, il contrario se scende; riga ritagliata | `dur-roll` | `ease-drawer` |
| Cambio vento | la parola esce nel verso del vento (60% della sua larghezza, sfumando), la nuova entra dal lato opposto | `dur-roll` | `ease-drawer` |
| HUD | compare e scompare in dissolvenza | `dur-state` | ease |
| Apertura foglio | telefono: foglio da sotto lo schermo, fondo `backdrop` in dissolvenza, fuoco al 75% e su un frame dopo il ridimensionamento della griglia. Desktop: pannello da destra (`translateX(100%)` → 0), fuoco fermo | `dur-sheet-in` | `ease-drawer` |
| Chiusura foglio | foglio giù (desktop: a destra) e fondo in dissolvenza, da dove si trovano | `dur-sheet-out` | `ease-out` |
| Pagina Controlli | entra da destra (`translateX(100%)` → 0) ed esce a destra, con le curve del foglio. Aperta dalle impostazioni su desktop occupa lo stesso pannello: il contenuto delle impostazioni scivola a sinistra del 30% e si attenua; i gruppi entrano salendo di 16px, 40ms l'uno dall'altro | `dur-sheet-in`, `dur-sheet-out`, `dur-reveal` | `ease-drawer`, `ease-out` |
| Dimostrazioni dei gesti | un dito su un fuoco in miniatura: tocco doppio, su e giù (il fuoco cresce), ai lati (il fuoco si piega), su a fuoco spento (il fuoco si accende). In loop, solo a pagina aperta | `dur-demo` | `ease-in-out` (il tocco `ease-out`) |
| Ritorno del fuoco | fuoco giù e al 100% | `dur-fire-return` | `ease-in-out` |

- Valori senza animazione durante il trascinamento sul fuoco e per i tasti: sono azioni rapide e ripetute. Durante un'animazione un nuovo valore la sostituisce.
- Quando la HUD cambia grandezza (da Intensità a Vento) il primo valore compare fermo.

## Splash e partenza

| Momento | Cosa si muove | Durata | Curva |
|---|---|---|---|
| Entrata splash | titolo e CTA salgono di 16px e compaiono; CTA +60ms | `dur-splash-rise` | `ease-out` |
| Tocco su Accendi il fuoco | titolo e CTA salgono di 20px e svaniscono (CTA +40ms); la splash sfuma dopo 160ms | `dur-splash-exit`, `dur-surface` | `ease-out` |
| Partenza | pannello sale dal basso (ritardo 200ms); fuoco da 108% a 100%; pulsanti in alto compaiono (ritardo 400ms) | `dur-surface`, `dur-detail` | `ease-out` |
| Esci | la splash ricompare subito in dissolvenza, titolo e CTA risalgono; il pannello scende; il fuoco torna a `scale-fire-prestart` | `dur-detail`, `dur-splash-rise`, `dur-surface` | `ease-out` |

## Prestazioni

- Il canvas del fuoco ha `will-change: transform` solo mentre si muove; lo toglie a fine transizione.
- Gli hover cambiano solo colore e contorno, e solo su dispositivi con puntatore fine (`hover: hover` e `pointer: fine`).
- La base del fuoco insegue l'intensità con una costante di tempo di 120ms: ogni cambio è morbido anche senza animazioni CSS.

## Movimento ridotto

Con prefers-reduced-motion niente spostamenti e niente scale; le dimostrazioni dei gesti restano ferme sulla loro posa: foglio e splash compaiono e spariscono in dissolvenza (`dur-reduced`), la HUD mantiene la sua dissolvenza, i valori cambiano senza rotazione.
