# 🍕 Ore Pizzeria

App per tracciare le ore di lavoro in pizzeria, con riepilogo settimanale e calcolo automatico della paga.

## Funzionalità

- **Calendario mensile** — visualizza i giorni lavorati con le ore registrate
- **Input ore e minuti** — inserisci le ore lavorate per ogni giornata
- **Riepilogo settimanale** — somma automatica delle ore per ogni settimana (lun→dom)
- **Paga oraria configurabile** — imposta la tua tariffa e vedi il totale € in tempo reale
- **Totale mensile** — ore totali, giorni lavorati e guadagno del mese
- **Mobile-first** — ottimizzata per iPhone

## Deploy su Streamlit Cloud (gratis)

1. **Fork o crea un repo GitHub** con questi file
2. Vai su [share.streamlit.io](https://share.streamlit.io)
3. Clicca **"New app"**
4. Seleziona il tuo repo, branch `main`, file `app.py`
5. Clicca **Deploy**

L'app sarà disponibile a un URL tipo `https://tuonome-pizzeria-ore.streamlit.app`

### Aggiungi alla Home Screen di iPhone

1. Apri l'URL dell'app in Safari
2. Tocca l'icona **Condividi** (quadrato con freccia)
3. Seleziona **"Aggiungi alla schermata Home"**
4. L'app apparirà come un'icona sulla Home

## Esegui in locale

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Struttura

```
pizzeria-ore/
├── app.py                  # App principale
├── requirements.txt        # Dipendenze
├── .streamlit/
│   └── config.toml         # Tema e configurazione
└── README.md
```

## Note

I dati vengono salvati in un file `data.json` locale. Su Streamlit Cloud i dati persistono finché l'app non viene re-deployata. Per persistenza a lungo termine, considera di collegare un database esterno (es. Google Sheets, Supabase).
