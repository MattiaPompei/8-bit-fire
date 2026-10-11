# ControlPanel

Il pannello in basso: tre righe, dal meno al più importante scendendo verso il pollice.

## Struttura

1. Vento (WindSelector)
2. Intensità (IntensitySlider)
3. Accensione (PrimaryButton) e impostazioni

- Fondo `panel`, bordo superiore `line`, padding `space-24` su tutti i lati (lo stesso margine della splash), righe a `space-16`, contenuto largo al massimo `size-panel`. Circa 232px di altezza: il fuoco tiene circa il 72% di uno schermo da 844px.
- Ancorato in basso, alto quanto il contenuto, mai scrollabile. A schermo intero e con H sparisce.
- Alla partenza sale dal basso (`dur-surface`, ritardo 200ms, `ease-out`).

## Da non fare

- Non aggiungere righe: le impostazioni generali vanno nel foglio (SettingsSheet).
