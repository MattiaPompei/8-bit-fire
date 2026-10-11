# Hud

L'etichetta che ripete sul fuoco la grandezza che stai cambiando con un gesto, o lo stato dopo un tocco.

## Uso

- Centrata in basso nell'area del fuoco, a `space-32` dal fondo; a schermo intero a `space-32` dal fondo dello schermo.
- Chiave in `key` color `label`, valore in `value` color `fg`. Valori: "Intensità N/10", "Vento Sinistra/Fermo/Destra", "Fuoco Acceso/Spento".
- Compare in `dur-state` (solo opacità, anche con movimento ridotto); resta finché dura il gesto, poi sparisce 700ms dopo il rilascio (`dur-hud-hold` dopo un tocco).
- Il valore usa la stessa rotazione o lo stesso scorrimento di ValueLabel; al cambio di grandezza il primo valore compare fermo.
- Fondo `hud` (88%): leggibile anche sulla base bianca del fuoco.
- Solo visiva (`aria-hidden`): il valore finale di ogni gesto va a una regione `aria-live` nascosta, così i lettori di schermo non ricevono ogni passo.
- Messaggi speciali: "Fuoco · Tocca ancora per spegnere" al primo tocco a fuoco acceso; "Gesti · Trascina il fuoco" una sola volta, alla prima partenza.

## Da non fare

- Non usarla come notifica generica: parla solo dei gesti sul fuoco.
