# Splash

La schermata d'apertura: il fuoco in loop dietro un velo, il titolo pixel e la CTA che fa partire l'interfaccia.

## Struttura

- Sotto: un loop di 2 secondi (40 frame a 20 fps) del fuoco con le impostazioni predefinite (intensità 7, vento a sinistra, altezza 100%, celle 8 px), registrato all'avvio.
- Sopra: velo `veil` al 50%.
- Titolo PixelTitle con il centro a 1/3 dell'altezza; PrimaryButton in fondo, a `space-24` dai lati e dal fondo più il margine di sicurezza: gli stessi margini e lo stesso pulsante del pannello.
- In alto a destra il pulsante "i" (secondario in vetro, `aria-label` "Controlli"), a `space-24` dai bordi più i margini di sicurezza: apre la pagina Controlli.
- Copre tutto (`z-splash`); il gioco dietro è `inert`; il fuoco reale aspetta fermo dietro, a `scale-fire-prestart`.

## Movimento

- Entrata: titolo e CTA salgono di 16px e compaiono (`dur-splash-rise`, CTA +60ms, `ease-out`).
- Uscita al tocco della CTA: titolo e CTA salgono e svaniscono (`dur-splash-exit`, CTA +40ms), la splash sfuma sul fuoco vero (`dur-surface`, ritardo 160ms), il pannello sale, il fuoco si assesta al 100% (`dur-surface`), i pulsanti in alto compaiono per ultimi (`dur-detail`, ritardo 400ms). Tutto con `ease-out`.
- Il fuoco parte sempre acceso, con intensità e vento predefiniti.

- Esci, dalla pagina del fuoco, riporta qui: la splash torna subito in dissolvenza (`dur-detail`, nessun ritardo) e titolo e CTA risalgono.

## Da non fare

- Niente altri testi, sottotitoli o loghi: titolo e CTA bastano.
