# 8-bit fire

Fuoco in pixel (algoritmo del fuoco di Doom) per telefono, PWA. Rispondi in italiano.

## Dove si lavora
- **Modifica solo `src/app.html`.** È l'app in formato artifact (niente doctype né head). L'audio è segnato con `{{AUDIO_LOW}}` e `{{AUDIO_HIGH}}`: non incollare mai base64 nei file sorgente e non leggere `dist/`, `docs/play.html` o i file `*_App_vNN.html` per intero (sono ~2 MB). Per cercare nel sorgente usa `grep -n` e `sed -n 'a,bp'`.
- Non modificare a mano `docs/play.html`, `docs/sw.js`, `dist/`: li genera `tools/build.py`.
- Design system: `design-system/` (specchio locale) e artifact https://claude.ai/artifact/TpYa1XftPX4Qgz9dA1XhXQ. Se cambiano token, componenti o comportamenti, aggiornali entrambi. Prima di pubblicare rileggi l'indice e aggiorna `lastChange`.

## Routine dopo ogni modifica
1. `python3 tools/build.py` (aggiunge `--snapshot` per salvare una nuova versione `AAAA-MM-GG_8-bit-fire_App_vNN.html`, solo ai traguardi).
2. Pubblica `dist/app-artifact.html` sull'artifact https://claude.ai/artifact/5o4Hq4Dfce5iaVeKwnWdHo (stesso `url`).
3. `tools/sync.sh "messaggio"`: ricostruisce, fa commit e push. GitHub Pages serve `main` `/docs`.

## Convenzioni
- File: `AAAA-MM-GG_Progetto_Descrizione_vNN`.
- Griglia di 8 px: margine esterno 24, distanze 16, tap area 48, primari 56. Un solo accento: `#e2561a`. Font: IBM Plex Mono, Silkscreen solo per il titolo.
- Animazioni: `ease-out`, `ease-drawer`, `ease-in-out`; mai ease-in, mai sopra i 300 ms per la UI.
- Accessibilità: WCAG 2.1 AA, tap area ≥ 48, `prefers-reduced-motion` rispettato.
- Repo: https://github.com/MattiaPompei/8-bit-fire (pubblico). Link online: https://mattiapompei.github.io/8-bit-fire/play.html
- Critica di design e audit di accessibilità si rifanno solo ai traguardi, non a ogni ritocco.
