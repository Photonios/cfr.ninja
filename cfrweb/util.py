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
