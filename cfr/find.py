from typing import List

from bs4 import BeautifulSoup

from . import strip
from .iter import pairwise
from .viewstate import ViewState


class TrainNotFound(Exception):
    """Raises when the user entered the
    number of a train there's no information of."""


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
        'rank': strip.text(values['Rang']),
        'number': strip.text(values['Tren']),
        'operator': strip.text(values['Operator']),
        'route': strip.text(values['Relatia']),
        'state': strip.text(values['Stare']),
        'last_info': strip.text(values['Ultima informatie']),
        'date_time': strip.text(values['Data si ora']),
        'delay': strip.number(values['Intarziere']),
        'destination': strip.text(values['Statia destinatie']),
        'arrival_at': strip.text(values['Sosire']),
        'next_stop': strip.text(values['Urmatoarea oprire']),
        'distance': strip.text(values['Distanta']),
        'duration': strip.text(values['Durata calatoriei'])
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
            'delay': strip.number(columns[6].text),
            'notes': strip.text(columns[7].text)
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

    state = ViewState('http://appiris.infofer.ro/MytrainRO.aspx')

    state.request('GET')

    response = state.request('POST', data={
        'TextTrnNo': number,
        'Button1': 'Informatii tren'
    })

    if 'Lipsa informatii.' in response.text:
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
