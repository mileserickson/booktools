"""Tools for retrieving information about books."""

import requests
from bs4 import BeautifulSoup

def get_list_price(isbn):
    """Return the list price of a book.

    Parameters
    ----------
    isbn : string
        ISBN-10 or ISBN-13 of a book.

    Returns
    -------
    list_price : float
        List price of the book in US dollars.

    Examples
    --------
    >>> get_list_price("9780262029445")
    74.0
    """
    pass
