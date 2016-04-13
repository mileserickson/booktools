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
        List price of the book in US dollars, or None if not found.

    Examples
    --------
    >>> get_list_price("9780262029445")
    74.0
    """
    AMAZON_URL = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="
    search_result = requests.get(AMAZON_URL+isbn)
    book_soup = BeautifulSoup(search_result.content, 'lxml')

    price = book_soup.select_one("span.a-text-strike").get_text()
    if price[0] == '$':
        return float(price[1:])
    else:
        return None
