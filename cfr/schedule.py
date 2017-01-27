from typing import List

from bs4 import BeautifulSoup
import bs4
import requests

from . import strip


def _extract_rows(document: BeautifulSoup) -> List[bs4.element.Tag]:
    """Extracts the HTML rows from the document, where
    each row is a train.

    Arguments:
        document:
            The HTML document to extract
            the rows from.

    Returns:
        The rows that were extracted.
    """

    rows = document.find(id='divContainer').find('table').find_all('tbody')
    return rows


def _extract_trains(rows: List[bs4.element.Tag]) -> list:
    """Extracts listed trains from the specified list
    of rows.

    This is interesting as it also displays connecting
    trains. When searching for trains from Brasov-Cluj
    for example, it also shows a train going from Cluj
    to Sibiu, and then from Sibiu to Brasov. Therefor
    we have to keep trains as lists of lists. That
    way, we don't lose that information.

    Arguments:
        rows:
            A list of table rows to extract
            train listings from.

    Returns:
        A list of trains.
    """

    trains = []

    for row in rows:
        new_train = []

        for sub_row in row.find_all('tr'):
            columns = sub_row.find_all('td', attrs={'rowspan': None})
            new_train.append({
                'number': strip.text(columns[1].text),
                'departure_station': strip.text(columns[2].text),
                'arrival_station': strip.text(columns[3].text),
                'departs_at': strip.text(columns[4].text),
                'arrives_at': strip.text(columns[5].text),
                'duration': strip.text(columns[8].text),
                'distance': strip.number(columns[10].text)
            })

        trains.append(new_train)

    return trains


def schedule(date, departure_station: str, arrival_station: str) -> List[List[dict]]:
    """Finds all trains departing from the specified
    station, arroving at the specified station on
    the specified date.

    Arguments:
        date:
            The date to find trains on.

        departure_station:
            The departure station to
            search for.

        arrival_station:
            The arrival station to
            search for.

    Returns:
        A list of trains.
    """

    # format the date in a format that the cfr website understands
    date_formatted = date.strftime('%d-%m-%Y')

    # compose the url to search for trains
    url = ('https://bilete.cfrcalatori.ro/vanzare/rute_.aspx'
           '?keyimt=dtm={}'
           '&p={}&d={}'
           '&ora=CURRENT%20TIME'
           '&cautavans=0&lng=en')

    url = url.format(date_formatted, departure_station, arrival_station)

    # make the request with the composed url
    response = requests.get(url)
    document = BeautifulSoup(response.text, 'html.parser')

    rows = _extract_rows(document)
    return _extract_trains(rows)
