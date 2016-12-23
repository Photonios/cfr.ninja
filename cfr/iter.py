def pairwise(it):
    """Iterates over the specified iterator,
    two items at the time.

    Arguments:
        it:
            The iterate to iterate
            over two items at the time.
    """

    it = iter(it)
    while True:
        yield next(it), next(it)
