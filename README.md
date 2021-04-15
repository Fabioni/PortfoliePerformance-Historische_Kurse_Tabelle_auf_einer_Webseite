# Portfolie Performance – Historische Kurse – Link für „Tabelle auf einer Webseite“
Automatisiertes Erstellen eines Links, um ihn bei Portfolie Performance bei „Tabelle auf einer Website“ einzufügen.

## How it looks like



```
python3 main.py
ISIN: LU0125951151
0: Baader Bank (EUR, Echtzeit)
1: Berlin (EUR, Echtzeit)
2: Düsseldorf (EUR, Echtzeit)
3: Frankfurt (EUR, verzögert)
4: gettex (EUR, Echtzeit)
5: Hamburg (EUR, Echtzeit)
6: KVG (EUR, Echtzeit)
7: München (EUR, Echtzeit)
8: Quotrix (EUR, Echtzeit)
9: Stuttgart (EUR, Echtzeit)
10: Swiss Exchange (EUR, verzögert)
11: Tradegate (EUR, Echtzeit)
stockmarket: 3
Startdate (any format): 2018-05-01
https://www.onvista.de/onvista/times+sales/popup/historische-kurse/?notationId=15912438&dateStart=01.05.2018&interval=Y5&assetName=LU0125951151_MFS%20Meridian-Eur.Value%20A1%20EUR&exchange=Frankfurt%20%28EUR%2C%20verz%C3%B6gert%29
```


## Setup

1. install python3

1. Download .zip from GitHub and unzip it

1. open a terminal at this folder location

1. run `pip3 install -r requirements.txt` inside

1. run the script with `python3 main.py`. It asks for ISIN and startdate, the maximal time period of 5 years is used.


## Interaction

- Pull Request are welcome
  - especially if something on OnVista changes so the script needs to be modified
  - or if you want to add another source besides OnVista
- use the Issues tap to report bugs or feature requests
- use the Discussion tap to ask stuff or talk about ideas or whatever is on your mind
