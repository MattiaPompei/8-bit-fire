## Design Critique: 8-bit fire

Pagina: https://claude.ai/artifact/5o4Hq4Dfce5iaVeKwnWdHo · Fase: rifinitura · Contesto: giocattolo grafico per telefono in verticale, un fuoco in pixel da accendere e regolare con le dita.

### Overall Impression
Il fuoco domina come deve e l'interfaccia scura, monospaziata e su griglia di 8px gli lascia la scena. L'occasione più grande sta nei gesti sul fuoco, potenti ma invisibili, e nel pulsante "Spegni il fuoco", che è l'elemento più vistoso del pannello pur essendo l'azione che chiude l'esperienza.

### Usability
| Finding | Severity | Recommendation |
|---------|----------|----------------|
| I gesti sul fuoco (tocco al centro, trascinamento verticale e orizzontale) non hanno nessun indizio visivo: chi non li conosce usa solo il pannello. | 🟡 Moderate | Alla prima partenza mostra per 3 secondi nella HUD "Trascina per intensità e vento · tocca per spegnere", poi mai più (salvato nel browser). |
| "Spegni il fuoco" è pieno arancio anche a fuoco acceso: l'azione più evidente del pannello è quella che spegne. | 🟡 Moderate | Tieni forma, misure e testo del primario uniformi, ma a fuoco acceso usa un fondo neutro (`btn`) e riserva `accent` ad "Accendi il fuoco". |
| Un tocco al centro del fuoco lo spegne: chi tocca il fuoco "per giocare" lo spegne per sbaglio. La HUD lo segnala, ma l'azione è già avvenuta. | 🟢 Minor | Valuta il doppio tocco per spegnere, oppure lascia il tocco singolo solo per riaccendere. |
| Con il telefono in orizzontale o con lo zoom del testo alto, il foglio impostazioni può superare l'altezza dello schermo e venire tagliato senza scorrimento. | 🟡 Moderate | `max-height` pari all'altezza disponibile e `overflow-y: auto` sul foglio. |
| Esci sta accanto a schermo intero, senza conferma: un tocco sbagliato riporta alla splash e azzera intensità e vento. | 🟢 Minor | Accettabile perché si riparte con un tocco; se diventa un problema, sposta Esci a sinistra o separalo con più spazio. |
| Le scorciatoie da tastiera (Spazio, H, F, M, +, −, frecce) non sono indicate da nessuna parte. | 🟢 Minor | Una riga nel foglio impostazioni: "Tastiera: Spazio accende, H nasconde, F schermo intero, M audio". |

### Visual Hierarchy
- **What draws the eye first**: il fuoco, poi il pulsante arancio. Il fuoco come primo elemento è corretto; il pulsante arancio come secondo è troppo forte quando la sua azione è "spegni".
- **Reading flow**: dall'alto verso il basso, fuoco → vento → intensità → pulsante. Le righe del pannello si leggono bene grazie alla colonna fissa da 96px chiave/valore e al rapporto 12/16px tra chiave e valore.
- **Emphasis**: la barra arancio sotto il vento selezionato e la parte piena del binario dell'intensità sono accenti misurati e giusti. Nella splash il titolo pixel e la CTA in fondo sono chiari e non competono.

### Consistency
| Element | Issue | Recommendation |
|---------|-------|----------------|
| Pulsanti in alto a destra | Esci è l'unico secondario di testo tra due icone. È voluto (un'icona di uscita sarebbe ambigua), ma rompe la fila. | Va bene così; documentato in TopActions. In alternativa, un'icona "freccia che esce" con etichetta accessibile "Esci". |
| Cursori degli slider | Intensità ha la fiamma, gli altri slider un quadrato arrotondato da 24px. | Coerente con il ruolo (l'intensità è il controllo del fuoco); nessuna modifica. |
| Distanze dai bordi | Pulsanti in alto a 24px, HUD a 32px dal fondo dell'area: entrambi sulla griglia di 8. | Nessuna modifica. |
| Pulsante di accensione | Uniformato al primario della splash, ma il colore non comunica più lo stato. | Vedi Usability: fondo neutro a fuoco acceso. |
| HUD sopra il fuoco | Vetro al 60% di opacità: sopra la base bianca del fuoco perde contrasto (vedi Accessibility). | Opacità all'88% o fondo `panel` pieno. |

### Accessibility
- **Color contrast**: il pannello è ottimo (testo 16.6:1, chiavi 9.9:1, testo su arancio 5.1:1). La HUD sopra la base bianca del fuoco scende a 2.6:1 per la chiave e 4.3:1 per il valore: non passa. Dettagli nell'audit di accessibilità.
- **Touch targets**: tutti almeno 48px, con 16px tra tap area diverse. Passa.
- **Text readability**: IBM Plex Mono, chiavi 12px e valori 16px con interlinea 1.2; leggibili. Il titolo pixel è decorativo e il suo testo è anche nel titolo della pagina.

### What Works Well
- Il fuoco occupa sempre lo spazio disponibile, anche con le impostazioni aperte e a schermo intero.
- Griglia di 8px applicata con disciplina: margini uniformi da 24px tra splash e pagina, primario identico nei due contesti.
- Movimento coerente dopo la revisione: tre curve, durate brevi sull'interfaccia, nessun ease-in, dissolvenze con movimento ridotto.
- Stati dei pulsanti secondari chiari e distinti senza bordi a riposo (barra di selezione, contorno solo in hover).
- Il suono segue l'intensità e si abbassa con le impostazioni aperte: rafforza il gesto senza essere invadente.

### Priority Recommendations
1. **Contrasto della HUD sopra il fuoco** — è l'unico testo che oggi non si legge nel caso peggiore (base bianca a intensità alta). Porta il vetro all'88% di opacità.
2. **Rendere scopribili i gesti** — sono il modo più diretto di giocare con il fuoco ma nessuno li trova. Un suggerimento una tantum nella HUD basta.
3. **Ridurre l'enfasi di "Spegni il fuoco"** — fondo neutro a fuoco acceso, arancio solo per "Accendi": l'accento torna a indicare l'azione che vuoi incoraggiare.
