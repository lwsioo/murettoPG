# Muretto di Perugia - Gestione Tornei Freestyle & Generatore Parole

[![Ultimo Commit](https://img.shields.io/github/commit-date/lwsioo/murettoPG.svg?style=flat-square)](https://github.com/lwsioo/murettoPG/commits/main)
[![Linguaggi](https://img.shields.io/github/languages/top/lwsioo/murettoPG.svg?style=flat-square)](https://github.com/lwsioo/murettoPG)

Benvenuto in **MurettoPG**, il sito web dedicato alla gestione dei tornei di freestyle rap per il Muretto di Perugia. Questo progetto nasce per facilitare l'organizzazione e il monitoraggio delle competizioni di freestyle, offrendo al contempo un generatore casuale di parole e argomenti per le sfide.

---

## Caratteristiche principali

### Gestione Tornei (tournament.html)

- Creazione automatica del tabellone partecipanti con modalità:
  - **1v1 Classico**: incontri diretti in singolo elimina.
  - **Rumble 4vs**: gruppi da 4 MC, con selezione di più vincitori a ogni round.
- Inserimento personalizzato dei nomi degli MC (uno per riga).
- Visualizzazione interattiva e ordinata del tabellone con fasi e match.
- Avanzamento manuale dei vincitori con possibilità di annullare l'ultima azione.
- Salvataggio automatico dello stato del torneo nel browser (localStorage).
- Supporto a situazioni particolari come match a 3 vie in caso di partecipanti dispari.

### Generatore di Parole e Argomenti (generator.html)

- Estrazione casuale di parole e argomenti da liste JSON predefinite.
- Supporto a parole elaborate tramite Morph-it! per garantire risorse linguistiche di qualità.
- Interfaccia semplice e intuitiva per supportare le sfide freestyle con input creativo.

### Script Python di Supporto

- Script per generare la lista JSON di lemmi da utilizzare nel generatore di parole.
- Estrazione automatica di nomi, aggettivi, avverbi e verbi da Morph-it!, esclusi i verbi ausiliari "essere" e "avere".
- Produzione del file `lemmi.json` in UTF-8 per utilizzo diretto nel frontend.

---

## Tecnologie utilizzate

- HTML, CSS e JavaScript puro per la parte frontend.
- Utilizzo di localStorage per la persistenza dei dati lato client.
- Python per la generazione e gestione dei dati linguistici di supporto.

---

## Come usare

1. Apri `tournament.html` per gestire un torneo, inserendo i nomi degli MC e scegliendo la modalità.
2. Usa i pulsanti per generare il tabellone, avanzare i vincitori, annullare mosse e resettare il torneo.
3. Apri `generator.html` per generare casualmente parole e argomenti da utilizzare durante le sfide freestyle.

---

## Contatti

Per suggerimenti e richieste puoi contattare l'autore tramite il repository GitHub.

---

Grazie per aver scelto MurettoPG per le tue sfide di freestyle a Perugia!
