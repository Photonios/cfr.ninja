import sys


def text(value: str) -> str:
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


def number(value: str, default=0) -> int:
    """Strips the specified text and converts
    it to a number.

    Arguments:
        value:
            The string to strip and convert
            to a number.

        default:
            Value to return if the specified
            value could not be converted to
            a number.

    Returns:
        The stripped string as a number, or
        zero if the string was empty.
    """

    text = sys.modules[__name__].text(value)
    return int(text) if text else default
