# 8-bit fire

Un fuoco in pixel da tenere acceso sul telefono: si accende, si scalda e si piega al vento con un dito. Una sola pagina HTML, senza dipendenze, con il suono del fuoco incorporato.

- **Gioca**: [docs/play.html](docs/play.html) (con GitHub Pages attivo: `https://<utente>.github.io/8-bit-fire/play.html`)
- **Pagina del progetto**: [docs/index.html](docs/index.html)
- **Versione pubblicata su Claude**: https://claude.ai/artifact/5o4Hq4Dfce5iaVeKwnWdHo
- **Design system** (privato): https://claude.ai/artifact/TpYa1XftPX4Qgz9dA1XhXQ

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
| `2026-10-11_8-bit-fire_App_v02.html` | versione attuale dell'app (file sorgente) |
| `2026-10-11_8-bit-fire_App_v01.html` | versione precedente |
| `docs/play.html` | copia dell'app servita da GitHub Pages |
| `docs/index.html` | pagina con tutte le informazioni sul progetto |
| `design-system/` | token, brand book, sezioni (fuoco, interazioni, animazioni, audio), componenti con anteprime, icone SVG |
| `audio/` | registrazioni originali (mp3), versioni AAC incorporate nell'app (m4a), audio muto per iPhone |
| `*_Design-critique_v01.md` | critica di design |
| `*_Accessibility-review_v01.md` | audit WCAG 2.1 AA |

I file seguono la convenzione `AAAA-MM-GG_Progetto_Descrizione_vNN`. Quando aggiorni l'app, copia la nuova versione anche in `docs/play.html`.

## Design system in breve

- Tema unico scuro; un solo accento, l'arancio del fuoco `#e2561a`.
- IBM Plex Mono per l'interfaccia, Silkscreen solo per il titolo pixel.
- Griglia di 8px: margine esterno 24, distanze 16, tap area 48, pulsanti primari 56.
- Tre curve: `ease-out` per entrate e pressioni, `ease-drawer` per i pannelli, `ease-in-out` per il fuoco che torna al suo posto. Mai ease-in.

## Crediti

- Suoni del fuoco: SoundReality (`fire-sound-334130`, `blazing-fire-394355`). Verifica che la licenza consenta la pubblicazione in un repository pubblico.
- Algoritmo del fuoco: tecnica del fuoco di Doom (PSX).
- Progetto e direzione: Mattia. Sviluppo con Claude.
