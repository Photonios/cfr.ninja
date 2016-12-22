from .train import Train
from .viewstate import ViewState


def train(number: int) -> Train:
    """Gets details about the train with
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

    state.request('POST', data={
        'TextTrnNo': number,
        'Button1': 'Informatii tren'
    })

    response = state.request('POST', data={
        'TextTrnNo': number,
        'Button2': 'Arata detalii'
    })

    print(response)

__all__ = [
    'train'
]
