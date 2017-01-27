from typing import List

from bs4 import BeautifulSoup

from . import strip
from .iter import pairwise
from .viewstate import ViewState
from .exceptions import TrainNotFound


def _extract_info_table(document: BeautifulSoup) -> dict:
    """Extracts the table of of general information
    about the train from the specified document.

    Arguments:
        document:
            The document to extract
            the information from.

    Returns:
        A dictionary containing information
        about the train, exctracted from
        the specified document.
    """

    rows = document.find(id='DetailsView1').find_all('td')
    values = dict()

    for key, value in pairwise(rows):
        values[key.text] = value.text.strip()

    values = {
        'rank': strip.text(values['Rank']),
        'number': strip.text(values['Train']),
        'operator': strip.text(values['RU']),
        'route': strip.text(values['Distance traffic']),
        'state': strip.text(values['Status']),
        'last_info': strip.text(values['Last information']),
        'date_time': strip.text(values['Date and time']),
        'delay': strip.number(values['Delay']),
        'destination': strip.text(values['Destination station']),
        'arrival_at': strip.text(values['Arrival']),
        'next_stop': strip.text(values['Next stop']),
        'distance': strip.text(values['Distance']),
        'duration': strip.text(values['Time trip'])
    }

    return values


def _extract_schedule_table(document: BeautifulSoup) -> List[dict]:
    """Extracts the table containing the stops
    the train has been at or is going at from
    the specified document.

    Arguments:
        document:
            The document to extract
            the information from.

    Returns:
        A list of stations the train
        will stop at.
    """

    rows = document.find(id='GridView1').find_all('tr')[1:]
    values = list()

    for row in rows:
        columns = row.find_all('td')

        values.append({
            'km': strip.number(columns[0].text),
            'station': strip.text(columns[1].text),
            'arriving_at': strip.text(columns[2].text),
            'staying_for': strip.number(columns[3].text),
            'leaving_at': strip.text(columns[4].text),
            'is_estimation': 'Estimat' in columns[5].text,
            'delay': strip.number(columns[6].text)
        })

    return values


def find(number: str) -> dict:
    """Finds details about the train with
    the specified number.

    Arguments:
        number:
            The number of the train to
            search for.

    Returns:
        None if no such train exists
        and details about the specified
        train if it does.
    """

    if not number:
        raise TrainNotFound()

    state = ViewState('http://appiris.infofer.ro/MytrainEN.aspx')

    state.request('GET')

    response = state.request('POST', data={
        'TextTrnNo': number,
        'Button1': 'Informatii tren'
    })

    if 'No informations.' in response.text:
        raise TrainNotFound()

    document = state.request('POST', data={
        'TextTrnNo': number,
        'Button2': 'Arata detalii'
    })

    details = _extract_info_table(document)
    details['schedule'] = _extract_schedule_table(document)

    return details

__all__ = [
    'find'
]
