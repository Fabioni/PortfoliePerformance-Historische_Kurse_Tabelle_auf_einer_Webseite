import urllib.parse
from typing import cast

import dateutil.parser
from requests_html import HTMLSession, HTMLResponse


def main():
    isin = input("ISIN: ")
    #isin = "LU0125951151"
    asession = HTMLSession()
    r = cast(HTMLResponse, asession.get("https://www.onvista.de/fonds/" + isin))
    r.html.render(sleep=2, keep_page=True)

    notationNameIds = [(opt.text, opt.attrs['value']) for opt in r.html.find('select#select-market', first=True).find('option')]

    # chose one
    print(notationNameIds)
    idx = int(input("index?: "))
    notationId = notationNameIds[idx][1]
    boerse = urllib.parse.quote(notationNameIds[idx][0])
    name = urllib.parse.quote(r.html.find("h1.headline", first=True).text)

    startdate = dateutil.parser.parse(input("Startdate: "))

    startdatestring = startdate.strftime("%d.%m.%Y")

    # interval ist wichtig
    print(f"https://www.onvista.de/onvista/times+sales/popup/historische-kurse/?notationId={notationId}&dateStart={startdatestring}&interval=Y5&assetName={isin}_{name}&exchange={boerse}")


if __name__ == '__main__':
    main()
