
# https://github.com/Fabioni/PortfoliePerformance-Historische_Kurse_Tabelle_auf_einer_Webseite
import datetime
import urllib.parse
from typing import cast
import dateutil.parser
from requests_html import HTMLSession, HTMLResponse


def main():
    isin = input("ISIN: ").strip()
    #isin = "LU0125951151"
    asession = HTMLSession()
    r = cast(HTMLResponse, asession.get("https://www.onvista.de/fonds/" + isin))
    r.html.render(sleep=2, keep_page=True)

    notationNameIds = [(opt.text, opt.attrs['value']) for opt in r.html.find('select#select-market option')]
    #notationNameIds = [('Baader Bank (EUR, Echtzeit)', '28299034'), ('Berlin (EUR, Echtzeit)', '15876426'), ('Düsseldorf (EUR, Echtzeit)', '16043559'), ('Frankfurt (EUR, verzögert)', '15912438'), ('gettex (EUR, Echtzeit)', '120540319'), ('Hamburg (EUR, Echtzeit)', '16009935'), ('KVG (EUR, Echtzeit)', '6334133'), ('München (EUR, Echtzeit)', '22980888'), ('Quotrix (EUR, Echtzeit)', '178563840'), ('Stuttgart (EUR, Echtzeit)', '24072743'), ('Swiss Exchange (EUR, verzögert)', '77698999'), ('Tradegate (EUR, Echtzeit)', '155594393')]
    if len(notationNameIds) == 0:
        print("For this ISIN nothing can be found, sorry!")
        exit()
    # chose one
    print("\n".join([str(i) + ": " + name_notation[0] for (i, name_notation) in enumerate(notationNameIds)]))

    while True:
        idx = input("stockmarket: ")
        if idx.isdigit() and int(idx) in range(len(notationNameIds)):
            idx = int(idx)
            break
        print("wrong input")
    notationId = notationNameIds[idx][1]
    boerse = urllib.parse.quote(notationNameIds[idx][0])
    name = urllib.parse.quote(r.html.find("h1.headline", first=True).text)

    variabelDate = None
    variabelDateString = "{TODAY:dd.MM.yyyy:-P5Y}"
    while True:
        startdate = input("Startdate (any format, leave empty for variabel Portfolio Performance Link only): ")
        if startdate.isspace() or startdate == "":
            variabelDate = True
            break
        else:
            try:
                startdatestring = dateutil.parser.parse(startdate).strftime("%d.%m.%Y")
                variabelDate = False
                break
            except Exception:
                pass
        print("wrong input")


    linkFixed = None
    if not variabelDate:
        print("\nThe Link:")
        linkFixed = f"https://www.onvista.de/onvista/times+sales/popup/historische-kurse/?notationId={notationId}&dateStart={startdatestring}&interval=Y5&assetName={isin}_{name}&exchange={boerse}"
        print(linkFixed)

    print("The Link with variabel startdate, works in Portfolio Performance, not in  the Browser")
    link = f"https://www.onvista.de/onvista/times+sales/popup/historische-kurse/?notationId={notationId}&dateStart={variabelDateString}&interval=Y5&assetName={isin}_{name}&exchange={boerse}"
    print(link)

    try:
        with open("save.txt", "a") as f:
            f.write(datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))
            f.write("\n")
            f.write(f"ISIN: '{isin}' | Name: '{name}' | exchange: '{boerse}'")
            f.write("\n")
            if linkFixed is not None:
                f.write(linkFixed)
                f.write("\n")
            f.write(link)
            f.write("\n\n\n")
            print("The link is saved in save.txt in the same folder as this script is")
    except:
        pass


if __name__ == '__main__':
    main()
