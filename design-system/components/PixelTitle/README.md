# PixelTitle

Il titolo della splash in stile insegna arcade: pixel, due toni, contorno e ombra a gradino.

## Costruzione

- `pixel` (Silkscreen 700), maiuscolo, `title-pixel` a dimensione fluida clamp(21px, 9.375vw, 60px): il testo misura circa 7em, cioè circa due terzi della larghezza dello schermo.
- Due toni con `background-clip: text`: `focus` sopra, `accent` dal 63% in giù.
- Contorno di 1/16 em in `bg` sui quattro lati e ombra a gradino di due passi in basso a destra, con `drop-shadow` a raggio 0 (un `text-shadow` coprirebbe il gradiente).

## Uso

- Solo il nome `8-bit fire`, solo nella splash, centrato nello spazio sopra la CTA.

## Da non fare

- Non usarlo per titoli di sezione o testo di interfaccia.
