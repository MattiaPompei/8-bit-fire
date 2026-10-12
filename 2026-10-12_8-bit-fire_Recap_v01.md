# 8-bit fire — recap per riprendere il lavoro

Aggiornato: 2026-10-12. Per riprendere, apri una sessione di Claude Code in questa cartella e scrivi: "leggi il recap e CLAUDE.md, poi riprendiamo da…".

## Cos'è
Un fuoco in pixel (algoritmo del fuoco di Doom) da tenere acceso sul telefono. Gesti: due tocchi spengono, trascina in su o in giù per l'intensità, a sinistra o a destra per il vento. Audio: due registrazioni SoundReality (royalty free) in dissolvenza secondo l'intensità. È una PWA installabile e funziona offline.

## Link
- Gioca (GitHub Pages): https://mattiapompei.github.io/8-bit-fire/play.html
- Pagina del progetto: https://mattiapompei.github.io/8-bit-fire/
- Repository (pubblico): https://github.com/MattiaPompei/8-bit-fire
- Artifact dell'app su Claude: https://claude.ai/artifact/5o4Hq4Dfce5iaVeKwnWdHo
- Design system su Claude (privato): https://claude.ai/artifact/TpYa1XftPX4Qgz9dA1XhXQ

## Stato
- App completa alla versione v02: splash, pagina Controlli, impostazioni (foglio dal basso su telefono, pannello a destra su desktop), audio, schermo intero, tastiera.
- Critica di design e audit di accessibilità (WCAG 2.1 AA) fatti e applicati.
- Design system pubblicato (versione 8) e allineato all'app.
- PWA attiva e verificata online con un browser automatico. Non provata su un iPhone o Android reali.

## Come si lavora
- Si modifica solo `src/app.html` (l'audio è un segnaposto). Non toccare a mano `docs/play.html`, `docs/sw.js`, `dist/`.
- Dopo una modifica: `python3 tools/build.py`, poi pubblicare `dist/app-artifact.html` sull'artifact (stesso link), poi `tools/sync.sh "messaggio"` per commit e push.
- Versioni numerate (`*_App_vNN.html`): si salvano solo ai traguardi con `python3 tools/build.py --snapshot`.
- Se cambiano token, componenti o comportamenti, aggiornare anche `design-system/` e l'artifact del design system.
- Dettagli e convenzioni: `CLAUDE.md`.

## Decisioni da non rimettere in discussione
- Tema unico scuro, un solo accento arancio `#e2561a`; IBM Plex Mono per la UI, Silkscreen solo per il titolo.
- Griglia di 8 px: margine esterno 24, distanze 16, tap area 48, primari 56.
- Animazioni: mai ease-in, UI sotto i 300 ms.
- Impostazioni e Controlli si aprono da destra; Controlli aperto dalle impostazioni sta dentro il pannello con tasto Indietro.
- Esci in alto a sinistra; audio e schermo intero in alto a destra.
- Mix audio: 95/5 a intensità 1, 60/40 a 7, 25/75 a 10.

## Cartella
| Percorso | Contenuto |
|---|---|
| `src/app.html` | sorgente dell'app |
| `tools/` | `build.py`, `sync.sh`, `make_icons.py` |
| `docs/` | pagine pubblicate su GitHub Pages, manifest, service worker, icone |
| `audio/` | mp3 originali, m4a incorporati, audio muto per iPhone |
| `design-system/` | token, brand book, componenti, icone SVG |
| `*_App_v01/v02.html` | versioni salvate |
| `*_Design-critique_v01.md`, `*_Accessibility-review_v01.md` | critica e audit |
| `CLAUDE.md`, `README.md` | istruzioni per Claude Code, presentazione del repo |

## Da fare / idee
- Provare l'installazione su un iPhone e un Android reali: icona, schermo intero, audio con tasto silenzioso.
- Verificare con VoiceOver o NVDA (l'audit è fatto solo sul codice e su screenshot).
- Da decidere: se la pagina del progetto debba avere un dominio o un'immagine di anteprima per la condivisione.
