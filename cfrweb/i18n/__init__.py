import gettext

from ..config import settings


def activate(language: str=None):
    """Actives the specified language as
    the currently active one.

    Arguments:
        language:
            The two-digit code
            of the language to
            switch to.
    """

    language = language or settings.I18N_PRIMARY_LANGUAGE

    translation = gettext.translation(
        settings.I18N_DOMAIN,
        settings.I18N_LOCALE_DIR,
        languages=[language]
    )

    translation.install()
