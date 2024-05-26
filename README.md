# Financial distress models in Slovak enterprises
This repository contains code for the Bachelor´s thesis - Financial distress models in Slovak enterprises.
The goal of the thesis is to create alternative models of financial distress based on financial statements data of Slovak companies from the years 2014-2021, to justify and select criteria for assessing the predictive ability of the models, as well as choose the optimal predictive model.

Repozitár obsahuje scripty v jupyter notebookoch použité pri bakalárskej práci.
## Štruktúra repozitára

CODE
- TRANSFORM
  - obsahuje transformačnú pipeline od surových dát po finálnu vzorku
  - poradie podľa názvov súborov
      - zakladne upravy (1-3)
      - parsovanie hodnot z vykazov v json (4)
      - tvorba pomerovych ukazovatelov (5)
      - spracovanie dat z registra upadcov pre ucel kriteria fin tazkosti (6)
      - doplnujuce upravy
      - generovanie finalnej mnoziny
  - repozitár neobsahuje sťahovací mechanizmus z API pripojenia
- EXPLORATORY
  - scripty k vybranym castiam sekcie 2.2 a k sekcii 3.1
- MODELLING
  - scripty k tuningu hyperparametrov (+RFE) jednotlivych modelov (sekcia 3.2) (1-4)
  - suhrnne porovnanie 4 finalnych (sekcia 3.3)
- OTHER
  - pomocne scripty
- ARCHIVE

CLASSIFIERS
- uložené objekty finálnych modelov (zo scikit-learn)


