from typing import List

from bs4 import BeautifulSoup

from .iter import pairwise
from .viewstate import ViewState


class TrainNotFound(Exception):
    """Raises when the user entered the
    number of a train there's no information of."""


def _text_and_strip(value: str) -> str:
    """Strips the specified text and returns
    None if it's empty.

    Arguments:
        value:
            The string to strip.

    Returns:
        The stripped string or None
        if it was empty.
    """

    text = value.strip()if value != '\xa0' else None
    return text if text else None


def _number_and_strip(value: str) -> int:
    """Strips the specified text and converts
    it to a number.

    Arguments:
        value:
            The string to strip and convert
            to a number.

    Returns:
        The stripped string as a number, or
        zero if the string was empty.
    """

    text = _text_and_strip(value)
    return int(text) if text else 0


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
        'rank': _text_and_strip(values['Rang']),
        'number': _text_and_strip(values['Tren']),
        'operator': _text_and_strip(values['Operator']),
        'route': _text_and_strip(values['Relatia']),
        'state': _text_and_strip(values['Stare']),
        'last_info': _text_and_strip(values['Ultima informatie']),
        'date_time': _text_and_strip(values['Data si ora']),
        'delay': _number_and_strip(values['Intarziere']),
        'destination': _text_and_strip(values['Statia destinatie']),
        'arrival_at': _text_and_strip(values['Sosire']),
        'next_stop': _text_and_strip(values['Urmatoarea oprire']),
        'distance': _text_and_strip(values['Distanta']),
        'duration': _text_and_strip(values['Durata calatoriei'])
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
            'km': _number_and_strip(columns[0].text),
            'station': _text_and_strip(columns[1].text),
            'arriving_at': _text_and_strip(columns[2].text),
            'staying_for': _number_and_strip(columns[3].text),
            'leaving_at': _text_and_strip(columns[4].text),
            'is_estimation': 'Estimat' in columns[5].text,
            'delay': _number_and_strip(columns[6].text),
            'notes': _text_and_strip(columns[7].text)
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

    state = ViewState('http://appiris.infofer.ro/MytrainRO.aspx')

    state.request('GET')

    response = state.request('POST', data={
        'TextTrnNo': number,
        'Button1': 'Informatii tren'
    })

    if 'Lipsa informatii.' in response.text:
        raise TrainNotFound()

    state.request('POST', data={
        'TextTrnNo': number,
        '__EVENTTARGET': 'DetailsView1',
        '__EVENTARGUMENT': 'Page$2'
    })

    document = state.request('POST', data={
        'TextTrnNo': number,
        'Button2': 'Arata detalii'
    })

    details = _extract_info_table(document)
    details['schedule'] = _extract_schedule_table(document)

    return details

__all__ = [
    'train'
]
