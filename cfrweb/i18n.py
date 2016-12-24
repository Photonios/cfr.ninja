import gettext

from .config import settings


def get(language: str=None):
    """Gets the translation object
    for the specified language.

    Arguments:
        language:
            The two-digit code of
            the language to get
            the translations of.
    """

    language = language or settings.I18N_PRIMARY_LANGUAGE

    translation = gettext.translation(
        settings.I18N_DOMAIN,
        settings.I18N_LOCALE_DIR,
        languages=[language]
    )

    return translation
