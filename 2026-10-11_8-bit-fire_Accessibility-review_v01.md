## Accessibility Audit: 8-bit fire
**Standard:** WCAG 2.1 AA | **Date:** 2026-10-11

Pagina: https://claude.ai/artifact/5o4Hq4Dfce5iaVeKwnWdHo. Audit sul codice e su screenshot in formato telefono (375×812); non testato con VoiceOver o NVDA reali.

### Summary
**Issues found:** 11 | **Critical:** 1 | **Major:** 5 | **Minor:** 5

### Findings

#### Perceivable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | Testo della HUD sopra la base bianca del fuoco: chiave 2.6:1, valore 4.3:1 (16px, non è testo grande). Succede a intensità alta, proprio dove la HUD si trova (32px sopra la base). | 1.4.3 Contrast (Minimum) | 🔴 Critical | Fondo della HUD da `rgba(20,18,16,0.6)` a `rgba(20,18,16,0.88)`, oppure `panel` pieno. |
| 2 | Il canvas del fuoco ha `aria-label` ma nessun ruolo: molti lettori di schermo lo ignorano. | 1.1.1 Non-text Content | 🟡 Major | Aggiungi `role="img"` al canvas. |
| 3 | Manca il landmark principale: l'app non è dentro `<main>`. | 1.3.1 Info and Relationships | 🟢 Minor | Avvolgi area del fuoco e pannello in `<main>`. |

#### Operable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 4 | Scorciatoie a un solo tasto (Spazio, H, F, M, +, −) sempre attive, senza modo di disattivarle o rimapparle: chi usa il controllo vocale le attiva per sbaglio. | 2.1.4 Character Key Shortcuts | 🟡 Major | Attivale solo quando il focus è sull'area del fuoco, oppure aggiungi un interruttore "Scorciatoie da tastiera" nel foglio impostazioni. |
| 5 | Dopo "Accendi il fuoco" il focus resta sul pulsante della splash, che viene nascosto: il focus si perde. | 2.4.3 Focus Order | 🟡 Major | A partenza avvenuta sposta il focus sul pulsante di accensione (o sull'area del fuoco con `tabindex="-1"`). |
| 6 | Con il telefono in orizzontale o con il testo ingrandito il foglio impostazioni supera l'altezza dello schermo; la pagina non scorre (`overflow: hidden`) e i controlli in fondo diventano irraggiungibili. | 1.4.10 Reflow | 🟡 Major | Sul foglio `max-height: 100%` e `overflow-y: auto`. |
| 7 | L'anello di focus `focus` (#ffd9a8) è debole sopra la base chiara del fuoco, per i pulsanti in vetro se il fuoco li raggiunge. | 2.4.7 Focus Visible | 🟢 Minor | Aggiungi un secondo anello scuro: `outline: 2px solid var(--focus); box-shadow: 0 0 0 4px var(--bg)`. |
| — | Trascinamenti sul fuoco: hanno alternative a puntatore singolo (slider, pulsanti). Tap area tutte ≥ 48px. Esc chiude il foglio e il focus resta intrappolato nel dialog. | 2.5.1, 2.5.5, 2.1.2 | ✅ Pass | — |

#### Understandable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 8 | Il pulsante di accensione cambia etichetta ("Spegni il fuoco" / "Accendi il fuoco") e ha anche `aria-pressed`: il lettore annuncia "Spegni il fuoco, premuto", contraddittorio. | 4.1.2 Name, Role, Value | 🟡 Major | Tieni l'etichetta che dice l'azione e togli `aria-pressed`, oppure un'etichetta fissa "Fuoco" con `aria-pressed`. |
| 9 | Audio e schermo intero fanno lo stesso: "Disattiva audio, premuto". | 4.1.2 Name, Role, Value | 🟢 Minor | Etichetta fissa ("Audio", "Schermo intero") con `aria-pressed`. |

#### Robust
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 10 | La HUD è `aria-live="polite"` e cambia a ogni passo del trascinamento: il lettore di schermo viene inondato di annunci. | 4.1.3 Status Messages | 🟢 Minor | Togli `aria-live` dalla HUD e annuncia il valore finale al rilascio in una regione nascosta. |
| 11 | Gli slider Altezza e Velocità non hanno `aria-valuetext` con l'unità (viene letto "100", "20"). | 4.1.2 Name, Role, Value | 🟢 Minor | `aria-valuetext` "100 per cento", "20 fotogrammi al secondo". |

### Color Contrast Check
| Element | Foreground | Background | Ratio | Required | Pass? |
|---------|-----------|------------|-------|----------|-------|
| Valori (Sinistra, 7/10) | #f4f1ec | #141210 pannello | 16.6:1 | 4.5:1 | ✅ |
| Chiavi (Vento, Intensità) | #c4bcb2 | #141210 | 9.9:1 | 4.5:1 | ✅ |
| Testo dei pulsanti primari | #1a0a02 | #e2561a | 5.1:1 | 4.5:1 | ✅ |
| Primario in hover | #1a0a02 | #ef6a2c | 6.2:1 | 4.5:1 | ✅ |
| Icone dei pulsanti secondari | #f4f1ec | #2c2723 | 13.1:1 | 3:1 | ✅ |
| Barra di selezione del vento | #e2561a | #2c2723 | 3.9:1 | 3:1 | ✅ |
| Parte piena del binario | #e2561a | #141210 | 5.0:1 | 3:1 | ✅ |
| Cursore degli slider | #f4f1ec | #141210 | 16.6:1 | 3:1 | ✅ |
| Anello di focus | #ffd9a8 | #141210 | 14.0:1 | 3:1 | ✅ |
| HUD chiave, sopra fuoco nero | #c4bcb2 | vetro su #070707 | 10.3:1 | 4.5:1 | ✅ |
| HUD chiave, sopra fuoco giallo | #c4bcb2 | vetro su rgb(183,183,47) | 4.2:1 | 4.5:1 | ❌ |
| HUD chiave, sopra fuoco bianco | #c4bcb2 | vetro su #ffffff | 2.6:1 | 4.5:1 | ❌ |
| HUD valore, sopra fuoco bianco | #f4f1ec | vetro su #ffffff | 4.3:1 | 4.5:1 | ❌ |
| Icone/Esci in vetro, sopra fuoco bianco | #f4f1ec | vetro su #ffffff | 7.3:1 | 3:1 | ✅ |
| Icona audio attivo, sopra fuoco bianco | #ff9a66 | vetro su #ffffff | 3.95:1 | 3:1 | ✅ |

### Keyboard Navigation
| Element | Tab Order | Enter/Space | Escape | Arrow Keys |
|---------|-----------|-------------|--------|------------|
| Splash: Accendi il fuoco | 1 (ha il focus all'apertura) | parte l'app | — | — |
| Audio, Schermo intero, Esci | 1-3 | attivano | — | — |
| Vento (radiogroup) | 4-6 | seleziona | — | ← ↓ → cambiano il vento (scorciatoie globali) |
| Intensità (slider) | 7 | — | — | cambiano il valore |
| Accendi/Spegni, Impostazioni | 8-9 | attivano; Spazio è anche scorciatoia globale | — | — |
| Foglio impostazioni | focus intrappolato nel dialog | — | chiude | slider |

### Screen Reader
| Element | Announced As | Issue |
|---------|-------------|-------|
| Canvas del fuoco | spesso nulla | manca `role="img"` (#2) |
| Pulsante di accensione | "Spegni il fuoco, interruttore premuto" | stato e azione contraddittori (#8) |
| Audio | "Disattiva audio, premuto" | idem (#9) |
| Vento | "Vento, gruppo di pulsanti di opzione, Verso sinistra, selezionato" | ok |
| Intensità | "Intensità, regolatore, 7 su 10" | ok |
| Altezza / Velocità | "Altezza, regolatore, 100" | manca l'unità (#11) |
| HUD | annuncia ogni valore durante il trascinamento | troppo verbosa (#10) |

### Priority Fixes
1. **HUD leggibile sopra il fuoco** — colpisce chiunque usi i gesti a intensità alta; il valore che stai regolando diventa illeggibile.
2. **Foglio scorrevole in orizzontale e con testo grande** — chi ingrandisce il testo non raggiunge "Ripristina valori predefiniti" né la Velocità.
3. **Focus dopo la partenza e scorciatoie a un tasto** — chi naviga da tastiera perde il punto in cui si trova; chi usa il controllo vocale può spegnere il fuoco o nascondere l'interfaccia per sbaglio.
4. **Nomi e stati coerenti per i pulsanti toggle** — accensione, audio e schermo intero annunciano stato e azione insieme.
5. **Rifiniture** — `role="img"` sul canvas, `<main>`, unità negli slider, HUD non verbosa.
