# 8-bit fire

Un fuoco in pixel da tenere acceso sul telefono: si accende, si scalda e si piega al vento con un dito. Una sola pagina HTML, senza dipendenze, con il suono del fuoco incorporato.

- **Gioca**: https://mattiapompei.github.io/8-bit-fire/play.html
- **Pagina del progetto**: https://mattiapompei.github.io/8-bit-fire/
- **Versione pubblicata su Claude**: https://claude.ai/artifact/5o4Hq4Dfce5iaVeKwnWdHo
- **Design system** (privato): https://claude.ai/artifact/TpYa1XftPX4Qgz9dA1XhXQ

## Installa sul telefono

8-bit fire è una PWA: si installa dal browser, senza store, e dopo la prima apertura funziona offline.

- **iPhone e iPad**: apri il link in Safari → Condividi → "Aggiungi alla schermata Home".
- **Android**: apri il link in Chrome → "Installa app" (oppure ⋮ → "Aggiungi a schermata Home").
- **Computer**: in Chrome o Edge, icona di installazione nella barra degli indirizzi.

## Come si gioca

| Gesto o controllo | Effetto |
|---|---|
| Tocco al centro del fuoco | riaccende il fuoco spento; a fuoco acceso servono due tocchi per spegnerlo |
| Trascina in su o in giù | intensità da 1 a 10 |
| Trascina a sinistra o a destra | vento: sinistra, fermo, destra |
| A fuoco spento, trascina in su | riaccende da intensità 1 |
| Pannello | vento, intensità, accensione, impostazioni |
| Impostazioni | altezza delle fiamme (10-100%), celle (4-48 px), velocità (20-60 fps) |
| In alto | Esci a sinistra; audio e schermo intero a destra |
| Tastiera | Spazio accende e spegne, + e − intensità, ← ↓ → vento, F schermo intero, M audio, H nasconde l'interfaccia, Esc chiude i pannelli |

## Come funziona

Il fuoco è l'algoritmo classico del fuoco di Doom: una griglia di celle da 0 a 36, ognuna con un colore della palette dal nero al bianco. La riga in fondo vale la temperatura di base; a ogni passo ogni cella prende il valore della cella sotto, sottrae a caso 0, 1 o 2 e si sposta dello stesso numero di colonne nel verso del vento. La base insegue l'intensità con una costante di tempo di 120 ms, così ogni cambio è morbido.

L'audio sono due registrazioni in loop, mixate in dissolvenza secondo l'intensità (95/5 a intensità 1, 60/40 a 7, 25/75 a 10), più due suoni di accensione e spegnimento generati con Web Audio.

## Struttura

| Percorso | Contenuto |
|---|---|
| `src/app.html` | sorgente dell'app (l'audio è un segnaposto, si modifica solo questo file) |
| `*_App_vNN.html` | versioni salvate con `tools/build.py --snapshot` |
| `docs/play.html` | l'app per GitHub Pages, generata da `tools/build.py` |
| `docs/manifest.webmanifest`, `docs/sw.js`, `docs/icons/` | PWA: manifest, service worker (offline), icone |
| `tools/` | `build.py` (inserisce l'audio e genera `dist/`, `docs/play.html`, `docs/sw.js`), `sync.sh` (build, commit e push), `make_icons.py` (icone pixel) |
| `CLAUDE.md` | istruzioni di progetto per Claude Code |
| `docs/index.html` | pagina con tutte le informazioni sul progetto |
| `design-system/` | token, brand book, sezioni (fuoco, interazioni, animazioni, audio), componenti con anteprime, icone SVG |
| `audio/` | registrazioni originali (mp3), versioni AAC incorporate nell'app (m4a), audio muto per iPhone |
| `*_Design-critique_v01.md` | critica di design |
| `*_Accessibility-review_v01.md` | audit WCAG 2.1 AA |

I file seguono la convenzione `AAAA-MM-GG_Progetto_Descrizione_vNN`. Dopo ogni modifica a `src/app.html` lancia `tools/sync.sh "messaggio"`: ricostruisce l'app con l'audio, rigenera `docs/play.html`, aggiorna la cache del service worker (così i telefoni ricevono l'aggiornamento), poi fa commit e push.

## Design system in breve

- Tema unico scuro; un solo accento, l'arancio del fuoco `#e2561a`.
- IBM Plex Mono per l'interfaccia, Silkscreen solo per il titolo pixel.
- Griglia di 8px: margine esterno 24, distanze 16, tap area 48, pulsanti primari 56.
- Tre curve: `ease-out` per entrate e pressioni, `ease-drawer` per i pannelli, `ease-in-out` per il fuoco che torna al suo posto. Mai ease-in.

## Crediti

- Suoni del fuoco: SoundReality (`fire-sound-334130`, `blazing-fire-394355`), royalty free.
- Algoritmo del fuoco: tecnica del fuoco di Doom (PSX).
- Progetto e direzione: Mattia. Sviluppo con Claude.
