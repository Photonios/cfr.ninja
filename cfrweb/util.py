import copy


def merge_dict_r(dict_a: dict, dict_b: dict):
    """Recursively merges :paramref:dict_b into
    :paramref:dict_a.

    Arguments:
        dict_a:
            The dictionary to merge into.

        dict_b:
            The dictionary to merge into
            :paramref:dict_b.

    Returns:
        A new dictionary that is a merge
        of :paramref:dict_a and :paramref:dict_b.
    """

    result = copy.deepcopy(dict_a)

    for key, value in dict_b.items():
        if isinstance(dict_a.get(key), dict):
            result[key] = merge_dict_r(dict_a[key], value)
        else:
            result[key] = value

    return result


def reverse_url(router, language: str, name: str, *args, **kwargs):
    """Gets a URL to the specified view.

    Arguments:
        router:
            The router to use.

        language:
            The language to return
            the URL in.

        name:
            The name of the view
            to get the URL of.

        *args:
            Positional arguments
            to pass to the view.

        **kwargs:
            Keyword arguments
            to pass to the view.

    Returns:
        A URL that leads to the
        specified view.
    """

    return '/%s%s' % (
        language,
        router[name].url_for(*args, **kwargs)
    )
